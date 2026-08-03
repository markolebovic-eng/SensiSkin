# Site Moves, Migrations and Redirects

The migration playbook. Every fact traced to
`/search/docs/crawling-indexing/site-move-with-url-changes` unless noted.

Two different documents apply depending on what is changing:

| Change | Document |
|---|---|
| URLs change (domain, path, HTTP→HTTPS, merging hostnames) | site move **with** URL changes — this file |
| Hosting, CDN, IP, server software; URLs unchanged | site move **without** URL changes (`/search/docs/crawling-indexing/site-move-no-url-changes`) |

---

## Before the move

**Split the move if the site is large.** Move one section first, pick a section that changes
infrequently and is not event-driven, and watch traffic and indexing. Google's caveat: one
section "is not necessarily representative of a whole site move".

**Change one thing at a time.** New domain, new CMS, new layout — sequence them, do not ship
them together. When they ship together a regression cannot be attributed.

**Time it to a traffic trough** — seasonal dip or a low weekday. Fewer users affected and more
server headroom for the crawl surge.

**Provision for the crawl surge.** After a migration Google crawls the new site *more heavily
than usual*, because old-site crawls redirect into it on top of normal crawling. Tell the host
in advance for a large site.

**Search Console preparation:**
- Verify **every variant** of both old and new: `example.com`, `www.example.com`, HTTP and
  HTTPS, and every subdomain.
- Confirm verification survives the move. HTML-file verification means copying the
  verification file into the new site; meta-tag or Analytics verification means the new CMS
  must emit it too. Tokens can differ when the URL changes.
- Set crawl rate to "Let Googlebot determine" on **both** properties.
- Re-upload any **disavow file** under the new property.
- On a **purchased domain**, clear the previous owner's baggage: check the Manual Actions
  report (file a reconsideration request if there is one) and the Removals tool for a
  leftover site-wide URL removal.

**Prepare the new site's robots.txt and `noindex` rules for launch day.** Sites commonly block
all crawling during development. Write the production robots.txt in advance and list every URL
whose `noindex` must be removed at cutover. Forgetting this list is the single most common
migration failure.

**Deleted content returns 404 or 410** on the new site. Do not silently drop it.

---

## URL mapping

Sources for the old URL list, in Google's order:
1. Sitemaps (most important URLs were already submitted there)
2. Server logs or analytics — highest-traffic URLs
3. Search Console "Links to your site" — pages with internal and external links
4. The CMS URL listing
5. Server logs for anything visited at least once in a period that covers seasonal variation

**Include embedded assets.** Videos, images, JS and CSS URLs move like everything else. Image
and video URLs may already carry traffic or links.

For a straight domain swap with identical paths, a wildcard server-side redirect avoids
enumerating URLs at all.

---

## Update the new site before cutover

- **Self-referencing `rel="canonical"`** on every new URL.
- **Update hreflang annotations** to the new URLs if the site is multilingual.
- **Rewrite internal links** from old URLs to new URLs, using the mapping. Do not rely on
  redirects for internal navigation.
- Save two artefacts for the cutover: a sitemap of the new URLs, and the list of external sites
  linking to old URLs (from Search Console).

---

## Redirects

- **Server-side permanent redirects.** 301 or 308. Client-side redirects are a last resort.
- **301 and other permanent redirects do not cause a loss in PageRank.** State this plainly
  when a client asks about "losing link juice" — it is documented.
- **Chains:** Googlebot follows up to **10 hops**. Google's recommendation is to redirect
  straight to the final destination; if a chain is unavoidable, keep it to **no more than 3,
  and fewer than 5**. Chains add user latency and not all user agents follow long ones.
- **Never mass-redirect old URLs to the home page** or another irrelevant destination. Google
  may treat it as a **soft 404**. Consolidating several old pages onto one genuinely
  consolidated new page is fine.
- **Keep redirects at least 1 year**, and Google's stronger framing: from a user's perspective,
  consider keeping them indefinitely. A year is how long signal transfer and third-party
  relinking need. Because redirects are slow for users, chase down high-volume inbound links
  and get them updated at the source.

**Move all at once or in sections?**
- Small and medium sites: move **all URLs simultaneously**. Google's systems detect the move
  and update the index faster.
- Large sites: section by section is acceptable and makes problems easier to isolate.

---

## Cutover checklist

1. Enable the redirects.
2. Verify `rel="canonical"` on the new site now points at new URLs, and that any development
   `noindex` rules are gone.
3. Test redirects — URL Inspection for spot checks, a script for bulk.
4. Submit **Change of Address** in Search Console for the old site.
   - **Not needed for HTTP → HTTPS.**
   - For a domain move, submit it for **every subdomain and both www and non-www variants** of
     the old domain, including variants you do not actively use. All must be verified.
5. Submit the new sitemap. The old sitemap can then be removed.
6. Monitor traffic and indexing on **both** properties.

---

## What to tell the client about timing

"A medium-sized website can take a few weeks for most pages to move in our index; larger sites
can take longer." Speed depends on URL count and server speed. Submitting a sitemap speeds
discovery. The move is complete only once Googlebot has visited every URL on both old and new
sites at least once — there are no fixed crawl frequencies, and the move happens per URL.

Ranking fluctuation during this window is expected, not evidence of a mistake. Do not start
making corrective changes inside the first few weeks unless a technical check fails.

---

## When a migration drop is not recovering

Work this list before concluding the migration "just cost rankings":

- Redirects returning 302 rather than 301/308
- Redirect chains beyond 3 hops, or loops
- Old URLs 404ing instead of redirecting
- Many-to-one redirects to the home page, now classified as soft 404s
- Development `noindex` or a blanket `Disallow: /` still live on the new site
- Canonicals still pointing at old URLs
- Internal links still pointing at old URLs, so every navigation click is a redirect
- hreflang still referencing old URLs (the whole cluster is discarded)
- Change of Address not submitted, or submitted for only one variant
- New sitemap not submitted, or containing non-canonical URLs
- Server unable to absorb the post-migration crawl surge — 5xx or 429 responses, which lower
  the crawl capacity limit exactly when it needs to be high

Cross-check against `search-diagnostics.md` step 2: a migration drop and a core-update drop
land in the same week often enough that assuming causation is a real risk.
