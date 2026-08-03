---
name: seo-audit
description: Use for organic search work on Google and Bing with no AI-answer component — audits, diagnosis, and fixes. Trigger phrases: "SEO audit," "technical SEO," "why am I not ranking," "SEO issues," "on-page SEO," "meta tags review," "SEO health check," "my traffic dropped," "lost rankings," "not showing up in Google," "site isn't ranking," "Google update hit me," "core update," "manual action," "page speed," "core web vitals," "crawl errors," "indexing issues," "canonical," "hreflang," "sitemap," "redirects," "site migration," "we're replatforming," "faceted navigation," "JavaScript SEO," "featured snippet," "Google Discover." Use this even for a vague "my SEO is bad" or "help with SEO" — start with an audit. ROUTING — the moment the request touches AI search (AI Overviews, AI Mode, ChatGPT, Perplexity, Claude, Copilot, GEO, AEO, LLMO, "get cited by AI," llms.txt, "are AI bots blocked"), stop and use **geo** instead. geo is the umbrella skill; it already contains this entire technical and content SEO layer, so running both duplicates work and produces conflicting recommendations. Use seo-audit only when the engagement is purely Google/Bing organic. For building pages at scale, see programmatic-seo. For implementing structured data as its own task, see schema.
metadata:
  version: 3.0.0
  last-research: 2026-08-04
  corpus: 178-page Google Search Central + crawling-infrastructure harvest (research/raw/pages)
---

# SEO Audit

You are an expert in search engine optimization. Your goal is to identify SEO issues and provide actionable recommendations to improve organic search performance.

Every claim in this skill is traceable to Google's own documentation. Where a widespread industry
practice has no documented basis, it is labelled as a heuristic rather than presented as a rule.
Do not add unsourced numbers, thresholds, or "studies show" claims to client deliverables.

## Route the request before auditing

```
"My traffic dropped" / "did an update hit us" / "we got a manual action"
  └─> This is a DIAGNOSIS, not an audit. references/search-diagnostics.md.
      Running a health checklist at a traffic drop finds unrelated issues and
      misses the cause.

"We're migrating / replatforming / changing domain / moving to HTTPS"
  └─> references/site-moves.md. Pre-move, not post-mortem.

Ecommerce site, faceted navigation, large catalogue
  └─> references/ecommerce-seo.md.

Multiple languages or regions
  └─> International section below + references/international-seo.md.

Anything touching AI search, AI Overviews, ChatGPT, Perplexity, citations
  └─> STOP. Use the geo skill. It contains this whole layer. Do not run both.

Otherwise
  └─> The audit framework below.
```

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before auditing, understand:

1. **Site Context**
   - What type of site? (SaaS, e-commerce, blog, etc.)
   - What's the primary business goal for SEO?
   - What keywords/topics are priorities?

2. **Current State**
   - Any known issues or concerns?
   - Current organic traffic level?
   - Recent changes or migrations?

3. **Scope**
   - Full site audit or specific pages?
   - Technical + on-page, or one focus area?
   - Access to Search Console / analytics?

---

## Audit Framework

### Schema Markup Detection Limitation

**`web_fetch` and `curl` cannot reliably detect structured data / schema markup.**

Many CMS plugins (AIOSEO, Yoast, RankMath) inject JSON-LD via client-side JavaScript — it won't appear in static HTML or `web_fetch` output (which strips `<script>` tags during conversion).

**To accurately check for schema markup, use one of these methods:**
1. **Browser tool** — render the page and run: `document.querySelectorAll('script[type="application/ld+json"]')`
2. **Google Rich Results Test** — https://search.google.com/test/rich-results
3. **Screaming Frog export** — if the client provides one, use it (SF renders JavaScript)

Reporting "no schema found" based solely on `web_fetch` or `curl` leads to false audit findings — these tools can't see JS-injected schema.

### Priority Order
1. **Crawlability & Indexation** (can Google find and index it?)
2. **Technical Foundations** (is the site fast and functional?)
3. **On-Page Optimization** (is content optimized?)
4. **Content Quality** (does it deserve to rank?)
5. **Authority & Links** (does it have credibility?)

---

## Things Google says don't matter

Every item below is stated by Google in the corpus. Each one is also a finding that appears
routinely in commercial SEO audits. **Do not raise these as issues, and correct the client if
another agency has sold them as issues** — this is where our technical credibility is won.

Source unless noted: `/search/docs/fundamentals/seo-starter-guide`, "SEO myths" section.

| Common finding | What Google actually says |
|---|---|
| "Multiple H1s / skipped heading levels" | Semantic heading order "is fantastic for screen readers, but from Google Search perspective, it doesn't matter if you're using them out of order." Also: "there's no magical, ideal amount of headings" |
| "Content is too short / needs 1,500 words" | "The length of the content alone doesn't matter for ranking purposes (there's no magical word count target, minimum or maximum)" |
| "Improve your E-E-A-T score" | Under the heading *Thinking E-E-A-T is a ranking factor*: "No, it's not." It is a quality framing, not a signal you can tune |
| "Put the keyword in the domain or URL" | "the keywords in the name of the domain (or URL path) alone have hardly any effect beyond appearing in breadcrumbs" |
| "You need a .com" | TLD "only matters if you're targeting a specific country's users, and even then it's usually a low impact signal" |
| "Duplicate content penalty" | "it's fine; don't fret about it. It's inefficient, but it's not something that will cause a manual action." Copying *others'* content is a different matter |
| "Move to subdirectories / subdomains for SEO" | "do whatever makes sense for your business" |
| "Keywords meta tag" | Google doesn't use it |
| "Improve crawl rate to rank better" | "Crawling is a ranking factor" is false. Necessary for inclusion, not a ranking signal (`/crawling/docs/myths-about-crawling`) |
| "Update the date to signal freshness" | "content is rated by quality, regardless of age… there's no additional value in making pages artificially appear to be fresh by making trivial changes and updating the page date" (same source) |
| "Get important pages within 3 clicks" | Home-page proximity affects **crawl frequency**, not ranking: pages linked from the home page "may be seen as more important, and therefore crawled more often. However, this doesn't mean that these pages will be ranked more highly" (same source). Keep it as an architecture heuristic; do not sell it as a ranking fix |
| "Add `crawl-delay` to robots.txt" | "not processed by Google's crawlers" (same source) |
| "Add `rel=next`/`rel=prev` to paginated pages" | "Google no longer uses these tags" (`/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading`) |
| "Compress your sitemaps to save crawl budget" | "It won't. Zipped sitemaps still have to be fetched" (`/crawling/docs/myths-about-crawling`) |
| "There's a single page-experience ranking signal" | "There is no single signal." Core Web Vitals *are* used by ranking systems, but good CWV "doesn't guarantee that your pages will rank at the top" (`/search/docs/appearance/page-experience`) |

Full list, with the crawl-budget myths: `references/search-diagnostics.md`.

---

## Technical SEO Audit

### Crawlability

**Robots.txt**
- Check for unintentional blocks; verify important pages allowed
- Check sitemap reference
- **Present on every host**, including subdomains — crawl rules and crawl budget are per hostname
- Do not use it for canonicalisation or to suppress indexing (see the `noindex` trap below)
- `crawl-delay` is not processed by Google; its presence is not a control and its absence is not
  a finding

**Edge / origin access — run this every audit, not just once**

robots.txt is only one of three access layers. Run this from the repo root:

```bash
python .claude/skills/geo/scripts/crawler_access_check.py https://client.com --live --delay 9 --json access.json
```

This catches two failures robots.txt never shows and Search Console never reports:
1. An HTTP block (403/429) at the CDN, WAF, or origin server, keyed on user agent
2. A **bot-challenge interstitial returned with HTTP 200** — the status says success, the body is a JS challenge no crawler can execute. If this fires for Googlebot, Google can index the challenge page instead of the site.

**Regresses silently** whenever a host enables a default, a security plugin updates, or a WAF option is switched on. Diff `access.json` against the previous audit.

Before reporting a failure, follow the diagnostic protocol in `.claude/skills/geo/references/crawler-access.md` — rapid test requests trip volumetric rate limits that look exactly like a user-agent policy block.

**XML Sitemap**

Source: `/search/docs/crawling-indexing/sitemaps/overview` and `.../build-sitemap`.

- Exists, returns 200, submitted in Search Console **and** referenced from robots.txt
- Contains only **canonical, indexable, 200** URLs — a sitemap is a statement of which URLs you
  want in results, and sitemap inclusion is a (weak) canonicalisation signal
- **Hard limits: 50,000 URLs or 50MB uncompressed per file**, whichever comes first. A sitemap
  index file may itself list up to 50,000 `<loc>` entries
- **`<priority>` and `<changefreq>` are ignored by Google.** Their presence is not a finding and
  their absence is not either. Do not put "add priority values" in an action plan
- **`<lastmod>` is used only if it is "consistently and verifiably accurate."** A CMS that stamps
  today's date on every URL every night has made the field worthless. Check this before trusting it
- URL order does not matter

**Does the client even need one?** Google's threshold: you *might not* need a sitemap if the site
is **about 500 pages or fewer** (counting only pages you want in results), is comprehensively
internally linked, and has few video/image/news assets. Conversely a sitemap earns its keep for a
new site with few external links, or a site with substantial media. Judge before recommending.

**Site Architecture**
- Logical hierarchy; complete internal linking from navigation down to leaf pages
- No orphan pages
- Priority pages reachable in few clicks from the home page — a crawl-frequency and usability
  heuristic, **not** a ranking rule (see the myths table)

**Crawl Budget Issues** — only for sites in Google's stated scope

Google's guide is explicitly for: 1M+ pages changing weekly, 10K+ pages changing daily, or sites
with a large share of URLs in "Discovered – currently not indexed". Google calls these numbers
"a rough estimate… not exact thresholds". Below that: "you don't need to read this guide" —
keeping the sitemap current and reading the Page Indexing report is adequate. **Do not sell crawl
budget work to a 400-page site.**

Crawl budget is allocated **per hostname** — `www.example.com` and `shop.example.com` have
separate budgets.

Where it does apply: parameterised URLs controlled, faceted navigation contained
(`references/ecommerce-seo.md`), infinite scroll with a crawlable pagination fallback, no session
IDs in URLs, no spider traps from timestamps or infinite calendars, 5xx and 429 rates low
(they actively lower the crawl capacity limit).

### Indexation

**Index Status**
- site:domain.com check
- Search Console coverage report
- Compare indexed vs. expected

**Indexation Issues**
- `noindex` on important pages (meta robots **or** `X-Robots-Tag` header — check both)
- Canonicals pointing the wrong direction
- Redirect chains and loops
- Soft 404s
- Duplicate content without canonicals

**The robots.txt / `noindex` trap.** A page blocked in robots.txt can still appear in results,
because the crawler never fetches the page and therefore never sees the `noindex` rule. The two
controls are not interchangeable: robots.txt controls *crawling*, `noindex` controls *indexing*,
and `noindex` requires crawling to work. `noindex` in robots.txt is not supported by Google.
Source: `/search/docs/crawling-indexing/block-indexing`.

**Snippet directives — check these, most audits don't.**
Source: `/search/docs/crawling-indexing/robots-meta-tag`.

| Directive | Effect |
|---|---|
| `nosnippet` | No snippet at all. Also removes featured-snippet eligibility |
| `max-snippet:0` | Equivalent to `nosnippet` |
| `max-snippet:[n]` | Caps snippet length **and** caps how much content may be used as direct input for AI Overviews and AI Mode |
| `max-snippet:-1` | Google chooses. This is what you usually want |
| `data-nosnippet` | Element-level exclusion. Use to exclude one block (a price, a disclaimer) without disabling snippets for the page |
| `max-image-preview:large` | Required for large image previews; **a precondition for Google Discover** |
| `noimageindex`, `notranslate`, `unavailable_after`, `indexifembedded` | Situational; `indexifembedded` only has effect alongside `noindex` |

`nosnippet` beats `data-nosnippet` when both are present. A page carrying `nosnippet` or
`max-snippet:0` is fully indexed and **silently ineligible for featured snippets, AI Overviews and
AI Mode** — a standard indexability check passes it. Flag it explicitly.

**Canonicalization**

Source: `/search/docs/crawling-indexing/canonicalization` and `.../consolidate-duplicate-urls`.

**A canonical is a hint, not a rule.** Google clusters pages it judges duplicate and picks the
version it considers "most complete and useful". It may pick a different one than you declared.
When it does, the fix is a content difference, not a stronger tag.

Signal strength, strongest first:
1. **Redirects** — "a strong signal that the target of the redirect should become canonical"
2. **`rel="canonical"`** in HTML `<head>`, or as an HTTP `Link` header for non-HTML files
3. **Sitemap inclusion** — "a weak signal"

Check for:
- Self-referencing canonicals on unique pages, including on the canonical page itself
- HTTP → HTTPS, www vs non-www, trailing-slash consistency
- **No contradictory declarations across methods** — a sitemap saying one URL and `rel="canonical"`
  saying another is a documented error
- No URL **fragment** declared as canonical (never valid)
- No `robots.txt` used for canonicalisation ("Google may still index URLs" it cannot crawl)
- No URL-removal tool used for canonicalisation (it hides from Search, it does not consolidate)
- `noindex` not used to suppress a duplicate — Google explicitly does not recommend it;
  `rel="canonical"` is preferred
- Canonical set only in HTML, or if set by JavaScript, set to the **same value** already present
  in the original HTML

When Google picks a different canonical (`/search/docs/crawling-indexing/canonicalization-troubleshooting`),
the documented causes are: same content across locales without hreflang annotations; a CMS or
plugin emitting an incorrect canonical; server misconfiguration serving one domain's content on
another; hacked code injecting a cross-domain canonical; syndicated content (the canonical link
element is **not** the recommended fix for syndication); and a copycat site. Re-evaluation takes
time, and pages "split out faster if the content difference is larger" — request indexing via URL
Inspection after fixing content, not before.

### Site Speed & Core Web Vitals

**Core Web Vitals** — thresholds per `/search/docs/appearance/core-web-vitals`
- LCP (Largest Contentful Paint): most loads within **2.5 seconds**
- INP (Interaction to Next Paint): **under 200 milliseconds** (replaced FID in March 2024)
- CLS (Cumulative Layout Shift): **under 0.1**

**How to talk about this without overclaiming.** Google: "Core Web Vitals are used by our ranking
systems." Also Google: "there is no single page experience signal", and good CWV scores don't
"guarantee that your pages will rank at the top of Google Search results; there's more to great
page experience than Core Web Vitals scores alone." So: real, worth fixing, not a ranking lever
you can pull in isolation. Frame speed work as user experience with a ranking component, not as a
ranking fix with a UX side effect.

**The rest of page experience** (`/search/docs/appearance/page-experience`) — Google's own
self-assessment questions, all of which belong in an audit: good Core Web Vitals; served securely;
displays well on mobile; not an excessive amount of ads distracting from or interfering with the
main content; **no intrusive interstitials**; main content easily distinguishable from the rest of
the page.

**Speed Factors**
- Server response time (TTFB)
- Image optimization
- JavaScript execution
- CSS delivery
- Caching headers
- CDN usage
- Font loading

**Tools**
- PageSpeed Insights
- WebPageTest
- Chrome DevTools
- Search Console Core Web Vitals report

### Mobile-Friendliness

- Responsive design (not separate m. site)
- Tap target sizes
- Viewport configured
- No horizontal scroll
- Same content as desktop
- Mobile-first indexing readiness

### Security & HTTPS

- HTTPS across entire site
- Valid SSL certificate
- No mixed content
- HTTP → HTTPS redirects
- HSTS header (bonus)

### URL Structure

- Readable, descriptive URLs — descriptive words help Google understand the page, but see the
  myths table: keywords in the URL "alone have hardly any effect beyond appearing in breadcrumbs".
  Write URLs for humans and stop there
- Consistent structure; lowercase and hyphen-separated
- No unnecessary or temporary parameters (session IDs, tracking codes, timestamps)
- Never use fragments (`#`) to vary page content — Google does not use fragments in indexing, so
  `/shirt#black` and `/shirt#white` are one page

Detail and the parameter rules: `references/ecommerce-seo.md`.

### JavaScript SEO

Source: `/search/docs/crawling-indexing/javascript/javascript-seo-basics`.

**How Google actually processes a JS site — three phases: crawl, render, index.** Googlebot
fetches the HTML, parses `href` links into the crawl queue, then queues **every 200-response page**
for rendering by a headless evergreen Chromium. It "may stay on this queue for a few seconds, but
it can take longer." Rendered HTML is then re-parsed for links and used for indexing.

Two consequences that decide most JS audits:
- **Non-200 pages may skip rendering entirely.** A JS app that 200s an error page and then renders
  "not found" gets indexed as a soft 404.
- **Blocked resources are never rendered.** "Google Search won't render JavaScript from blocked
  files or on blocked pages." JS and CSS must not be disallowed in robots.txt.

**Check for:**
- Main content present in server-rendered HTML. Google still recommends SSR or pre-rendering:
  it is faster for users and crawlers, "and not all bots can run JavaScript"
- Links are real `<a href>` elements. "Google can only discover your links if they are `<a>` HTML
  elements with an `href` attribute." JS click handlers on divs and buttons are invisible
- **SPA routing uses the History API, not fragments.** `href="#/products"` cannot be resolved
- Soft 404s in SPAs handled by one of Google's two documented patterns: JS-redirect to a URL the
  server 404s, or inject `<meta name="robots" content="noindex">` on the error state
- Meaningful HTTP status codes throughout — 404 for missing, 401 behind login
- Canonical set in HTML. If JS must set it, it must set the **same value** already in the HTML
- Lazy loading does not hide primary content

**Dynamic rendering is not a solution.** Google's current wording: "Dynamic rendering was a
workaround and not a long-term solution… it creates additional complexities and resource
requirements." If a client is running it, the recommendation is to migrate to SSR or hydration,
not to fix the prerenderer.

---

## International SEO & Localization

Check when the site serves multiple languages or regions. Misconfigurations can suppress indexing
of entire locale variants, or drag down site-wide quality signals via the helpful-content system.

**Full detail, evidence and source URLs: [references/international-seo.md](references/international-seo.md).**
That reference is the authority; this is the checklist.

**Hreflang** — three equivalent placements (HTML `<link>`, HTTP `Link` header, sitemap
`<xhtml:link>`); if you use more than one they must agree, or Google drops the conflicting pair.
Prefer sitemap-based past ~10 locales.
- Self-referencing entry on every page — missing it invalidates the whole set
- Reciprocal: if A points to B, B must point back, or both are ignored
- Valid codes: ISO 639-1 language + optional ISO 3166-1 Alpha 2 region. `en-GB`, never `en-UK`
- `x-default` present, pointing at the fallback
- Every target returns 200, is indexable, and equals its own canonical
- No duplicate language-region code pointing to two URLs
- Not required on every page — focus it where wrong-language traffic is landing
- Bing treats hreflang as a weak signal: also set `<html lang>` and `content-language`

**Canonical + hreflang** — the interaction that breaks most implementations:
- Every locale page self-canonicals. **Never cross-locale canonical** — it suppresses that locale
- The canonical URL must appear in its own hreflang set, or all hreflang is ignored
- Canonical overrides hreflang on conflict
- Protocol and domain variant consistent across canonical, hreflang and sitemap
- Paginated locale pages: self-referencing canonical per page, never page 2+ → page 1

**International sitemaps** — `xmlns:xhtml` namespace on `<urlset>`; each `<url>` lists every
locale including itself; `x-default` included; absolute URLs; split by content type, not by locale.
*Next.js caveat:* `alternates.languages` does not auto-include the self-referencing entry.

**Locale URL structure** — subdirectories recommended, subdomains and ccTLDs acceptable, URL
parameters (`?lang=en`) not recommended. All locales prefixed (hiding the locale from URLs stops
Google distinguishing versions). Root handled as `x-default`. **No IP or `Accept-Language`
content negotiation** — Googlebot crawls from US IPs and sends no `Accept-Language` header.
Trailing-slash and case consistency across paths, canonicals, hreflang and sitemaps. The Search
Console International Targeting report is deprecated.

**Content quality across locales**
- Translate **all** main content, not just navigation chrome. Google determines page language
  from visible content; boilerplate-only translation produces duplicates
- AI translation is not inherently spam, but scaled low-value translation can trigger the scaled
  content abuse policy
- Thin locale pages are a **site-wide** risk — the helpful content system is site-level, so weak
  locales can suppress strong pages. Don't `noindex` them (wastes crawl budget) and don't
  cross-locale canonical them (conflicts with hreflang). Don't create them
- Broken hreflang targets waste crawl budget **and** invalidate the cluster
- Localise currency, phone format and addresses where they apply

---

## On-Page SEO Audit

### Title Tags

Source: `/search/docs/appearance/title-link`.

**Google's actual position on length:** "there's no limit on how long a `<title>` element can be,
the title link is truncated in Google Search results as needed, typically to fit the device
width." There is no character limit to comply with. The familiar **50–60 character** figure is an
industry heuristic for staying inside typical desktop truncation — useful for writing, but do not
report "title is 68 characters" as a defect on its own. Report it when truncation loses meaning.

**Check for:**
- Unique, descriptive title per page
- Primary term early — for users scanning a result, not for an algorithm
- Not "unnecessarily long or verbose"
- **Not boilerplate.** Google's named failure: titles that vary "by only a single piece of
  information" make it "impossible for users to distinguish between two pages"
- Brand name placement (end, usually)
- Latin-script sites: title in the page's language. Google may rewrite the title link if it
  detects a script mismatch between the title and the page

**Common issues:** duplicate titles · boilerplate titles · keyword stuffing · missing entirely ·
truncation that cuts the meaningful part.

Note: Google generates the title link and may not use your `<title>`. That is normal, not a bug.

### Meta Descriptions

Source: `/search/docs/appearance/snippet`.

**Google's actual position on length:** "there's no limit on how long a meta description can be,
but the snippet is truncated in Google Search results as needed." The **150–160 character** figure
is again an industry heuristic, not a Google rule.

**Check for:**
- Unique description per page, programmatically generated from on-page content where the page
  count makes hand-writing impractical — Google explicitly endorses this
- Actually descriptive, not a keyword string. "Meta descriptions comprised of long strings of
  keywords don't give users a clear idea of the page's content"
- Clear value proposition

**Underused, and worth recommending:** a meta description does not have to be prose. Google's own
example uses structured facts — `Author: …, Price: $17.99, Length: 784 pages`. On product,
listing and reference pages this outperforms a sentence.

**Common issues:** duplicate descriptions · keyword strings · no reason to click · missing on
pages where Google's generated snippet is worse than a written one would be.

Google uses the meta description "when it describes the page better than" the on-page text it
would otherwise extract. It is an input, not a directive.

### Heading Structure

**Check for:**
- Headings that describe the content beneath them
- Headings phrased the way people actually ask the question
- Content broken into paragraphs and sections so users can navigate it

**Do not report as issues:** multiple H1s, skipped levels (H1 → H3), or heading count. Google:
semantic heading order "doesn't matter" from a Search perspective, and "there's no magical, ideal
amount of headings a given page should have." Semantic order is still correct practice for screen
readers — recommend it as accessibility, not SEO, and price it accordingly.

**A missing or non-descriptive H1 is still worth flagging** — not because of a heading rule, but
because Google uses heading text as a candidate for the generated title link.

### Content Optimization

**Primary Page Content**
- Answers the search intent
- Related terms used naturally — "if you are varying the words (writing naturally to not be
  repetitive), you have more chances to show up in Search simply because you are using more
  keywords"
- Better than what currently ranks
- **Length is not a target.** "The length of the content alone doesn't matter for ranking
  purposes." Never put a word count in a content brief as an SEO requirement
- Keyword stuffing — "excessively repeating the same words over and over (even in variations)" —
  is a spam-policy violation, not merely bad style

**Thin Content Issues**
- Pages with little unique content
- Tag/category pages with no value
- Doorway pages
- Duplicate or near-duplicate content

### Image Optimization

**Check for:**
- Descriptive file names
- Alt text on all images
- Alt text describes image
- Compressed file sizes
- Modern formats (WebP)
- Lazy loading implemented
- Responsive images

### Internal Linking

**Check for:**
- Important pages well-linked
- Descriptive anchor text
- Logical link relationships
- No broken internal links
- Reasonable link count per page

**Common issues:**
- Orphan pages (no internal links)
- Over-optimized anchor text
- Important pages buried
- Excessive footer/sidebar links

### Keyword Targeting

**Per Page**
- Clear primary keyword target
- Title, H1, URL aligned
- Content satisfies search intent
- Not competing with other pages (cannibalization)

**Site-Wide**
- Keyword mapping document
- No major gaps in coverage
- No keyword cannibalization
- Logical topical clusters

---

## Content Quality Assessment

### E-E-A-T

**E-E-A-T is not a ranking factor.** Google states this flatly in the starter guide's myths
section. It is a framing that describes what Google's systems try to reward, and it is the
vocabulary of the Quality Rater Guidelines — not a score, not a signal, and not something to
"improve" as a line item.

Use it as a self-assessment lens, which is what Google's own content guidance
(`/search/docs/fundamentals/creating-helpful-content`) does. Never quote an "E-E-A-T score" or
promise to raise one.

**Experience**
- First-hand experience demonstrated
- Original insights/data
- Real examples and case studies

**Expertise**
- Author credentials visible
- Accurate, detailed information
- Properly sourced claims

**Authoritativeness**
- Recognized in the space
- Cited by others
- Industry credentials

**Trustworthiness**
- Accurate information
- Transparent about business
- Contact information available
- Privacy policy, terms
- Secure site (HTTPS)

### Content Depth

- Comprehensive coverage of topic
- Answers follow-up questions
- Better than top-ranking competitors
- Updated and current

### User Engagement Signals

Time on page, bounce rate in context, pages per session, return visits.

**These are business diagnostics, not documented ranking signals.** Nothing in the corpus states
that Google uses analytics engagement metrics for ranking. Use them to judge whether a page is
doing its job; do not present them as SEO levers.

---

## Structured Data — what Google currently supports

Do not recommend a rich result type without checking it is still live. Google retires features,
and audit templates lag by years. Full list: `/search/docs/appearance/structured-data/search-gallery`.

**Supported as of the 2026-06-15 gallery:** Article · Breadcrumb · Carousel · Course list ·
Dataset · Discussion forum · Education Q&A · Employer aggregate rating · Event · Image metadata ·
Job posting · Local business · Math solver · Movie · Organization · Product · Profile page ·
Q&A · Recipe · Review snippet · Software app · Speakable · Subscription and paywalled content ·
Vacation rental · Video. Plus the merchant extensions: product snippet, merchant listing, product
variants, shipping policy, return policy, loyalty program.

**Retired — do not recommend, and remove from client roadmaps:**

| Feature | Status |
|---|---|
| **FAQ** (`FAQPage` rich result) | **Dead.** Deprecation notice added May 2026; feature stopped appearing **7 May 2026**; documentation removed June 2026. Markup is harmless but produces nothing |
| **How-to** (`HowTo` rich result) | **Dead.** Documentation removed; "no longer shown in search results, on both desktop and mobile" |

If a client asks for FAQ or How-to schema, say so plainly and redirect the effort. The `schema`
skill's examples still contain both — treat this table as authoritative over it.

**Rules that change how you report structured data findings**
(`/search/docs/appearance/structured-data/sd-policies`):

- **A structured-data manual action costs rich-result eligibility only.** It "doesn't affect how
  the page ranks in Google web search." Do not escalate it as a ranking emergency
- Valid markup **does not guarantee** a rich result. "Using structured data enables a feature to
  be present, it does not guarantee that it will be present"
- **Markup must match visible content.** Marking up content not visible to readers is a violation
  — this is the most common real defect, and it is invisible to validators
- Missing a **required** property means no eligibility at all. More recommended properties raises
  result quality, and "rich result ranking takes extra information into consideration"
- Structured data pages must not be blocked by robots.txt or `noindex`
- **Put the same structured data on duplicate pages, not only the canonical** — Google's explicit
  recommendation
- All image URLs in structured data must be crawlable and indexable
- JSON-LD recommended; Microdata and RDFa also supported

Implementation belongs to the `schema` skill. Detection caveats: see the limitation section above.

---

## Search Appearance Features

### Featured snippets

Source: `/search/docs/appearance/featured-snippets`.

- **You cannot mark a page as a featured snippet.** "You can't. Google systems determine whether
  a page would make a good featured snippet." Any deliverable promising featured-snippet placement
  is unsellable. Optimise the passage; do not promise the box
- Also appear inside People Also Ask groups
- A click takes the user **directly to the passage** that appeared, auto-scrolled, with no
  annotation needed from the site
- **Opting out:** `nosnippet` blocks all snippets (regular and featured). To block featured only,
  lower `max-snippet` progressively — but this is not guaranteed, and Google does not publish the
  minimum length, because it varies by information, language and platform. `nosnippet` is the only
  guaranteed method
- `data-nosnippet` text is excluded from featured and regular snippets alike

### Google Discover

Source: `/search/docs/appearance/google-discover`.

- **Eligibility is automatic** for indexed content meeting Discover's content policies. "No
  special tags or structured data are required." Older content can surface if it matches interests
- **Image requirements are the one concrete lever** — and the one most often missed:
  - at least **1200 px wide**
  - more than **300,000 total pixels**
  - **16:9** aspect ratio, cropped for landscape (do not blindly force a vertical image into 16:9)
  - **enabled by `max-image-preview:large`** (or AMP) — without this directive the large image
    never shows, and large images are "more likely to generate visits from Discover"
  - specify it via schema.org markup or `og:image`; avoid generic images such as the site logo,
    and avoid text-heavy images
- Avoid clickbait, exaggerated or withheld preview detail, and sensationalism catering to "morbid
  curiosity, titillation, or outrage" — these are policy grounds, and Discover has its own manual
  actions under Security and Manual Actions in Search Console
- **Set the expectation before the client sees the graph:** "traffic from Discover is less
  predictable or dependable when compared to keyword-driven search visits… consider traffic from
  Discover as supplemental." Discover volatility is normal and frequently unrelated to content
  quality or publishing frequency
- Discover is part of Search and uses the same helpful-content signals, so core updates move it

---

## Common Issues by Site Type

### SaaS/Product Sites
- Product pages lack content depth
- Blog not integrated with product pages
- Missing comparison/alternative pages
- Feature pages thin on content
- No glossary/educational content

### E-commerce
Full playbook: **`references/ecommerce-seo.md`** — faceted navigation, pagination and infinite
scroll, URL and parameter design, Merchant Center, and the ranked failure list. Headlines:
- Faceted navigation crawled without limit (the usual root cause)
- Products not linked from any category page — Googlebot does not use site search
- Infinite scroll or load-more with no crawlable pagination beneath it
- Page 2+ canonicalised to page 1
- Thin category pages; duplicate manufacturer product descriptions
- Missing or contradictory product structured data
- Out-of-stock pages mishandled

### Content/Blog Sites
- Outdated content not refreshed
- Keyword cannibalization
- No topical clustering
- Poor internal linking
- Missing author pages

### Multilingual / Multi-Regional Sites
See the International section above. The four that account for most damage: cross-locale
canonicals suppressing a locale, missing self-referencing hreflang invalidating the whole set,
boilerplate-only translation producing duplicates, and IP-based redirects hiding content from
Googlebot's US-based crawl.

### Local Business
- Inconsistent NAP
- Missing `LocalBusiness` schema (still a fully supported feature — see the structured data
  section) and no Google Business Profile optimisation
- Missing location pages, or location pages that are the same page with the city swapped —
  that is doorway abuse under the spam policies, not a programmatic SEO win
- No genuinely local content

---

## Output Format

### Audit Report Structure

**Executive Summary**
- Overall health assessment
- Top 3-5 priority issues
- Quick wins identified

**Technical SEO Findings**
For each issue:
- **Issue**: What's wrong
- **Impact**: SEO impact (High/Medium/Low)
- **Evidence**: How you found it
- **Fix**: Specific recommendation
- **Priority**: 1-5 or High/Medium/Low

**On-Page SEO Findings**
Same format as above

**Content Findings**
Same format as above

**Prioritized Action Plan**
1. Critical fixes (blocking indexation/ranking)
2. High-impact improvements
3. Quick wins (easy, immediate benefit)
4. Long-term recommendations

### Reporting discipline

- **Every finding carries its evidence.** "How you found it" is not optional — it is what
  separates this from a template. If the evidence is a script output, name the script and quote
  the line.
- **Cite Google when correcting a belief.** When you tell a client their previous agency's finding
  is wrong, give the documentation path. See the "Things Google says don't matter" table.
- **Never promise placement.** Featured snippets cannot be marked up for. Rich results are enabled,
  not guaranteed. Ranking changes are not guaranteed by any change — Google says so explicitly.
- **Never assert that one change caused one metric move.** State scope performed and metrics
  moved, in that order, and let the reader connect them.
- **No unsourced numbers.** If you cannot trace a threshold or statistic to Google's docs or to the
  client's own data, it does not go in the deliverable.

---

## References

**This skill's own:**
- [Search Diagnostics](references/search-diagnostics.md) — traffic-drop method, core updates,
  spam policies and manual actions, crawl-budget myths. **Start here for "my traffic dropped."**
- [Site Moves](references/site-moves.md) — migration playbook, redirect rules, Change of Address,
  and the non-recovering-migration checklist
- [Ecommerce SEO](references/ecommerce-seo.md) — faceted navigation, pagination, URL and parameter
  design, Merchant Center
- [International SEO](references/international-seo.md) — hreflang, canonical + i18n, international
  sitemaps, locale URL structure, content quality across locales
- [AI Writing Detection](references/ai-writing-detection.md) — AI writing patterns to avoid in
  content deliverables

**Shared with the geo skill — read these, do not duplicate them here:**
- `.claude/skills/geo/references/technical-checklist.md` — the condensed pass/fail technical checklist. Use it
  as the audit worksheet; this SKILL.md is the reasoning behind it
- `.claude/skills/geo/references/crawler-access.md` — every crawler user agent, per-engine controls, WAF/CDN
  behaviour, IP verification, and the diagnostic protocol for a suspected block
- `.claude/skills/geo/references/risk-register.md` — spam-policy risk and compliant variants. **Read before
  recommending anything at scale**
- `.claude/skills/geo/references/evidence-ledger.md` — internal confidence tiers. Never quoted to a client

**Scripts — reuse, do not reimplement.** All live in `.claude/skills/geo/scripts/` and are tested
against live sites. Run them from the repo root:

| Script | Use in an SEO audit |
|---|---|
| `crawler_access_check.py <url> --live --delay 9 --json access.json` | Crawlability. Catches edge/WAF blocks and HTTP-200 bot-challenge interstitials |
| `indexability_check.py --urls priority.txt --json index.json` | Indexation. Status, redirects, canonical, robots directives, snippet eligibility, render volume |
| `schema_extract.py --urls priority.txt --json schema.json` | Structured data. JSON-LD extraction with `@graph` flattening, required-property gaps, and **retired-feature flagging** (FAQPage, HowTo) |

Build `priority.txt` from the client's sitemap:

```bash
curl -s -A "Mozilla/5.0" https://client.com/page-sitemap.xml \
  | grep -o '<loc>[^<]*</loc>' | sed 's|</\?loc>||g' > priority.txt
```

For AI search work (AEO, GEO, LLMO, AI Overviews, AI Mode citations) use the **geo** skill. It is
the umbrella skill and embeds this entire technical layer — do not run both.

---

## Tools Referenced

**Free Tools**
- **Google Search Console** — essential. The reports this skill depends on: Performance,
  Page indexing, Crawl stats, Security Issues, Manual Actions, Core Web Vitals, Sitemaps,
  URL Inspection, Data Anomalies, and the Search Status Dashboard for update timing
- Google PageSpeed Insights · Chrome Lighthouse · WebPageTest
- Bing Webmaster Tools
- Rich Results Test (**use this for schema validation — it renders JavaScript**)
- Schema.org Validator
- Google Trends — required to separate a site-specific drop from a market-wide one

**Retired — do not reference in a deliverable:** the Mobile-Friendly Test and the Search Console
Mobile Usability report were removed from Google's documentation (December 2023). Assess mobile
via Lighthouse and URL Inspection's rendered output instead.

> **Note on schema detection:** `web_fetch` strips `<script>` tags (including JSON-LD) and cannot detect JS-injected schema. Use the browser tool, Rich Results Test, or Screaming Frog instead — they render JavaScript and capture dynamically-injected markup. See the Schema Markup Detection Limitation section above.

**Paid Tools** (if available)
- Screaming Frog
- Ahrefs / Semrush
- Sitebulb
- ContentKing

---

## Task-Specific Questions

1. What pages/keywords matter most?
2. Do you have Search Console access? (Without it, most of the diagnostic method above is
   unavailable — say so rather than substituting third-party estimates for it.)
3. Any recent changes or migrations? Any planned?
4. Who are your top organic competitors?
5. What's your current organic traffic baseline?
6. Has another agency given you an SEO report? (Worth reading against the myths table before
   you produce a second one that contradicts it without explanation.)

---

## Related Skills

- **geo**: The umbrella skill for AI search (AEO, GEO, LLMO, AI Overviews, AI Mode, ChatGPT,
  Perplexity, Claude, Copilot). It contains this whole SEO layer — route there and do not run
  both. (`ai-seo` is a deprecated alias that now forwards to `geo`.)
- **programmatic-seo**: For building SEO pages at scale — gated by
  `.claude/skills/geo/references/risk-register.md`, because per-query-variation page generation is named
  scaled content abuse
- **site-architecture**: For page hierarchy, navigation design, and URL structure
- **schema**: For implementing structured data
- **cro**: For optimizing pages for conversion (not just ranking)
- **analytics**: For measuring SEO performance
