---
name: wordpress-publish-needs-bash
description: The wordpress-edit skill (live WP publishing) needs Bash/curl, which the orchestrator lacks — delegate the execution half to a Bash-capable subagent
metadata:
  type: feedback
---

The `wordpress-edit` skill executes against the live sensiskinstudio.com WP REST API via `curl` (auth, fetch, POST/PATCH, verify). The **orchestrator agent has no Bash tool** (Read/Write/Glob/Grep/Task/Edit only), and the `seo` agent deliberately has no Bash either.

**Why:** Publishing/editing live WP posts is curl-only in this project. The skill itself says the "analysis/proposal" half is the seo agent's job and the "authenticate/fetch/patch/verify" half belongs to "whoever has Bash." Neither orchestrator nor seo qualifies.

**How to apply:** When a task requires actually writing to WordPress (create post, edit title/meta/body, apply FAQ schema), do all the prep the orchestrator CAN do (read context, verify SEO/title/meta/slug against MEMORY Master Keyword Table, finalize body, write schema JSON files), then delegate ONLY the technical publish to a Bash-capable agent (`general-purpose`), run synchronously so you can report the result. Give it a tight brief: read the SKILL first, verify `.env`/auth as a STOP-gate, sample an existing post's block structure to replicate visual identity, create as `status: "private"` for new posts (never "publish"), no manual Article schema (SASWP auto-adds it on Post type), FAQ as a core/html block. Confirmed working 2026-07-10 (post ID 2661). Note: `.env` with WP creds does exist on the Windows machine (Glob won't match root dotfiles — don't conclude it's missing from a Glob miss; have the Bash agent `test -f .env`). Related: [[trend-lag-routing]].
