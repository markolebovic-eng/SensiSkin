# Measurement

## What exists, and what each thing actually measures

### 1. GSC Generative AI performance report (Search and Discover)

Launched **2026-06-03**, rolling out to a subset of properties.

| | |
|---|---|
| Metric | **Impressions only — no clicks, no CTR, no position** |
| Dimensions | Pages, Countries, Devices (Search only), Dates |
| Granularity | Hourly, daily, weekly, monthly |
| Surfaces | AI Overviews, AI Mode; separate Discover report |
| Availability | Subset rollout — check the property, don't assume |

### 2. GSC standard Performance report

AI Overviews and AI Mode data **is included** here, under the **"Web" search type**, and continues to be. Google: "This data is included in the overall performance report, where it will continue to be tracked… Today, we are launching a separate view dedicated to visibility from generative AI features."

**The resolution of the apparent contradiction between the two Google doc pages: both are true.** The generative AI report is a *filtered view of the same Web-search-type data*, not a new data source.

**Two consequences to state in every report:**
1. **AI impressions are a subset of Search impressions.** They can never be added to total Search traffic. Reporting them as incremental is a fabrication.
2. **AI-specific CTR is not computable.** The gen-AI report has no click data, and clicks in the main report aren't attributable to the AI surface. Anyone quoting an "AI Overview CTR" from Search Console is inventing it.

### 3. AI referral traffic

Segment in GA4 and server logs by referrer host: `chatgpt.com`, `perplexity.ai`, `claude.ai`, `copilot.microsoft.com`, `gemini.google.com`. Build a dedicated GA4 channel group. Low volume is normal and not a failure signal — most AI answers are zero-click by design.

### 4. AI crawler hit rate

From server logs, verified by IP against the published JSON ranges. Answers the most basic question in the pipeline: **are the engines actually fetching us?** A zero hit-rate for `OAI-SearchBot` is a finding that no other measurement surfaces. Track: hits per bot per week, status codes served, pages crawled, crawl recency on priority URLs.

### 5. Per-engine prompt-set citation tracking — the core GEO metric

The only cross-engine visibility measurement that exists.

**Method.** Fix a set of 20–50 prompts reflecting real customer intent — not keywords, actual questions. Run each on a fixed cadence (monthly minimum) across Google AI Mode/AI Overviews, ChatGPT, Perplexity, Claude, Copilot. For each: was the client cited? Which URL? Which competitors were cited? Where in the answer?

Record in `templates/prompt-set-baseline.csv`.

**Discipline that makes it defensible:**
- Same prompts, same wording, every run. Changing the prompt set resets the baseline.
- Record the date and, where visible, the model version.
- Fresh session, no personalisation, consistent locale.
- Multiple runs per prompt where feasible — these systems are stochastic and a single run is a sample, not a measurement.

**Honesty requirement.** This is a *sampled observation of a non-deterministic system*, not a rank tracker. Say so once, then report the numbers with confidence. Do not present it as deterministic ranking data, and never present any third-party tool's output as internal engine data — Google states plainly that no third-party tool has access to its ranking or AI systems.

### 6. Share of voice

Client citations ÷ total citations across the prompt set, tracked against named competitors. The most commercially legible GEO metric, and the one clients understand immediately.

### 7. Bing Webmaster Tools

Bing's index feeds Copilot and ChatGPT. Most clients have never verified there. Baseline it.

---

## Building a defensible before/after narrative

1. **Baseline everything before changing anything.** Access status, indexability, prompt-set citations, GSC, referrals, crawler hit rate.
2. **Log every change with a date.** Access fixes, content changes, schema deploys. `H4` in the catalog.
3. **Define the measurement window** to start after the change plus the engine's propagation delay (~24h for OpenAI/Perplexity robots.txt; days-to-months for Google recrawl).
4. **Report movement alongside scope**, never as causation.

### The reporting rule

**This protects revenue, not Google's feelings.**

✅ *"AI Overview impressions rose 40% over the engagement. During this period we restored crawler access for four AI engines, implemented Organization and LocalBusiness structured data across 34 pages, and rebuilt 12 service pages with sourced statistics and expert attribution."*

Strong, true, sells the full scope, and cannot be disproved.

❌ *"Our llms.txt implementation caused your AI citations to rise 40%."*

A claim the client's next technical hire can disprove. That is how accounts churn and referrals die.

The honest version is also the *better sales document*, because it reports the entire scope of work rather than attributing everything to one line item.

---

## Monthly reporting checklist

- [ ] GSC generative AI impressions — trend, top pages, countries
- [ ] GSC Web search type — impressions, clicks, top queries
- [ ] AI referral sessions by source
- [ ] AI crawler hit rate by bot, with status codes
- [ ] Prompt-set citation rate and share of voice vs competitors
- [ ] Access status — re-run `crawler_access_check.py --live`, confirm no regressions
- [ ] Work performed this period
- [ ] Next period's priorities
- [ ] Standing note: AI impressions are a subset of Search impressions; AI-specific CTR is not computable
