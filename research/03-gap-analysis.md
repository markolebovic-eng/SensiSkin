# 03 — Gap Analysis: Before / After

## Architecture

| | Before | After |
|---|---|---|
| AI-search skills | `ai-seo` (485 lines, 3 refs, 0 scripts) | `geo` umbrella (190-line SKILL.md, 11 refs, 3 tested scripts, 3 templates) + `agentic-readiness` |
| GEO/SEO relationship | Siblings, ~40% duplicated, unclear routing | GEO is the umbrella and embeds SEO; explicit boundaries in both descriptions |
| Executable tooling | **None across all five search skills** | 3 scripts, each tested against live sites |
| Client templates | None | Audit report, monthly report, prompt-set CSV — no confidence-tier language |
| Evidence base | Uncited vendor figures | 178 primary Google pages + 6 official engine crawler docs + the KDD paper, in a tiered ledger |
| Google corpus coverage | ~22% | ~65% of the pages that bear on AI visibility; full crawler-infrastructure tree |

## Factual corrections shipped

Six claims in the old skill were wrong in ways a client's developer could catch. All corrected, and preserved in the deprecated `ai-seo/SKILL.md` so they aren't reintroduced.

1. **Google-Extended does not control AI Overviews.** It governs Gemini Apps and Vertex AI. Google states it "does not impact a site's inclusion in Google Search."
2. **OAI-SearchBot, not GPTBot,** governs ChatGPT search visibility. GPTBot is training only.
3. **Claude-SearchBot and Claude-User** drive Claude visibility; `anthropic-ai` is no longer listed by Anthropic; the Brave-backend claim was unsourced.
4. **AI-specific Search Console reporting exists** since 2026-06-03.
5. **The GEO paper's per-method percentage table was invented.** The real Table 2 shows effects inverting by rank.
6. **Google recommends structured data** for rich results in the same paragraph where it says it isn't required for AI features.

## New capabilities that did not exist before

| # | Capability | Why it matters |
|---|---|---|
| 1 | **GSC generative-AI inclusion check** | Google-documented hard eligibility gate. A client who is off it has zero AI Overview visibility regardless of everything else. |
| 2 | **WAF/CDN access audit with live per-UA testing** | The most common silent cause of zero AI visibility. Invisible in Search Console. Verified working — it found real edge-level divergence on the client's own site (403 for Bytespider, 429 for GPTBot and meta-externalagent, while robots.txt allowed all). |
| 3 | **Eight citation-critical user agents** previously absent | OAI-SearchBot, Claude-SearchBot, Claude-User, Perplexity-User, OAI-AdsBot, Amzn-SearchBot, Amzn-User, Google-Agent. |
| 4 | **IP-range verification** via published JSON endpoints | Real bot verification instead of trusting spoofable UA strings. |
| 5 | **Rank-stratified content tactics** | The KDD Table 2 inversion. A genuine specialist position, and the opposite of standard GEO advice. |
| 6 | **Snippet-eligibility as an AI check** | `nosnippet` / `max-snippet:0` leave a page indexed and AI-ineligible. Standard indexability audits pass it. |
| 7 | **`isAccessibleForFree` as an Apple AI control** | Structured data as a per-engine AI control surface. |
| 8 | **`noarchive` as Amazon's training opt-out** | A Google-deprecated tag with live commercial meaning elsewhere. |
| 9 | **Per-engine propagation and caching SLAs** | ~24h for OpenAI/Perplexity; up to 30 days for Amazon; days-to-months for Google recrawl. |
| 10 | **Per-engine prompt-set citation baseline** | The only cross-engine visibility measurement that exists, with a method that makes it defensible. |
| 11 | **Objection-handling script** | Answers "Google says GEO isn't real" from primary sources, including two Google sentences that support us. |
| 12 | **Risk register with compliant variants** | Every risky tactic has a compliant version that achieves the same goal, not a refusal. |
| 13 | **`agentic-readiness` skill** | New sellable line item in genuinely new territory. |
| 14 | **Web Bot Auth readiness** | Emerging cryptographic bot verification. |

## Competitive coverage test (Phase 1G)

Checked against the deliverable categories a prospect would find in an established GEO/AEO offering.

| Category a competitor offers | Covered? |
|---|---|
| AI visibility audit | Yes — full workflow |
| AI bot access / robots.txt | Yes — 22 UAs, exceeds typical scope (WAF layer is rarely offered) |
| Brand/citation monitoring across engines | Yes — G4, G5, with method |
| Share of voice vs competitors | Yes — G5 |
| Content optimization for citation | Yes — C1–C11, with rank stratification competitors don't have |
| Schema / structured data | Yes — D1–D7 |
| llms.txt implementation | Yes — with honest per-engine status |
| Entity / knowledge graph | Yes — D2, F1–F6 |
| Technical SEO foundation | Yes — embedded, not sold separately |
| AI referral analytics | Yes — G3 |
| Prompt/query research | Yes — C6 fan-out mapping, prompt-set design |
| Competitor citation gap analysis | Yes — in audit template §2 |
| Reporting and dashboards | Yes — templates |
| Agentic/AI-commerce readiness | Yes — separate skill; most competitors don't offer this |
| Ecommerce feed optimization | **Partial** — D7 only. Full Merchant Center depth deferred; no ecommerce client currently. |
| Site migration under AI surfaces | **Not covered** — deferred. |

Two gaps, both deliberate deferrals with no current client need, recorded rather than papered over.

## Remaining gaps

| Gap | Plan |
|---|---|
| `ecommerce-seo` skill (9 ecom pages + 7 shopping schema guides + Merchant Center) | Build when an ecommerce client signs |
| `site-migration` skill | Build when a replatform is scoped |
| Full 39-page structured-data matrix + validated recipes | `schema` skill expansion — next pass |
| Raw-vs-rendered diff script (B2) | Needs headless browser; specified, not yet built |
| Internal link graph script (B4) | Specified, not yet built |
| AI-referral log parser (G3) | Specified, not yet built |
| Per-engine citation tracker script (G4) | Needs API keys per engine; manual method documented and usable now |
| Bing/Microsoft primary documentation | Fetch blocked — see `04-open-questions.md` |
| Meta crawler primary documentation | HTTP 400 — see `04-open-questions.md` |
