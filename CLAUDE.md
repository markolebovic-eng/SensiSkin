# SensiSkin — Claude Code Project

## What this project is
SensiSkin is a skincare brand. This repo contains the business code, marketing 
assets, and AI agent system used to run marketing for SensiSkin and client brands.

## How the agent system works
- All marketing tasks go through the **orchestrator** agent first
- The orchestrator reads this file and .agents/product-marketing.md, then 
  delegates to the right specialist subagent(s)
- Every agent reads .agents/memory/MEMORY.md at the start and updates it 
  with any decisions, outputs, or state worth preserving
- Specialist agents are masters of their own domain — trust their output

## Rules for all agents
1. Always read .agents/product-marketing.md before any task
2. Always read .agents/memory/MEMORY.md before starting
3. Always append key outputs and decisions to .agents/memory/MEMORY.md when done
4. Never modify another agent's .md definition file
5. Write all deliverables to the /outputs/ folder with a timestamp in the filename

## Project structure
- /outputs/        → all generated marketing assets go here
- .claude/agents/  → agent definition files (do not edit during runtime)
- .agents/         → shared context and memory
