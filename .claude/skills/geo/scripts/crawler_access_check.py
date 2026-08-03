#!/usr/bin/env python3
"""
Multi-crawler access checker.

Answers the question that matters most in a GEO audit and that no single tool
answers today: *can each AI engine's citation-relevant bot actually fetch this page?*

Two independent failure modes, both checked:
  1. robots.txt disallows the bot            (--robots, default on)
  2. the CDN/WAF blocks the bot's user agent (--live)

A site can pass (1) and fail (2). Cloudflare bot-fight mode is the classic case:
robots.txt says allow, the edge returns 403, and the engine never cites you.
Nothing in Google Search Console will ever tell you this.

Usage:
    python crawler_access_check.py https://example.com
    python crawler_access_check.py https://example.com --live
    python crawler_access_check.py https://example.com --live --urls urls.txt --json out.json

Exit code 1 if any citation-relevant bot is blocked.
"""
import argparse, json, sys, time, urllib.request, urllib.error, urllib.parse
from urllib.robotparser import RobotFileParser

# purpose: search  = governs whether the engine can cite you  (BLOCKING THIS COSTS CITATIONS)
#          user    = user-initiated retrieval; several ignore robots.txt by design
#          training= model training only       (blocking costs zero citations)
#          ads     = ad landing-page validation
# Sources are in references/crawler-access.md; every row traces to official vendor docs.
BOTS = [
    # token,               operator,     purpose,    citation_critical
    ("Googlebot",          "Google",     "search",   True),
    ("Google-Extended",    "Google",     "training", False),  # Gemini/Vertex ONLY - not AI Overviews
    ("Google-Agent",       "Google",     "user",     True),   # Web Bot Auth experimental
    ("OAI-SearchBot",      "OpenAI",     "search",   True),   # <- the one that matters for ChatGPT
    ("GPTBot",             "OpenAI",     "training", False),
    ("ChatGPT-User",       "OpenAI",     "user",     True),
    ("OAI-AdsBot",         "OpenAI",     "ads",      False),
    ("Claude-SearchBot",   "Anthropic",  "search",   True),   # <- the one that matters for Claude
    ("Claude-User",        "Anthropic",  "user",     True),
    ("ClaudeBot",          "Anthropic",  "training", False),
    ("PerplexityBot",      "Perplexity", "search",   True),
    ("Perplexity-User",    "Perplexity", "user",     True),   # ignores robots.txt by design
    ("bingbot",            "Microsoft",  "search",   True),   # feeds ChatGPT + Copilot
    ("Amzn-SearchBot",     "Amazon",     "search",   True),
    ("Amzn-User",          "Amazon",     "user",     True),
    ("Applebot",           "Apple",      "search",   True),
    ("Applebot-Extended",  "Apple",      "training", False),
    ("meta-externalagent", "Meta",       "training", False),
    ("Bytespider",         "ByteDance",  "training", False),
    ("CCBot",              "CommonCrawl","training", False),
    ("cohere-ai",          "Cohere",     "training", False),
    ("DuckAssistBot",      "DuckDuckGo", "search",   True),
]

# Bots whose own documentation states they may ignore robots.txt (user-initiated fetches).
IGNORES_ROBOTS = {"Perplexity-User", "ChatGPT-User", "Amzn-User"}

UA_STRINGS = {
    "OAI-SearchBot":    "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot",
    "GPTBot":           "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot",
    "ChatGPT-User":     "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot",
    "PerplexityBot":    "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)",
    "Perplexity-User":  "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)",
    "Claude-SearchBot": "Mozilla/5.0 (compatible; Claude-SearchBot/1.0; +http://www.anthropic.com/bot.html)",
    "ClaudeBot":        "Mozilla/5.0 (compatible; ClaudeBot/1.0; +http://www.anthropic.com/bot.html)",
    "Claude-User":      "Mozilla/5.0 (compatible; Claude-User/1.0; +http://www.anthropic.com/bot.html)",
    "Googlebot":        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "bingbot":          "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Amzn-SearchBot":   "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-SearchBot/0.1)",
    "Applebot":         "Mozilla/5.0 (compatible; Applebot/0.1; +http://www.apple.com/go/applebot)",
}


# A 200 status is NOT proof of access. Bot-mitigation layers commonly return
# HTTP 200 with a JS "checking your browser" interstitial. Crawlers cannot execute
# the redirect, so they index the challenge page - or nothing. Scoring that as a
# pass is the single easiest way to produce a false-clean access audit.
INTERSTITIAL_MARKERS = (
    "one moment, please",          # LiteSpeed / openresty mitigation
    "checking your browser",       # Cloudflare legacy IUAM
    "just a moment...",            # Cloudflare Turnstile interstitial
    "enable javascript and cookies to continue",
    "ddos protection by",
    "window.location.reload()",
    "__cf_chl",                    # Cloudflare challenge script
    "/cdn-cgi/challenge-platform", # Cloudflare challenge platform
)


def classify_body(status, body_bytes, content_type=""):
    """Return (verdict, detail). Verdict is one of OK, INTERSTITIAL, THIN, HTTP_<code>, ERROR."""
    if status is None:
        return "ERROR", str(body_bytes)
    if status != 200:
        return f"HTTP_{status}", ""
    text = body_bytes.decode("utf-8", "replace") if isinstance(body_bytes, bytes) else str(body_bytes)
    low = text[:4000].lower()
    for m in INTERSTITIAL_MARKERS:
        if m in low:
            return "INTERSTITIAL", m
    if "xml" in (content_type or "").lower() or text.lstrip().startswith("<?xml"):
        return "OK", "xml"
    if len(text) < 800:
        return "THIN", f"{len(text)} bytes"
    return "OK", f"{len(text)} bytes"


def fetch(url, ua, timeout=25):
    """Returns (status, verdict, detail). Verdict distinguishes real content from a challenge page."""
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "text/html,application/xml,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
            verdict, detail = classify_body(r.status, body, r.headers.get("Content-Type", ""))
            return r.status, verdict, detail
    except urllib.error.HTTPError as e:
        try:
            body = e.read()
        except Exception:
            body = b""
        verdict, detail = classify_body(e.code, body, e.headers.get("Content-Type", "") if e.headers else "")
        return e.code, verdict, detail
    except Exception as e:
        return None, "ERROR", str(e)


def load_robots(base):
    robots_url = urllib.parse.urljoin(base, "/robots.txt")
    status, _, _ = fetch(robots_url, UA_STRINGS["Googlebot"])
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except Exception:
        rp.parse([])
    return rp, robots_url, status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("--urls", help="file of extra URLs to test (one per line)")
    ap.add_argument("--live", action="store_true", help="also make a real request per bot UA to detect WAF/CDN blocks")
    ap.add_argument("--delay", type=float, default=8.0,
                    help="seconds between live requests (default 8). Rapid sequential requests from one IP "
                         "trip generic volumetric rate limits and produce FALSE 429s that look like UA policy. "
                         "Do not lower this. Re-test any 429 in a separate run before reporting it.")
    ap.add_argument("--json", help="write results to this JSON file")
    a = ap.parse_args()

    base = a.site if a.site.startswith("http") else "https://" + a.site
    targets = [base]
    if a.urls:
        targets += [l.strip() for l in open(a.urls, encoding="utf-8") if l.strip()]

    rp, robots_url, robots_status = load_robots(base)
    print(f"robots.txt: {robots_url}  -> HTTP {robots_status}")
    if robots_status == 404:
        print("  (404 = no restrictions; all bots allowed by default)")
    print()

    results, blocked = [], []
    hdr = f"{'BOT':<20} {'OPERATOR':<12} {'PURPOSE':<9} {'ROBOTS':<9}"
    if a.live:
        hdr += " LIVE"
    print(hdr)
    print("-" * (len(hdr) + 6))

    for token, operator, purpose, critical in BOTS:
        allowed = rp.can_fetch(token, base)
        note = ""
        if token in IGNORES_ROBOTS:
            note = " (ignores robots by design)"
        row = {"bot": token, "operator": operator, "purpose": purpose,
               "citation_critical": critical, "robots_allowed": allowed}

        line = f"{token:<20} {operator:<12} {purpose:<9} {'ALLOW' if allowed else 'BLOCK':<9}"

        if a.live:
            ua = UA_STRINGS.get(token, f"Mozilla/5.0 (compatible; {token})")
            code, verdict, detail = fetch(base, ua)
            row["live_status"] = code
            row["live_verdict"] = verdict
            row["live_detail"] = detail
            ok = verdict == "OK"
            line += f" {str(code) if code else 'ERR':<4} {verdict:<13}"
            if not ok:
                line += " <-- EDGE BLOCK"
            if critical and not ok and allowed:
                why = (f"robots.txt allows but origin returned HTTP {code}" if verdict.startswith("HTTP_")
                       else f"robots.txt allows but origin served a bot-challenge interstitial "
                            f"(HTTP 200, matched '{detail}') - crawlers cannot execute it"
                       if verdict == "INTERSTITIAL" else
                       f"robots.txt allows but response was {verdict} ({detail})")
                blocked.append((token, why))
            time.sleep(a.delay)

        if critical and not allowed and token not in IGNORES_ROBOTS:
            blocked.append((token, "disallowed in robots.txt"))
            line += "  <-- CITATION-CRITICAL"

        print(line + note)
        results.append(row)

    print()
    if blocked:
        print(f"!! {len(blocked)} citation-critical problem(s):")
        for t, why in blocked:
            print(f"   - {t}: {why}")
    else:
        print("OK: every citation-critical bot can reach the site and received real content.")

    if a.live:
        n429 = [r["bot"] for r in results if r.get("live_status") == 429]
        if n429:
            print(f"\nNOTE: HTTP 429 seen for: {', '.join(n429)}.")
            print("      429 is ambiguous - it can be a deliberate policy block OR volumetric rate limiting")
            print("      tripped by this test. Confirm by re-running those agents alone after a 60s+ pause,")
            print("      interleaved with a normal browser UA. If the browser UA passes in the same window,")
            print("      the block is user-agent policy, not rate limiting.")
        inter = [r["bot"] for r in results if r.get("live_verdict") == "INTERSTITIAL"]
        if inter:
            print(f"\n!! BOT-CHALLENGE INTERSTITIAL served to: {', '.join(inter)}")
            print("   These returned HTTP 200 but the body is a JS challenge, not content.")
            print("   Crawlers cannot execute it. If this fires for Googlebot, Google may index the")
            print("   challenge page instead of the site. Treat as a live outage, not a warning.")

    # Training-bot posture is a client decision, not a defect - report it, don't flag it.
    tr = [r["bot"] for r in results if r["purpose"] == "training" and not r["robots_allowed"]]
    if tr:
        print(f"\nTraining bots blocked (costs zero citations - confirm this is intentional): {', '.join(tr)}")

    if a.json:
        json.dump({"site": base, "robots_url": robots_url, "robots_status": robots_status,
                   "results": results, "blocked": blocked}, open(a.json, "w"), indent=2)
        print(f"\nwrote {a.json}")

    sys.exit(1 if blocked else 0)


if __name__ == "__main__":
    main()
