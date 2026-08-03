#!/usr/bin/env python3
"""
Indexability and AI-snippet-eligibility checker.

Google's own rule: to appear in AI Overviews or AI Mode a page must be indexed
AND eligible to be shown with a snippet. So `nosnippet` / `max-snippet:0` are
silent AI-visibility killers that a normal indexability audit will pass, because
the page is perfectly indexed - it just can't be quoted.

Checks per URL:
  - HTTP status, redirect chain, final URL
  - robots meta + X-Robots-Tag header: noindex, nosnippet, max-snippet, noarchive, none
  - canonical: present, self-referencing, or pointing elsewhere
  - data-nosnippet regions
  - raw-HTML text volume (a proxy for "is the content actually server-rendered?")

Usage:
    python indexability_check.py https://example.com/a https://example.com/b
    python indexability_check.py --urls urls.txt --json out.json
"""
import argparse, json, re, sys, urllib.request, urllib.error, urllib.parse

UA = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

# Directives that block or limit AI-surface eligibility, and what each actually costs.
DIRECTIVE_IMPACT = {
    "noindex":    "not indexed -> ineligible for all Google surfaces incl. AI Overviews/AI Mode",
    "nosnippet":  "indexed but NOT snippet-eligible -> INELIGIBLE for AI Overviews/AI Mode",
    "none":       "equivalent to noindex,nofollow -> ineligible",
    "noarchive":  "Google: no cached copy. Amazon: treats it as 'do not use for model training'",
    "max-snippet:0": "zero-length snippet -> INELIGIBLE for AI Overviews/AI Mode",
}


class Redirects(urllib.request.HTTPRedirectHandler):
    def __init__(self):
        self.chain = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.chain.append((code, newurl))
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(url):
    h = Redirects()
    opener = urllib.request.build_opener(h)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with opener.open(req, timeout=30) as r:
            return r.status, dict(r.headers), r.read().decode("utf-8", "replace"), r.url, h.chain
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), "", url, h.chain
    except Exception as e:
        return None, {}, str(e), url, h.chain


def text_volume(html):
    b = re.sub(r'<(script|style|noscript|svg|head)[^>]*>.*?</\1>', ' ', html, flags=re.S | re.I)
    b = re.sub(r'<[^>]+>', ' ', b)
    return len(re.sub(r'\s+', ' ', b).strip())


def check(url):
    status, headers, html, final, chain = fetch(url)
    r = {"url": url, "status": status, "final_url": final,
         "redirects": [{"code": c, "to": u} for c, u in chain],
         "directives": [], "issues": [], "ai_eligible": True}

    if status != 200:
        r["issues"].append(f"HTTP {status} - not indexable")
        r["ai_eligible"] = False
        return r

    # robots directives from meta tags (name=robots or any googlebot-family token) and headers
    found = []
    for m in re.finditer(
        r'<meta[^>]+name=["\'](robots|googlebot|google)["\'][^>]*content=["\']([^"\']+)["\']', html, re.I
    ):
        found += [d.strip().lower() for d in m.group(2).split(",")]
    xr = headers.get("X-Robots-Tag", "")
    if xr:
        found += [d.strip().lower() for d in xr.split(",")]
        r["x_robots_tag"] = xr
    r["directives"] = sorted(set(found))

    for d in r["directives"]:
        key = "max-snippet:0" if re.match(r'max-snippet\s*:\s*0\b', d) else d
        if key in DIRECTIVE_IMPACT:
            r["issues"].append(f"{d} -> {DIRECTIVE_IMPACT[key]}")
            if key in ("noindex", "nosnippet", "none", "max-snippet:0"):
                r["ai_eligible"] = False

    # canonical
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', html, re.I)
    if m:
        can = urllib.parse.urljoin(final, m.group(1))
        r["canonical"] = can
        if can.rstrip("/") != final.rstrip("/"):
            r["issues"].append(f"canonical points elsewhere: {can} (this URL will not be indexed in its own right)")
    else:
        r["issues"].append("no canonical tag")

    if 'data-nosnippet' in html:
        n = html.count('data-nosnippet')
        r["issues"].append(f"{n} data-nosnippet region(s) - that text cannot be quoted in AI answers or snippets")

    if chain:
        r["issues"].append(f"{len(chain)} redirect hop(s) before final URL")

    r["text_chars"] = text_volume(html)
    if r["text_chars"] < 500:
        r["issues"].append(f"only {r['text_chars']} chars of text in raw HTML - likely JS-rendered; "
                           "verify with a renderer (agents and some crawlers may see an empty page)")
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--urls", dest="file")
    ap.add_argument("--json")
    a = ap.parse_args()

    targets = list(a.urls)
    if a.file:
        targets += [l.strip() for l in open(a.file, encoding="utf-8") if l.strip()]
    if not targets:
        ap.error("give URLs or --urls FILE")

    out = []
    for u in targets:
        r = check(u)
        out.append(r)
        flag = "OK " if r["ai_eligible"] and not r["issues"] else ("AI-INELIGIBLE" if not r["ai_eligible"] else "WARN")
        print(f"\n[{flag}] {u}  HTTP {r['status']}  {r.get('text_chars','?')} chars")
        if r["directives"]:
            print(f"   directives: {', '.join(r['directives'])}")
        for i in r["issues"]:
            print(f"   - {i}")

    bad = [r for r in out if not r["ai_eligible"]]
    print(f"\n{len(out)} checked, {len(bad)} ineligible for Google AI surfaces")
    if a.json:
        json.dump(out, open(a.json, "w"), indent=2)
        print(f"wrote {a.json}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
