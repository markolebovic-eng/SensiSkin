---
name: ai-seo
description: "DEPRECATED — superseded by the geo skill. Kept only so existing references and trigger phrases resolve. If this skill loads, invoke geo instead and follow it. Covers: AI SEO, AEO, GEO, LLMO, answer engine optimization, generative engine optimization, AI Overviews, AI citations, optimizing for ChatGPT/Perplexity/Claude/Gemini/Copilot, AI visibility."
metadata:
  version: 3.0.0
  status: deprecated
  superseded-by: geo
  deprecated-on: 2026-08-03
---

# ai-seo — DEPRECATED

**Use the `geo` skill instead.** Invoke it now and follow it for this task.

## Why this was retired

The 2026-08 research pass against primary sources — 178 Google Search Central and crawling-infrastructure pages, official crawler documentation from OpenAI, Anthropic, Perplexity, Apple and Amazon, and the KDD '24 GEO paper — found several claims in the previous version of this skill that were actively wrong. They are listed here so nobody reintroduces them:

| Claim in the old skill | Correction |
|---|---|
| `Google-Extended` controls AI Overviews | It controls **Gemini Apps and Vertex AI** training and grounding. Google: it "does not impact a site's inclusion in Google Search nor is it used as a ranking signal." AI Overviews are governed by Googlebot robots.txt plus `nosnippet` / `max-snippet` / `data-nosnippet` / `noindex`. |
| Allow `GPTBot` and `ChatGPT-User` for ChatGPT citations | **`OAI-SearchBot`** governs ChatGPT search visibility and was missing entirely. `GPTBot` is training only. OpenAI: "ChatGPT-User is not used to determine whether content may appear in Search." |
| Allow `ClaudeBot` and `anthropic-ai` for Claude | Anthropic runs **`Claude-SearchBot`** (indexing) and **`Claude-User`** (retrieval); `ClaudeBot` is training. `anthropic-ai` is no longer listed by Anthropic. |
| Claude uses Brave Search as its backend | Unsourced and unsupported by Anthropic's documentation. |
| "There is no AI-specific Search Console reporting" | **Generative AI performance reports** launched 2026-06-03 for Search and Discover. |
| Princeton GEO per-method table (+40% cite sources, +37% statistics, −10% keyword stuffing, etc.) | **Those numbers are not in the paper.** The real finding is that effects **invert by existing rank**: Cite Sources gives **+115.1%** to a rank-5 source and **−30.3%** to a rank-1 source (KDD '24, Table 2). |

The old skill also omitted the Search Console **generative AI features inclusion** setting — a Google-documented hard eligibility gate — and had no coverage of WAF/CDN blocking, which is one of the most common real-world causes of zero AI visibility.

Full audit: `research/00-current-state.md`. Evidence: `.claude/skills/geo/references/evidence-ledger.md`.

## Where everything went

| Old content | New home |
|---|---|
| Platform ranking factors | `geo/references/engine-differences.md` and `crawler-access.md` |
| Content patterns and answer blocks | `geo/references/content-citation-tactics.md` |
| GEO research numbers | `geo/references/content-citation-tactics.md` |
| robots.txt for AI bots | `geo/references/crawler-access.md` |
| llms.txt and machine-readable files | `geo/references/llms-txt-and-ai-files.md` |
| Monitoring and AI visibility tools | `geo/references/measurement.md` |
| Agentic experiences | `agentic-readiness` skill |
| "What NOT to do" | `geo/references/risk-register.md` |
