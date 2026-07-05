---
name: firecrawl-credit-baseline
description: Actual measured firecrawl credit cost for a "global-only" topic research run (no competitor scrape) — useful for budgeting future runs
metadata:
  type: project
---

On 2026-07-05, the first SensiSkin topic-research run (global trend flow only, zero competitor
scrapes since competitors.md had no verified URLs yet) cost **17 credits** total:
- 5x `firecrawl search --limit 5` = 2 credits each = 10 credits
- 7x `firecrawl scrape --only-main-content` (single page each, markdown) = 1 credit each = 7 credits

Measured via `firecrawl --status` before (1,014) and after (997).

**Why this matters:** This confirms the credit-cost-data estimate already logged elsewhere
(scrape/map = 1 credit/page, search = 2 credits/10 results) actually holds in practice, and
gives a concrete anchor: a "global only" run comfortably fits in the 10-20 credit default
budget with room left over for competitor scraping once competitors.md URLs are confirmed.

**How to apply:** When competitors.md URLs are confirmed and a future run adds competitor
map+scrape on top of this same global flow, budget ~1 credit per competitor page scraped
(map itself may add a handful more per site depending on subpages fetched). A run scraping
~9 competitor blog/service pages on top of this global flow would land around 26-30 credits
total — flag to the user if that exceeds the 10-20 default budget, per the research agent's
own credit-discipline rule.
