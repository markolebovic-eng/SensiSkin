# llms.txt and AI-Specific Files — Spec, Implementation, Honest Status

## Status per engine — say exactly this and nothing more

| Engine | Consumes third-party `llms.txt`? | Evidence |
|---|---|---|
| **Google Search** (incl. AI Overviews, AI Mode) | **No — confirmed** | Google: "You don't need to create new machine readable files, AI text files, markup, or Markdown to appear in Google Search… Google Search itself doesn't use them." And: "Doing so will neither harm nor help your site's visibility or rankings in Google Search, as Google Search ignores them." |
| **ChatGPT / OpenAI** | **Unknown** | No published statement about reading third-party `llms.txt`. OpenAI **does publish one for its own docs** (`platform.openai.com/llms.txt`) and serves `.md` variants of every doc page. That endorses the pattern for docs ingestion; it is not evidence their crawler reads yours. |
| **Perplexity** | **Unknown** | Same situation: `docs.perplexity.ai/llms.txt` exists and their doc pages instruct AI agents to fetch it. No statement about third-party sites. |
| **Claude / Anthropic** | **Unknown** | No published statement. |
| **Copilot / Bing** | **Unknown** | Not retrieved this pass — Bing Webmaster help returned a JS shell. |
| **Apple, Amazon** | **Unknown** | No published statement; both document robots.txt and meta-tag controls instead. |
| **Agent frameworks / dev tooling** | **Partially evidenced** | The OpenAI and Perplexity docs pattern — `llms.txt` index plus `.md` page variants, explicitly addressed "For AI agents" — is real and vendor-endorsed for documentation consumption. |

**Do not claim consumption. Do not claim non-consumption beyond Google.** "Unknown" in our ledger is worth more than a confident guess.

## Why we ship it anyway

1. **Zero policy risk.** Google states explicitly that it neither harms nor helps. There is no penalty vector.
2. **Near-zero cost.** A generated file and a build step.
3. **Asymmetric payoff.** If any engine or agent framework adopts consumption, the client is already covered. If none does, we lost an hour.
4. **Clients expect it.** It is the single most-asked-about GEO artifact. Not having one reads as a gap whether or not it is one.
5. **The underlying discipline is genuinely useful.** Producing a good `llms.txt` forces a clean inventory of the site's canonical, most valuable pages — which surfaces orphans, duplicates, and thin content regardless.

**How to describe it to a client:** "We implement the emerging AI-file standards so your site is covered as engines adopt them. Google has stated it ignores these files with no penalty either way; we implement them for the broader ecosystem." Confident, accurate, no hedging about our own confidence.

**How NOT to describe it:** as the cause of any measured change. See the reporting rules.

## The spec (llmstxt.org)

A markdown file at `/llms.txt`. Structure:

```markdown
# Client Name

> One-sentence description of what the organisation does and who it serves.

Optional short paragraph of essential context — location, specialisms, languages served.

## Core pages

- [Homepage](https://example.com/): What the business does
- [Services](https://example.com/services): Full service list with pricing
- [About](https://example.com/about): Team, credentials, history

## Content

- [Guide title](https://example.com/guide): One-line summary

## Optional

- [Secondary page](https://example.com/x): Lower-priority context
```

Rules: H1 is the name. The `>` blockquote is the summary. H2 sections group links. Every link needs a description. `## Optional` is the documented section an ingesting system may skip when trimming for context.

Companion convention: `/llms-full.txt` containing the full text of key pages inline.

## Implementation checklist

- [ ] `/llms.txt` at the root, served as `text/plain` or `text/markdown`, HTTP 200
- [ ] Canonical URLs only — no redirects, no parameters
- [ ] Every listed URL returns 200 and is indexable
- [ ] Descriptions written for a machine reader: factual, specific, no marketing adjectives
- [ ] Regenerated on publish, not hand-maintained (stale is worse than absent)
- [ ] Referenced from `robots.txt` as a comment for discoverability
- [ ] Not in conflict with robots.txt — do not list pages you disallow
- [ ] In the client's language, matching site content

## Markdown page variants (`.md`)

The pattern OpenAI and Perplexity use for their own docs: every page available at `page.md` as clean markdown. Worth doing for documentation-shaped content — guides, references, service descriptions. Skip for transactional pages.

Serve via content negotiation or a static build step. The markdown must be equivalent to the HTML. **Serving different content at `.md` than at the HTML URL, or varying by user agent, is cloaking** — see `risk-register.md`.

## Machine-readable pricing

No engine documents reading a `/pricing.md`. But the principle underneath it is well-supported by Google's own agentic guidance: an agent evaluating options needs pricing that is **public, crawlable, server-rendered, and not behind a form**. If a competitor's pricing is parseable and the client's is "contact sales" inside a React modal, the client is absent from agent-mediated comparison.

Priority order: make the real pricing page public and server-rendered (high value, evidenced) → add `Offer`/`PriceSpecification` schema (evidenced, parseable) → add a `/pricing.md` mirror (unevidenced, cheap, harmless).

## Files to be honest about

- **`AGENTS.md`** — a convention for coding agents working *in a repository*. It is not a website file and no search engine reads it. Do not ship it as a GEO deliverable.
- **`ai.txt`, `robots-ai.txt`** — proposals with no engine adoption. Skip.
