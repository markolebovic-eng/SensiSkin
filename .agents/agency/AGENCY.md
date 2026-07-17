# AI Marketing Agency — Master Context

## Agency overview

This is an AI-powered marketing agency system built on Claude Code's multi-agent 
architecture. The agency serves multiple clients, each with their own dedicated 
context folder. All marketing work goes through the orchestrator agent which 
coordinates specialist subagents.

## Active client

**Always read `.agents/agency/active-client.md` first.** This file contains the 
slug of the currently active client. Use this slug to construct all file paths:

- Brand context: `.agents/clients/{client-slug}/product-marketing.md`
- Project memory: `.agents/clients/{client-slug}/memory/MEMORY.md`
- Output folder: `/outputs/{client-slug}/`

To switch clients, the orchestrator updates `active-client.md` with the new slug.

## Client registry

| Client slug | Brand name | Status |
|-------------|------------|--------|
| sensiskin | Sensi Skin Kozmetološki Centar | Active |
| casa-montana | Casa Montana (luksuzna brvnara, Kopaonik) | Active |

*(Add new clients here as they are onboarded)*

## Services this agency offers

Each service maps to one or more available skills:

### Content & Copy
- Copywriting (web, ads, social, email) → `copywriting`, `copy-editing`
- Content strategy & planning → `content-strategy`
- Marketing psychology & persuasion → `marketing-psychology`
- Social media content (captions, scripts, calendars) → `social`, `video`

### Search & Visibility
- SEO audit & technical fixes → `seo-audit`, `schema`, `site-architecture`
- Keyword research & on-page SEO → `seo-audit`, `ai-seo`
- AI search optimization (AEO/GEO) → `ai-seo`
- Programmatic SEO at scale → `programmatic-seo`
- Local directory submissions → `directory-submissions`

### Paid Advertising
- Meta, Google, TikTok campaign setup → `ads`
- Ad creative & copy variations → `ad-creative`
- Competitor ad intelligence → `competitor-profiling`, `competitors`

### Email & Lifecycle
- Welcome, nurture, win-back sequences → `emails`
- SMS campaigns → `sms`
- Churn prevention flows → `churn-prevention`

### Conversion & Growth
- Landing page & funnel optimization → `cro`
- A/B testing design → `ab-testing`
- Signup flow optimization → `signup`
- Onboarding flow → `onboarding`
- Popup & lead capture → `popups`
- Paywall optimization → `paywalls`
- Referral program design → `referrals`
- Lead magnet creation → `lead-magnets`
- Free tools strategy → `free-tools`

### Strategy & Planning
- Full marketing plan (12-month) → `marketing-plan`
- Product launch strategy → `launch`
- Competitor intelligence → `competitor-profiling`, `competitors`
- Customer & market research → `customer-research`
- Pricing strategy → `pricing`
- Co-marketing & partnerships → `co-marketing`

### Analytics & Data
- GA4 + GTM setup → `analytics`
- Attribution & reporting → `analytics`
- Revenue operations → `revops`

### Sales & Business Development
- Cold email outreach → `cold-email`
- B2B prospecting → `prospecting`
- Sales enablement materials → `sales-enablement`

### Video Production
- Cinematic property walkthrough videos (real estate/rental listings) →
  `property-walkthrough` agent (NOT a skill — invoke the agent directly;
  uses Higgsfield MCP for generation/stitching, Apify for Booking.com photo
  scraping, direct fetch for Airbnb)

## How agents use skills

Skills are invoked using the `Skill` tool. Each specialist agent should invoke 
the relevant skill(s) for their task instead of working purely from first 
principles. Skills contain proven frameworks, templates, and best practices.

Example: When the SEO agent is asked for a site audit, it should invoke 
`Skill({ skill: "seo-audit" })` to access the full audit framework, rather 
than improvising the audit structure.

## Standard operating procedure

1. Orchestrator receives task from user
2. Orchestrator reads `active-client.md` to identify current client
3. Orchestrator reads client's `product-marketing.md` and `MEMORY.md`
4. Orchestrator delegates to specialist agent(s) with: task, client slug, context summary
5. Each specialist reads the client folder using the slug from the brief
6. Specialist invokes relevant skill(s) for their task
7. Specialist writes output to `/outputs/{client-slug}/[task-name]-[YYYY-MM-DD].[ext]`
8. Specialist updates client's `MEMORY.md` with decisions and outputs
9. Orchestrator synthesizes and returns summary to user

## Language rule

All client-facing content and deliverables must match the client's language 
setting (see their `product-marketing.md`). SensiSkin: Serbian, Latin script. 
Internal notes and agent-to-agent communication may remain in English.

## Onboarding a new client

1. Duplicate `.agents/clients/_template/` folder → `.agents/clients/{new-slug}/`
2. Fill in `product-marketing.md` with real client data
3. Create empty `memory/MEMORY.md` using the standard template
4. Add client to the registry table above
5. Update `active-client.md` to the new slug
6. Create `/outputs/{new-slug}/` folder
