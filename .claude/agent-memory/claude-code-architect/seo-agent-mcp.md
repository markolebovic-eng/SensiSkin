---
name: seo-agent-mcp
description: State of the SEO agent's google-seo-mcp tool wiring and the in-session connectivity gap that blocks live tool audits
metadata:
  type: project
---

The `.claude/agents/seo.md` agent (model sonnet, memory project) lists 22 `mcp__google-seo-mcp__*` tools in frontmatter plus Read, Write, Glob, Grep, Bash, WebSearch. It references google-seo-mcp v0.8.5 (~102 tools total per user).

There is NO `.mcp.json` in the repo. The google-seo-mcp server is therefore configured at user/enterprise scope, not project scope — so it is not reproducible from the repo and not guaranteed present in any given session.

KEY BLOCKER (observed 2026-06): in audit sessions, NO `mcp__google-seo-mcp__*` tool is callable. Both `get_capabilities` and `gsc_list_sites` returned "No such tool available." The server is not connected to the agent-thread session that runs these audits. Consequence: cannot retrieve the live ~102-tool catalog, so cannot do exact name-matching of frontmatter IDs or a complete gap analysis against ground truth. Do NOT guess the catalog from memory.

**Why:** Tasks that ask to call get_capabilities and compare the 22 listed tools against the live list cannot be completed in the agent-thread environment as-is.
**How to apply:** If asked again for a live SEO MCP tool audit, first re-test one cheap tool (e.g. gsc_list_sites). If it errors, report the connectivity gap up front rather than fabricating tool names. The main Claude Code session (not the subagent thread) may have the server connected — suggest the user run the live-comparison portion there.
