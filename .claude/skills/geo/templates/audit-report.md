# [Client] — AI Search Visibility Audit
**Prepared:** [date] · **Domain:** [domain] · **Scope:** [tier]

> **Template rules — delete before sending.** No confidence-tier language. State findings and fixes. Write in the client's language per `product-marketing.md`.

---

## 1. Executive summary

[Three to five sentences. What is blocking AI visibility today, what the biggest opportunity is, and what we recommend doing first.]

**Top priorities**

| # | Finding | Impact | Effort |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## 2. Current AI visibility

Prompt set of [N] real customer questions, run [date] across [engines].

| Engine | Cited | Rate |
|---|---|---|
| Google AI Mode / AI Overviews | /[N] | |
| ChatGPT | /[N] | |
| Perplexity | /[N] | |
| Claude | /[N] | |
| Copilot | /[N] | |

**Competitors cited where [Client] was not:** [list, with what they had that we did not]

*Sampled observation of non-deterministic systems; fixed prompt set and cadence make the trend comparable.*

---

## 3. Crawler access and eligibility

The first question in any AI visibility audit: can each engine actually fetch the site? Two independent layers — robots.txt, and the CDN or firewall. The second fails silently and does not appear in Search Console.

| Engine | Crawler | robots.txt | Live request | Status |
|---|---|---|---|---|
| Google | Googlebot | | | |
| ChatGPT | OAI-SearchBot | | | |
| Claude | Claude-SearchBot | | | |
| Perplexity | PerplexityBot | | | |
| Copilot | bingbot | | | |
| Apple | Applebot | | | |
| Amazon | Amzn-SearchBot | | | |

**Model training stance:** [what is currently allowed/blocked, and whether it matches the client's intent. Note that on most engines training and citation are separate controls — declining training does not cost citations.]

**Search Console generative AI features inclusion:** [status]

---

## 4. Index and snippet eligibility

| Check | Result |
|---|---|
| Priority pages indexed | |
| Priority pages snippet-eligible | |
| Canonical configuration | |
| Content server-rendered | |
| Sitemap valid | |

[Note any `nosnippet` or `max-snippet:0` findings prominently — these leave a page fully indexed and entirely ineligible for AI Overviews and AI Mode.]

---

## 5. Content and citation-worthiness

| Page | Current position | Sourced statistics | External citations | Expert attribution | Assigned tactic tier |
|---|---|---|---|---|---|
| | | | | | |

[Tactic assignment is by current search position — the approaches that give the largest gains to pages outside the top results behave differently on pages that already lead.]

---

## 6. Structured data

| Template | Types present | Valid | Gaps |
|---|---|---|---|
| | | | |

---

## 7. Entity presence

| Signal | Status |
|---|---|
| Organization schema with `sameAs` | |
| Google Business Profile | |
| Wikipedia / Wikidata | |
| Review platforms | |
| NAP consistency | |

---

## 8. Recommended roadmap

### Phase 1 — Access and eligibility [timeframe]
| # | Action | Owner |
|---|---|---|

### Phase 2 — Structure and structured data [timeframe]
| # | Action | Owner |
|---|---|---|

### Phase 3 — Content and entity [timeframe]
| # | Action | Owner |
|---|---|---|

---

## 9. Measurement setup

[What we will baseline and track, and the reporting cadence. Include the standing note: AI impressions are a subset of Search impressions, and AI-specific click-through rate is not available from Search Console.]
