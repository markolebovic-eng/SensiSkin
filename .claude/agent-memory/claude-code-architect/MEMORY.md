# Claude Code Architect — Project Memory

Index of durable facts about the SensiSkin repo as a Claude Code project.

- [Repo Layout & Conventions](repo-layout.md) — how this AI-marketing-agency repo is structured and what is tracked vs not
- [Audit Findings Log](audit-findings.md) — known weaknesses surfaced across audits (e.g. C1 .gitignore)
- [Settings Decision](settings-decision.md) — use the minimal deny-focused settings.json (Candidate A); verified permission-rule semantics
- [SEO Agent MCP Wiring](seo-agent-mcp.md) — seo.md lists 22 google-seo-mcp tools; server NOT connected in agent-thread sessions, blocks live tool audits
- [Multi-Client Scaling Risks](multi-client-scaling.md) — active-client global pointer, cross-client memory bleed, reproducibility/MCP gap, machine divergence
- [WordPress-Edit SPOF](wordpress-edit-spof.md) — only live-prod write path; undefined executor (no subagent has Bash) + ephemeral rollback
