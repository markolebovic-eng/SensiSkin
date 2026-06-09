# AI Marketing Agency — Claude Code Project

## What this project is
This is an AI-powered marketing agency. The repo contains the multi-agent system, 
client context files, and all generated marketing deliverables for each client. 
The first and currently active client is Sensi Skin Kozmetološki Centar.

## How the agent system works
- All marketing tasks go through the **orchestrator** agent first
- The orchestrator reads `.agents/agency/AGENCY.md` and determines the active 
  client by reading `.agents/agency/active-client.md`
- The orchestrator reads the active client's `product-marketing.md` and `MEMORY.md`, 
  then delegates to the right specialist subagent(s)
- Every agent reads the client's MEMORY.md at the start and updates it with any 
  decisions, outputs, or state worth preserving
- Specialist agents are masters of their own domain — trust their output

## Rules for all agents

0. LANGUAGE: All client-facing outputs, copy, content, and deliverables must match 
   the client's language setting in their `product-marketing.md`. SensiSkin: Serbian 
   (srpski jezik), Latin script (not Cyrillic) unless user requests Cyrillic. 
   Agent-to-agent communication and internal MEMORY.md notes may stay in English.

1. Always read `.agents/agency/active-client.md` first to get the client slug.
   Then construct all paths using that slug: `.agents/clients/{slug}/`

2. Always read `.agents/clients/{slug}/product-marketing.md` before any task

3. Always read `.agents/clients/{slug}/memory/MEMORY.md` before starting

4. Always append key outputs and decisions to `.agents/clients/{slug}/memory/MEMORY.md` 
   when done

5. Never modify another agent's `.md` definition file

6. Write all deliverables to `/outputs/{slug}/` with a timestamp in the filename

7. Always invoke the relevant Skill before working on a task — do not reinvent 
   frameworks that already exist in the skill library

## How to determine the active client

Read `.agents/agency/active-client.md`. The file contains a single line with the 
client slug (e.g., `sensiskin`). Use this slug for all file paths. 
If the user mentions a different client name in their message, the orchestrator 
should update `active-client.md` to the new slug before delegating.

## Project structure

```
.agents/
├── agency/
│   ├── AGENCY.md          → agency-level context, services, skill catalog
│   └── active-client.md   → single line: current client slug
└── clients/
    ├── sensiskin/
    │   ├── product-marketing.md   → SensiSkin brand context
    │   └── memory/
    │       └── MEMORY.md          → SensiSkin project memory
    └── _template/
        ├── product-marketing.md   → blank template for new clients
        └── memory/
            └── MEMORY.md          → blank memory template

.claude/
├── agents/    → agent definition files (do not edit during runtime)
└── skills/    → 44 pre-built skill frameworks (invoke via Skill tool)

outputs/
└── sensiskin/ → all SensiSkin deliverables go here
    └── [new-client-slug]/ → deliverables per client
```
