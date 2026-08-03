---
name: geo
description: "Use for any work on visibility in AI search and AI answers, on any engine. Trigger phrases: 'GEO,' 'generative engine optimization,' 'AEO,' 'answer engine optimization,' 'LLMO,' 'AI SEO,' 'AI search visibility,' 'AI Overviews,' 'AI Mode,' 'get cited by AI,' 'AI citations,' 'why don't we show up in ChatGPT,' 'why doesn't Perplexity mention us,' 'optimize for ChatGPT/Claude/Perplexity/Gemini/Copilot,' 'LLM optimization,' 'AI visibility audit,' 'llms.txt,' 'are AI bots blocked,' 'zero-click search.' This is the UMBRELLA skill for AI search engagements and it INCLUDES the full technical and content SEO layer — do not run seo-audit separately alongside it. Use seo-audit instead only when the request is purely about Google/Bing organic rankings with no AI-surface component. For structured data implementation invoked as its own task, see schema. For AI agents browsing, comparing, or transacting on the site, see agentic-readiness."
metadata:
  version: 1.0.0
  last-research: 2026-08-03
---

# GEO — Generative Engine Optimization

You optimize client visibility across every AI answer surface: Google AI Overviews and AI Mode, ChatGPT Search, Perplexity, Claude, Microsoft Copilot, Apple, and Amazon — plus the SEO foundation all of them are grounded in.

**GEO is a superset of SEO, not a sibling.** A client buying GEO gets the full technical and content SEO program as part of it, because every major AI surface retrieves from a search index. Never scope a GEO engagement without the SEO layer.

## Before starting

Read `.agents/clients/{slug}/product-marketing.md` and `memory/MEMORY.md`. All client-facing output goes in the client's language (SensiSkin: Serbian, Latin script).

Then establish:
1. **Domain(s) and priority URLs** — the 20–50 pages that carry the business.
2. **Priority prompts** — 20–50 real questions a customer would ask an AI assistant. This becomes the measurement baseline; nothing else measures cross-engine visibility.
3. **Access** — Search Console, analytics, server logs, CDN/WAF dashboard, CMS.
4. **Named competitors** — for share of voice.
5. **Model-training stance** — do they want to allow AI training, or only citation? These are separate controls on most engines and it is a client decision, not ours.

## Decision tree

```
Client asks about AI visibility / GEO / AEO / being cited by AI
  └─> THIS SKILL. Run the workflow below.

Client asks "why did organic traffic drop", no AI angle
  └─> seo-audit

Client asks to implement specific structured data
  └─> schema (this skill invokes it)

Client asks about AI agents buying / booking / comparing on their site
  └─> agentic-readiness

Client asks to build many pages at scale
  └─> programmatic-seo, BUT read references/risk-register.md first.
      Scaled content abuse is the one thing that can destroy the whole engagement.
```

## Workflow

Run in this order. Stages 1–2 are binary and gate everything downstream — a page a bot cannot fetch cannot be cited, no matter how good it is.

### 1. Intake & scoping
Pick deliverables from the catalog below against the client's budget tier. Record the prompt set and competitor list. Baseline before changing anything.

### 2. Crawl & access audit across all AI crawlers — *always first, and re-run every audit*
```bash
python scripts/crawler_access_check.py https://client.com --live --delay 9 --json access.json
```
**Three** independent failure modes, not two: robots.txt, an HTTP-level block at the CDN/WAF/origin, and a **bot-challenge interstitial served with HTTP 200**. The last is the nastiest — the status code says success and the body is a JS challenge no crawler can execute. The script detects it; never judge access by status code alone.

Then verify the Search Console **generative AI features inclusion** setting — a Google-documented hard eligibility gate.

**This regresses silently.** A host enables a default, a security plugin updates, a WAF option flips on — and nothing in Search Console reports it. Re-run on every audit and every monthly report, and diff against the previous `access.json`.

**Before reporting any failure, rule out your own test as the cause.** See the diagnostic protocol in `references/crawler-access.md` — a 429 from rapid sequential testing looks identical to a policy block, and acting on it wastes a client's time on a fix they don't need.

### 3. Index & render audit
```bash
python scripts/indexability_check.py --urls priority.txt --json index.json
```
Catches `nosnippet` and `max-snippet:0`, which leave a page perfectly indexed and completely ineligible for AI Overviews. Confirm server-rendered content; JS-only pages lose both crawlers and browser agents.

### 4. Content quality & structure
Rank-stratify first (see catalog C1 — tactics invert by existing position), then apply. `references/content-citation-tactics.md`.

### 5. Structured data
Audit, validate, fill gaps. Invoke `schema`. Remember `isAccessibleForFree` is an Apple AI control, not just a paywall signal.
```bash
python scripts/schema_extract.py --urls priority.txt --json schema.json
```

### 6. AI-file implementation
`llms.txt`, markdown variants, public machine-readable pricing. Low cost, zero risk, honest status per engine: `references/llms-txt-and-ai-files.md`.

### 7. Entity & off-site
Organization/`sameAs` graph, Wikipedia/Wikidata accuracy, review platforms, NAP, authentic community presence. The slowest lever and the hardest for a competitor to take away.

### 8. Per-engine citation baseline
Run the prompt set across engines, record which sources each cites. `references/measurement.md`.

### 9. Prioritized roadmap
Sequence by (impact × certainty) ÷ effort. Access fixes are almost always first: highest impact, lowest effort, highest certainty.

### 10. Measurement setup
GSC generative AI performance report, AI referral segmentation, crawler hit-rate from logs, prompt-set cadence.

### 11. Reporting
`templates/monthly-report.md`. **Scope performed and metrics moved. Never assert that a specific deliverable caused a specific metric change.**

---

## Deliverable catalog — scoping menu

Full detail with implementation steps, tooling, and QA checks: `references/deliverable-catalog.md`.
Engines: G=Google AI · C=ChatGPT · P=Perplexity · Cl=Claude · B=Copilot/Bing · A=Apple · Am=Amazon · Ag=agents · ★=all

### A. Crawler access & eligibility
`A1` Multi-crawler robots.txt audit (20+ UAs) ★ · `A2` Training-vs-citation policy decision ★ · `A3` **WAF/CDN allowlist audit** ★ · `A4` IP-range allowlist implementation (C,P,Am) · `A5` **GSC generative-AI inclusion check** (G) · `A6` Snippet-eligibility audit (G,A) · `A7` Google-Extended decision (G/Gemini) · `A8` Crawl-delay tuning (Cl) · `A9` Bot verification vs spoofing ★ · `A10` Web Bot Auth readiness (G,Ag) · `A11` Per-host robots.txt coverage (Am,Cl) · `A12` HTTP/DNS health ★

### B. Index & render
`B1` Indexability audit ★ · `B2` Raw-vs-rendered diff ★ · `B3` Sitemap validation ★ · `B4` Internal link graph ★ · `B5` Crawl budget & faceted nav (G) · `B6` IndexNow (B)

### C. Content & citation-worthiness
`C1` **Rank-stratified tactic assignment** ★ · `C2` Statistics addition ★ · `C3` Authoritative source citation ★ · `C4` Expert quotation addition ★ · `C5` Self-contained answer passages (C,P,Cl) · `C6` Query fan-out coverage mapping (G) · `C7` Comparison/definition/FAQ blocks (C,P,Cl) · `C8` Freshness & byline discipline ★ · `C9` E-E-A-T author entities ★ · `C10` Non-commodity content program ★ · `C11` Domain-targeted method selection ★

### D. Structured data
`D1` Schema inventory & validation ★ · `D2` Organization + `sameAs` entity graph ★ · `D3` Feature-eligible schema per template (G) · `D4` Schema/visible-text parity (G) · `D5` **`isAccessibleForFree` AI-grounding control** (A) · `D6` Types beyond Google's supported set ★ · `D7` Merchant Center + Business Profile (G)

### E. AI files & agent readiness
`E1` `llms.txt` · `E2` Markdown page variants · `E3` Public machine-readable pricing (Ag) · `E4` Accessibility-tree readiness (Ag) · `E5` Semantic HTML & stable selectors (Ag) · `E6` Public critical facts (Ag) · `E7` UCP monitoring (Ag) · `E8` `noarchive` decision (Am)

### F. Entity & off-site
`F1` Wikipedia/Wikidata accuracy ★ · `F2` Review-platform completeness ★ · `F3` Authentic community playbook ★ · `F4` Digital PR / earned coverage ★ · `F5` NAP & local directories (G) · `F6` YouTube for how-to intent (G)

### G. Measurement
`G1` GSC Generative AI performance report baseline (G) · `G2` GSC standard baseline (G) · `G3` AI-referral segmentation ★ · `G4` **Per-engine prompt-set citation baseline** ★ · `G5` Share of voice ★ · `G6` Crawler hit-rate from logs ★ · `G7` Bing Webmaster Tools (B) · `G8` Monthly reporting ★

### H. Governance
`H1` Spam-policy review · `H2` Scaled-content gate · `H3` Cloaking prohibition · `H4` Change log tied to measurement windows

### Budget tiers
- **Essential** — A1, A3, A5, A6, B1, D1, G1, G3, G4, H1. The access-and-measurement floor. Nothing above matters if these fail.
- **Standard** — Essential + A2, A4, A9, B2–B4, C1–C3, C6, C8, D2–D4, E1, F1, F2, F5, G2, G5, G6.
- **Comprehensive** — everything, plus ongoing content production and quarterly re-audit.

---

## Non-negotiables

**Never get the client penalised.** The only reason to refuse a tactic is downside risk to the client's site, not lack of proof. Unproven tactics ship. Risky ones get a compliant variant. Read `references/risk-register.md` before any programmatic, link-building, or mention-seeking work. The hard line: **never serve different content to crawlers than to users** — that is cloaking, and it is manual-action territory.

**Scope every claim to an engine.** "Structured data isn't required" is a statement about Google's AI features. It is unverified everywhere else. An unscoped claim is a bug.

**Client deliverables carry no confidence-tier language.** The evidence ledger is an internal tool for deciding what to lead with. A proposal that hedges every line sells nothing. Write scope of work, actions taken, metrics moved.

**Report honestly.** "AI Overview impressions up 40% over the engagement, during which we did X, Y, Z" is true, strong, and durable. "Our llms.txt caused a 40% rise" is a claim the client's next technical hire can disprove. Never fabricate attribution.

**Two measurement facts to state in every report:** AI impressions are a *subset* of Search impressions, never additive. And because the generative AI report carries no click data, AI-specific CTR is not computable.

---

## Key corrections to common practice

Things most GEO advice gets wrong. These are our credibility in a technical conversation.

| Common belief | Reality | Source |
|---|---|---|
| Block GPTBot and you lose ChatGPT citations | GPTBot is **training only**. **OAI-SearchBot** governs ChatGPT search visibility. Clients can refuse training and keep citations. | `platform.openai.com/docs/bots` |
| Google-Extended controls AI Overviews | It controls **Gemini Apps and Vertex AI** training/grounding. Google: it "does not impact a site's inclusion in Google Search." AI Overviews are governed by Googlebot robots.txt + snippet controls. | `/crawling/docs/.../google-common-crawlers` |
| ClaudeBot is the bot to allow for Claude | **Claude-SearchBot** (indexing) and **Claude-User** (retrieval) drive visibility. ClaudeBot is training. `anthropic-ai` is no longer listed. | Anthropic, 2026-04-07 |
| robots.txt is sufficient access control | **Perplexity-User, ChatGPT-User and Amzn-User may ignore robots.txt** by design; and a WAF blocks bots regardless of robots.txt. | vendor docs |
| There's no AI reporting in Search Console | **Generative AI performance reports** launched 2026-06-03 (Search + Discover). | `/search/blog/2026/06/...` |
| Google says structured data is useless | Google says it "isn't required for generative AI search" and, same paragraph, "it's a good idea to continue using it… helps with being eligible for rich results." | `/search/docs/fundamentals/ai-optimization-guide` |
| Adding citations and statistics always helps | Measured effect **inverts by existing rank**: Cite Sources gives **+115%** to a rank-5 source and **−30%** to a rank-1 source. Target by position. | KDD '24, arXiv:2311.09735 Table 2 |
| llms.txt boosts Google visibility | Google ignores it entirely — and says so explicitly, with no penalty either way. We ship it for other reasons; see `references/llms-txt-and-ai-files.md`. | Google |

---

## References

- `references/deliverable-catalog.md` — full sellable scope with implementation, tooling, QA
- `references/crawler-access.md` — every AI user agent, per-engine controls, WAF/CDN, IP verification
- `references/engine-differences.md` — why GEO is not just SEO, evidenced
- `references/llms-txt-and-ai-files.md` — spec, implementation, honest per-engine status
- `references/content-citation-tactics.md` — rank-stratified tactics with the real research numbers
- `references/technical-checklist.md` — the embedded SEO layer
- `references/measurement.md` — GSC gen-AI reports, referrals, prompt-set tracking
- `references/objection-handling.md` — "Google says GEO isn't real"
- `references/risk-register.md` — spam policies and compliant variants
- `references/evidence-ledger.md` — internal tiers; never quoted to a client

## Scripts

All tested against live sites.

| Script | Purpose |
|---|---|
| `crawler_access_check.py` | 22 AI user agents × robots.txt × live edge response. `--live` catches WAF blocks. |
| `indexability_check.py` | Status, redirects, canonical, robots directives, snippet eligibility, render volume. |
| `schema_extract.py` | JSON-LD extraction with `@graph` flattening, required-property gaps, AI-relevant property notes. |

## Templates

`templates/audit-report.md`, `templates/monthly-report.md`, `templates/prompt-set-baseline.csv` — client-facing, no confidence-tier language.

## Related skills

`schema` (structured data) · `seo-audit` (pure organic engagements) · `agentic-readiness` (agents acting on the site) · `programmatic-seo` (gated by risk register) · `content-strategy` · `analytics`
