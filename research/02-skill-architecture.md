# 02 — Skill Architecture

## Constraint

**GEO is the umbrella skill.** It is comprehensive, embeds the SEO layer, and is the skill a GEO engagement is assembled from. `seo-audit` remains for engagements sold as SEO. This is a product decision, not a technical one.

## Candidate assessment

Criteria: (a) enough distinct material, (b) triggered independently by real client phrasing, (c) sellable as a distinct line item. A skill nobody triggers is worse than a good reference file.

| Candidate | Source volume | Triggered independently? | Sellable line item? | Verdict |
|---|---|---|---|---|
| **geo** (umbrella) | Everything | Yes — "GEO", "AEO", "AI search", "why don't we show up in ChatGPT" | **Yes — the flagship** | **Build** |
| **seo-audit** (exists) | ~90 Google pages | Yes — "SEO audit", "traffic dropped" | Yes | **Keep, deepen, deduplicate** |
| **structured-data** | 39 Google feature guides + schema.org beyond Google's set + validation | Yes — "schema", "rich results", "JSON-LD", "review stars" | Yes | **Merge into existing `schema` skill and expand.** Volume clearly justifies it; a separate new skill would collide with `schema`. |
| **agentic-readiness** | `web.dev/ai-agent-site-ux`, UCP, a11y tree, Web Bot Auth, agent commerce | Yes — "AI agents", "agentic commerce", "can ChatGPT buy from us" | **Yes — strong GEO upsell, new territory** | **Build** |
| **search-console-diagnostics** | 15 monitor/debug pages + gen-AI reports + GSC help | Yes — "traffic dropped", "Search Console says" | Marginal alone | **Reference file inside `geo` + `seo-audit`.** Diagnostic work is always *inside* an engagement, rarely bought standalone. |
| **ecommerce-seo** | 9 ecom pages + 7 shopping schema guides + Merchant Center | Yes — "product feed", "Merchant Center" | Yes | **Defer.** Real volume, but no current client. Build when an ecommerce client signs. Recorded in gap analysis. |
| **international-seo** | 4 pages | Partly | Rarely alone | **Keep as `seo-audit` reference** — the existing one is genuinely strong. |
| **site-migration** | Site moves, redirects, A/B tests, pausing | Yes — "we're replatforming" | Yes, high-stakes | **Defer.** Checklist-shaped and high-value, but not the current bottleneck. |
| **content-quality-review** | Helpful content, E-E-A-T, spam policies, AI-content, reviews system | Overlaps `copy-editing`, `content-strategy`, `stop-slop` heavily | No | **Reject as a skill.** Becomes `geo/references/content-quality.md`. Adding a fourth skill in territory three already occupy would make routing worse. |

## Final architecture

```
geo/                        ← UMBRELLA. Owns the AI-visibility engagement end to end.
├── SKILL.md                  triggers, decision tree, deliverable catalog as scoping menu
├── references/
│   ├── deliverable-catalog.md      full sellable scope, budget tiers
│   ├── crawler-access.md           every AI UA, per-engine controls, WAF/CDN, IP verification
│   ├── engine-differences.md       the "why GEO ≠ SEO" evidence
│   ├── llms-txt-and-ai-files.md    spec, implementation, honest per-engine status
│   ├── technical-checklist.md      the embedded SEO layer
│   ├── content-citation-tactics.md rank-stratified tactics, KDD numbers
│   ├── measurement.md              GSC gen-AI reports, referrals, prompt-set tracking
│   ├── objection-handling.md       the Google-says-GEO-isn't-real conversation
│   ├── risk-register.md            spam policies + compliant variants
│   ├── evidence-ledger.md          internal tiers (copy of research ledger)
│   └── content-quality.md          E-E-A-T, helpful content, AI-content policy
├── scripts/                  tested, executable
└── templates/                client-facing — no confidence-tier language
    ├── audit-report.md
    ├── monthly-report.md
    └── prompt-set-baseline.csv

schema/         ← expand to full 39-feature matrix + recipes + beyond-Google types
seo-audit/      ← deepen; deduplicate against geo; keep international ref
agentic-readiness/  ← NEW: agents, a11y tree, UCP, Web Bot Auth, agent commerce
ai-seo/         ← DEPRECATE → thin pointer to geo (preserves existing triggers)
```

**Why `ai-seo` becomes a pointer rather than being deleted:** its `description` already captures the right trigger phrases and may be referenced elsewhere. Deleting it risks a routing hole; leaving it live risks the contradicted claims (C1–C5) being served to a client. A pointer solves both.

## Boundaries (to prevent misrouting)

- **geo** — anything about visibility in AI answers, any engine, plus the full engagement. Owns cross-engine crawler access.
- **seo-audit** — Google/Bing organic ranking diagnosis when AI surfaces aren't the ask.
- **schema** — structured data implementation, invoked *by* geo and seo-audit.
- **agentic-readiness** — agents *acting* on the site (browsing, comparing, transacting), not answering questions about it.
