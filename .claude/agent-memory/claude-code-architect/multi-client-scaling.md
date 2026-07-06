---
name: multi-client-scaling
description: Structural risks that will break the SensiSkin agency repo when it grows from 1 client to 2-5 clients
metadata:
  type: project
---

Audit 2026-07-06 (repo moving from 1-client to multi-client). Durable scaling risks found:

- **Single global active-client pointer.** `.agents/agency/active-client.md` is one tracked line mutated by the orchestrator on client switch. Two machines (Win+Mac) working two clients in parallel = race + git merge conflicts on this file, plus mid-conversation client bleed. This is THE multi-client bottleneck. Fix direction: pass client slug per-task/per-conversation, not via shared mutable global state.
- **Cross-client memory bleed.** `memory: project` agent memory is per-AGENT, not per-client (e.g. `.claude/agent-memory/seo/project_serbian_trends_2026.md` is SensiSkin-specific but stored in a client-agnostic dir). At 2+ clients the native agent memory mixes client facts. Per-client durable state should live only in `.agents/clients/{slug}/memory/`.
- **Reproducibility gap (biggest team-onboarding break).** No `.mcp.json` in repo — google-seo-mcp (~40 tools referenced across seo/analytics/research) is user-scope, external. Firecrawl CLI + FIRECRAWL_API_KEY, WP `.env` creds also external. A clone gives agents that reference tools/CLIs that won't exist, with NO documented setup procedure in the repo.
- **Machine divergence, silent.** wordpress-edit skill is Windows/Git-Bash-authored (--ssl-no-revoke, PYTHONIOENCODING, /tmp-doesn't-resolve). research/firecrawl runs on Mac (firecrawl CLI NOT installed on Windows). Two machines have different capabilities; neither documented as a requirement.

Consistency / hygiene facts (verified this audit):
- Orchestrator `tools:` still lists `Task` — works only as a backward-compat ALIAS; `Task` was renamed to `Agent` in v2.1.63 (doc-confirmed). Rename to `Agent` for hygiene; not broken.
- research agent references firecrawl-deep-research / -market-research / -competitive-intel skills that do NOT exist in `.claude/skills/` (likely user-scope plugin skills — unverifiable from repo). Dead-or-external reference.
- README stale: says "9 specialists / 43 skills", omits the `research` agent entirely; actual = 10 specialists + architect, 47 skills. AGENCY.md skill catalog omits wordpress-edit, research/firecrawl, brand-voice-extractor, stop-slop, format-adapter.
- Stray empty `SensiSkin` (0-byte) file at repo root — untracked, accidental.
- No hooks anywhere and no quality/grading loop — all QA is manual owner review. A gap for scaling output volume.
