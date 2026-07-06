---
name: wordpress-edit-spof
description: The wordpress-edit skill is the only live-production write path; its execution-path and rollback risks
metadata:
  type: project
---

`.claude/skills/wordpress-edit/SKILL.md` (v1.0.0) is the ONLY capability with write access to the live sensiskinstudio.com WordPress site (REST API + Application Password Basic Auth). Single point of failure for production.

Key structural issues (audit 2026-07-06):
- **Undefined executor.** Skill needs Bash (curl) to run. But `seo` agent has NO Bash (deliberately dropped, commit 1f01de6) and `orchestrator` has NO Bash (tools: Read,Write,Glob,Grep,Task). So NO subagent can execute it — only the main-thread session (all tools) can. Yet CLAUDE.md says "all tasks go through orchestrator." Execution path for the most dangerous capability is contradictory in config. Skill text itself says "orchestrator or whoever has Bash" but orchestrator lacks Bash.
- **No durable rollback.** Skill backs up pre-write state to the scratchpad temp dir (ephemeral, machine-local, lost between sessions/machines). If a live page breaks, the only backup may be gone / on the other machine. No committed snapshot.
- Skill is otherwise well-disciplined: propose-before-apply, never-change-slug, never-print-credential, Elementor dual-write (content + _elementor_data), verify-against-live-frontend, credit/indexing hygiene. The DISCIPLINE is good; the SPOF + executor ambiguity + rollback are the risks.

Reference-page canonical example currently `/leto-i-promene-na-kozi/` (post 2047); skill notes it will be replaced by the next new-blog-post template.
