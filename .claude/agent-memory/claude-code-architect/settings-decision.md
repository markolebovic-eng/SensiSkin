---
name: settings-decision
description: Decision on which .claude/settings.json permissions design to use for this repo, and the verified rule semantics behind it
metadata:
  type: project
---

The repo's `.claude/settings.json` should use the minimal, deny-focused design (the user's "Candidate A").

**Why:** Compared against a broader allow-list alternative ("Candidate B"), A was correct on every disputed point. Idiomatic Claude Code permissions = allow-list only the non-trivial commands you actually run, let the built-in read-only set cover the rest, lean on deny for safety.

**How to apply:** If asked to revisit settings, start from A; do not reintroduce B's broad allow list. Verified facts behind the decision (per https://code.claude.com/docs/en/permissions and /permission-modes):
- Valid `defaultMode` values: default, acceptEdits, plan, auto, dontAsk, bypassPermissions. `"ask"` is NOT valid. `auto` is ignored from project/local settings (user-level only).
- `Read(.env)` (bare filename = matches any depth, gitignore semantics) is stronger than `Read(./.env)` (cwd-anchored only). Prefer bare-filename deny rules.
- `*` matches within one path segment; `**` matches across directories. Use `Write/Edit(.claude/agents/**)` not `/*` to protect nested agent files.
- `.claude/` is a protected path: allow rules never auto-approve writes there; deny rules still work and are absolute. Deny order: deny -> ask -> allow.
- Keep both `Bash(git push)` and `Bash(git push *)` to unambiguously block the bare-upstream push form.
- Built-in read-only Bash commands (ls, cat, echo, pwd, head, tail, grep, find, wc, which, diff, stat, du, cd, read-only git) never prompt, so allow-listing them is redundant. Read/Glob/Grep are also free.

The validated file lives at c:\Users\Marko\SensiSkin\.claude\settings.json (the user maintains it; this agent is read-only on the repo). Related: [[repo-layout]], [[audit-findings]].
