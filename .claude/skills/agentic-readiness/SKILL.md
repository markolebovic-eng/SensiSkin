---
name: agentic-readiness
description: "Use when AI agents need to act on a site rather than just read it — browse, compare, fill forms, book, or buy on a user's behalf. Trigger phrases: 'AI agents,' 'agentic commerce,' 'agent-friendly,' 'can ChatGPT buy from us,' 'AI shopping agents,' 'browser agents,' 'agent checkout,' 'Operator,' 'Computer Use,' 'UCP,' 'Universal Commerce Protocol,' 'MCP for our site,' 'will an AI be able to book with us,' 'agent-readable pricing,' 'accessibility tree,' 'Web Bot Auth.' For visibility and citation in AI answers, see geo. For conversion optimization for human visitors, see cro. For structured data implementation, see schema."
metadata:
  version: 1.0.0
  last-research: 2026-08-03
---

# Agentic Readiness

Optimizing a site for AI agents that **act** — navigate, compare, transact — rather than AI search that **cites**. Distinct problem, distinct evidence base, and a strong upsell alongside a GEO engagement.

## Why this is its own skill

GEO asks "will an AI answer mention us?" Agentic readiness asks "**can an AI complete a task on our site, or will it give up and recommend a competitor?**" The failure mode is different: not invisibility, but abandonment mid-task. And the fix set is different — it is accessibility, form semantics, state stability, and public machine-readable facts, not content and citations.

## How agents access a site

Google documents three mechanisms browser agents use:

1. **Visual rendering** — screenshots interpreted as a user would see them
2. **DOM inspection** — parsing the page's HTML structure
3. **The accessibility tree** — the same semantic layer assistive technology consumes: roles, labels, landmarks, headings, states

**The third is the leverage point.** A site that is genuinely accessible is substantially agent-ready as a by-product, and a site with `<div onclick>` buttons and unlabelled inputs is opaque to agents no matter how good it looks. Accessibility work now has a direct commercial return, which is a useful thing to be able to tell a client.

## Audit checklist

### Perceivable content
- [ ] Main content in server-rendered HTML — an agent that screenshots a loading spinner sees nothing
- [ ] No content requiring hover, scroll-triggered loading, or animation to appear
- [ ] Critical facts as text, not baked into images
- [ ] Reasonable load time — agents time out

### Accessibility tree
- [ ] Landmarks: `<main>`, `<nav>`, `<header>`, `<footer>`, `<aside>`
- [ ] Logical heading hierarchy, no skipped levels
- [ ] Every interactive element has an accessible name
- [ ] Native elements (`<button>`, `<a>`, `<select>`) over ARIA-decorated `<div>`s
- [ ] ARIA used correctly or not at all — wrong ARIA is worse than none
- [ ] Form inputs have associated `<label>`, correct `type`, and `autocomplete`
- [ ] Error messages programmatically associated with their fields
- [ ] State changes announced (`aria-live` where relevant)
- [ ] Full keyboard operability — a strong proxy for agent operability

### Structural stability
- [ ] Stable, semantic selectors — not hashed build-generated class names
- [ ] Layout does not re-render unpredictably on interaction
- [ ] Meaningful URLs for meaningful states, so an agent can navigate directly
- [ ] Back button works
- [ ] No CAPTCHA on read-only paths (Anthropic states its bots will not attempt to bypass CAPTCHAs; others behave similarly)

### Machine-readable facts
- [ ] **Pricing public, server-rendered, not gated.** The single highest-value item. An agent comparing options cannot evaluate "contact sales."
- [ ] Specs, dimensions, compatibility as structured text or tables
- [ ] Hours, location, contact details public and marked up
- [ ] Availability and stock status accurate
- [ ] `Product` / `Offer` / `PriceSpecification` / `LocalBusiness` schema present
- [ ] Optional: `/pricing.md` mirror (no engine documents reading it; cheap and harmless)

### Transaction paths
- [ ] Checkout or booking completable without hover-only interactions
- [ ] Guest checkout available
- [ ] No forced account creation before price disclosure
- [ ] Clear confirmation states
- [ ] Predictable multi-step flows with visible progress

### Agent identification
- [ ] Agent traffic distinguishable in logs by UA
- [ ] `Google-Agent` recognised; **Web Bot Auth** signatures (`agent.bot.goog`) verified if the CDN supports it
- [ ] Bot management does not block legitimate agents — the same WAF problem as GEO
- [ ] Decision recorded on which agents may transact

## Emerging protocols

**Universal Commerce Protocol (UCP)** — referenced by Google as an emerging standard giving Search agents standardised hooks for catalogue discovery, pricing, and checkout. Not yet a deliverable. Monitor `ucp.dev`; the structural work above is the precursor and is useful regardless of whether UCP wins.

**Web Bot Auth** — IETF draft for cryptographic bot request signing. Google is testing it, explicitly experimental, with major CDNs and WAFs adding support. Google's own guidance is to keep IP, reverse-DNS and user-agent verification as the fallback, because not every request is signed. Deliverable today: confirm CDN support and ensure agent traffic is not blocked.

**MCP** — relevant if the client has an API worth exposing to agents directly. Scope separately; it is a product decision, not a marketing one.

## Deliverables

| # | Deliverable | Value |
|---|---|---|
| AR1 | Accessibility-tree audit against agent operability | High — dual accessibility and commercial return |
| AR2 | Server-render audit of critical paths | High |
| AR3 | Public machine-readable pricing and specs | **Highest** — direct effect on agent-mediated comparison |
| AR4 | Form and checkout semantics review | High for transactional sites |
| AR5 | Selector and state stability review | Medium |
| AR6 | Commerce structured data (`Product`, `Offer`, `LocalBusiness`) | High |
| AR7 | Agent traffic identification and bot-management review | High |
| AR8 | Web Bot Auth readiness | Medium, rising |
| AR9 | UCP monitoring brief | Low today |
| AR10 | Agent task-completion test — actually attempt the client's key tasks with a browser agent and record where it fails | **Highest diagnostic value** |

**AR10 is the demo that sells the engagement.** Recording an agent failing to book an appointment on the client's own site is more persuasive than any audit table.

## Related skills

`geo` (visibility and citation in AI answers — this skill's sibling) · `cro` (human conversion) · `schema` (structured data) · `seo-audit` (organic rankings)
