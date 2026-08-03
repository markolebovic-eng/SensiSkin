# 01 — Synthesis

## 1. The full optimization surface, mapped to the pipeline

Every AI answer that cites a client passes through seven stages. A failure at any stage makes all downstream work worthless, which is why the audit runs in this order.

| Stage | What happens | What can break | Who owns it |
|---|---|---|---|
| **Crawl** | An engine's bot requests the URL | robots.txt disallow; **WAF/CDN block**; bot-fight mode; IP block; 4xx/5xx; DNS | GEO — per engine |
| **Index** | Content enters that engine's retrievable store | `noindex`; canonical pointing away; soft-404; not snippet-eligible; **not included in Search generative AI features** | GEO + SEO |
| **Render** | JS executes; final DOM produced | Content only present after hydration; blocked JS/CSS; agent sees an empty shell | SEO/technical |
| **Rank** | Core relevance/quality scoring | Thin or commodity content; weak E-E-A-T; site-wide quality drag | SEO |
| **Retrieve** | RAG selects passages for *this* query and its fan-out | Passage not self-contained; topic cluster incomplete; fan-out sub-questions unanswered | GEO |
| **Cite** | Model picks which retrieved sources to attribute | Weak citation-worthiness signals: no statistics, no sourced claims, no quotable expert attribution | GEO |
| **Measure** | Attribution back to us | No AI-referral instrumentation; no prompt-set baseline; GSC gen-AI report not enabled/available | GEO |

Two observations that shape the whole offering:

- **Stages 1–2 are per-engine and binary.** They are also where nearly all silent failures live. A Cloudflare rule blocking `OAI-SearchBot` is invisible in Google Analytics, invisible in Search Console, and produces exactly zero ChatGPT citations forever. This is the highest-value, lowest-effort work we do, and Google's documentation will never surface it because it only speaks for Google.
- **Stages 5–6 are where the independent research applies**, and where effects invert by existing rank (§2 below).

## 2. What actually drives AI visibility — four different problems

Collapsing these is the most common error in vendor GEO offerings. They have different levers and different owners.

**Retrieval eligibility** (binary, per engine). Can the engine fetch, index, and consider the page at all? Levers: robots.txt per UA, WAF/CDN allowlisting, IP verification, GSC AI-features inclusion, snippet eligibility, render completeness. *Highest ROI. Fix first, always.*

**Ranking** (continuous, mostly Google-derived). Because Google's AI features are RAG over the core index — and ChatGPT/Copilot ride Bing's — classical SEO is the substrate. Levers: content quality, E-E-A-T, internal links, technical health, topical coverage. *This is why GEO contains SEO rather than replacing it.*

**Citation selection** (continuous, per engine, weakly understood). Given a set of retrieved passages, which get attributed? This is where the KDD research lives: citations, credible quotations, statistics. **Critically, effects invert by the source's existing rank** — Cite Sources gives **+115.1%** to a rank-5 source and **−30.3%** to a rank-1 source. *Therefore: apply aggressive citation-density tactics to challenger pages; apply them cautiously, and measure, on pages that already lead.*

**Entity strength** (slow, compounding, off-site). Whether the model has a coherent internal representation of the brand — knows what it is, who it serves, that it exists. Levers: Organization/`sameAs` schema, consistent NAP, Wikipedia/Wikidata accuracy, authentic third-party presence, review platforms. *Slowest to move, hardest for a competitor to take away, and the only lever that works on engines we can't crawl-optimise for at all.*

## 3. The complete GEO deliverable catalog

**This is the sellable scope.** Every line is executable. Engine column: G=Google AI, C=ChatGPT, P=Perplexity, Cl=Claude, B=Bing/Copilot, A=Apple, Am=Amazon, Ag=browser agents, ★=all.

### A. Crawler access & eligibility audit *(always first)*

| # | Deliverable | Implementation | Tooling | QA check | Engines |
|---|---|---|---|---|---|
| A1 | Multi-crawler robots.txt audit | Evaluate robots.txt against all 20+ AI UA tokens with correct group-matching precedence | `scripts/crawler_access_check.py` | Every citation-relevant UA resolves ALLOW on priority URLs | ★ |
| A2 | Training-vs-retrieval policy decision | Separate the client's model-training stance from their citation stance; document per bot | policy matrix in `crawler-access.md` | Client sign-off recorded | ★ |
| A3 | **WAF/CDN allowlist audit** | Test live fetches with each AI UA against the origin; inspect Cloudflare bot-fight / rate limits / managed rules | `crawler_access_check.py --live` | 200 OK for every allowed UA, not just "robots.txt permits" | C, P, Cl, ★ |
| A4 | IP-range allowlist implementation | Pull published IP JSON (OpenAI ×4, Perplexity ×2, Amazon ×2), build UA+IP WAF rules per Perplexity's Cloudflare/AWS procedure | `scripts/fetch_bot_ips.py` | Rules present; automated refresh scheduled | C, P, Am |
| A5 | **GSC generative-AI inclusion check** | Verify the site is included in Search generative AI features | GSC | Setting confirmed ON, screenshot in report | G |
| A6 | Snippet-eligibility audit | Find `nosnippet`, `max-snippet:0`, `data-nosnippet`, `noindex` suppressing AI eligibility | `scripts/indexability_check.py` | No unintended suppression on priority URLs | G, A |
| A7 | Google-Extended decision | Set deliberately; document that it governs Gemini/Vertex, **not** AI Overviews | robots.txt | Decision recorded with correct rationale | G (Gemini) |
| A8 | `Crawl-delay` / rate-limit tuning | Anthropic honours `Crawl-delay`; Google and Amazon do not | robots.txt | Per-engine directives correct | Cl |
| A9 | Bot verification / log truth | Reverse-DNS + published IP verification to separate real bots from spoofers | `scripts/verify_bot.py` | Spoofed traffic identified | ★ |
| A10 | Web Bot Auth readiness | Confirm CDN supports it; recognise `Google-Agent` / `agent.bot.goog` | CDN config | Documented; fallback verification retained | G, Ag |
| A11 | Per-host robots.txt coverage | Amazon and Anthropic read robots.txt per host — every subdomain needs its own | crawler script | All hosts covered | Am, Cl |
| A12 | HTTP status & DNS health for crawlers | 5xx, redirect chains, DNS failures degrade all engines | `scripts/indexability_check.py` | Clean status on priority set | ★ |

### B. Index & render audit

| # | Deliverable | Implementation | QA check | Engines |
|---|---|---|---|---|
| B1 | Indexability audit | canonical / noindex / status / redirect-chain per priority URL | Self-canonical, 200, indexable | ★ |
| B2 | **Raw-vs-rendered diff** | Fetch without JS, then with; diff visible text and links | Core content + links present pre-hydration | ★, Ag |
| B3 | Sitemap validation | Canonical-only, 200-only, correct extensions, under limits | Zero invalid entries | ★ |
| B4 | Internal link graph | Crawl depth, orphans, hub coverage | Priority pages ≤3 clicks, zero orphans | ★ |
| B5 | Crawl-budget / faceted-nav control | Parameter handling, faceted URL containment | Crawl waste reduced | G |
| B6 | IndexNow submission | Bing/Yandex instant notification | Key deployed, submissions accepted | B |

### C. Content structure & citation-worthiness

| # | Deliverable | Implementation | QA check | Engines |
|---|---|---|---|---|
| C1 | **Rank-stratified tactic assignment** | Bucket priority pages by current position; assign aggressive citation tactics to rank 3+ only, measured trials on rank 1–2 (KDD Table 2) | Every page has an assigned tactic tier | ★ |
| C2 | Statistics addition | Replace qualitative claims with sourced quantitative ones | Each priority page carries ≥3 sourced statistics | ★ |
| C3 | Citation of authoritative sources | Named, linked, dated references | ≥3 external authoritative citations | ★ |
| C4 | Expert quotation addition | Real named quotes with title and organisation | Attribution complete and verifiable | ★ |
| C5 | Self-contained answer passages | Each key claim readable without surrounding context | Passage passes standalone read test | C, P, Cl |
| C6 | Query fan-out coverage mapping | Enumerate sub-queries per priority topic; map to existing/needed content | Every fan-out branch has a home | G |
| C7 | Comparison tables, definition blocks, FAQ blocks | Extractable formats for vs/what-is/question intent | Present where intent matches | C, P, Cl |
| C8 | Freshness & byline discipline | Visible author, published + modified dates, real review cycle | Dates present and truthful | ★ |
| C9 | E-E-A-T / author entity build-out | Author pages, credentials, `Person` + `ProfilePage` schema | Every author has an entity page | ★ |
| C10 | Non-commodity content program | Original data, first-hand experience — Google's stated top factor | Each piece has a defensible unique claim | ★ |
| C11 | Domain-targeted method selection | Choose tactic by content category (KDD Table 3) | Recorded per content cluster | ★ |

### D. Structured data

| # | Deliverable | QA check | Engines |
|---|---|---|---|
| D1 | Schema inventory & validity audit (JS-injected included) | Zero errors in Rich Results Test | ★ |
| D2 | Organization + `sameAs` entity graph | Complete, consistent across profiles | ★ |
| D3 | Feature-eligible schema per template (Article, Product, LocalBusiness, FAQ, HowTo, Event, Recipe, JobPosting, Video, Breadcrumb…) | Eligible + matches visible text | G |
| D4 | Schema-visible-text parity | No markup claiming what the page doesn't show | Parity verified | G |
| D5 | **`isAccessibleForFree` AI-grounding control** | Set deliberately per Apple's page-level semantics | Decision recorded | A |
| D6 | Types beyond Google's supported set (`Dataset`, `DefinedTerm`, `ClaimReview`, `Occupation`, `Service`…) | Valid JSON-LD; parseable by non-Google consumers | ★ |
| D7 | Merchant Center feed + Business Profile accuracy | Feed live, GBP complete | G |

### E. AI-specific files & agent readiness

| # | Deliverable | Honest status | Engines |
|---|---|---|---|
| E1 | `llms.txt` implementation | Google ignores it, explicitly without penalty. No engine has documented consuming third-party files. OpenAI and Perplexity both publish one for their own docs. **Shipped as low-cost, zero-risk coverage.** | unresolved — see ledger 5.1 |
| E2 | Markdown `.md` page variants | Same pattern OpenAI/Perplexity use for their own docs | unresolved |
| E3 | `/pricing.md` or public machine-readable pricing | No engine documents reading it; the underlying principle — pricing must be public, crawlable, non-JS — **is** well-supported | Ag |
| E4 | Accessibility-tree readiness | Google-documented: agents read the a11y tree | Ag |
| E5 | Semantic HTML + stable selectors + labelled controls | Google-documented agent access path | Ag |
| E6 | Public, non-gated critical facts (pricing, specs, contact, hours) | Direct agent-commerce prerequisite | Ag |
| E7 | UCP monitoring | Emerging; track adoption | Ag |
| E8 | `noarchive` decision | Live training-opt-out meaning on Amazon | Am |

### F. Entity & off-site

| # | Deliverable | Risk | Engines |
|---|---|---|---|
| F1 | Wikipedia/Wikidata accuracy review | none (accuracy only, never promotional editing) | ★ |
| F2 | Review-platform profile completeness | none | ★ |
| F3 | Authentic community participation playbook | `requires-compliant-variant` | ★ |
| F4 | Digital PR / earned coverage | `requires-compliant-variant` (never paid links) | ★ |
| F5 | NAP consistency + local directory audit | none | G, ★ |
| F6 | YouTube presence for how-to intent | none | G |

### G. Measurement & reporting

| # | Deliverable | Engines |
|---|---|---|
| G1 | GSC **Generative AI performance report** baseline (Search + Discover) | G |
| G2 | Standard GSC baseline (Web search type — contains AI impressions) | G |
| G3 | AI-referral segmentation in GA4 + server logs by referrer and UA | ★ |
| G4 | **Per-engine prompt-set citation baseline** — fixed prompt set, run across engines, record cited sources | ★ |
| G5 | Share-of-voice vs named competitors on that prompt set | ★ |
| G6 | AI crawler hit-rate from server logs (are they actually coming?) | ★ |
| G7 | Bing Webmaster Tools baseline | B |
| G8 | Monthly reporting: scope performed + metrics moved, no fabricated causation | ★ |

### H. Governance

| # | Deliverable |
|---|---|
| H1 | Spam-policy compliance review of all planned tactics |
| H2 | Scaled-content gate for any programmatic work |
| H3 | Cloaking prohibition — never serve different content by UA |
| H4 | Change log tied to measurement windows, so before/after has real boundaries |

## 4. Engine-by-engine divergence — what justifies GEO as a distinct service

Everything here is true of a non-Google engine and absent from Google's documentation. This is the answer to "isn't this just SEO?"

| Divergence | Consequence | Deliverable |
|---|---|---|
| **Separate training vs search bots with independent controls** (OpenAI, Anthropic, Perplexity, Apple, Amazon) | A client can refuse model training and keep full citation visibility. Google offers no such split for its AI Search features. | A2 |
| **The citation-critical bot is not the famous one** (OAI-SearchBot, not GPTBot; Claude-SearchBot, not ClaudeBot) | Nearly every published robots.txt template on the internet optimises the wrong bot. | A1 |
| **User-initiated fetchers ignore robots.txt** (Perplexity-User, ChatGPT-User, Amzn-User) | robots.txt is not a complete access-control model. Blocking must happen at the edge if truly required. | A3 |
| **WAF/CDN is a first-class access surface** — Perplexity publishes Cloudflare and AWS procedures | Google has never published WAF guidance. This is invisible to a Google-only practitioner. | A3, A4 |
| **Published IP-range JSON endpoints** | Real verification and real allowlists, not UA-string trust. | A4, A9 |
| **`Crawl-delay` is honoured by Anthropic, ignored by Google and Amazon** | Per-engine robots.txt, not one file for all. | A8 |
| **`noarchive` means "no model training" to Amazon** | A tag Google deprecated carries live commercial meaning elsewhere. | E8 |
| **`isAccessibleForFree: false` gates Apple AI grounding** | Structured data as a per-engine AI control. | D5 |
| **robots.txt read per host** (Amazon, Anthropic) | Subdomain coverage is mandatory, not optional. | A11 |
| **~24h robots.txt propagation** (OpenAI, Perplexity) | Remediation SLAs differ per engine. | A1 |
| **Independent indexes** — Bing (ChatGPT, Copilot), Perplexity's own, Google's | Being indexed by Google is not being retrievable everywhere. IndexNow and Bing Webmaster Tools become GEO deliverables. | B6, G7 |
| **KDD effect inversion by rank** | Rank-stratified content strategy — no Google doc will ever tell you this. | C1 |

## 5. Structured data reference

Full matrix lives in `references/structured-data-matrix.md` (39 Google feature guides harvested, required vs recommended properties, eligibility, deprecation status) with validated JSON-LD in `references/schema-recipes.md`.

Three framing points that matter commercially:

1. **Google did not say schema is useless.** It said schema "isn't required for generative AI search" and in the same breath "it's a good idea to continue using it as part of your overall SEO strategy, as it helps with being eligible for rich results." Rich results remain fully supported.
2. **Schema is an AI control surface on other engines** — `isAccessibleForFree` on Apple being the concrete, documented case.
3. **Types beyond Google's supported set are still GEO surface area.** Google publishes ~30 feature guides; schema.org has hundreds of types. Non-Google parsers and agent tooling consume the vocabulary, not Google's supported subset. Implementing `Service`, `DefinedTerm`, `ClaimReview`, `Occupation` costs nothing and is machine-readable regardless of whether it triggers a Google rich result.

## 6. Measurement

**What we can measure honestly:**

- **GSC Generative AI performance report** — impressions, pages, countries, devices, dates. Search and Discover. Rolling out; not every property has it.
- **GSC standard Performance, Web search type** — contains AI impressions and clicks. *AI impressions are a subset, so they can never be added to total Search impressions, and because the gen-AI report carries no clicks, AI-specific CTR is not computable.* State this once in every report.
- **AI referral traffic** — GA4 + server logs, segmented by referrer host and UA.
- **AI crawler hit rate** — server logs, verified by IP. Answers "are the engines even fetching us?"
- **Prompt-set citation tracking** — a fixed set of 20–50 real client-intent prompts, run on a fixed cadence across engines, recording which sources each engine cites. This is a sampled observation, and it is the only cross-engine visibility measurement that exists.
- **Share of voice** — client citations ÷ total citations on that prompt set, vs named competitors.

**Building a defensible before/after narrative.** Baseline everything before any change. Log every change with a date. Report as: *metrics moved over the window, and the scope of work performed during it.* Never assert that deliverable X caused metric Y. The honest version is stronger anyway — it reports the full scope rather than one attributable line, and it cannot be disproved by the client's next technical hire.

**Never:** third-party "AI ranking scores" presented as internal Google data. Google states plainly that no third-party tool has access to its ranking or AI systems.

## 7. Objection handling — "Google says GEO isn't a thing, why am I paying for it?"

*Delivered confidently, without defensiveness. Full script in `references/objection-handling.md`.*

**What Google actually said.** That for *Google Search*, generative AI features are grounded in core Search ranking, so SEO best practices remain the path — and that llms.txt, chunking, AI-specific rewriting, and mention-seeking aren't needed *for Google*. That is accurate, and we agree with it. It is also the reason our GEO engagement contains a complete technical and content SEO program rather than sitting beside one.

**What Google did not say.** It did not say structured data is useless — it recommends it for rich results in the same paragraph. It did not say AI files are harmful — it says they "neither harm nor help." And it does not speak for ChatGPT, Perplexity, Claude, Copilot, Apple, or Amazon, because it can't.

**Where Google's scope ends and ours begins.** Google's guidance covers one engine. Meanwhile: OpenAI runs a search crawler distinct from its training crawler, and the one most robots.txt templates block is the wrong one. Perplexity publishes WAF configuration procedures because firewall rules block AI crawlers routinely and silently. Anthropic honours a directive Google ignores. Apple reads a schema property to decide whether your content can ground an AI answer. Amazon reads a meta tag Google deprecated. None of that is in Google's documentation, and none of it is discoverable by reading it.

**What independent research measured.** Peer-reviewed work at KDD 2024 measured up to 40% visibility gains from adding citations, credible quotations, and statistics — validated on Perplexity at up to 37%. It also found the effect inverts by existing rank, which is why we assign these tactics by position rather than applying them everywhere.

**And one thing on Google itself.** Google's own AI optimization guide states that a site must be included in Search generative AI features in Search Console to be eligible at all. That's a switch, and a client who is off it has zero AI Overview visibility regardless of content quality. Checking it is a GEO deliverable.

**The close.** The engagement delivers a complete SEO foundation plus per-engine access, structure, entity, and measurement work across every major AI surface. If Google's position is entirely correct, the client still gets the full SEO program that position endorses. Everything else is upside on engines Google doesn't speak for.

## 8. Risk register

Full version with compliant variants: `references/risk-register.md`.

| Tactic | Risk | Threshold | Compliant variant |
|---|---|---|---|
| Pages per query / fan-out variant | **Scaled content abuse** — named explicitly in Google's AI guide | Generating pages primarily to capture query permutations rather than serve a distinct need | Build **one comprehensive resource per topic cluster** covering the fan-out sub-questions as sections. Achieves the same retrieval coverage; is what Google says its systems now understand natively. |
| Programmatic page generation | Scaled content abuse | Template + data with no unique value per page | Programmatic **only** where each page has genuinely distinct data a user wants (real inventory, real locations, real datasets). Gate: could this page stand alone and satisfy someone? Enforce a per-page unique-value assertion before publish. |
| Parasite / third-party hosting | **Site reputation abuse** | Publishing on a third party's domain to borrow its ranking | Earn genuine editorial placement; own-domain content for commercial intent. |
| Paid mentions, link buying, mass guest posting | **Link schemes** | Compensation or scale without disclosure | Digital PR with a real story; original data others cite voluntarily; `rel="sponsored"` where anything of value changed hands. |
| Mention-seeking for AI visibility | Inauthentic mentions (Google-named) | Manufactured or incentivised mentions at scale | Be genuinely referenceable: original research, public data, expert availability. Participate under a real identity with disclosed affiliation. |
| **UA-based serving to AI crawlers** | **Cloaking** — severe, manual-action territory | Any material difference between what a crawler and a user receive | **Never.** If content should be excluded, use `noindex`/`nosnippet`/robots.txt — mechanisms designed for it. Prerendering is acceptable only when the rendered output is equivalent. |
| Mass AI-generated content | Scaled content abuse | Scale without editorial value | AI-assisted, human-directed, meeting Search Essentials. Google permits this explicitly. |
| Aggressive citation-density on rank-1 pages | **Not a policy risk** — an efficacy risk (−30.3%, KDD Table 2) | Applying challenger tactics to leading pages | Measured trial on a subset, hold the rest, compare. |

## 9. Changelog — 24 months, for re-running this research as a diff

| Date | Change | Source |
|---|---|---|
| 2026-07-10 | AI optimization guide substantially rewritten: adds the **GSC inclusion requirement**, the mythbusting section (llms.txt, chunking, rewriting, mentions, structured data), Generative AI performance report, agentic experiences, UCP | `/search/docs/fundamentals/ai-optimization-guide` |
| 2026-06-03 | **Generative AI performance reports** launched in Search Console (Search + Discover), subset rollout | `/search/blog/2026/06/gen-ai-performance-reports` |
| 2026-06 | Search Console **AI-features inclusion toggle**, UK-first (CMA-driven); not a core-search ranking signal | Google via SEL 479298 |
| 2026-05-04 | **Web Bot Auth** experimental guidance published; `Google-Agent` UA / `agent.bot.goog` | `/crawling/docs/crawlers-fetchers/web-bot-auth` |
| 2026-04-07 | Anthropic crawler doc updated — three bots incl. **Claude-SearchBot**; `anthropic-ai` no longer listed | `support.anthropic.com/.../8896518` |
| current | **OAI-AdsBot** added to OpenAI's crawler roster | `platform.openai.com/docs/bots.md` |
| current | Amazon: **Amzn-SearchBot / Amzn-User** supersede the single Amazonbot identity; `noarchive` = training opt-out | `developer.amazon.com/amazonbot` |
| 2025-12-10 | Bulk republish timestamp across 115 of 178 Google doc pages — **not** 115 content updates | scrape index |
| 2025-12-10 | `/search/docs/appearance/ai-features` states AI traffic reported in standard Performance report, "Web" type — still true, now incomplete | `/search/docs/appearance/ai-features` |
| 2024-08 | GEO paper published, KDD '24 | arXiv:2311.09735 |

**Re-research triggers and cadence** → `04-open-questions.md`.
