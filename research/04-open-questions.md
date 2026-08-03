# 04 — Open Questions, Monitoring List, Re-Research Triggers

Explicit unknowns are worth more than confident guesses. Each entry says what we don't know, why we don't know it, and how to close it.

## Unresolved

| # | Question | Why unresolved | How to close |
|---|---|---|---|
| 1 | Does **any** consumer AI engine consume third-party `llms.txt`? | Only Google has published a position (it does not). No other vendor has stated either way. OpenAI and Perplexity publish `llms.txt` for **their own docs** — that endorses the pattern for docs ingestion, not for their crawlers reading yours. | Controlled test: deploy `llms.txt` on a low-traffic property listing a URL not linked anywhere else, then watch logs for fetches of that URL by each AI UA. Only real evidence available. |
| 2 | Do agent frameworks / dev-tool crawlers / MCP tooling consume `llms.txt`? | Partially evidenced by the OpenAI/Perplexity docs pattern; not systematically surveyed. | Survey agent framework docs (LangChain, LlamaIndex, Firecrawl, Browserbase) for `llms.txt` support. Half a day. |
| 3 | Microsoft/Bing AI crawler tokens and Copilot answer guidance | `bing.com/webmasters/help/...` returned a JS shell with an empty body via both curl and WebFetch. | Escalate to a headless browser, or use Bing Webmaster Tools help via a different entry point. **Highest-priority remaining harvest gap** — Bing's index feeds both Copilot and ChatGPT. |
| 4 | Meta crawler primary documentation | `developers.facebook.com` returned HTTP 400 on two URL variants. | Retry with a browser session or via Meta's business help centre. |
| 5 | Do ChatGPT, Perplexity or Claude weight structured data in citation selection? | No engine has documented it. The widely repeated "30–40% higher AI visibility with schema" has no traceable source. | Likely unclosable from public sources. Could be approached with a controlled prompt-set experiment on matched pages. Until then: implement schema for the reasons that *are* evidenced, never claim this one. |
| 6 | Has the GSC AI-features inclusion toggle rolled out beyond the UK? | Google stated UK-first with intent to expand; no timing published. | Check Search Console on each client property; watch Search Central blog. |
| 7 | xAI/Grok, Mistral, DuckDuckGo crawler specifics | Not reached this pass. Third-party listicles only (Tier C). | Fetch primary docs. Low priority — small citation share. |
| 8 | Sitemap-based cross-check of the Google docs URL inventory | `developers.google.com` rate-limited the 40-part nested sitemap fetch: HTTP 500 above 4 concurrent, timeouts at or below 4. | Re-run with 1 request per 3–5 seconds over a longer window, or fetch individual parts across sessions. **Low priority** — the nav parse (178) sits inside the expected 180–220 band and every structured-data feature page listed in the search gallery was present. |
| 9 | Whether AI Overview impressions are counted per-appearance or per-scroll-into-view | GSC help documents impressions for AI features but the counting methodology differs between AI Overviews and AI Mode without full detail. | Read `support.google.com/webmasters/answer/16984139` in full plus the linked counting docs. Matters for how we frame impression trends. |

## Monitoring list — what to re-check and how often

| Source | Cadence | Watch for | Diff method |
|---|---|---|---|
| `/search/docs/fundamentals/ai-optimization-guide` | **Monthly** | The single most volatile page. Rewritten 2026-07-10. Any change to the mythbusting section or the inclusion requirement | Re-scrape, diff against `research/raw/pages/*.md` |
| `/search/docs/appearance/ai-features` | Monthly | Whether it catches up on the Generative AI performance report | same |
| Search Central Blog | **Weekly** | AI features, crawler changes, GSC reports, core/spam updates | RSS |
| `/search/updates` | Monthly | Documentation change log | same |
| `/crawling/docs/changelog` | Monthly | Crawler and robots.txt changes | same |
| `/crawling/docs/crawlers-fetchers/web-bot-auth` | Quarterly | Movement from experimental to stable | same |
| `platform.openai.com/docs/bots.md` | **Monthly** | New bots (OAI-AdsBot appeared this way), policy changes | Fetch the `.md` variant — cheap and diffable |
| `support.anthropic.com/.../8896518` | Monthly | Bot roster changes | Article carries a visible date |
| `docs.perplexity.ai/guides/bots.md` | Monthly | WAF guidance, IP endpoints | `.md` variant |
| `support.apple.com/en-us/119829` | Quarterly | Applebot controls | — |
| `developer.amazon.com/amazonbot` | Quarterly | Bot renames — already happened once | — |
| IP JSON endpoints (all 8) | **Weekly, automated** | Range changes that would break WAF allowlists | Diff the JSON |
| `llmstxt.org` + adoption | Quarterly | Any engine announcing consumption | — |
| `ucp.dev` | Quarterly | Protocol maturity, adoption | — |
| arXiv / KDD / SIGIR | Quarterly | GEO replication, RAG citation-selection research | Search "generative engine optimization", "LLM citation selection" |
| GSC on each client property | Monthly | Gen-AI report availability, inclusion toggle appearing | — |

## Re-research triggers — drop everything and re-run

1. **Google publishes a new AI-features doc or rewrites the AI optimization guide.** It has moved materially twice in eight months.
2. **Any engine announces `llms.txt` consumption.** Immediately upgrades E1 from unresolved to a Tier-A deliverable and changes how we sell it.
3. **The GSC AI-features inclusion toggle rolls out to a client's market.** Becomes a mandatory check with a real chance of accidental opt-out.
4. **Any engine adds or renames a crawler.** Update `crawler-access.md`, the script's `BOTS` table, and the recommended robots.txt together.
5. **Web Bot Auth leaves experimental status.** Bot verification methodology changes industry-wide.
6. **A GEO replication study publishes.** Our strongest independent evidence is a single unreplicated paper.
7. **Google adds click data to the Generative AI performance report.** Would make AI-specific CTR computable and change every report template.
8. **A client receives a manual action.** Re-audit the risk register against what triggered it.

## Standing re-run procedure

The harvest is scripted and reproducible:

```bash
cd research/raw
python scrape.py          # re-scrapes all 178 Google URLs, skips unchanged, writes scrape_index.json
python fetch_engines.py    # re-fetches engine crawler docs
git diff research/raw/pages/    # the diff IS the changelog
```

`scrape.py` records the `Last updated ... UTC` footer per page. **Remember that 115 of 178 pages carry the same 2025-12-10 bulk-republish timestamp** — treat that date as "unknown true age", not "recently reviewed". Only dates that differ from it carry signal.
