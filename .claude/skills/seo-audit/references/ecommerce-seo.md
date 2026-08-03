# Ecommerce SEO

Google's ecommerce guidance, condensed. Sources are the nine pages under
`/search/docs/specialty/ecommerce/` plus `/crawling/docs/faceted-navigation`.

Most of this applies equally to sites that only *list* products sold in physical stores.

**If the client is on a mainstream platform (Shopify, WooCommerce, Magento, BigCommerce), skip
the URL-design section.** Google's own note: "If you're using an ecommerce platform, you can
most likely skip this section, as the platform has most likely already considered these issues
for you." Auditing URL design on a platform you cannot change wastes the engagement's budget.

---

## Site structure — the thing Google actually reads

**Google infers page importance from internal linkage, not from URL depth.** Two documented
mechanisms: the number of links it must follow to reach a page, and the number of links
pointing at it. Explicitly: "Google generally doesn't look at the structure of URLs to work out
the structure of a site. Instead, it analyzes the linkages between pages."

Consequence for the audit:
- The navigation chain must be complete: menu → category → sub-category → **every product page**.
- **If category pages don't link to every product in the category, Googlebot may never find
  those products.** Products reachable only through the site's own search box are effectively
  invisible — "Googlebot generally doesn't try to submit searches into a search box."
- Where linking to every product is impossible, a sitemap or a **Google Merchant Center feed**
  is the documented substitute. Both can surface URLs a crawler would not otherwise find.
- Links must be `<a href>`. JavaScript event handlers on other DOM elements are not links.
- To promote a hero product, link it from the home page and from content — "the more links a
  page has to it within a site, the higher the relative importance of the page."

---

## Faceted navigation

The single largest crawl liability on an ecommerce site. Parameter-based facets generate
infinite URL spaces, causing **overcrawling** (crawlers must fetch a URL to learn it is
useless) and **slower discovery** of genuinely new URLs.

**Decide first: do you need facet URLs indexed at all?** Usually no.

**If not — prevent crawling.** In order of documented effectiveness:

1. **robots.txt disallow.** Google's own example:
   ```
   user-agent: Googlebot
   disallow: /*?*products=
   disallow: /*?*color=
   disallow: /*?*size=
   allow: /*?products=all$
   ```
   Google's framing: "Oftentimes there's no good reason to allow crawling of filtered items."
   Allow the individual product pages and one unfiltered listing page.
2. **URL fragments for filters** — `#products=fish&color=green`. Google generally doesn't
   support fragments in crawling and indexing, so a fragment-based filter has *no* crawl impact,
   positive or negative.
3. `rel="canonical"` to the unfiltered version, and `rel="nofollow"` on facet anchors, are both
   documented but Google calls them "generally less effective in the long term". `nofollow` only
   works if **every** anchor to that URL carries it — one missed link defeats it.

**If facet URLs must be indexable**, Google's four requirements:
- Use `&` as the parameter separator. Comma, semicolon and brackets are not reliably detected
  as separators.
- If filters are encoded in the path (`/products/fish/green/tiny`), the filter order must be
  stable and duplicates impossible.
- **Return 404 when a filter combination has no results** — and serve it at the URL where it
  was encountered, not by redirecting to a generic error page. Same for duplicate filters,
  nonsensical combinations, and non-existent pagination URLs.
- Accept the cost: crawling facets "tends to cost sites large amounts of computing resources".

---

## Pagination, load-more, infinite scroll

Google documents the trade-offs rather than picking a winner. Choose on UX, then make the
chosen pattern crawlable.

| Pattern | Google's stated limitation |
|---|---|
| Pagination | Content split across pages; viewing more requires new page loads |
| Load more | "Can't handle very large numbers of results as all results are on a single page" |
| Infinite scroll | Scrolling fatigue, unclear result size; same volume ceiling |

**The crawl reality that decides it:** "Google's crawlers don't 'click' buttons and generally
don't trigger JavaScript functions that require user actions to update the current page
contents." Load-more and infinite scroll are JS-driven by default, so without crawlable
`<a href>` pagination underneath, the content past the first screen does not exist to Google.

**Pagination requirements:**
- Link pages **sequentially** with `<a href>`, page n → page n+1.
- Consider linking every page in a collection **back to page 1** — a documented hint that page 1
  is the better landing page.
- **Each page gets a unique URL** (`?page=n`). Google: "We see the most URL mistakes in
  pagination URL structures."
- **Each page gets its own self-referencing canonical.** Never canonical page 2+ to page 1.
- **Never use fragments for page numbers.** Google ignores fragments and may not follow a link
  that differs only after the `#`, believing it already has the page.
- Paginated pages **may share titles and descriptions**. This is an explicit exemption from the
  unique-titles rule — do not flag it as a duplicate-title defect. "Google tries to recognize
  pages in a sequence and index them accordingly."
- `<link rel="next">` / `rel="prev">`: **Google no longer uses these.** Other engines may.
  Their absence is not a finding.
- Filters and alternative sort orders (`?order=price`) returning the same result set: block with
  `noindex` or discourage crawling via robots.txt.

---

## URL design (own-build sites only)

Three documented failure modes:
- **Fragments used to vary content.** `/product/t-shirt#black` and `#white` are one page to
  Google; one variant gets discarded.
- **Multiple URLs returning identical content** (`/product/black-t-shirt` vs `/product?sku=1234`).
  Google cannot tell from the URL alone and must fetch both.
- **Continually changing values** — timestamps, `?now=12:34am` — read as an infinite page space.

Rules:
- Descriptive words in paths: `/product/black-t-shirt-with-a-white-collar`, not `/product/3243`.
- Normalise case if the server treats case identically.
- `?key=value`, never bare `?value`. `/t-shirt?color=green`, not `/t-shirt?green`.
- Never repeat a parameter — `?type=candy,sweet`, not `?type=candy&type=sweet`. Googlebot may
  ignore one value.
- Never internally link to temporary parameters: session IDs, tracking codes, `location=nearby`,
  `time=last-week`, current time. "Use long-term, persistent URLs."
- Every paginated page needs its own unique URL.

---

## Product data and structured data

Two channels, and they are complementary rather than alternatives:

1. **Product structured data on the page.** Increases eligibility for Product rich results, and
   improves the accuracy of Google's reading of price, discount and shipping — which also feeds
   Merchant Center's verification of feeds against the site.
2. **A Google Merchant Center feed.** Not mandatory for organic Search results, but **mandatory
   for some surfaces, including the Shopping tab.** For small, slow-changing catalogues, an
   automated feed can be built from crawled web content — and on-page structured data improves
   that extraction's accuracy.

Ecommerce-relevant structured data types with their own Google feature guides: `Product`,
product snippet, **product variants**, merchant listing, **shipping policy**, **return policy**,
**loyalty program**, review snippet, breadcrumb, local business, organization, carousel.

Note the four bolded ones — they are recent additions most audit checklists have not caught up
with, and they are the cheapest differentiators on a merchant listing.

To stop Google forming a snippet from a specific element (a price block being misread, say), use
the `data-nosnippet` attribute on that element — not `nosnippet` on the page, which also removes
the page from AI Overviews and AI Mode eligibility.

---

## Launching a new ecommerce site

Timing matters: register the site with Google (Search Console, Merchant Center) before, not
after, the catalogue goes live, so discovery starts on day one rather than after the first
marketing push has already missed. See
`/search/docs/specialty/ecommerce/how-to-launch-an-ecommerce-website`.

---

## The ecommerce failure list, ranked by how often it is the actual cause

1. Facet URLs crawled without limit — crawl budget consumed, new products discovered late
2. Products not linked from any category page, reachable only via site search
3. Infinite scroll or load-more with no crawlable pagination beneath it
4. Page 2+ canonicalised to page 1, so deep catalogue pages never index
5. Out-of-stock pages 404'd or redirected to the home page instead of kept live
6. Thin category pages — no unique copy, just a product grid
7. Manufacturer-supplied product descriptions duplicated across the whole market
8. No product structured data, or structured data whose prices contradict the visible page
9. Sort-order URLs indexed alongside the canonical listing
10. Session IDs or tracking parameters in internal links
