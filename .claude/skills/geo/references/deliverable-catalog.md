# Deliverable Catalog

The complete sellable scope, with implementation, tooling, QA check, and engine applicability per item.

Engines: G=Google AI · C=ChatGPT · P=Perplexity · Cl=Claude · B=Copilot/Bing · A=Apple · Am=Amazon · Ag=agents · ★=all

## A. Crawler access & eligibility — always first

| # | Deliverable | Implementation | Tooling | QA check | Engines |
|---|---|---|---|---|---|
| A1 | Multi-crawler robots.txt audit | Evaluate robots.txt against 22 AI UA tokens with correct group-matching precedence | `crawler_access_check.py` | Every citation-critical UA resolves ALLOW on priority URLs | ★ |
| A2 | Training-vs-citation policy | Separate the client's model-training stance from their citation stance; document per bot; obtain sign-off | `crawler-access.md` matrix | Signed decision recorded | ★ |
| A3 | WAF/CDN allowlist audit | Live fetch per AI UA against origin; inspect Cloudflare bot-fight mode, managed rules, rate limits, AI-scraper toggles | `crawler_access_check.py --live` | HTTP 200 for every allowed bot | C,P,Cl,★ |
| A4 | IP-range allowlist | Pull published IP JSON; build UA+IP WAF rules per Perplexity's Cloudflare/AWS procedure; schedule refresh | vendor JSON endpoints | Rules live; refresh automated | C,P,Am |
| A5 | GSC generative-AI inclusion check | Confirm the site is included in Search generative AI features | Search Console | Setting ON, screenshot in report | G |
| A6 | Snippet-eligibility audit | Find `nosnippet` / `max-snippet:0` / `data-nosnippet` / `noindex` suppressing AI eligibility | `indexability_check.py` | No unintended suppression | G,A |
| A7 | Google-Extended decision | Set deliberately; document that it governs Gemini and Vertex only | robots.txt | Decision plus correct rationale recorded | G (Gemini) |
| A8 | Crawl-delay tuning | Anthropic honours it; Google and Amazon do not | robots.txt | Per-engine directives correct | Cl |
| A9 | Bot verification | Reverse DNS plus published IP ranges, to separate real bots from spoofers | log analysis | Spoofed traffic identified | ★ |
| A10 | Web Bot Auth readiness | Confirm CDN support; recognise `Google-Agent` / `agent.bot.goog` | CDN config | Documented; fallback verification retained | G,Ag |
| A11 | Per-host robots.txt coverage | Amazon and Anthropic read robots.txt per host | run checker per host | All hosts covered | Am,Cl |
| A12 | HTTP and DNS health for crawlers | 5xx, redirect chains, DNS failures degrade all engines | `indexability_check.py` | Clean status on priority set | ★ |

## B. Index & render

| # | Deliverable | Implementation | Tooling | QA check | Engines |
|---|---|---|---|---|---|
| B1 | Indexability audit | Canonical, noindex, status, redirect chain per priority URL | `indexability_check.py` | Self-canonical, 200, indexable | ★ |
| B2 | Raw-vs-rendered diff | Fetch without JS, then with; diff visible text and links | fetch + headless | Core content and links present pre-hydration | ★,Ag |
| B3 | Sitemap validation | Canonical-only, 200-only, correct extensions, within limits | sitemap parse | Zero invalid entries | ★ |
| B4 | Internal link graph | Crawl depth, orphan detection, hub coverage | crawl | Priority pages ≤3 clicks; zero orphans | ★ |
| B5 | Crawl budget & faceted nav | Parameter handling, faceted URL containment | log analysis | Crawl waste reduced | G |
| B6 | IndexNow | Deploy key, submit on publish | IndexNow API | Key deployed, submissions accepted | B |

## C. Content & citation-worthiness

Rank-stratify first — see `content-citation-tactics.md`. Tactic effects invert by existing position.

| # | Deliverable | Implementation | QA check | Engines |
|---|---|---|---|---|
| C1 | Rank-stratified tactic assignment | Bucket priority pages by current position; assign aggressive tactics to rank 3+ only | Every priority page has an assigned tactic tier | ★ |
| C2 | Statistics addition | Replace qualitative claims with sourced quantitative ones | ≥3 sourced statistics per priority page | ★ |
| C3 | Authoritative source citation | Named, linked, dated external references | ≥3 external citations, all resolving 200 | ★ |
| C4 | Expert quotation addition | Real named quotes with title and organisation | Attribution complete and verifiable; never fabricated | ★ |
| C5 | Self-contained answer passages | Each key claim readable without surrounding context | Passes standalone read test | C,P,Cl |
| C6 | Query fan-out coverage mapping | Enumerate sub-queries; cover them as sections of one resource | Every fan-out branch has a home — never one page per variant | G |
| C7 | Comparison, definition and FAQ blocks | Extractable formats matched to query intent | Present where intent matches | C,P,Cl |
| C8 | Freshness and byline discipline | Visible author, published and modified dates, real review cycle | Dates present and truthful | ★ |
| C9 | E-E-A-T author entities | Author pages, credentials, `Person` + `ProfilePage` schema | Every author has an entity page | ★ |
| C10 | Non-commodity content program | Original data and first-hand experience | Each piece has a defensible unique claim | ★ |
| C11 | Domain-targeted method selection | Choose tactic by content category (KDD Table 3) | Recorded per content cluster | ★ |

## D. Structured data

| # | Deliverable | Implementation | QA check | Engines |
|---|---|---|---|---|
| D1 | Schema inventory & validation | Extract and validate all JSON-LD, including JS-injected | `schema_extract.py` + Rich Results Test | Zero errors | ★ |
| D2 | Organization + `sameAs` entity graph | Complete profile links across every platform | Consistent across profiles | ★ |
| D3 | Feature-eligible schema per template | Article, Product, LocalBusiness, FAQ, HowTo, Event, Recipe, JobPosting, Video, Breadcrumb | Eligible and matches visible text | G |
| D4 | Schema/visible-text parity | No markup claiming what the page does not show | Parity verified | G |
| D5 | `isAccessibleForFree` AI-grounding control | Set deliberately per Apple's page-level semantics | Decision recorded; `hasPart` not used | A |
| D6 | Types beyond Google's supported set | `Dataset`, `DefinedTerm`, `ClaimReview`, `Occupation`, `Service` | Valid JSON-LD, parseable | ★ |
| D7 | Merchant Center feed + Business Profile | Feed accuracy, GBP completeness | Feed live, GBP complete | G |

## E. AI files & agent readiness

| # | Deliverable | Honest status | Engines |
|---|---|---|---|
| E1 | `llms.txt` | Google ignores it explicitly, with no penalty. Others unresolved. Ship as zero-risk coverage. | unresolved |
| E2 | Markdown page variants | The pattern OpenAI and Perplexity use for their own docs | unresolved |
| E3 | Public machine-readable pricing | No engine documents reading it; the underlying principle is well-supported | Ag |
| E4 | Accessibility-tree readiness | Google-documented agent access path | Ag |
| E5 | Semantic HTML, stable selectors, labelled controls | Google-documented | Ag |
| E6 | Public critical facts — pricing, specs, hours, contact | Agent-commerce prerequisite | Ag |
| E7 | UCP monitoring | Emerging; track adoption | Ag |
| E8 | `noarchive` decision | Live training-opt-out meaning on Amazon | Am |

## F. Entity & off-site

| # | Deliverable | Risk | Engines |
|---|---|---|---|
| F1 | Wikipedia/Wikidata accuracy review | none — accuracy only, disclosed COI, never promotional editing | ★ |
| F2 | Review-platform profile completeness | none | ★ |
| F3 | Authentic community participation playbook | requires-compliant-variant | ★ |
| F4 | Digital PR / earned coverage | requires-compliant-variant — never paid links | ★ |
| F5 | NAP consistency + local directory audit | none | G,★ |
| F6 | YouTube presence for how-to intent | none | G |

## G. Measurement

| # | Deliverable | Engines |
|---|---|---|
| G1 | GSC Generative AI performance report baseline (Search + Discover) | G |
| G2 | GSC standard baseline (Web search type — contains AI impressions) | G |
| G3 | AI-referral segmentation in GA4 and server logs | ★ |
| G4 | Per-engine prompt-set citation baseline | ★ |
| G5 | Share of voice vs named competitors | ★ |
| G6 | AI crawler hit-rate from logs, IP-verified | ★ |
| G7 | Bing Webmaster Tools baseline | B |
| G8 | Monthly reporting — scope performed and metrics moved, no fabricated attribution | ★ |

## H. Governance

| # | Deliverable |
|---|---|
| H1 | Spam-policy compliance review of all planned tactics |
| H2 | Scaled-content gate for any programmatic work, decision recorded per page |
| H3 | Cloaking prohibition — no user-agent-varied content, anywhere |
| H4 | Change log tied to measurement windows |

## Budget tiers

**Essential** — A1, A3, A5, A6, B1, D1, G1, G3, G4, H1.
The access-and-measurement floor. Nothing else matters if these fail, and they catch the majority of real-world zero-visibility causes.

**Standard** — Essential plus A2, A4, A9, B2–B4, C1–C3, C6, C8, D2–D4, E1, F1, F2, F5, G2, G5, G6.

**Comprehensive** — everything, plus ongoing content production and quarterly re-audit.
