# Stojanov Auto — Shared Agent Memory

This file is read and updated by all agents working on this client. 
It acts as the project's persistent memory across sessions.

## Last updated
2026-08-05 — discovery + baseline general audit complete

## Client snapshot
Stojanov Auto DOO — authorized Renault / Dacia / Nissan dealer + service centre.
Zrenjaninski put 12, Novi Sad. Full chain on one site: new/used/commercial sales,
authorized service, technical inspection + registration, tyre hotel, 24h towing.
Stack: WordPress + Elementor Pro, Rank Math SEO, Redirection, CF7 + Forminator.

## Onboarding status
- [x] Client folder created (`.agents/clients/stojanov-auto/`)
- [x] Output folder created (`outputs/stojanov-auto/`)
- [x] Set as active client
- [x] WP admin verified working (REST 200, `*_STOJANOVAUTO` keys in `.env`)
- [x] product-marketing.md filled from discovery
- [x] General/baseline audit → `outputs/stojanov-auto/2026-08-05-generalni-audit-baseline.md`
- [ ] Google Business Profile audit — NOT DONE, likely the #1 channel, do next
- [ ] Full SEO audit (run seo-audit skill on top of this baseline)
- [ ] GSC access — client said not yet (2026-08-05)
- [ ] GA4 access — client said not yet (2026-08-05). GA4 already installed: G-SFXW7G5GZC

## Known constraints
- No GSC/GA4 access — client explicitly deferred it 2026-08-05. Prioritization is
  therefore by size-of-problem, not size-of-loss (~50-55% of full audit value).
  Technical + on-page layers unaffected.
- `serp_check` unusable — no DataForSEO credentials in the MCP server.
- PageSpeed Insights API hit its daily quota on 2026-08-05 (429) — CWV never measured.
- `.env` uses SUFFIXED keys for this client (`WP_SITE_URL_STOJANOVAUTO` etc.), but the
  `wordpress-edit` skill reads UNSUFFIXED names (`WP_SITE_URL`...). Must be resolved
  before running that skill against Stojanov Auto or it will edit SensiSkin by mistake.

## Baseline audit — headline findings (2026-08-05)
Score 4/10. Site is technically sound but marketing-inert.
1. No title tag on the site contains "Novi Sad" — local intent entirely untargeted,
   while autocomplete shows strong local demand + named competitors (Wolf, S&G tim,
   Atlas, Autokomerc).
2. Homepage has zero H1. Title is "STOJANOV AUTO - Stojanov Auto".
3. Schema is bare `Organization`, not `AutoDealer`/`AutoRepair`. `addressLocality`
   missing, no opening hours, no telephone, no ratings. Bogus `Article` schema on pages.
4. Duplicates: `/polovna-vozila/` vs `/prodaja/polovna-vozila/`; `/naslovna-old/`
   and `/akcije-old/` still indexed and in sitemap.
5. No per-vehicle pages — entire stock on one 378 KB page. Zero long-tail capture.
6. No prices published anywhere, though "cena" is the top local query modifier.
7. Dead Universal Analytics (UA-179394377-1) still loading.
8. ~50% of images missing alt (homepage: 80 of 104).
9. All 16 AI bots allowed (good) but no llms.txt and nothing citable on the site.

## Key decisions made
2026-08-05 | Onboard Stojanov Auto BEFORE running the full SEO audit — client's call,
  and correct: an SEO audit without positioning context yields generic recommendations.
2026-08-05 | Do not request GSC/GA4 access yet — client deferred. Proceed with the
  ~55% that does not depend on it; revisit prioritization when access lands.

## Completed tasks log
2026-08-05 | claude | Discovery + baseline general audit | 2026-08-05-generalni-audit-baseline.md | saved to /outputs/stojanov-auto/

## SEO targets

### Phase status
Baseline done. Proposed 4-phase remediation plan lives in the audit doc §8.
Nothing executed on the live site yet — no WP writes have been made.

### Keyword pipeline
Not yet built — needs GSC data or a paid keyword source. Interim signal from
`google_suggest` (hl=sr, gl=RS): tehnicki pregled novi sad (+cena/+radno vreme/
+najjeftiniji), slep sluzba novi sad (+cena), renault ovlasceni servis novi sad,
polovna vozila novi sad (+na kredit/+na lizing).

## Brand voice reminders
Serbian, Latin script. Expert, reliable, no hype — this is a 15-40k EUR purchase and
a safety-critical service. Concrete: prices, deadlines, opening hours, named people
with their phone numbers. Avoid marketing filler, exclamation marks, ALL-CAPS headings
(currently used), and literally translated factory slogans that mean nothing in Serbian
(e.g. "Potražite elektrificirane supermoći kod Nissan vozila").

## Analytics baselines
None recorded — no GA4/GSC access. GA4 G-SFXW7G5GZC, GTM-PCJ3KQ69, Meta Pixel active,
dead UA-179394377-1 still firing.

## Active campaigns
[agents document any live campaigns here]

## Key decisions made
[YYYY-MM-DD] | [decision summary and rationale]

## Completed tasks log
[YYYY-MM-DD] | [agent] | [task] | [output] | saved to /outputs/[client-slug]/[filename]

## Brand voice reminders
[copywriter logs approved phrasings and tone rules here]

## SEO targets

### Keyword pipeline
[seo agent logs keyword assignments, status, and rationale here]

### Phase status
[seo agent tracks which phase of SEO work is active]

## Conversion insights
[cro agent logs A/B test results and winning variants here]

## Ad performance notes
[paid-ads agent logs what's working and what isn't here]

## Email metrics
[email agent tracks open rates, sequence performance here]

## Analytics baselines
[analytics agent records key metric benchmarks here]
