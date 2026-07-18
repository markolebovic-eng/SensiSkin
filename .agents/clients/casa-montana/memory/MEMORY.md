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

2026-07-18 | Client website found on GitHub: github.com/ognjenzekovic/casa-montana
(React 19 + Vite + TS, deployed via GitHub Actions to GitHub Pages, custom
domain casamontana.rs configured in Pages settings but DNS not resolving yet
— site is currently unreachable to visitors, needs owner/registrar check).
Marko is a collaborator on it (repo owner: ognjenzekovic, separate from his
own markolebovic-eng account/SensiSkin repo). Cloned locally to
`/Users/marko/casa-montana` — a SIBLING folder to this SensiSkin repo, not
nested inside it, so `git push` in either location only ever affects that
repo's own remote. Site code/SEO/schema/blog work happens in that folder
against the `ognjenzekovic/casa-montana` remote; all marketing strategy,
copy, and this MEMORY.md continue to live here in SensiSkin regardless of
which client. Repo audit done 2026-07-18 found: Specs.tsx has literal
`[XXX] m²` placeholders (living space + plot size) awaiting real figures,
Trust.tsx has unverified stats (5.0 rating / 14 reviews / 13 years) and a
guest quote that need confirming against real Booking/Airbnb data before
trusting them, Gallery.tsx only has 1 real photo + 5 text placeholders
despite 66 real photos already sourced (in this repo's
`.agents/clients/casa-montana/photos/` and copied to the owner's Desktop),
video walkthrough not embedded anywhere, favicon not wired to the real
brand asset, Instagram link is a dead generic placeholder, and site
messaging is sale-only (ignores the dual sale/rental positioning).

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

brand-voice-extractor skill NOT run for this client (no existing blog/site
corpus to extract from — skill's own prerequisites aren't met; site is
still "u izradi"). Copywriter proceeds directly from product-marketing.md
positioning until real client-authored content exists to calibrate against.

## GBP "description" field — approved 2026-07-18
Owner-facing GBP profile description (683/750 chars), approved final text
for copy-paste replacing the old inventory-only description:

"Casa Montana je brvnara na Kopaoniku koja spaja rustični duh prave
planinske kuće s luksuznim enterijerom: chalet u Alpima, ali na Kopaoniku.
Kuća stoji izolovano usred prirode, a do staza i centra Kopaonika stižete
lako. Dnevni boravak ima kamin i prostranu terasu, kuhinja je potpuno
opremljena, tu su dve spavaće sobe, dva kupatila i sauna za opuštanje posle
dana na stazama. Terase na oba sprata gledaju na šumu, a Wi-Fi je brz i
pogodan i za posao i za odmor. Casa Montana godinama prima goste preko
Booking-a i Airbnb-a, a nezavisni vodiči je svrstavaju među vodeće luksuzne
chalete na Kopaoniku. Prima do šest gostiju. Rezervišite boravak u
planinskoj kući s pravim karakterom."

Reuse this phrasing pattern (positioning line up front, functional details
woven into sentences not bulleted, external reputation stated without
naming J2Ski directly) for any future GBP/website description copy for this
client.

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

## Brand cover slike (2026-07-18)
- 2 cover/teaser varijante u /outputs/casa-montana/brand/ (cover-v1-front-aerial, cover-v2-topdown), 2560x1440 (16:9).
- NAČIN IZRADE — bitno za buduće: NIJE korišćen AI (vlasnik tražio "ništa izmišljeno, skroz realistično") — osnova su PRAVE dron fotografije sa Airbnb listinga, "CASA MONTANA / KOPAONIK" natpis dodat programski (Pillow, Didot font, razmaknuta velika slova, cinematični edge-gradijent) — tekst savršeno oštar, fotografija netaknuta.
- OTKRIĆE: Airbnb servira i 2560px verzije fotografija sa ?im_w=2560 parametrom na original URL (originalno skinute bile 1200x900) — hi-res verzije 3 dron kadra u photos/hires/.
- Higgsfield MCP bio diskonektovan tokom ovog zadatka (drugi put u sesiji; prošli put se sam vratio) — nije ni bio potreban za covere.
