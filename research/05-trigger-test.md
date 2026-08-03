# 05 — Trigger Test

20 realistic client requests routed against the final skill descriptions. Checked by reading each `description` field and confirming which skill claims the phrasing and which explicitly disclaims it.

| # | Client request | Expected | Routes to | Pass |
|---|---|---|---|---|
| 1 | "Zašto se ne pojavljujemo u ChatGPT-u?" / "Why don't we show up in ChatGPT?" | geo | geo — verbatim trigger phrase | ✅ |
| 2 | "We need GEO for our site" | geo | geo — 'GEO' | ✅ |
| 3 | "Can you do AEO / answer engine optimization?" | geo | geo — 'AEO', 'answer engine optimization' | ✅ |
| 4 | "How do we get into Google AI Overviews?" | geo | geo — 'AI Overviews' | ✅ |
| 5 | "Are AI bots blocked on our site?" | geo | geo — 'are AI bots blocked' | ✅ |
| 6 | "Should we add an llms.txt file?" | geo | geo — 'llms.txt' | ✅ |
| 7 | "Our organic traffic dropped 30% last month" | seo-audit | seo-audit — 'my traffic dropped'; geo disclaims pure-organic-no-AI | ✅ |
| 8 | "Run a technical SEO audit" | seo-audit | seo-audit | ✅ |
| 9 | "Add FAQ schema to our service pages" | schema | schema — 'FAQ schema' | ✅ |
| 10 | "Will an AI assistant be able to book an appointment on our site?" | agentic-readiness | agentic-readiness — 'will an AI be able to book with us' | ✅ |
| 11 | "What's UCP and do we need it?" | agentic-readiness | agentic-readiness — 'UCP' | ✅ |
| 12 | "Build 200 city landing pages" | programmatic-seo (+ risk gate) | programmatic-seo; description now mandates reading geo risk-register first | ✅ |
| 13 | "AI SEO please" | geo | geo — 'AI SEO'; ai-seo is deprecated and redirects | ✅ |
| 14 | "Why does Perplexity cite our competitor and not us?" | geo | geo — 'why doesn't Perplexity mention us' | ✅ |
| 15 | "Improve our AI search visibility" | geo | geo — 'AI search visibility' | ✅ |
| 16 | "Our Core Web Vitals are failing" | seo-audit | seo-audit — 'core web vitals' | ✅ |
| 17 | "Set up tracking so we can see AI traffic" | geo (then analytics) | geo owns AI-referral segmentation (G3); analytics for GA4 plumbing | ✅ |
| 18 | "Do we need to worry about LLMO?" | geo | geo — 'LLMO' | ✅ |
| 19 | "Should we block GPTBot?" | geo | geo — 'are AI bots blocked' + crawler-access reference | ✅ |
| 20 | "Write a blog post about skincare trends" | copywriting / content-strategy | Neither geo nor seo-audit claims content production | ✅ |

**20/20 route correctly.**

## Misfires found and fixed during the test

| Issue | Fix applied |
|---|---|
| "AI SEO" and "GEO" matched both `ai-seo` and the new `geo` | `ai-seo` description rewritten to start with "DEPRECATED — superseded by the geo skill… invoke geo instead" |
| "AI Overviews" ambiguous between geo and seo-audit | `seo-audit` description now scoped to "Google/Bing organic rankings, with no AI-surface component" and explicitly hands off AI phrasings to geo |
| Risk of both geo and seo-audit running on one GEO engagement (duplicated work) | Both descriptions state the umbrella relationship explicitly: "do not run both" |
| "structured data" could pull geo instead of schema | geo description bounds it: "For structured data implementation invoked as its own task, see schema" |
| "AI agents" ambiguous between geo and agentic-readiness | Both descriptions draw the line at citation (geo) vs acting on the site (agentic-readiness) |

## Boundary statements now present in every description

- **geo** — umbrella; owns AI visibility on all engines; embeds SEO; hands off to schema and agentic-readiness
- **seo-audit** — Google/Bing organic only; hands off all AI phrasings to geo
- **schema** — structured data implementation; invoked by geo and seo-audit
- **agentic-readiness** — agents acting; hands off citation questions to geo
- **programmatic-seo** — gated on the geo risk register
- **ai-seo** — deprecated pointer
