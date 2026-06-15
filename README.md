# AI Marketing Agency — Claude Code

A multi-agent AI marketing agency built on Claude Code's subagent architecture. An orchestrator agent coordinates a team of specialist subagents, each with its own skill library, working against isolated per-client context folders. The system is client-agnostic — any number of clients can be onboarded by adding a context folder and updating a single pointer file.

## Architecture

```
User → Orchestrator → Specialist agent(s) → Skills → Output files
                   ↓
          Reads active-client.md
          Loads client product-marketing.md + MEMORY.md
          Delegates with context
          Synthesizes and returns result
```

- **Orchestrator** — entry point for all tasks; reads client context, routes to specialists, runs parallel when possible
- **Specialist agents** (9) — each owns one domain; invoke relevant Skills rather than working from first principles
- **Skills** (43) — reusable frameworks and templates invoked via the `Skill` tool
- **Per-client context** — brand context and project memory isolated in `.agents/clients/{slug}/`

Full service catalog and 9-step SOP: [.agents/agency/AGENCY.md](.agents/agency/AGENCY.md)

## Subagents

| Agent | What it does |
|-------|-------------|
| `orchestrator` | Central coordinator for all marketing tasks across any client — routes, delegates, synthesizes |
| `seo` | Site audits, keyword research, schema markup, technical SEO, AI search optimization (AEO/GEO), local SEO |
| `copywriter` | Homepage and service page copy, taglines, CTAs, brand narratives, video scripts; brand voice guardian |
| `analytics` | GA4/GTM setup, pixel tracking, conversion tracking, performance reporting, attribution, revenue operations |
| `cro` | Landing page audits, booking form optimization, A/B test planning, funnel and signup flow analysis |
| `email` | Welcome, nurture, and win-back sequences; newsletters; SMS campaigns; lifecycle flow strategy |
| `paid-ads` | Meta, Google, and TikTok campaign strategy; ad creative and copy; audience targeting; performance analysis |
| `social` | Instagram/TikTok/LinkedIn strategy, monthly content calendars, captions, Reels scripts, hashtag research |
| `strategy` | 12-month marketing plans, go-to-market strategy, competitor intelligence, pricing, growth planning |
| `claude-code-architect` | Claude Code setup auditor — scans `.claude/` config and advises on architecture, agent design, and MCP |

## Running the System

All tasks go through the orchestrator. In Claude Code, simply describe the task:

```
"Write a blog post about facial treatments for SensiSkin"
"Audit the SEO on sensiskinstudio.com"
"Build a 3-month content calendar for Instagram"
```

The orchestrator identifies the active client, loads context, delegates to the right specialist(s), and returns a synthesized result. Specialists write deliverables to `outputs/{slug}/` and update `MEMORY.md`.

Full SOP (9 steps): [.agents/agency/AGENCY.md → Standard operating procedure](.agents/agency/AGENCY.md)

## Multi-Client Model

The active client is determined by a single pointer file:

```
.agents/agency/active-client.md   → contains one line: the client slug (e.g. "sensiskin")
```

All agents construct their file paths from this slug:

| File | Purpose |
|------|---------|
| `.agents/clients/{slug}/product-marketing.md` | Brand context, positioning, tone, target audience, services |
| `.agents/clients/{slug}/memory/MEMORY.md` | Accumulated project memory — decisions, deliverables, next steps |
| `outputs/{slug}/` | All deliverables for this client, organized in numbered subfolders |

To switch clients, update `active-client.md` to the new slug. The orchestrator handles this automatically when a different client is mentioned.

## Onboarding a New Client

1. Copy `.agents/clients/_template/` → `.agents/clients/{new-slug}/`
2. Fill in `product-marketing.md` with real brand data
3. Initialize `memory/MEMORY.md` from the template
4. Add the client to the registry in `.agents/agency/AGENCY.md`
5. Update `.agents/agency/active-client.md` to the new slug
6. Create `outputs/{new-slug}/` with a `.gitkeep`

## Repo Structure

```
.agents/
├── agency/
│   ├── AGENCY.md             # Agency-level context, service catalog, SOP, client registry
│   └── active-client.md      # Single line: current client slug
└── clients/
    ├── _template/            # Blank template — copy this for each new client
    └── {slug}/               # One folder per client
        ├── product-marketing.md
        └── memory/MEMORY.md

.claude/
├── agents/                   # Subagent definition files (10 agents)
├── skills/                   # 43 skill frameworks invoked via Skill tool
└── agent-memory/             # Agent-scoped persistent memory (auto-managed)

outputs/
└── {slug}/                   # All deliverables for a client, organized in subfolders

scripts/                      # Utility scripts (PDF report generator, etc.)

CLAUDE.md                     # Project-level rules loaded into every Claude Code session
```
