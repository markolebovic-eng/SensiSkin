# Risk Register — Spam Policies and Compliant Variants

The only reason to exclude or gate a tactic is **downside risk to the client's site**. Unproven is fine; risky is not. Google's spam policies can trigger manual actions or algorithmic suppression that destroy organic visibility — and because every major AI surface is grounded in a search index, that takes AI visibility down with it.

Every entry below gives the risk, the threshold at which it becomes a violation, and **a compliant version that achieves the same client goal**. We want the aggressive playbook executed in a way that doesn't get a client torched.

Reference: `/search/docs/essentials/spam-policies`.

---

## 1. Scaled content abuse — `requires-compliant-variant`

**The risk.** Google's AI optimization guide names this explicitly: creating separate content for every variation of how people might search, "for example, by focusing on other queries that people have asked, or fan-out queries", primarily to manipulate rankings, "violates Google's scaled content abuse spam policy."

**Threshold.** Generating pages primarily to capture query permutations rather than to serve a distinct user need. Not a page count — a purpose test. A thousand genuinely distinct location pages with real inventory are fine; fifty near-identical pages targeting fan-out phrasings are not.

**Why it's the top entry.** This is the tactic most GEO vendors sell, it is the fastest route to a manual action, and it would take the entire engagement's results down with it.

**Compliant variant.** Build **one comprehensive resource per topic cluster**, covering the fan-out sub-questions as sections within it. This achieves the same retrieval coverage — Google states its systems now understand relevance "even when there is no exact match between the query and the page's primary content" — with no policy exposure and less maintenance.

**Gate before any programmatic work.** For each templated page, answer in writing: *what does this page contain that no other page on this site contains, and would a person be satisfied landing here?* If the answer is "a different keyword in the heading", do not publish it. Record the gate decision.

## 2. Site reputation abuse (parasite SEO) — `policy-risk`

**The risk.** Publishing on a third party's domain to exploit its ranking signals.

**Threshold.** Content hosted on someone else's domain with little first-party oversight, published primarily for ranking benefit.

**Compliant variant.** Earn genuine editorial placement where the host has real editorial control and the content serves their audience. Keep commercial-intent content on the client's own domain. Guest contributions are fine when they are real contributions.

## 3. Link schemes — `requires-compliant-variant`

**The risk.** Buying, exchanging, or scaling links or mentions to manipulate ranking.

**Threshold.** Anything of value exchanged for a link without `rel="sponsored"` / `rel="nofollow"`; large-scale guest posting with optimised anchors; link exchanges.

**Compliant variant.** Digital PR built on a real story. Original research and public data that others cite because it is useful. Genuine partnerships. Correct `rel` attributes wherever anything of value changed hands. **We never buy links, and we say so to the client up front** — it is a differentiator, not an apology.

## 4. Inauthentic mention-seeking — `requires-compliant-variant`

**The risk.** Google's AI guide calls out "seeking inauthentic 'mentions'" directly, noting core ranking systems focus on high-quality content while other systems block spam, and that AI features depend on both.

**Threshold.** Manufactured, incentivised, or undisclosed-affiliate mentions at scale. Astroturfing Reddit or review platforms.

**Compliant variant.** Be genuinely worth referencing: publish original research, make experts available for comment, maintain accurate profiles. Participate in communities under a real identity with disclosed affiliation. **On Wikipedia: correct factual errors through proper channels with disclosed conflict of interest. Never edit promotionally.** The goal — being present where AI systems look — is legitimate; only the shortcut is not.

## 5. Cloaking — `policy-risk`, hard prohibition

**The risk.** Serving different content to crawlers than to users. Severe; manual-action territory.

**Threshold.** Any material difference in content based on user agent, including serving enriched content specifically to AI crawlers.

**This is a hard no.** It is also a live temptation in GEO specifically, because "give the AI bots a cleaner version" sounds reasonable and is exactly the violation.

**Compliant variant.** If content should be excluded from an engine, use the mechanisms designed for it — `robots.txt`, `noindex`, `nosnippet`, `data-nosnippet`, `isAccessibleForFree`. If you want machine-readable content, publish it at its own URL, available to everyone, linked from the site. Prerendering is acceptable **only** when the prerendered output is equivalent to what a user sees. Markdown `.md` variants are acceptable **only** when equivalent to the HTML and served to all agents equally.

## 6. Mass AI-generated content — `requires-compliant-variant`

**The risk.** Scaled content abuse. Google's position: AI-generated content is acceptable **if** it meets Search Essentials and the spam policies. Automation for ranking manipulation is not.

**Threshold.** Scale without editorial value or human accountability.

**Compliant variant.** AI-assisted, human-directed, subject-matter-reviewed, with a named accountable author. Every piece must clear the same bar as human-written content. Run `stop-slop` before publication.

## 7. Doorway pages — `policy-risk`

**Threshold.** Multiple similar pages targeting variations that all funnel to the same destination without independent value.

**Compliant variant.** One strong page per genuine user need. Location pages only where there is a real location with distinct information.

## 8. Misleading structured data — `policy-risk`

**The risk.** Structured data policy violations trigger manual actions against rich-result eligibility.

**Threshold.** Markup describing content not visible on the page; fabricated reviews or ratings; `Product` markup on non-product pages.

**Compliant variant.** Schema/visible-text parity, enforced (deliverable D4). Only mark up what is genuinely on the page. Never generate review markup for reviews that do not exist.

## 9. Aggressive citation-density on top-ranking pages — **efficacy risk, not policy risk**

Included so it is not confused with the entries above. Applying Cite Sources / Quotation Addition / Statistics Addition to a page that already ranks #1 measurably **reduced** its citation visibility by 20–30% in the KDD study. No policy exposure — just a bad idea. Mitigation: rank-stratified assignment (`content-citation-tactics.md`), or a controlled trial on a subset.

---

## Pre-flight gate

Before any engagement ships work, confirm in writing:

- [ ] No page exists primarily to capture a query variation
- [ ] Every programmatic page passed the unique-value gate, recorded
- [ ] No compensated link lacks `rel="sponsored"`
- [ ] No content differs by user agent — none, anywhere
- [ ] All structured data matches visible page content
- [ ] All quotes, statistics, and experts are real and verifiable
- [ ] Community and Wikipedia activity is disclosed and non-promotional
- [ ] AI-assisted content has a named accountable human reviewer
