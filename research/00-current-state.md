# 00 — Current State Audit

Date: 2026-08-03. Scope: every search-related skill in `.claude/skills/`.

## Inventory

| Skill | SKILL.md | References | Scripts | Templates |
|---|---|---|---|---|
| `ai-seo` | 485 lines, v2.0.1 | `content-patterns.md` (285), `content-types.md` (71), `platform-ranking-factors.md` (152) | none | none |
| `seo-audit` | 497 lines, v2.0.0 | `ai-writing-detection.md` (200), `international-seo.md` (230) | none | none |
| `schema` | 179 lines | `schema-examples.md` (398) | none | none |
| `site-architecture` | 357 lines | 3 refs (814 total) | none | none |
| `programmatic-seo` | 238 lines | `playbooks.md` (308) | none | none |

Adjacent: `content-strategy`, `competitors`, `directory-submissions`, `analytics`. Also a `seo` **agent** (`.claude/agents/seo.md`) wired to ~40 `google-seo-mcp` tools, and a `market-seo` skill (content audit).

**Zero executable scripts across all five skills.** Everything is prose instruction. This is the single largest structural gap: a GEO engagement is substantially a technical audit, and we have no tooling to perform it.

---

## Factual assertion audit

Every substantive claim in `ai-seo` and the shared references, tagged against the Phase 1 harvest.

### `[CONTRADICTED]` — actively wrong, will embarrass us in front of a client's developer

| # | Claim | Where | What's actually true | Source |
|---|---|---|---|---|
| C1 | "**Google-Extended** — Google Gemini and AI Overviews" (listed as the AI-Overviews opt-out) | `ai-seo` SKILL.md L164; `platform-ranking-factors.md` L124 | Google-Extended controls **training + grounding for Gemini Apps and Vertex AI only**. Google states verbatim: "Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal in Google Search." AI Overviews/AI Mode are governed by **Googlebot robots.txt + `nosnippet`/`max-snippet`/`data-nosnippet`/`noindex`**. Advising a client to block Google-Extended to control AI Overviews does nothing; advising they allow it to *get into* AI Overviews is equally wrong. | `/crawling/docs/crawlers-fetchers/google-common-crawlers`; `/search/docs/appearance/ai-features` |
| C2 | "there is **no AI-specific Search Console reporting**" | `ai-seo` SKILL.md L413 | False since **2026-06-03**. Google launched dedicated **Generative AI performance reports** for Search and Discover. Impressions, pages, countries, devices, dates (hourly→monthly). Rolling out to a subset of properties. | `/search/blog/2026/06/gen-ai-performance-reports` |
| C3 | Princeton GEO per-method table: Cite sources +40%, Statistics +37%, Quotations +30%, Authoritative +25%, Clarity +20%, Technical terms +18%, Unique vocab +15%, Keyword stuffing **−10%** | `ai-seo` SKILL.md L208–220 | **These numbers are not in the paper.** See the dedicated section below. The real Table 2 is more useful *and* points the opposite direction for high-ranking clients. | Aggarwal et al., KDD '24, arXiv:2311.09735v3 |
| C4 | "**Claude** uses Brave Search as its search backend… Allow ClaudeBot and **anthropic-ai** user agents" | `platform-ranking-factors.md` L98–110 | Anthropic's current crawler doc (updated **2026-04-07**) lists exactly three bots: **ClaudeBot** (training), **Claude-User** (user-initiated retrieval), **Claude-SearchBot** (search indexing). `anthropic-ai` is not listed. `Claude-SearchBot` — the one that governs search visibility — is **absent from our skill entirely**. The Brave-backend claim is unsourced and not supported by Anthropic's docs. | `support.anthropic.com/en/articles/8896518` |
| C5 | "**GPTBot** and ChatGPT-User — OpenAI (ChatGPT)" as the citation-relevant bots | `ai-seo` SKILL.md L161; `platform-ranking-factors.md` L119 | Backwards. **OAI-SearchBot** is the one that governs ChatGPT search visibility — and it is missing from our list. GPTBot is **training only**; blocking it costs zero citations. OpenAI: "Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers." And "ChatGPT-User is not used to determine whether content may appear in Search." We have the client optimising the wrong two bots and omitting the only one that matters. | `platform.openai.com/docs/bots.md` |
| C6 | "**Bingbot** — Microsoft Copilot (via Bing)" listed under AI bot access | `ai-seo` SKILL.md L164 | Not wrong, but incomplete to the point of being misleading — see `[UNSOURCED]` U7. | — |

### `[OUTDATED]` — was true, no longer is / superseded

| # | Claim | Correction |
|---|---|---|
| O1 | Google's guide "explicitly says you don't need new markup, AI files, or markdown" framed as the whole of Google's position | Still accurate as far as it goes, but the **2026-07-10** rewrite of `/search/docs/fundamentals/ai-optimization-guide` added a **hard eligibility gate we do not mention anywhere**: "a site must be **included in Search generative AI features in Search Console** to be eligible for display in generative AI features on Google Search." See G1 in the gap map — this is the single most important addition in this whole research pass. |
| O2 | "AI Overviews appear in ~45% of Google searches"; "reduce clicks by up to 58%"; "6.5x more likely cited via third-party"; "optimized content cited 3x more" | All four are undated, unattributed vendor figures. Not necessarily false, but not defensible. Must be re-sourced with study + date + N or dropped from client-facing use. |
| O3 | `platform-ranking-factors.md` cites "SE Ranking domain authority study" and "ZipTie content-answer fit analysis" with precise percentages (40%/35%/25% split; 55% content-answer fit; 3.2x freshness; 8.4 vs 6 citations) | No URLs, no dates, no methodology in our file. Unverifiable as written. Tier C at absolute best; currently presented with the confidence of Tier A. |

### `[UNSOURCED]` — plausible, shipped, but no citation

| # | Claim |
|---|---|
| U1 | "Content with proper schema shows 30-40% higher AI visibility on non-Google AI engines" |
| U2 | "Only about 15% of AI Overview sources overlap with conventional organic results" |
| U3 | "authoritative citations correlate with a 132% visibility boost… authoritative tone adds another 89%" (`platform-ranking-factors.md` L25) — note this looks like a garbled restatement of the GEO paper's Table 2 rank-5 figures |
| U4 | Content-type citation share table (comparison 33%, guides 15%, research 12%…) |
| U5 | Perplexity "prioritizes publicly accessible PDFs"; "maintains curated lists of authoritative domains (Amazon, GitHub…)"; "time-decay algorithm" |
| U6 | Copilot "sub-2-second load times are a clear threshold"; LinkedIn/GitHub "ranking boosts" |
| U7 | Wikipedia 7.8% / Reddit 1.8% / Forbes 1.1% of ChatGPT citations |
| U8 | `/pricing.md` and `AGENTS.md` as agent-consumed files — no evidence any engine reads either |

### `[SOURCED]` — verified against primary docs this pass

Query fan-out (with Google's own lawn-weeds example); RAG/grounding definition; scaled content abuse risk from per-query-variation page generation; "no ideal page length"; structured data not *required* for AI features but recommended for rich results; agentic access via screenshots + DOM + accessibility tree; UCP as emerging; Merchant Center + Business Profile for AI-surfaced commerce/local; nosnippet/data-nosnippet/max-snippet as the real Google AI preview controls; blocked crawler ⇒ no citation.

---

## The GEO paper table — what we published vs what the paper says

This is worth its own section because it is our most-quoted piece of evidence and it is currently wrong in a way that would reverse our advice for a client's best pages.

**What the paper (Aggarwal et al., *GEO: Generative Engine Optimization*, KDD '24, arXiv:2311.09735) actually reports:**

- Benchmark: **GEO-bench, 10,000 queries** across domains. Metrics: **Position-Adjusted Word Count** (objective: citation word count weighted by position) and **Subjective Impression** (LLM-judged: relevance, influence, uniqueness, click likelihood, diversity).
- Headline: GEO "can boost visibility by **up to 40%**."
- Top three methods — **Cite Sources, Quotation Addition, Statistics Addition** — achieved **30–40% relative improvement on Position-Adjusted Word Count** and **15–30% on Subjective Impression**.
- Best single method beat baseline by **41%** (PAWC) / **28%** (Subjective Impression).
- Real-world validation on **Perplexity.ai: up to 37%**.
- Keyword Stuffing "doesn't perform well" — the paper publishes **no −10% figure**.

**Table 2 — relative improvement (%) in visibility by the source's existing SERP rank.** This table is not in our skill at all and it is the most commercially important thing in the paper:

| Method | Rank-1 | Rank-2 | Rank-3 | Rank-4 | Rank-5 |
|---|---:|---:|---:|---:|---:|
| Cite Sources | **−30.3** | +2.5 | +20.4 | +15.5 | **+115.1** |
| Quotation Addition | **−22.9** | −7.0 | +3.5 | +25.1 | **+99.7** |
| Statistics Addition | **−20.6** | −3.9 | +8.1 | +10.0 | **+97.9** |
| Authoritative | −6.0 | +4.1 | −0.6 | +12.6 | +6.1 |
| Fluency Optimization | −2.0 | +5.2 | +3.6 | −4.4 | +2.2 |

Three consequences:

1. **The 115% figure is real** — but it is specifically *Cite Sources, applied to a rank-5 source*. Our skill states "Low-ranking sites benefit even more — up to 115%" which is roughly right by luck, while the per-method table above it is invented.
2. **These tactics measurably hurt rank-1 sources (−20% to −30%).** GEO content tactics are a **challenger strategy**. For a client who already ranks #1 for a query, aggressively adding citations/quotes/statistics to that page can *reduce* their citation share. Nothing in our current skill hints at this, and it is exactly the kind of nuance that makes us look like specialists.
3. Table 3 gives **per-domain best method** (e.g. Cite Sources → Law & Gov, Factual statements; Statistics Addition → Law & Gov, Debate, Opinion; Fluency → Business, Science, Health). We do no domain targeting at all.

**Limits to state honestly internally:** simulated generative engine for the main results (Perplexity was a separate, smaller real-world check); 2023–24 vintage, pre-dating AI Mode, ChatGPT Search, and current Perplexity; "visibility" is citation prominence, not traffic or revenue; single paper, not replicated at scale.

---

## Overlap map — `ai-seo` vs `seo-audit`

| Territory | `ai-seo` | `seo-audit` | Verdict |
|---|---|---|---|
| robots.txt / crawler access | AI bots only | Googlebot only | **Split down the middle — neither is complete.** Merge into one crawler-access model covering every UA. |
| Schema / structured data | "which schemas help AI" table | "we can't detect schema via web_fetch" + defers to `schema` | Three skills touch schema, none owns the full matrix. |
| E-E-A-T / content quality | Pillar 2 "Authority" | "Content Quality Assessment" | Near-duplicate prose, different words. |
| Freshness | "update monthly" | "outdated content not refreshed" | Duplicate. |
| Heading structure / semantic HTML | "H2/H3 match query phrasing" | "one H1, logical hierarchy" | Duplicate with different rationale. |
| Internal linking | topical clusters for fan-out | orphan pages, anchor text | Complementary, but split. |
| JS rendering | "don't hide content behind JS" | absent from technical section | Under-covered in the skill that should own it. |
| Measurement | third-party AI tools | GSC/GA | Split; neither covers the new Gen-AI GSC reports. |

Roughly **40% of `ai-seo` is restated `seo-audit`**. Under the umbrella architecture that duplication becomes the deliberate SEO layer *inside* GEO — but it has to be written once and referenced, not written twice differently.

## Gap map — what a competitor's GEO offering plausibly includes that we don't

| # | Gap | Severity |
|---|---|---|
| G1 | **Search Console "included in Search generative AI features" inclusion check.** Google-documented hard eligibility gate. A client opted out (or defaulted out in a rolled-out market) is invisible in AI Overviews/AI Mode no matter what else we do. We never check it. | **Critical** |
| G2 | **OAI-SearchBot, Claude-SearchBot, Claude-User, Perplexity-User, OAI-AdsBot, Amzn-SearchBot, Amzn-User, Google-Agent** — eight citation-relevant user agents absent from our robots.txt guidance. | **Critical** |
| G3 | **WAF / CDN allowlisting.** Perplexity publishes step-by-step Cloudflare and AWS WAF instructions; OpenAI, Perplexity and Amazon all publish **IP-range JSON endpoints**. A Cloudflare bot-fight rule silently blocking AI crawlers is a common, invisible, entirely fixable cause of zero AI visibility. We never mention WAFs. | **Critical** |
| G4 | Generative AI performance reports in GSC (Search + Discover). | High |
| G5 | **`isAccessibleForFree: false`** — Apple honours this schema property to exclude a page from Apple AI grounding while keeping it in search. Structured data as an *AI control surface*, per-engine. | High |
| G6 | **`noarchive`** meta as Amazon's model-training opt-out. Per-engine meaning of a tag we treat as legacy. | Medium |
| G7 | **Web Bot Auth** (IETF draft) + the new **Google-Agent** UA. Cryptographic bot verification, experimental at Google, supported by major CDNs/WAFs. | Medium (rising) |
| G8 | Per-engine citation baseline tracking (prompt set → which sources cited → share of voice). Named as a metric; no method, no tooling. | High |
| G9 | AI-referral identification in server logs / GA4 by UA and referrer. | High |
| G10 | Rank-aware tactic selection (Table 2 above). | High |
| G11 | `llms.txt` — we assert engines "parse" it with zero evidence either way. Never resolved per engine. | High |
| G12 | Faceted navigation, crawl budget, `http-status-codes`, `dns-network-errors`, `myths-about-crawling` — five substantial Google crawling docs, zero coverage. | Medium |
| G13 | ~30 structured-data feature guides; our `schema` skill covers a handful. | High |
| G14 | Site migration / redirects / A-B testing / pausing a site. | Medium |
| G15 | Ecommerce section (9 pages: Merchant Center, feeds, variants, return/shipping/loyalty schema, pagination). | Medium |
| G16 | No executable tooling anywhere. | **Critical** |

## Risk map — what's in our skills today that could get a client penalised

| Item | Where | Risk | Verdict |
|---|---|---|---|
| Programmatic page generation | `programmatic-seo` playbooks | **Scaled content abuse.** Google's AI guide names this exactly: creating separate content for every query variation "including fan-out queries… violates Google's scaled content abuse spam policy." | `requires-compliant-variant` — the skill needs a hard gate, currently has none |
| "Get featured in industry roundups", "guest posts" | `ai-seo` Pillar 3 | **Link schemes** if compensated or scaled. | `requires-compliant-variant` |
| "Participate authentically in Reddit", "Answer Quora questions" | `ai-seo` Pillar 3 | Fine as written (says *authentically*), one step from spam. | `none`, keep the guardrail explicit |
| "Seeking mentions" | `ai-seo` Pillar 3 | Google explicitly calls out inauthentic mentions. Our wording is close to the line. | `requires-compliant-variant` |
| Chunking / 40–60 word answer blocks | `ai-seo` Pillar 1 | **Not a policy risk.** Google says unnecessary *for Google*; it is not prohibited and plausibly helps other engines. | `none` — **keep and build out** |
| `llms.txt` | `ai-seo` | **Not a policy risk.** Google ignores it; ignoring ≠ penalising, and Google says so verbatim: "will neither harm nor help." | `none` — **keep** |
| UA-based serving to AI crawlers | *not currently present* | Would be **cloaking**. Must be pre-emptively documented as prohibited before anyone reaches for it. | Add to risk register |

## Coverage against the Google docs tree (178 pages)

| Section | Pages | Covered today |
|---|---:|---|
| Search Essentials | 3 | Partial — spam policies referenced, never enumerated |
| SEO fundamentals | 10 | Good (both AI pages, starter guide, helpful content) |
| Crawling and indexing | 41 | ~25% — robots/canonical/sitemaps basics; JS, AMP, site moves, removals, A/B testing absent |
| Ranking and appearance | 31 | ~20% — AI features, snippets, CWV; Preferred sources, Discover, byline dates, flexible sampling, reviews system, site names absent |
| Structured data | 39 | ~20% |
| Monitoring and debugging | 15 | ~30% |
| Site-specific (ecom/intl/explicit) | 14 | International good (`seo-audit` ref is genuinely strong); ecommerce ~0% |
| Crawling infrastructure | 22 | ~10% |

**Overall: roughly 22% of the Google corpus is reflected in our skills.**
