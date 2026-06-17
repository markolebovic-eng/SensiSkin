---
name: repo-layout
description: Structure and version-control conventions of the SensiSkin AI-marketing-agency Claude Code repo
metadata:
  type: project
---

SensiSkin is an AI marketing agency built ON Claude Code. Not a Node app — package.json/node_modules are tooling only (PDF generation etc.). Single Python script: scripts/generate_pdf_report.py.

Key structure (per CLAUDE.md and confirmed on disk):
- `.claude/agents/`, `.claude/skills/` — agent + skill definitions (committed).
- `.claude/agent-memory/<agent>/` — this repo overrides Claude Code's default machine-local auto-memory location into an IN-REPO path. So agent memory IS within version-control range and must be handled deliberately in .gitignore. As of audit, agent-memory/ is UNtracked (not committed).
- `.agents/agency/` and `.agents/clients/{slug}/` — client context, product-marketing.md, memory/MEMORY.md. Active client resolved via `.agents/agency/active-client.md`. Currently `sensiskin`.
- `outputs/{slug}/` — client deliverables (md/html/pdf/png). INTENTIONALLY TRACKED — these are the agency's product, not build artifacts. Do NOT propose ignoring outputs/.

Repo specifics found during .gitignore work (2026-06):
- A stray tracked file named `SensiSkin` (no extension) sits at `SensiSkin/SensiSkin` — looks accidental, worth flagging.
- `scripts/_capacity_audit_data.json` is an untracked scratch file (leading underscore convention may = scratch).
- Personal photos committed at root: WIN_*.jpg, moja-koza-slojevi-overlay.png — current .gitignore targets these.
- No secrets/.env/keys currently tracked (grep clean as of 2026-06).

**Why:** Determines what a correct .gitignore must protect vs preserve.
**How to apply:** Never recommend ignoring outputs/. Treat .claude/agent-memory and .agents/clients/*/memory as potentially sensitive client data when advising on ignore/secret rules.
