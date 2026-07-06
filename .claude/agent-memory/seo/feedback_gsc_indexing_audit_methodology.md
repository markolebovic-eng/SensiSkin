---
name: gsc-indexing-audit-methodology
description: How to run a thorough GSC indexing/visibility audit that catches legacy "ghost" URLs a sitemap-only check would miss
metadata:
  type: feedback
---

When running a full GSC indexing audit, do not limit the URL universe to what the current sitemap declares. Always cross-reference three sources:

1. `gsc_search_analytics` with `dimensions: ["page"]` over 90-180 days, high `row_limit` — this surfaces EVERY URL Google has clicks/impressions data for, including old/retired URLs no longer in the sitemap.
2. The live sitemap (fetch each child sitemap, not just the index) — this is the "should exist" list.
3. `gsc_inspect_url` on every URL in BOTH lists — sitemap URLs to confirm indexing health, and GSC-only URLs (not in sitemap) to catch legacy slugs.

**Why:** In one audit, the single most-clicked URL after the homepage (560 clicks/90d) turned out to be a legacy slug (`/cenovnik-usluga-2/`) that had gone live-404 and wasn't in the current sitemap at all — a sitemap-only check would have completely missed it. `gsc_traffic_drops` then confirmed the exact click collapse (551→1) tying the 404 to an active, ongoing traffic loss rather than old historical noise.

**How to apply:** Always verify suspected legacy-URL 404s with a direct `WebFetch` on the live URL in addition to `gsc_inspect_url` — GSC's crawl data can lag; a live fetch confirms the problem is current, not stale. Also check `gsc_cannibalization` for the brand-name query specifically — old duplicate slugs frequently show up there since they still rank for "[brand name]" long after the canonical page has moved. Pair with [[blog-topic-research-methodology]] pattern of cross-referencing multiple data sources before concluding.
