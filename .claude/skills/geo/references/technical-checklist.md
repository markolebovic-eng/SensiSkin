# Technical Checklist — The Embedded SEO Layer

The SEO foundation inside every GEO engagement. Written once here; `seo-audit` covers the same ground for pure-SEO engagements. Sourced from the 178-page Google Search Central + crawling-infrastructure harvest.

## Crawl

- [ ] robots.txt returns 200; no unintended `Disallow` on priority paths
- [ ] Sitemap referenced from robots.txt
- [ ] **Edge/CDN/WAF permits all citation-critical bots** (`crawler_access_check.py --live`) — the failure Search Console never shows
- [ ] No 5xx on priority URLs; no DNS or network errors
- [ ] Redirect chains no more than one hop
- [ ] Crawl budget: parameters controlled, faceted navigation contained, no spider traps, no session IDs in URLs
- [ ] Server response time sane under crawl load
- [ ] robots.txt present on **every host**, including subdomains

## Index

- [ ] Priority URLs return 200 and are indexable
- [ ] Self-referencing canonicals on unique pages; no cross-locale or homepage canonicals
- [ ] No unintended `noindex` (meta or `X-Robots-Tag`)
- [ ] **Snippet eligibility intact** — no `nosnippet`, no `max-snippet:0` on priority pages. These leave a page indexed but ineligible for AI Overviews and AI Mode
- [ ] `data-nosnippet` used deliberately only
- [ ] Sitemap contains only canonical, indexable, 200 URLs; under 50k URLs / 50MB per file
- [ ] www/non-www, http/https, trailing-slash consistency
- [ ] No soft 404s
- [ ] Duplicate content consolidated

## Render

- [ ] Main content present in server-rendered HTML (`indexability_check.py` flags thin raw HTML)
- [ ] JS and CSS not blocked in robots.txt
- [ ] Links are real `<a href>` elements, not JS click handlers
- [ ] Lazy loading does not hide primary content
- [ ] Raw-vs-rendered diff shows no missing content or links
- [ ] Agents see the same content as users — they read the DOM and the accessibility tree

## Structure

- [ ] Priority pages within 3 clicks of the homepage
- [ ] No orphan pages
- [ ] Descriptive internal anchor text
- [ ] Logical topic clusters with hub pages
- [ ] Breadcrumbs, marked up with `BreadcrumbList`
- [ ] Readable, stable, lowercase, hyphenated URLs

## On-page

- [ ] Unique title per page, primary term early, roughly 50–60 characters
- [ ] Unique meta description, roughly 150–160 characters
- [ ] One `<h1>`; logical heading hierarchy with no skipped levels
- [ ] Headings phrased the way people ask the question
- [ ] Descriptive `alt` text on meaningful images; empty `alt` on decorative ones
- [ ] Visible author, `datePublished`, `dateModified`
- [ ] No keyword cannibalisation

## Page experience

- [ ] LCP under 2.5s, INP under 200ms, CLS under 0.1
- [ ] HTTPS throughout, no mixed content
- [ ] Mobile-responsive; same content as desktop (mobile-first indexing)
- [ ] No intrusive interstitials

## International (if applicable)

- [ ] Self-referencing and reciprocal hreflang; valid codes (`en-GB`, never `en-UK`)
- [ ] `x-default` present
- [ ] Canonical URL appears in its own hreflang set
- [ ] No cross-locale canonicals
- [ ] All main content translated, not just navigation chrome
- [ ] No IP or `Accept-Language` redirects — Googlebot crawls from US IPs with no `Accept-Language` header

Detail: `seo-audit/references/international-seo.md`.

## Where the depth lives

This checklist is the pass/fail worksheet. When an item fails, the diagnostic method is in
`seo-audit`, not here — do not restate it:

- Traffic dropped, core update, manual action → `seo-audit/references/search-diagnostics.md`
- Migration or replatform → `seo-audit/references/site-moves.md`
- Faceted navigation, pagination, catalogue → `seo-audit/references/ecommerce-seo.md`
- Sitemaps, canonicalisation, JavaScript rendering, snippet directives, structured-data feature
  status, featured snippets, Discover → `seo-audit/SKILL.md`
- The list of things Google says don't matter → `seo-audit/SKILL.md`, "Things Google says don't
  matter". Worth reading before any audit; it prevents a whole class of false findings.

## Content quality

- [ ] Helpful, reliable, people-first; passes the "would a visitor be satisfied?" test
- [ ] **Non-commodity** — original perspective, not a restatement of the existing web. Google's stated highest-leverage factor
- [ ] E-E-A-T: named authors, real credentials, transparent sourcing, contact details
- [ ] AI-assisted content meets Search Essentials with a named human reviewer
- [ ] No thin, doorway, or scaled pages (see `risk-register.md`)
- [ ] Reviews are genuine first-hand assessments where the reviews system applies

## Monitoring

- [ ] Search Console verified; sitemap submitted
- [ ] Bing Webmaster Tools verified
- [ ] Analytics with an AI-referral channel group
- [ ] Server log access for crawler hit-rate
- [ ] Core Web Vitals and coverage reports reviewed monthly
