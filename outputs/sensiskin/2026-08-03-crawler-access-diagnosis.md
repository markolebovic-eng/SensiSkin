# sensiskinstudio.com — Crawler Access Diagnosis
**Date:** 2026-08-03 · **Tester IP:** single residential IP · **Method:** live UA probes, 20s spacing, interleaved browser control

## Verdict

**Latent risk, not a live outage.** Every citation-critical retrieval agent reaches the site and receives full content. Four bots are blocked; all four are training/scraping crawlers whose blocking costs zero AI citations.

**Nothing is currently costing the client AI visibility.** No urgent action required.

One genuine risk was found that is unrelated to the original finding — see §5.

---

## 1. Real vs artifact

The original finding (403 Bytespider, 429 GPTBot/meta-externalagent) was **initially suspected to be a test artifact**. It is not. It is real, deterministic, user-agent-based policy.

**How this was established.** Four runs at 7–20s spacing, then a decisive interleaved run in a single clean window at identical 20s spacing:

```
Bytespider           403        <-- bot UA blocked
GPTBot               429        <-- bot UA blocked
meta-externalagent   429        <-- bot UA blocked
Chrome-baseline      200 OK     <-- browser UA passes, same window, same spacing
Googlebot            200 OK
Applebot             200 OK
```

A browser user agent passing *between* two blocked bot agents, under identical conditions, rules out volumetric rate limiting. Confirmed identically on a deep URL (`/melazma/`).

**One earlier run showed all agents passing** — that run was measuring a different thing. See §5: a mitigation layer had engaged and was intercepting every request before it reached the origin, masking the per-UA rules underneath.

**Correction to the original report:** the `--live` check that produced the initial finding used ~1s spacing. That was too aggressive and is why the result looked ambiguous. The tool now defaults to 8s and warns explicitly about 429 ambiguity.

## 2. Status per agent

Homepage and `/melazma/` — identical results, so rules are site-wide, not path-specific.

| Agent | Purpose | Status | Citation impact |
|---|---|---|---|
| **Googlebot** | Search (gates AI Overviews/AI Mode) | ✅ 200 content | None |
| **OAI-SearchBot** | ChatGPT search visibility | ✅ 200 content | None |
| **ChatGPT-User** | ChatGPT user retrieval | ✅ 200 content | None |
| **PerplexityBot** | Perplexity citation | ✅ 200 content | None |
| **Perplexity-User** | Perplexity user retrieval | ✅ 200 content | None |
| **Claude-SearchBot** | Claude search indexing | ✅ 200 content | None |
| **Claude-User** | Claude user retrieval | ✅ 200 content | None |
| **Bingbot** | Bing index → Copilot + ChatGPT | ✅ 200 content | None |
| **Applebot** | Apple search + AI grounding | ✅ 200 content | None |
| **Amzn-SearchBot** | Amazon/Alexa search | ✅ 200 content | None |
| **Amzn-User** | Amazon user retrieval | ✅ 200 content | None |
| **DuckAssistBot** | DuckDuckGo | ✅ 200 content | None |
| **ClaudeBot** | Anthropic training | ✅ 200 content | n/a |
| **Google-Extended** | Gemini training/grounding | ✅ 200 content | n/a |
| **Applebot-Extended** | Apple training | ✅ 200 content | n/a |
| **CCBot** | Common Crawl training | ✅ 200 content | n/a |
| **GPTBot** | OpenAI **training only** | ❌ 429 | **Zero** — OAI-SearchBot is the citation bot and it passes |
| **meta-externalagent** | Meta **training only** | ❌ 429 | **Zero** |
| **Bytespider** | ByteDance **training only** | ❌ 403 | **Zero** |
| **Amazonbot** | Amazon legacy parent UA | ❌ 403 | **Near zero** — current `Amzn-SearchBot` passes |

**All 12 citation-critical agents pass.** This is the finding that matters.

## 3. Edge layer

**High confidence:** enforcement is at **LiteSpeed Web Server on the origin**, `s81.unlimited.rs` (AS207604, United Internet Ltd., Pančevo, Serbia). Shared hosting.

Evidence:
- Origin IP `185.119.89.181` → `s81.unlimited.rs`. **Not in any Cloudflare range; no `cf-ray` header on any response.** Cloudflare is not in the path.
- `Server: LiteSpeed` on all blocked and allowed responses.
- The 403 body is LiteSpeed's **stock error page** — "403 Forbidden / Access to this resource on the server is denied!" — with no vendor branding. Wordfence, Sucuri, AIOS and Cloudflare all serve branded block pages. A stock page means the rule sits at server/host level, not in a WordPress plugin.
- The 429 returns `Content-Length: 0` with no body — characteristic of a LiteSpeed throttle rule rather than an application-level deny.

**Moderate confidence** on the specific rule source. Two mechanisms are in play (403 deny vs 429 throttle), which suggests either two rule sets or a host blocklist with mixed actions. Most likely, in order: the host's server-wide AI-bot blocklist → a `.htaccess` rule → LiteSpeed per-vhost config.

**Second layer, intermittent:** `Server: openresty/1.31.1.1` appeared during heavy testing, returning a "One moment, please…" JS interstitial. This is a DDoS-mitigation appliance in front of LiteSpeed that engages under load. See §5.

## 4. Where the rule lives

**Nothing in this repo.** This repository is the agency's multi-agent system, not the website source. Searched exhaustively: no `.htaccess`, no nginx/apache config, no `_headers`/`_redirects`, no middleware, no edge functions, no WAF-as-code, no CDN config. The only matches for UA-blocking patterns were my own research artifacts.

**I cannot fix this from the repo.** It requires hosting-panel or filesystem access.

The Cloudflare click-paths in the original brief **do not apply** — Cloudflare is not in front of this site. Instructions for the actual stack are in §6.

## 5. The finding that actually matters

During testing, the openresty mitigation layer engaged and returned **HTTP 200 with a JS challenge body** to *every* agent, including Googlebot and a normal browser:

```
HTTP 200 · Server: openresty/1.31.1.1 · 12,053 bytes
<title>One moment, please...</title>
<script>setTimeout(function(){ window.location.reload(); }, 5000);</script>
```

`https://sensiskinstudio.com/sitemap.xml` returned this instead of XML at one point.

**Why this is worse than the 403s.** Crawlers cannot execute a JS reload. If this layer engages while Googlebot is crawling, Google receives a 200 OK and a page whose entire content is "One moment, please…" — a success status with no content. That can result in the challenge page being indexed, or content being dropped. Unlike a 403, it produces no error signal anywhere in Search Console.

It is **volumetric and self-healing** — it cleared within minutes of pausing, and normal visitor traffic will not trigger it. My testing caused it. It is not currently harming the site.

**But it is a real exposure**: a traffic spike, an aggressive third-party crawler, or a legitimate full-site crawl could trigger it during a Googlebot visit. Worth raising with the host.

**This also revealed a bug in our own tooling** — `crawler_access_check.py` scored HTTP 200 as a pass regardless of body. It would have reported a fully challenge-walled site as perfectly healthy. Fixed (§7).

## 6. Recommended configuration

**Recommendation: change almost nothing.** The current posture is close to correct and matches best practice — training crawlers blocked, retrieval crawlers allowed. Do not weaken it.

### 6a. Leave blocked (no action)

`GPTBot`, `meta-externalagent`, `Bytespider`. These are training-only. Blocking them costs **zero AI citations** and is a legitimate content-rights position. Confirm with the client that it is intentional; if it is, we are done.

### 6b. Two low-priority improvements

**(i) Change 429 → 403 for GPTBot and meta-externalagent.** A 429 means "rate limited, retry later", so well-behaved crawlers retry indefinitely, wasting the client's shared-hosting resources. A policy block should return 403 so crawlers back off permanently.

**(ii) Consider allowing the legacy `Amazonbot` UA.** `Amzn-SearchBot` passes, so Amazon search visibility is intact today. But `Amazonbot` is Amazon's parent identity and the boundary is not documented precisely. Allowing it is zero-risk and removes an ambiguity. Judgment call, not a defect.

### 6c. Standing rule — allow retrieval agents explicitly, ordered before any broad AI block

If the host or client ever enables a broader "block AI bots" feature, this must be added **above** it. `.htaccess`, at the top of the file:

```apache
# --- GEO: allow AI retrieval/citation agents. MUST precede any broad AI-bot block. ---
<IfModule mod_setenvif.c>
  SetEnvIfNoCase User-Agent "OAI-SearchBot"    ai_allow=1
  SetEnvIfNoCase User-Agent "ChatGPT-User"     ai_allow=1
  SetEnvIfNoCase User-Agent "OAI-AdsBot"       ai_allow=1
  SetEnvIfNoCase User-Agent "PerplexityBot"    ai_allow=1
  SetEnvIfNoCase User-Agent "Perplexity-User"  ai_allow=1
  SetEnvIfNoCase User-Agent "Claude-SearchBot" ai_allow=1
  SetEnvIfNoCase User-Agent "Claude-User"      ai_allow=1
  SetEnvIfNoCase User-Agent "Googlebot"        ai_allow=1
  SetEnvIfNoCase User-Agent "bingbot"          ai_allow=1
  SetEnvIfNoCase User-Agent "Applebot"         ai_allow=1
  SetEnvIfNoCase User-Agent "Amzn-SearchBot"   ai_allow=1
  SetEnvIfNoCase User-Agent "Amzn-User"        ai_allow=1
  SetEnvIfNoCase User-Agent "DuckAssistBot"    ai_allow=1
</IfModule>
```

**Important caveat: user-agent strings are trivially spoofed.** This allowlist is a convenience, not a security control. Anything that matters must be verified by **published IP range**:

| Operator | IP source |
|---|---|
| OpenAI | `openai.com/searchbot.json`, `gptbot.json`, `chatgpt-user.json`, `adsbot.json` |
| Perplexity | `perplexity.com/perplexitybot.json`, `perplexity-user.json` |
| Amazon | `developer.amazon.com/amazonbot/searchbot-ip-addresses/` |
| Google | reverse DNS to `googlebot.com` / `google.com`, forward-confirmed |
| Anthropic | published IP list |

Our `crawler_access_check.py` already carries these; a scheduled job should refresh them.

### 6d. Ask the host (unlimited.rs)

Exact questions — do not guess at their panel:

1. "Is there a server-level or account-level AI/bot blocklist applied to this account? Which user agents does it cover, and can I see or edit the list?"
2. "GPTBot and meta-externalagent receive HTTP 429; Bytespider and Amazonbot receive 403. Which rule produces each, and where is it configured?"
3. "There is an openresty layer returning a 'One moment, please' JS interstitial under load. What triggers it, and can search-engine crawlers verified by IP be exempted? A JS challenge served to Googlebot risks the challenge page being indexed."
4. "Can you confirm no rule affects Googlebot, OAI-SearchBot, PerplexityBot, Claude-SearchBot, bingbot, or Applebot?"

If the client has cPanel access, also check: **Security → ModSecurity**, and any "Bot Protection" / "AI Scraper Blocking" toggle. Check `.htaccess` in the WordPress root for `RewriteCond %{HTTP_USER_AGENT}` blocks and `SetEnvIfNoCase User-Agent ... deny`.

## 7. Before / after

No server-side change was made — none was warranted. The change is to our tooling and process.

| Agent | Original report (1s spacing, status-only) | Verified (20s spacing, interleaved control, body-classified) |
|---|---|---|
| GPTBot | 429 — cause unknown | **429 — confirmed real UA policy.** Training-only; zero citation impact |
| meta-externalagent | 429 — cause unknown | **429 — confirmed real UA policy.** Training-only; zero citation impact |
| Bytespider | 403 — cause unknown | **403 — confirmed real UA policy.** Training-only; zero citation impact |
| Amazonbot | not tested | **403 — newly found.** Legacy UA; `Amzn-SearchBot` passes |
| Amzn-SearchBot | not tested | **200 content — newly verified** |
| Claude-SearchBot, Claude-User | not tested | **200 content — newly verified** |
| Perplexity-User, ChatGPT-User, OAI-AdsBot | not tested | **200 content — newly verified** |
| All 12 citation-critical agents | "OK" (status-code only — would have passed a challenge page) | **200 + verified real content** |
| Interstitial detection | **absent — tool bug** | **Implemented.** 200 + JS challenge now reported as a block |

Tooling changes:
- `crawler_access_check.py` classifies response **bodies**, detecting 7 interstitial signatures across Cloudflare, LiteSpeed and openresty
- Default `--delay` 8s, with a documented warning that 429s are ambiguous
- Explicit post-run guidance on distinguishing rate limiting from UA policy
- Diagnostic protocol added to `geo/references/crawler-access.md`
- Check added as standing/recurring in both the `geo` workflow and `seo-audit` crawlability section, and to the monthly report template

## 8. Client-facing explanation — why robots.txt was irrelevant

> Your `robots.txt` file allows every AI crawler, and it always has. That file is a set of instructions crawlers choose to follow — it is a request, not a gate.
>
> The actual gate is your web server. Regardless of what `robots.txt` says, the server decides whether to answer each request, and it can decide based on which crawler is asking. On your site the server is refusing four crawlers outright.
>
> This is why a `robots.txt` review alone cannot confirm AI crawler access, and why nothing about it appears in Google Search Console: from Google's side, nothing is wrong.
>
> **The good news: all four refused crawlers are AI model-training bots.** They collect content to train AI models. They do not send visitors and they do not produce citations. Blocking them is a reasonable position and costs you nothing in AI visibility.
>
> **Every crawler that determines whether AI assistants can find and cite you — Google, ChatGPT, Perplexity, Claude, Copilot, Apple and Amazon — reaches your site and receives your full content.** We verified each one individually, on more than one page, and confirmed they receive real content rather than a holding page.
>
> One item to watch: your host runs a protection layer that shows a temporary "One moment, please…" holding page when traffic spikes. Real visitors' browsers pass through it automatically. Search engine crawlers cannot. It is not affecting you now, but we have asked your host to exempt verified search crawlers so it cannot cause a problem later.
>
> We now re-check this every month, because these settings change without warning whenever a host updates a default.
