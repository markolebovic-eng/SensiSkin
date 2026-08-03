# SEO skill pass — working note (2026-08-04)

Companion to the GEO pass (`00`–`05`, `evidence-ledger.md`). Same corpus, no new harvest.
This note records what changed in `seo-audit` and why, so the next pass doesn't re-derive it.

## Corpus areas worked

Structured data (~30 feature guides + sd-policies + search-gallery) · ecommerce (9) ·
international (4) · site moves (2) · JavaScript SEO (4) · page experience + CWV + interstitials ·
sitemaps (7) · canonicalization (3) · Search Console diagnostics + traffic drops · featured
snippets · Discover · spam policies · core and spam updates · crawl budget · faceted navigation ·
robots meta tag · block indexing · crawling myths · seo-starter-guide myths section ·
search_updates changelog (for deprecation dates).

## Fabricated / untraceable claims found and removed

All in the SEO skill, all now removed or reframed. None survived into a client-facing path.

| Claim | Where | Disposition |
|---|---|---|
| "A study of 374,756 domains found 67% of hreflang implementations had issues" | international-seo.md | **Removed.** Cited source is an SE Land article headlined 31%. Sample size and figure both untraceable |
| "Missing self-referencing is the #1 error found by Semrush audits" | international-seo.md | **Removed.** Unverifiable superlative |
| "A study found 8.9% of sites using hreflang contain invalid language codes" | international-seo.md | **Removed.** Not in the cited source |
| "~1.5KB per page" for 20-locale in-head hreflang | international-seo.md | **Removed.** Invented precision; replaced with the qualitative trade-off |
| "Plan for 2,000–5,000 URLs per sitemap when using full hreflang" | international-seo.md | **Reframed** as a derivation from the documented 50MB limit, not a quoted figure |
| "Reddit scaled AI translations to 35+ languages" | international-seo.md | **Removed.** Language count not verifiable from cited article |
| "rel=next/prev deprecated March 2019" | international-seo.md | **Reframed.** The date is not in current Google docs; the removal is what matters |
| Title "50–60 characters" presented as a rule | SKILL.md | **Reframed as heuristic.** Google: "there's no limit on how long a `<title>` element can be" |
| Meta description "150–160 characters" presented as a rule | SKILL.md | **Reframed as heuristic.** Google: "there's no limit on how long a meta description can be" |
| "One H1 per page", "skip levels" listed as issues | SKILL.md | **Inverted.** Google: heading order "doesn't matter" for Search |
| "Keyword in first 100 words" | SKILL.md | **Removed.** No documented basis |
| "Sufficient depth/length for topic" | SKILL.md | **Removed.** Google: "no magical word count target" |
| "Important pages within 3 clicks" as a ranking item | SKILL.md | **Reframed.** Documented effect is crawl frequency, not ranking |
| E-E-A-T presented as tunable signals | SKILL.md | **Corrected.** Google: "Thinking E-E-A-T is a ranking factor… No, it's not" |
| Engagement metrics implied as ranking signals | SKILL.md | **Reframed** as business diagnostics |

Verified-correct numbers (traced, kept): LCP 2.5s / INP 200ms / CLS 0.1; INP replaced FID
March 2024; sitemap 50,000 URLs / 50MB; helpful content system merged into core ranking
March 2024; crawl budget scope 1M+ weekly / 10K+ daily.

## Stale-fact corrections

- **FAQ rich result is dead.** Deprecation notice May 2026 → stopped appearing **7 May 2026** →
  documentation removed June 2026. **HowTo** likewise removed (2023). Neither is in the current
  search gallery. Confirmed live on the client site: `FAQPage` markup on three service pages
  producing nothing.
- **Mobile-Friendly Test and Mobile Usability report** removed from Google's docs Dec 2023.
- **Dynamic rendering** is documented as a workaround, not a solution.
- **Spam policies apply to generative AI responses** (doc update May 2026).
- **Structured-data manual actions** cost rich-result eligibility only, not web ranking.
- `crawl-delay` not processed by Google; `<priority>`/`<changefreq>` ignored in sitemaps.

## Files

**Edited:** `seo-audit/SKILL.md` (v2.1.0 → v3.0.0) · `seo-audit/references/international-seo.md` ·
`seo-audit/evals/evals.json` · `geo/SKILL.md` (description + decision tree) ·
`geo/references/technical-checklist.md` (pointer block) ·
`geo/scripts/schema_extract.py` (retired-type flagging).

**Created — three, each SEO-only, each >150 lines of source material, none fitting an existing
GEO reference:**
- `seo-audit/references/search-diagnostics.md` — traffic-drop method, core updates, spam policies,
  crawl-budget myths. GEO's `measurement.md` is AI-surface metrics; nothing covered Search
  diagnosis.
- `seo-audit/references/site-moves.md` — migration playbook. No existing file anywhere.
- `seo-audit/references/ecommerce-seo.md` — faceted nav, pagination, URL/parameter design,
  Merchant Center. No existing file anywhere.

## Known remaining rot — not fixed, out of scope of this pass

**`schema` skill still ships `FAQPage` and `HowTo` as live recommendations** in `SKILL.md`
(types table + example section) and in `references/schema-examples.md`, and eval 2 asserts FAQ
rich results are obtainable. `seo-audit` now carries the authoritative retirement table and
`schema_extract.py` flags the types at runtime, so a `seo-audit` run will not propagate the error —
but a direct `schema` invocation still will. Needs its own corpus pass against the ~30 feature
guides, which would also pick up the newer types (product variants, shipping/return policy,
loyalty program, vacation rental, discussion forum, profile page).

## End-to-end verification

Ran the skill against `sensiskinstudio.com` (10 priority URLs from `page-sitemap.xml`).

Real findings produced: `FAQPage` on 3 service pages (retired, no return); a `noindex` URL present
in the page sitemap; an untranslated English H1 (`My account`) on a Serbian site; `Bytespider`
403 at the edge (not citation-critical). `max-image-preview:large` present sitewide, so Discover
image eligibility is intact.

**False findings the pre-pass skill would have produced and this one now suppresses: ~13.**
All 10 meta descriptions fell in the 106–137 character band and would have been flagged "too
short" against the invented 150–160 rule; one title at 20 characters likewise; heading sequences
on nearly every page skip levels (`1426342444`) and would have been flagged as hierarchy defects.
That ratio — 13 false to 4 real — is the case for the myths table existing.

Executability bugs found and fixed during the run: script paths were written `../geo/scripts/…`
with no stated working directory (ambiguous, would fail); normalised to repo-root-relative and
added the `priority.txt` build command, which the skill referenced but never showed how to make.
