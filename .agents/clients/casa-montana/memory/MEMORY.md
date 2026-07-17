# Casa Montana — Shared Agent Memory

This file is read and updated by all agents working on this client.
It acts as the project's persistent memory across sessions.

## Last updated
2026-07-18 — onboarding (product-marketing.md written + confirmed by owner)

## Active campaigns
None yet — first deliverable in progress: cinematic video walkthrough for
the for-sale/for-rent listing.

## Key decisions made
2026-07-18 | New agency service "video walkthrough nekretnine" launched with
Casa Montana as first client. Architecture: `property-walkthrough` agent
uses Higgsfield MCP (already connected in this environment) for both
generation AND stitching/reframing — no ffmpeg dependency, unlike the
reference open-source project this was scoped against (charlesdove977/
re-walkthrough-pro, Zillow-only, ffmpeg-based). Photo sourcing is
Booking.com (via Apify, account not yet created by owner) + Airbnb (direct
fetch works, no Apify needed) + optional local folder, merged into one pool
before curation.

2026-07-18 | Owner confirmed: has usage rights to Booking.com/Airbnb photos.
Price is NOT to be disclosed in any marketing material or video. Target
buyer is dual (personal use OR investor continuing the rental) — owner
explicitly said either is fine, agency defined both personas in
product-marketing.md.

## Completed tasks log
2026-07-18 | orchestrator (direct, no subagent) | Pulled 15 real listing
photos directly from Airbnb via curl (no Apify needed for this source) |
saved to .agents/clients/casa-montana/photos/airbnb/ | Booking.com direct
fetch blocked by AWS WAF bot challenge — confirmed Apify is required for
that source, as anticipated.

## Photo sourcing status
- Airbnb: DONE — 15 photos in photos/airbnb/, visually verified as genuine
  property photos (exterior, drone shot, terrace view).
- Booking.com: BLOCKED (bot protection) — needs Apify account + token in
  .env as APIFY_TOKEN, then a Booking.com photos actor via the
  property-walkthrough agent.
- Local folder (owner-supplied, outside Airbnb/Booking): not yet provided —
  can be added anytime to photos/local/.

## Brand voice reminders
Positioning line to reuse verbatim across future copy: "chalet u Alpima, ali
na Kopaoniku." Never disclose price. Never claim "3D" or "Matterport" for
the walkthrough video — always "cinematic walkthrough."

## SEO targets
Not started — website for Casa Montana brand is planned by owner but not
yet built. Revisit once site work begins.

## Conversion insights
[cro agent logs A/B test results and winning variants here]

## Ad performance notes
[paid-ads agent logs what's working and what isn't here]

## Email metrics
[email agent tracks open rates, sequence performance here]

## Analytics baselines
[analytics agent records key metric benchmarks here]

## Prvi video walkthrough isporučen (2026-07-17)
- Model: Kling 3.0 Turbo (budžetska varijanta, 720p, 3s/klip, 16:9) — vlasnik odobrio nakon preflight poređenja cena (Seedance 2.0 std = 22.5 kr/klip vs Kling Turbo = 4.5 kr/klip, 80% jeftinije).
- Svih 12 prepoznatljivih prostorija animirano (kuća je manja pa nije rađena standardna 6-10 kuracija) — pokrivene sve iz rasporeda OSIM garaže i nedovršenog apartmana (nisu se pojavile ni na Airbnb ni na Booking galeriji, potrebne dodatne fotografije od vlasnika).
- Fotografije: 15 sa Airbnb (direktan fetch, bez Apify-ja) + 44 sa Booking.com (Apify akter `voyager~booking-scraper`, ~$0.005) — spojeno u jedan pool pre kuracije.
- Spajanje: Higgsfield `explainer_video` — potvrđeno besplatno (54 kredita potrošeno = tačno 12×4.5, spajanje nije dodalo trošak).
- 9:16 verzija NIJE napravljena (176-288 kredita samo za reframe, nesrazmerno skupo za budžet; video ide na sajt, ne na društvene mreže).
- Trošak: 271→217 kredita (54 potrošeno), Higgsfield plan "starter".
- Deliverable: /outputs/casa-montana/property-walkthroughs/2026-07-17/final/walkthrough-16x9.mp4 (~36s, 1280×720, 9.3MB) + PROPERTY.md + shot-list.md.
- Istražen i odbačen kao neupotrebljiv za ovaj slučaj: github.com/anil-matcha/open-generative-ai ("open source Higgsfield alternativa") — u suštini isti plaćeni MuAPI aggregator, pravo besplatno lokalno video generisanje (Wan2GP) zahteva CUDA GPU koji vlasnik nema na Mac-u.
