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

2026-07-19 | SITE REVIEW ADOPTED AS CURRENT FINAL PLAN + owner decisions
(these SUPERSEDE earlier "99% rental / 1% sale" framing). Full plan:
outputs/casa-montana/site-review/revizija-sajta-2026-07-19.md — every agent
working on this client/site MUST read it first.
- IMPORTANT REFRAME: **sale matters financially to the AGENCY** (we earn a
  percentage when the house sells through us); rental is a bonus for the
  client. So the goal is NOT a rental-only site. The current dual
  sale/rental balance on the site STAYS; a dedicated "prodaja" (sale)
  button is planned as an addition. Do NOT aggressively flip tone to
  rental. Only concrete copy tasks left: fix the one line that disparages
  renting (Intro "ne za jedan izdatak") and add the positioning line
  "chalet u Alpima, ali na Kopaoniku" (currently absent from the site).
- APPROVAL GATE: NOTHING on the client site/repo (ognjenzekovic/casa-montana)
  gets changed without Marko's explicit prior approval. Ask first for EVERY
  change, execute only after he approves (via PR).
- GA4: create a NEW property (no existing account to connect).
- Missing data (m², plot size, ratings, working email, IG handle, map
  coords) will be supplied by owner in due time — stay open until then.
- Domain: waiting for the regular domain (casamontana.rs). Site lives on the
  github.io URL for now; finalize canonical/og:url/email only once the
  domain is known.

## Completed tasks log
2026-07-28 | claude | Fresh live-site review (site now LIVE at casamontana.rs,
DNS fixed, HTTPS ok) after dev pushed 8 commits | report:
outputs/casa-montana/site-review/revizija-sajta-2026-07-28.md. DEV PROGRESS
since 2026-07-19: gallery fully populated incl. sauna+terrace with day/night
variants; Specs filled (200 m² living / 700 m² plot); SR/EN localization
(client-side localStorage toggle); 2nd sale button + Instagram + mobile nav.
STILL OUR WORK (all unaddressed): SPA has NO prerender (content invisible to
AI/GEO), NO analytics/GA4, blog is HASH-routed (#/blog) + MOCK placeholder
content (zero SEO value, cards link nowhere), no robots.txt/sitemap.xml, no
JSON-LD schema, og:image still relative (broken social share), title/meta
still sale-only, bilingual but NO hreflang/per-language URLs (EN version
invisible to search), no canonical, Trust rating inconsistency persists
(Trust 5.0/14/13 vs Book 9.8/10 — label sources), video walkthrough still not
embedded, intro line "ne za jedan izdatak" still disparages rental. Proposed
3 waves: (1) quick PR wins (GA4+click tracking, og/canonical/title/meta,
schema, robots+sitemap, alts, video embed, copy tweaks); (2) architecture:
prerender (unlocks GEO + indexable blog + hreflang) + blog real routing;
(3) content: real bilingual blog posts on local/GEO topics. Repo change gate
still applies — nothing pushed, awaiting Marko's pick of what to start.
2026-07-28 | claude | Wave 1 (part 1) SHIPPED AS PR (not merged): branch
`seo/wave-1-technical` → **PR #1** https://github.com/ognjenzekovic/casa-montana/pull/1
(ognjenzekovic requested as reviewer). Additive technical SEO/GEO only:
index.html canonical + absolute og:image/og:url/twitter:image/og:locale +
static LodgingBusiness JSON-LD in <head> (rating/phone omitted pending source
confirm); new public/robots.txt (allows AI bots + sitemap link) + public/
sitemap.xml (homepage). DO NOT MERGE without Marko/dev approval (merge = push
to main = auto-deploy). Process choice: PR stays open until dev/owner approves.
Deferred to next PRs (need Marko input): GA4 (needs Measurement ID), video
walkthrough embed (self-host vs YouTube decision), title/meta rewrite (needs
approved wording), aggregateRating (needs rating sources: Trust 5.0/14/13 vs
Book 9.8/10 — which is Airbnb vs Booking). Self-contained todo for a follow-up
PR: gallery rich alt texts + soften "ne za jedan izdatak" line.
2026-07-28 (later) | claude | EXTENDED PR #1 (2 commits, still branch
`seo/wave-1-technical`, still OPEN/not merged) to cover most of Wave 1 after
Marko said "moze sve osim video" + confirmed 9.8=Booking, 5.0=Airbnb.
Commit 2 adds: title/meta rewrite sr+en (sale-only -> "luksuzna brvnara sa
saunom na Kopaoniku" / rental+brand+local kw, "izdavanje i prodaja") in
index.html + translations.ts; aggregateRating 9.8/10 Booking in the JSON-LD
(ratingCount=14 = TO VERIFY vs Booking actual); richer localized gallery alt
(room+day/night+"luksuzna brvnara na Kopaoniku"); rating-source disambiguation
(Trust label -> "Prosečna ocena na Airbnb-u" for 5.0; Book body -> "9.8/10 na
Booking-u"); softened intro ("ne za jedan izdatak" -> "ne za jedan trenutak").
Ran `npm ci && npm run build` locally = build PASSES (TS + vite ok). PR title/
body updated to full Wave-1 scope. STILL DEFERRED (need input): GA4 (Measurement
ID — create property or provide G-XXXX; deliberately NOT shipped as inert
placeholder), video embed (no final video yet). Wave 2 = prerender + hreflang +
real blog routing (architecture). PR must NOT be merged without dev/owner
approval (merge=deploy).
2026-07-28 (later still) | claude | GA4 ADDED to PR #1 (3rd commit, still
OPEN/not merged). Marko created the GA4 property himself in the GA dashboard
(couldn't be done via API/agent — needs Marko's Google login) and pasted the
gtag snippet with **Measurement ID G-K1SZ80NW26** — CONFIRMED via
mcp__google-seo-mcp__ga4_list_properties that this is a genuinely NEW property
(the only pre-existing GA4 property on the connected Google account is
SensiSkin's "Kozmetološki Centar", properties/532419831 — correctly NOT
reused). Added: gtag.js snippet in index.html; new src/lib/analytics.ts
(trackOutboundClick() helper, no-op if gtag absent); wired onClick ->
'outbound_click' GA4 event on Book.tsx's Booking/Airbnb/Instagram buttons and
Close.tsx's mailto CTA (destination='contact', covers the ~1% sale-inquiry
path). This makes click-to-OTA — the agreed conversion metric — measurable
for the first time. Consent Mode (EEA GDPR) explicitly NOT configured: only
functions with a cookie-consent banner (CMP) feeding it signals, which this
site doesn't have; flagged as a possible future task, not done now. `npm run
build` verified passing after each commit. **Wave 1 is now COMPLETE except
video embed** (no final video yet) — everything else (technical schema/meta/
robots/sitemap + title/meta rewrite + ratings + alt text + copy + GA4/
tracking) is in PR #1, still awaiting dev/owner review, still NOT merged.
2026-07-20 | claude (direct) | Exterior cinematic reel from 12 owner-shot
iPhone clips (~/Desktop/Casa Montana/Snimci - Claude/) | ffmpeg LOCAL, no
Higgsfield/no AI — pure edit | output: outputs/casa-montana/exterior-video/
casa-montana-eksterijer-9x16-2026-07-20.mp4 (1080x1920, 30fps, silent,
~22.5s, 32MB) + EDIT.md. Curated 8 of 12 clips into arrival→facade→forest→
craft→stream→stream-to-house→entrance→brand-sign order, 0.5s crossfades,
fade in/out. NOTE for future video work: these iPhone clips are 4K 10-bit
HLG HDR (BT.2020); the brew ffmpeg 8.1.2 build here has NO zscale/libzimg/
libplacebo, so proper HDR tonemap isn't available — used direct decode +
gentle grade (eq contrast1.08/sat1.12/gamma0.975 + unsharp), visually
verified fine. Interior folder not yet provided (only exterior done). ffmpeg
installed via brew this session.
2026-07-21 | claude (direct) | v3 exterior showcase reel (owner rejected v1:
bad dissolve transitions, over-compressed, broken HDR) | output:
outputs/casa-montana/exterior-video/vikendica_reel_v3.mp4 (1080x1920, 30fps,
Rec.709-tagged, hard cuts only, 20.0s, 36.6MB) + vikendica_reel_v3_EDIT.md.
KEY FIX for HDR: brew ffmpeg lacks zscale, so downloaded a static arm64
ffmpeg WITH zscale (Martin Riedl build, saved at scratchpad/ffbin/ffmpeg via
https://ffmpeg.martin-riedl.de/redirect/latest/macos/arm64/release/ffmpeg.zip)
and did a proper HLG->SDR tonemap (zscale linear npl=100 -> tonemap hable ->
bt709), validated on 3 test frames. Target is SDR Rec.709 (NOT HDR — IG/TikTok
break HDR). Encode CRF19 + maxrate 16M (no more 12M cap that caused mushy
foliage). Order by trend ruleset (hook=approach push-in, journey, shot-scale
rhythm, match cut on stream pans, loop-friendly wide closer). Folder now has
11 clips: 1.MOV = renamed approach (ex-IMG_4896); owner deleted the CASA
MONTANA sign clip (ex-4901). Reel is MUTE (owner adds music later; cut list
in EDIT.md for beat-sync). Interior folder still not provided.

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
⚠️ RETIRED (2026-07-31, Marko explicit correction): "chalet u Alpima, ali na
Kopaoniku" — do NOT reuse this line in any NEW copy (site, blog, social,
future GBP updates). Marko said he dislikes it outright. Scope confirmed:
the already-live GBP description (below) stays untouched as approved
historical text — this only affects future writing, not a retroactive edit
of live GBP copy. See brand-voice-script.md before/after #13 for the
corrected note. Never disclose price. Never claim "3D" or "Matterport" for
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
Site is now LIVE (2026-07-18/19) at http://ognjenzekovic.github.io/casa-montana/
(github.io URL, 200 OK — CNAME removed so no more redirect to dead
casamontana.rs; DNS still unresolved). Full site review done 2026-07-19:
outputs/casa-montana/site-review/revizija-sajta-2026-07-19.md. Headline
findings: (1) SPA with no prerender → content invisible to AI/GEO crawlers,
(2) NO analytics at all → our agreed click-to-OTA conversion metric is
unmeasurable, (3) whole site is written SALE-first ("na prodaju", "pre
kupovine", "posed") which contradicts the 99% rental/brand goal, (4) zero
JSON-LD schema, no robots.txt, no sitemap.xml, (5) og:image is a relative
path → broken social share preview, (6) live `[XXX] m²` placeholders in
Specs, (7) rating inconsistency (Trust says 5.0, Book says 9.8/10),
(8) video walkthrough still not embedded, (9) gallery has real photos by
room now BUT terase=0 and sauna missing entirely (our top differentiators),
(10) Instagram link dead (generic instagram.com), mailto uses dead domain.
Book.tsx DOES funnel to Booking+Airbnb (good, matches strategy). We are repo
collaborators so we can execute technical SEO/GEO fixes via PR; content
figures (m², ratings, email, IG handle) need owner data. Awaiting Marko's
decisions on tone-flip aggressiveness, what we may edit directly vs via
owner, GA4 account, and final domain.

## Marketing strategy scouting (2026-07-18)
Full report: outputs/casa-montana/research/marketing-strategije-2026-07-18.md
(scouting only, not a final plan — owner to pick 4-6 strategies). Firecrawl
spend: 6 credits (997→991), well under 15-25 budget; rest of research via
free WebSearch. Key findings worth remembering:
- **Villa Prive and Spa** (Casa Montana's closest named competitor per
  J2Ski) has NO confirmed own branded website — only a white-label OTA
  directory page (visitaserbia.com), relies entirely on Booking/Airbnb/
  directories. This is Casa Montana's biggest identified local gap: a real
  branded site (already planned) is a differentiator the moment it launches.
- **Kežman Mountain Houses** is the most sophisticated local competitor:
  own professional site, "Be direct with us" newsletter capture + seasonal
  book-direct promo codes (Black Friday, Early Bird) on the homepage,
  active weekly Instagram Reels embedded live on-site, ~8.5K IG followers.
  Worth studying their book-direct mechanic when Casa Montana's site goes
  live — see [[casa-montana-marketing-research]] for full breakdown.
- Global leaders (Firefly Collection, Oxford Ski Company, Consensio
  Chalets) are agency/portfolio operators (700-1000+ properties, decades
  of staff) — their scale tactics (press walls, concierge teams, loyalty
  programs) are NOT realistically transferable to a single house; only the
  underlying principle (sell the experience/trust, not the bed; one clear
  "why book direct" message) transfers in miniature.
- Global STR/Airbnb tactical layer (WebSearch only, no scrape): 3-5 Reels/
  week focused on the DESTINATION not the house, GBP profile is ~32% of
  local ranking weight, 20+ listing photos + amenity tagging drives Airbnb
  search visibility (flagged for the separate OTA agency, out of our
  scope), post-stay + anniversary emails are the two easiest automations
  to start an email list with.

## Conversion insights
[cro agent logs A/B test results and winning variants here]

## Ad performance notes
[paid-ads agent logs what's working and what isn't here]

## Email metrics
[email agent tracks open rates, sequence performance here]

## Analytics baselines
[analytics agent records key metric benchmarks here]

## ⏸ PAUSED (2026-07-30) — GSC/GA4 access for Casa Montana not yet connected
Marko verified `https://casamontana.rs/` in GSC himself (his own Google
login, via the "Google Analytics" method once Wave-1's gtag went live). But
the `google-seo-mcp` tool Claude uses is authenticated as a **service
account** scoped only to SensiSkin (`claude-gsc@sensiskin-analytics.iam.
gserviceaccount.com`) — so `gsc_list_sites`/`ga4_list_properties` don't see
Casa Montana yet, and Marko does NOT want to just add that same service
account to Casa Montana (reusing one identity across clients would make any
active-client switching meaningless — it'd see both always, regardless of
which credential file is "active"). Agreed plan: Marko creates a SEPARATE
GCP service account (in the same `sensiskin-analytics` GCP project, which is
just an IAM container, not a data-mixing risk) dedicated to Casa Montana,
grants it access on Casa Montana's GSC + GA4, sends Claude the JSON key —
then Claude repoints the MCP's env var at a neutral `active-gsc-sa.json`
path and copies the right client's key into it + calls `reload_credentials`
every time the active client changes. Full plan + exact steps: personal
memory `casa-montana-gsc-per-client-setup.md` (not in this repo). Explicitly
shelved for now — Marko wants to work on other Casa Montana things first.
DO NOT add the SensiSkin service account to Casa Montana's GSC/GA4 as a
shortcut — that defeats the whole point, revisit this note instead.

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

## Brand voice script konstruisan (2026-07-31)
Corpus research (research agent, 43 stranice, 64 kredita) + sinteza (glavna sesija) → `brand-voice-script.md` + `references/voice-corpus-analysis-2026-07.md`. Postojeći sajt copy je već većinom na glasu; samo 2-3 sitne ispravke (ponovljeno "bez kompromisa", činjenica umešana u atmosferski pasus). Sloj B (regionalni jezički most) NIJE ispunio svrhu — Vila Planinka čitana na engleskom, ne slovenačkom; ponoviti pre sledeće velike copy runde ako treba jači dokaz za srpsku adaptaciju.

## Homepage copy rewrite (2026-07-31) — PR #2, OPEN, nije merge-ovan
Marko i vlasnik: postojeći sajt copy "previše AI, razbacano, bez strukture". Dijagnoza: ista negacija-figura ("X nije, ovo je Y") ponovljena 3x (hero/intro/story) bez napretka, "katalog" 2x, "bez kompromisa"/"no compromises" 2x — tačno greška koju je istraživanje flagovalo kod konkurenta. Popravka (SR+EN sinhronizovano): figura ostaje SAMO u intro.statement; svaka sekcija sad nosi NOVU informaciju (hero=dolazak+izolacija, intro=greda+"poslednja kuća pre šume", story=zanat, location=pristup+privatnost); "bez kompromisa" zamenjeno konkretnim detaljem (bez komšijske kuće na vidiku); "kuhinja opremljena" (gola činjenica u atmosferskom pasusu) zamenjeno scenom (kuvanje večere za ceo sto); hero.scroll "nekretninu"→"kuću". Netaknuto namerno: Trust citat (pravi gost review), Book CTA (već dobar model), Closer, title/meta/OG/schema (SEO iz Wave 1, van obima). `npm run build` prošao, grep potvrdio 0 ostataka klišea. Branch `copy/brand-voice-rewrite` → PR #2 https://github.com/ognjenzekovic/casa-montana/pull/2, ognjenzekovic reviewer, NE MERGE-OVATI bez odobrenja.
2026-07-31 (isti dan, nastavak) | PR #2 PROŠIREN 2. commit-om — vlasnik odbio prvi patch kao "nedovoljan", tražio pun "kao da ne postoji tekst" rewrite u chatu. Iterirano uživo: (1) "chalet u Alpima, ali na Kopaoniku" TRAJNO POVUČENA — vlasniku se ne sviđa, ne koristiti nigde ubuduće (GBP ostaje netaknut, videti "Brand voice reminders" gore i brand-voice-script.md #13); (2) Hero POJEDNOSTAVLJEN na JEDNU činjeničnu rečenicu — vlasnik eksplicitno odbio poetske dodatke ("previše je lupati gluposti da bi rečenica izgledala bolje") — ubuduće: hero ostaje faktičan, ne "ulepšavati" veštački; (3) Story koristi Varijantu B — uvodi "potok" prvi put na sajtu (pravi detalj iz Trust gost-citata, stvara odjek umesto izolovanog pominjanja). VAŽNA ČINJENIČNA ISPRAVKA (ne stilska): "10 minuta od Nacionalnog parka" bilo POGREŠNO svuda (vlasnik potvrdio, stvarno je 5 minuta) — ispravljeno na SVIH 7 mesta uključujući već live Wave 1 SEO tekst (SR+EN meta description, SR+EN Location naslov, index.html meta/og/JSON-LD). Ovo je bila neotkrivena greška iz Wave 1 revizije. `npm run build` prošao, grep potvrdio 0 ostataka "10/deset minuta". I dalje isti PR #2, i dalje NE MERGE-OVATI bez odobrenja.
