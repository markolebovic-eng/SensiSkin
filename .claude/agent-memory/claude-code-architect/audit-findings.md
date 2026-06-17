---
name: audit-findings
description: Known weaknesses found while auditing the SensiSkin repo as a Claude Code project
metadata:
  type: project
---

Findings carried across audits/advisory sessions:

- **C1 — thin .gitignore.** Original .gitignore only had `node_modules/` plus two personal image rules (WIN_*.jpg, moja-koza-slojevi-overlay.png). No coverage for settings.local.json, .env/secrets, Python caches, OS cruft, editor dirs. Advisory spec for a hardened .gitignore delivered 2026-06 (read-only — not applied by this agent).

Verified doc facts used:
- `.claude/settings.local.json` should be gitignored; Claude Code auto-ignores it only when IT creates the file — if hand-created, must add manually. (code.claude.com/docs/en/settings)
- `CLAUDE.local.md` is the local personal memory file and should be gitignored. (code.claude.com/docs/en/memory)
- Default auto-memory lives at `~/.claude/projects/<project>/memory/` (machine-local, outside repo) — but THIS repo redirects agent memory in-repo, see [[repo-layout]].

**Why:** So re-audits build on prior context instead of re-discovering.
**How to apply:** On follow-ups about VCS hygiene/security, start from C1 status; check whether it was actually applied (read .gitignore) before assuming.
