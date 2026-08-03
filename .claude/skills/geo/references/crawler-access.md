# Crawler Access — Every AI User Agent and Control

Verified against primary vendor documentation, 2026-08-03. Every row traces to an official source.

**The core insight:** most engines run **separate bots for training and for search/citation**, with independent controls. The famous bot is usually the training one. Blocking it costs zero citations; blocking the quiet one costs all of them.

---

## The table

| Bot / token | Operator | Purpose | Citation-critical | Respects robots.txt | Source |
|---|---|---|:---:|---|---|
| `Googlebot` | Google | Search — and the gate for AI Overviews / AI Mode | **Yes** | Yes | `/crawling/docs/crawlers-fetchers/google-common-crawlers` |
| `Google-Extended` | Google | Training + grounding for **Gemini Apps and Vertex AI only** | No | Yes (control token, no separate UA) | same |
| `Google-Agent` | Google | AI agents; experimental Web Bot Auth signing as `agent.bot.goog` | Emerging | Yes | `/crawling/docs/crawlers-fetchers/web-bot-auth` |
| `OAI-SearchBot` | OpenAI | **Search — governs ChatGPT search visibility** | **Yes** | Yes | `platform.openai.com/docs/bots` |
| `GPTBot` | OpenAI | Foundation-model training only | No | Yes | same |
| `ChatGPT-User` | OpenAI | User-initiated fetch; **not** used to determine Search appearance | Yes (UX) | **"may not apply"** | same |
| `OAI-AdsBot` | OpenAI | Validates ChatGPT ad landing pages; not used for training | If running ads | Yes | same |
| `Claude-SearchBot` | Anthropic | **Search indexing — governs Claude search visibility** | **Yes** | Yes | `support.anthropic.com/.../8896518` |
| `Claude-User` | Anthropic | User-initiated retrieval | **Yes** | Yes | same |
| `ClaudeBot` | Anthropic | Training only | No | Yes | same |
| `PerplexityBot` | Perplexity | **Search/citation — explicitly not used for model training** | **Yes** | Yes | `docs.perplexity.ai/guides/bots` |
| `Perplexity-User` | Perplexity | User-initiated | **Yes** | **"generally ignores robots.txt"** | same |
| `bingbot` | Microsoft | Search index behind Copilot and ChatGPT | **Yes** | Yes | Bing |
| `Amzn-SearchBot` | Amazon | Search (e.g. Alexa); no training | **Yes** | Yes | `developer.amazon.com/amazonbot` |
| `Amzn-User` | Amazon | User-initiated | **Yes** | **"may not follow all"** | same |
| `Applebot` | Apple | Search (Siri, Spotlight, Safari) + AI grounding | **Yes** | Yes | `support.apple.com/en-us/119829` |
| `Applebot-Extended` | Apple | Training opt-out only; does not crawl | No | Control token | same |
| `meta-externalagent` | Meta | Training | No | Reported unreliable | third-party (Tier C) |
| `Bytespider` | ByteDance | Training | No | Reported unreliable | third-party (Tier C) |
| `CCBot` | Common Crawl | Training corpus | No | Yes | `commoncrawl.org/ccbot` |
| `DuckAssistBot` | DuckDuckGo | Search/assist | Yes | Yes | DuckDuckGo |

---

## Per-engine control notes that differ from Google

These are the details that make a GEO audit different from an SEO audit.

**OpenAI**
- Settings are independent. Allow `OAI-SearchBot`, disallow `GPTBot` → visible in ChatGPT search, excluded from training. This is the default recommendation for most clients.
- Opting out of `OAI-SearchBot` means the site "will not be shown in ChatGPT search answers, though can still appear as navigational links."
- **~24h propagation** from a robots.txt change.
- IP ranges: `openai.com/searchbot.json`, `gptbot.json`, `chatgpt-user.json`, `adsbot.json`.

**Anthropic**
- Supports the non-standard **`Crawl-delay`** directive. Google does not. Amazon does not.
- Reads robots.txt **per host** — every subdomain needs its own rules.
- IP blocking is explicitly discouraged as an opt-out: it prevents Anthropic reading robots.txt at all, so the opt-out may not register.

**Perplexity**
- Publishes step-by-step **Cloudflare and AWS WAF** allowlisting procedures — match on User-Agent **AND** source IP, action Allow, priority above blocking rules.
- Advises automating IP-range refresh from the JSON endpoints.
- `Perplexity-User` ignores robots.txt by design; blocking it requires an edge rule.

**Apple**
- `isAccessibleForFree: false` in structured data excludes a page from AI-grounded answers while keeping it search-eligible. **Page-level only — `hasPart` section-level markup is not supported.**
- `nosnippet` opts content out of broad world-knowledge AI answers.
- Disallowing `Applebot-Extended` does not remove pages from search; it only governs training use.

**Amazon**
- Honours **`noarchive`** as "do not use the page for model training" — a directive Google deprecated.
- Does **not** support `crawl-delay`.
- Caches robots.txt for up to **30 days**; reads per host.
- If robots.txt omits `Amzn-SearchBot` but allows other search bots, it follows the rules given to those.

**Google**
- **Google-Extended does not affect Google Search inclusion or ranking.** It governs Gemini Apps and Vertex AI only.
- AI Overviews / AI Mode: controlled by Googlebot robots.txt for access, and `nosnippet` / `data-nosnippet` / `max-snippet` / `noindex` for what may be shown.
- **Hard eligibility gate:** a site must be *included in Search generative AI features* in Search Console. UK-first rollout, CMA-driven. Not a core-search ranking signal, but opted-out sites receive no AI traffic or impressions. **Check this on every engagement.**

---

## Recommended default robots.txt

For a client who wants maximum AI citation visibility and no model training:

```
# Search & citation - allow (these determine whether AI engines can cite you)
User-agent: Googlebot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: bingbot
Allow: /

User-agent: Amzn-SearchBot
Allow: /

User-agent: Applebot
Allow: /

User-agent: DuckAssistBot
Allow: /

# Model training - client decision. Blocking these costs ZERO citations.
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: meta-externalagent
Disallow: /

# Rate limiting - honoured by Anthropic, ignored by Google and Amazon
User-agent: Claude-SearchBot
Crawl-delay: 1

User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
```

Two caveats to state to the client:
1. Blocking `Google-Extended` removes the site from Gemini app grounding. If Gemini visibility matters to them, allow it. It has no effect on AI Overviews either way.
2. `Perplexity-User`, `ChatGPT-User` and `Amzn-User` may fetch regardless. Genuine exclusion needs an edge rule.

---

## Diagnostic protocol — run this before reporting any access failure

Learned the hard way on a live client site. Skipping step 1 produces confident, wrong findings.

**Step 1 — rule out your own test.** Rapid sequential requests from one IP trip volumetric rate limiting that is indistinguishable from user-agent policy. Re-test with `--delay 9` or higher, at least twice.

**Step 2 — interleave a browser control.** Put a normal Chrome user-agent *between* the failing agents in the same run. This is the decisive test:

| Observation | Conclusion |
|---|---|
| Browser UA passes while bot UAs fail, **in the same window, same spacing** | **Real user-agent policy.** Deterministic. Act on it. |
| Everything fails together, and recovers after a pause | **Volumetric rate limiting** tripped by your test. Not a finding. Discard. |
| Failures move between agents across runs | Rate-limit noise. Discard. |

**Step 3 — classify the 200s.** A 200 is not proof of access. Check for a challenge interstitial. If the body contains "One moment, please", "Just a moment...", "Checking your browser", or `window.location.reload()`, the crawler got nothing.

**Step 4 — read the status code as policy signal.**

| Code | Usual meaning |
|---|---|
| **403** | Explicit deny rule. Deterministic, stable across runs. |
| **429** | Ambiguous — either a deliberate throttle-to-zero policy, or genuine rate limiting. **Always confirm with step 2.** |
| **200 + interstitial** | Bot-challenge layer engaged. Worst case: applies to *all* agents including Googlebot. |
| **503 + interstitial** | Same, with an honest status code. |

**Step 5 — identify the layer before recommending a fix.** Capture `Server`, `cf-ray`, `x-served-by`, `via`, `x-sucuri-id`, and the 403 body. Do not assume Cloudflare — many hosts run their own mitigation.

| Evidence | Layer |
|---|---|
| `cf-ray` header present | Cloudflare — use the dashboard click-paths below |
| `Server: LiteSpeed`, stock "403 Forbidden / Access to this resource on the server is denied!" | LiteSpeed at origin — `.htaccess`, server-level blocklist, or host default |
| `Server: openresty` + "One moment, please" interstitial | Host-level DDoS mitigation appliance in front of origin |
| `x-sucuri-id` | Sucuri WAF |
| Branded block page (Wordfence, AIOS, Solid Security) | WordPress security plugin |

A stock server error page rather than a branded one means the rule is at **server or host level**, not in a plugin — which usually means it is not in the repo and not in the site's admin.

## WAF / CDN audit — the step nobody runs

robots.txt permission is meaningless if the edge returns 403. This is common, silent, and entirely fixable.

1. Run `scripts/crawler_access_check.py <site> --live`. Any citation-critical bot with `ALLOW` in robots but a non-200 live status is an edge block.
2. In **Cloudflare**: check Bot Fight Mode, Super Bot Fight Mode, managed WAF rules, rate limiting, and any "block AI scrapers" toggle (Cloudflare ships one, and it is on by default for some plans — it blocks citation bots too).
3. Add allow rules matching **User-Agent AND source IP** from the published JSON endpoints, with priority above blocking rules.
4. Automate IP-range refresh — the endpoints change.
5. Re-run `--live` to confirm 200 for every allowed bot.

**Interpreting results:** 403 is a deliberate block. 429 is rate limiting — may be transient, re-test before reporting. 503 from an edge with an interstitial usually means a JS challenge, which bots cannot pass.

## Bot verification

User-agent strings are trivially spoofed. Before acting on log data:
- **Google**: reverse DNS to `googlebot.com` / `google.com`, then forward-confirm.
- **OpenAI, Perplexity, Amazon**: match source IP against the published JSON ranges.
- **Web Bot Auth** (experimental): cryptographic signature, `agent.bot.goog` for Google agents. Google explicitly says to keep IP/rDNS/UA verification as the fallback — not every request is signed.
