# Content & Citation Tactics — Rank-Stratified

The strongest independent evidence that content-side GEO tactics move citation rates, applied correctly.

## The research

**Aggarwal et al., "GEO: Generative Engine Optimization", KDD '24** (arXiv:2311.09735).

- **Benchmark:** GEO-bench — 10,000 queries across domains.
- **Metrics:** *Position-Adjusted Word Count* (objective — citation word count weighted by position in the response) and *Subjective Impression* (LLM-judged — relevance, influence, uniqueness, click likelihood, diversity).
- **Headline:** GEO methods boost visibility **up to 40%**.
- **Top three methods** — Cite Sources, Quotation Addition, Statistics Addition — achieved **30–40% relative improvement** on Position-Adjusted Word Count and **15–30%** on Subjective Impression.
- **Real-world validation on Perplexity.ai: up to 37%.**
- **Keyword stuffing performs poorly.** The paper publishes no specific negative percentage; do not invent one.

## The finding that changes how we work — Table 2

Relative improvement (%) in visibility, by the source's **existing search rank**:

| Method | Rank-1 | Rank-2 | Rank-3 | Rank-4 | Rank-5 |
|---|---:|---:|---:|---:|---:|
| **Cite Sources** | **−30.3** | +2.5 | +20.4 | +15.5 | **+115.1** |
| **Quotation Addition** | **−22.9** | −7.0 | +3.5 | +25.1 | **+99.7** |
| **Statistics Addition** | **−20.6** | −3.9 | +8.1 | +10.0 | **+97.9** |
| Authoritative tone | −6.0 | +4.1 | −0.6 | +12.6 | +6.1 |
| Fluency optimization | −2.0 | +5.2 | +3.6 | −4.4 | +2.2 |

**Read this carefully:** the three highest-performing tactics *reduce* citation visibility for sources that already rank first, by 20–30%. The paper's interpretation: generative engines weigh content signals more heavily than the backlink/domain factors that produce a rank-1 position, so these tactics let challengers close the gap — and dilute the incumbent's advantage.

### The operating rule

**Bucket every priority page by its current position for its primary query, then assign tactics.**

| Current position | Tactic assignment |
|---|---|
| **Rank 4+ / not ranking** | Full aggressive treatment. Cite Sources, Quotation Addition, Statistics Addition — all three. This is where +100% effects live. |
| **Rank 3** | Cite Sources (+20.4) and Statistics Addition (+8.1). Skip Quotation Addition (+3.5, not worth the effort). |
| **Rank 2** | Fluency optimization (+5.2) and Authoritative tone (+4.1) only. Avoid Quotation Addition (−7.0). |
| **Rank 1** | **Do not apply the aggressive three.** Fluency and authoritative tone are roughly neutral. If the client insists, run a measured trial on a subset and hold the rest as control. |

This is a genuine specialist position and it is defensible in front of a technical client. It is also the opposite of what every "add more citations and statistics" GEO blog post says.

### Per-domain method selection (Table 3)

Best-performing method varies by content category:

| Method | Strongest categories |
|---|---|
| Cite Sources | Factual statements, Law & Government |
| Quotation Addition | People & Society, Explanation, History |
| Statistics Addition | Law & Government, Debate, Opinion |
| Authoritative tone | Debate, History, Science |
| Fluency optimization | Business, Science, Health |

## Limits — internal only, never in a deliverable

- Primary results ran against a **simulated** generative engine. Perplexity was a separate, smaller real-world validation.
- **2023–24 vintage.** Predates AI Mode, ChatGPT Search in its current form, and current Perplexity.
- "Visibility" means citation prominence — **not traffic, not conversions, not revenue**.
- Single paper, not independently replicated at scale.

These limits govern how hard we lean on the numbers internally. They do not appear in a proposal, and they do not stop us shipping the tactics — the tactics are also just good content practice.

## Implementation

**C2 — Statistics addition.** Replace qualitative claims with sourced quantitative ones. "Treatment is effective" → "In a 2025 study of 340 patients, 87% saw measurable improvement within six weeks (source, linked)." Every statistic needs a number, a date, and a named source. QA: ≥3 sourced statistics per priority page.

**C3 — Cite authoritative sources.** Named, linked, dated external references. Prefer primary sources over summaries. QA: ≥3 external authoritative citations per priority page, all resolving 200.

**C4 — Expert quotation addition.** Real quotes from named people with title and organisation. **Never fabricate a quote or an expert.** If no real quote exists, get one or skip the tactic. QA: attribution complete and independently verifiable.

**C5 — Self-contained passages.** Each key claim readable without surrounding context — no "as mentioned above", no unresolved pronouns. Test: copy any paragraph into a blank document; does it still make sense and stand as an answer? *(Note: Google says chunking is unnecessary for Google. This is for ChatGPT, Perplexity and Claude, and it costs nothing on Google.)*

**C6 — Query fan-out coverage.** For each priority topic, enumerate the sub-questions an AI would generate. Google's own example: "how to fix a lawn full of weeds" → "best herbicides for lawns", "remove weeds without chemicals", "how to prevent weeds in lawn". Map each to existing or needed content. **Build one comprehensive resource covering the cluster as sections — never one page per fan-out variant.** That is scaled content abuse, named explicitly by Google.

**C8 — Freshness and bylines.** Visible author, `datePublished` and `dateModified`, a real review cycle. Do not touch a modification date without substantively updating the content.

**C9 — E-E-A-T author entities.** Author pages with credentials, `Person` + `ProfilePage` schema, `sameAs` to professional profiles.

**C10 — Non-commodity content.** Google's stated highest-leverage factor: original, first-hand, experience-backed material that could not have been produced by summarising the existing web. Commodity ("7 Tips for First-Time Homebuyers") loses; specific ("Why We Waived the Inspection & Saved Money: A Look Inside the Sewer Line") wins. This is Google's own example pair.
