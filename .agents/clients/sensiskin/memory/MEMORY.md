# SensiSkin — Shared Agent Memory

This file is read and updated by all agents. It acts as the project's 
persistent memory across sessions.

## Last updated
2026-06-09 — HydraFacial blog post written

## Active campaigns
- Local SEO re-strategy for sensiskinstudio.com (in progress).

## ▶ WHERE WE LEFT OFF (2026-06-09) — read this first next session
State: Client reviewed Phases 1 & 2, disliked Phase 2. We diagnosed it and re-prioritized for LOCAL SEO. Confirmed direction + key decisions (see "Confirmed strategic decisions" below). Delivered so far this session:
  1. /outputs/gbp-recenzije-vodic-2026-06-09.html — GBP + reviews guide (priority #1)
  2. /outputs/seo-restrategija-pregled-2026-06-09.md — half-page re-strategy overview
  3. /outputs/qr-recenzije-sensiskin-2026-06-09.png — static review QR (link: https://g.page/r/CTIeLyIMToV3EAE/review)
  4. /outputs/blog-hydrafacial-2026-06-09.md — edukativni blog post o HydraFacial tretmanu (Q&A format, ~800 words, SEO paket uključen)
Client decision: do the GBP guide IN PRACTICE first, before we write more docs.
NEXT SESSION — pick up with one of:
  - Phase B: NAP consistency + local directories cleanup (fix old "Vojvode Bojovića 5a" address; claim/fix navidiku.rs, virtualnigrad.com, mirandre.com, ordinacije.info).
  - Phase C: on-page redo (full guide replacing weak Phase 2) — correct real URLs, brand-voice title/meta, new keyword model (geo keywords only on Home/HydraFacial/Epilacija/Kontakt/O nama; thematic pages target treatment+problem).
  - Also pending: fix the GBP guide's step-4 wording (services can't hold clickable links — link pages via Google Posts instead).
Tone reminder: client is hands-on, asks "correct me if I'm wrong," prefers honest pushback over yes-manning. All deliverables in Serbian (Latin).

## Key decisions made
- 2026-06-09 | SEO re-prioritization. Client felt Phase 2 (keywords/title/meta) was weak. Confirmed: for a LOCAL business, on-page is only the ~4th biggest visibility lever. Real order: (1) Google Business Profile, (2) Reviews, (3) NAP/local citations, (4) on-page SEO, (5) local content/blog, (6) backlinks. Meta description is NOT a ranking factor (CTR only). "Yoast green" is a vanity metric.
- 2026-06-09 | GBP status = EXISTS BUT NEGLECTED (per client). Made it priority #1 — biggest untapped lever.
- 2026-06-09 | SITE STRUCTURE VERIFIED via live fetch of sensiskinstudio.com. Real page slugs (Phase 2 had guessed many WRONG):
  - Home: /
  - About: /kozmetoloski-centar-sensi-skin/
  - Magazine texts: /strucni-saveti-za-negu-koze/
  - Aura Reality: /aura-reality-3d-dijagnostika-koze/
  - Mesojet tretmani: /mesojet-tretmani/
  - Mesojet RF: /mesojet-rf/  (Phase 2 missed this)
  - Nega lica: /nega-lica/
  - HydraFacial: /hydrafacial-tretmani-lica-novi-sad/
  - Dermalux: /dermalux/
  - Epilacija: /epilacija/
  - Proizvodi: /kozmeticki-proizvodi-sensi-skin-studio/  (Phase 2 missed)
  - Blog: /saveti-za-negu-koze/
  - Kontakt: /kontakt-sensi-skin-novi-sad/
  - Cenovnik: /cenovnik-kozmetickih-tretmana-novi-sad/
- 2026-06-09 | ISSUES FOUND: (a) Ballancer Pro has NO page (only homepage H2) yet Phase 2 optimized for /ballancer-pro/ — page doesn't exist. (b) TWO near-duplicate blog sections (/saveti-za-negu-koze/ vs /strucni-saveti-za-negu-koze/) = cannibalization risk, must resolve. (c) URL slugs are ALREADY SEO-good — no need to change them. (d) Some Phase 2 meta descriptions violate brand voice (superlatives "najnagrađivaniji na svetu", "najpreciznija") — product-marketing.md forbids overclaiming.
- 2026-06-09 | BLOG SEO RULE confirmed: blog posts must NOT cannibalize service pages. Blog targets informational/question queries ("da li HydraFacial boli", "za koji tip kože", "koliko često raditi") while service page /hydrafacial-tretmani-lica-novi-sad/ targets local transactional queries ("hydrafacial Novi Sad"). Blog URL slug must differ clearly from service page slug.
- 2026-06-08 | Focus keyword for /mesojet-rf/ page: "mesojet RF Novi Sad" — chosen over "mesojet radiofrekvencija Novi Sad" because locals abbreviate RF, and competitor pages that rank use the "mesojet RF" short form. Transactional (booking) intent confirmed.
- 2026-06-08 | Title tag and meta description finalized for /mesojet-rf/ — Yoast green-light criteria met (keyword in first sentence of meta, 120–155 chars, CTA included, 50–60 char title).
- 2026-06-08 | Focus keyword for /nega-koze-sensi-skin/ page: "profesionalna nega kože Novi Sad" — chosen over "nega kože Novi Sad" (too broad/generic, high homepage-level competition) and "kozmetološki centar nega kože" (unnatural phrasing, low local search volume). "Profesionalna" qualifier narrows intent to service-seekers, not DIY skincare browsers, and matches the brand's positioning as a medical-aesthetic studio. This keyword is NOT duplicated — the homepage pipeline keyword "kozmetološki centar Novi Sad" remains available for the homepage.
- 2026-06-08 | Title tag and meta description finalized for /nega-koze-sensi-skin/ — Yoast green-light criteria met for the three elements delivered. Page requires significant content additions (minimum 300 words, images with alt text, internal and outbound links) before full Yoast green light is achievable.
- 2026-06-08 | Focus keyword for /blog/ page: "saveti za negu kože" — chosen over "blog o nezi kože" (weak search intent, people don't search for a blog, they search for advice) and "nega kože saveti Novi Sad" (awkward word order in Serbian, low natural-language match). "Saveti za negu kože" is the most natural informational query Novi Sad users type when looking for skincare guidance content. No local geo-modifier added because blog index pages target broad informational intent — adding "Novi Sad" would narrow audience and reduce reach for an already-local domain. Keyword is NOT duplicated — no other page uses this phrase.
- 2026-06-08 | Focus keyword for /proizvodi-sensi-skin-studio/ page: "dermokozmetika Novi Sad" — chosen over "kozmetički proizvodi Novi Sad" (too broad, attracts mass-market shoppers not aligned with premium studio positioning), "profesionalni proizvodi za negu kože" (too long, low search volume as exact phrase), and "prirodna kozmetika Novi Sad" (does not reflect the clinical/professional nature of studio-grade products). "Dermokozmetika" is the exact term informed consumers and professionals use for clinic-grade skincare; it attracts high-intent buyers who already understand the category and are ready to purchase or inquire. Clear commercial/transactional intent. No duplication with any assigned keyword.
- 2026-06-08 | Title tag and meta description finalized for /proizvodi-sensi-skin-studio/ — Yoast green-light criteria met for the three elements delivered. Page currently has 0 words of content and no meta description at all. Full Yoast green light requires client to add: minimum 300 words of body text, images with keyword-containing alt attributes, internal links to service pages, outbound links.
- 2026-06-08 | Phase 2 SEO Audit completed — Google search results as of June 2026 still show OLD title tags ("Kozmeticki salon i salon lepote — Sensi Skin") on all pages. Phase 2 changes have NOT yet propagated to Google index. Either: (a) changes were implemented too recently and Google has not re-crawled, or (b) changes were not saved correctly in Yoast. Client must verify in WordPress Yoast that all title tags are saved, then submit pages to GSC for re-indexing. Phase 2 honest SEO score: 5.5/10 — technically the right inputs are in, but ranking impact is ZERO until Google re-crawls and until content is added.

## Completed tasks log
- 2026-06-04 | orchestrator→copywriter | Homepage headline + subheadline | 3 variations delivered | saved to /outputs/homepage-headline-2026-06-04.md
- 2026-06-08 | SEO agent | Yoast-ready focus keyword + title tag + meta description for /mesojet-rf/ | Delivered in agent response (no file output required)
- 2026-06-08 | SEO agent | Yoast-ready focus keyword + title tag + meta description for /nega-koze-sensi-skin/ | Delivered in agent response (no file output required)
- 2026-06-08 | SEO agent | Yoast-ready focus keyword + title tag + meta description for /blog/ | Delivered in agent response (no file output required)
- 2026-06-08 | SEO agent | Yoast-ready focus keyword + title tag + meta description for /proizvodi-sensi-skin-studio/ | Delivered in agent response (no file output required)
- 2026-06-08 | SEO agent | Full Phase 2 SEO audit completed | Delivered as agent response text
- 2026-06-09 | SEO | GBP + Reviews guide (priority #1 deliverable) | covers profile optimization + systematic review generation, brand-voice templates | saved to /outputs/gbp-recenzije-vodic-2026-06-09.html
- 2026-06-09 | SEO | Re-strategy OVERVIEW (half-page, for direction confirmation) | saved to /outputs/seo-restrategija-pregled-2026-06-09.md
- 2026-06-09 | SEO | Review QR code (static, never-expires PNG) | saved to /outputs/qr-recenzije-sensiskin-2026-06-09.png | client confirmed plan: do GBP guide in practice first.
- 2026-06-09 | COPYWRITING | HydraFacial edukativni blog post | Q&A format (~800 reči), SEO paket uključen (title tag, meta opis, URL slug, 4x alt tekst) | saved to /outputs/blog-hydrafacial-2026-06-09.md

## GBP / local data (2026-06-09)
- Google listing CID (ludocid): 8612375676436028978 — permanent business ID. Feature ID hex: 0x475b11b33766c78d:0x77854e0c222f1e32.
- OFFICIAL REVIEW LINK (clean, permanent — use in SMS/email templates + QR): https://g.page/r/CTIeLyIMToV3EAE/review
- (also valid long form: https://www.google.com/search?...&ludocid=8612375676436028978&...&laa=merchant-review-solicitation)
- NAP INCONSISTENCY FOUND: current address = Braće Popović 3, but old address "Vojvode Bojovića 5a" still appears in directories (mirandre.com etc). Must fix in Phase B. Local directories to clean/claim: navidiku.rs, virtualnigrad.com, mirandre.com, ordinacije.info. Social: facebook.com/sensi.skin.studiozanegulepote (~4,237 likes), instagram.com/sensi_skin (~12k followers).
- CORRECTION logged: GBP "Services" descriptions can't hold clickable links. Link specific pages via Google Posts (button + URL), the main website field, and the booking/appointment link. (Guide wording to be fixed.)

## Confirmed strategic decisions (2026-06-09)
- NAMING: keep official business name "Sensi Skin" as-is for NAP/GBP consistency. Use word "kozmetički" (NOT "kozmetološki") in SEO copy + keywords — higher search volume in Serbia. Client preference + better SEO.
- KEYWORD MODEL: do NOT append "Novi Sad" to every page. Concentrate local/geo keywords ONLY on high-volume/high-intent pages: Home, HydraFacial, Epilacija, Kontakt, O nama. Niche/thematic pages (Nega lica, Aura Reality, Mesojet, Mesojet RF, Dermalux) target TREATMENT + PROBLEM it solves (e.g. "mezoterapija bez igala", "LED terapija za akne", "tretman za akne") — NOT "[service] Novi Sad" (near-zero volume + spammy). GBP carries local signal for those.
- BLOG: main blog /saveti-za-negu-koze/ = content hub (keep). Magazine section /strucni-saveti-za-negu-koze/ (only 3 PDF articles) = reposition as "Sensi Skin u medijima / Iz štampe" (authority signal) + transcribe PDFs to real text. Resolves cannibalization.
- PHASE ORDER (corrected): A=GBP+reviews (done), B=NAP+local directories, C=on-page redo (correct URLs, brand-voice title/meta, new keyword model), D=content, E=links.
- NEXT: deepen either Phase C (on-page redo) or Phase B (NAP/directories) — client to choose.

## Brand voice reminders
- Lead with customer frustration, not product features
- "Finally works" resonates with the disappointed-by-other-brands audience
- Empowerment framing ("Your skin isn't too sensitive") tests well vs. sympathy framing
- Avoid: "transform", "complexion", "mild" — use: "works", "skin", "gentle"
- Authority signal ("dermatologists reach for") adds credibility without overclaiming
- Blog tone: Q&A format works well — bold question as subheading, concise plain-language answer. Mirrors the owner's own writing style.
- For HydraFacial blog context: "Ovo nije reklamna fraza" is an approved device for defusing overclaiming suspicion while reinforcing credibility (e.g. "Odmah. To nije reklamna fraza — koža zaista izgleda drugačije već u ogledalu posle tretmana.")
- CTAs always end with the exact phone number in this format: "Pozovite nas na 065/333-8-338 i zakažite svoje konsultacije." — no price mentions, no discount promises.
- Never use "Novi Sad" in blog body text more than 1–2 times naturally. Blog targets informational queries, not local transactional ones.
- Brand differentiators to weave naturally into blog posts (not forced): Aura Reality 3D dijagnostika, individualan pristup (ne gotovi paketi), 20+ godina iskustva, Nataša Burka.

## SEO targets

### /proizvodi-sensi-skin-studio/ — Products page
- **Focus keyword**: dermokozmetika Novi Sad
- **Search intent**: Commercial/transactional (informed consumer or professional seeking clinic-grade skincare products available locally in Novi Sad; ready to inquire or purchase)
- **Title tag**: Dermokozmetika Novi Sad — proizvodi Sensi Skin Studio (53 karaktera) — keyword at START (Yoast requirement met)
- **Primary meta description**: Dermokozmetika Novi Sad dostupna u Sensi Skin studiju — profesionalni proizvodi za negu kože odabrani od strane stručnjaka. Posetite nas ili zakažite. (150 karaktera)
- **Status**: Delivered, pending client implementation in WordPress/Yoast
- **CRITICAL**: Page currently has 0 words of content and NO meta description at all. Full Yoast green light requires client to: write meta description in Yoast (this output), rewrite SEO title to start with exact keyword (this output), add minimum 300 words of body text, add images with keyword-containing alt attributes, add internal links to service pages, add at least one outbound link to an authoritative source, and include focus keyword in introduction, subheadings, and body text.

### /blog/ — Blog index page
- **Focus keyword**: saveti za negu kože
- **Search intent**: Informational (person seeking skincare advice, tips, education — not yet ready to book)
- **Title tag**: Stručni saveti za negu kože — Sensi Skin, Novi Sad (50 karaktera)
- **Primary meta description**: Saveti za negu kože koje zaista funkcionišu — čitajte blog Sensi Skin studija i naučite kako da brinete o koži uz stručne savete. Zakažite odmah. (145 karaktera)
- **Status**: Delivered, pending client implementation in WordPress/Yoast
- **CRITICAL**: Page currently has 0 words of content. Full Yoast green light requires client to add: minimum 300 words of body text (intro paragraph + category descriptions), images with keyword-containing alt attributes, internal links to service pages, and at least one outbound link to an authoritative skincare source.

### /mesojet-rf/ — Mesojet RF page
- **Focus keyword**: mesojet RF Novi Sad
- **Search intent**: Transactional / booking intent (person ready to book a treatment)
- **Title tag**: Mesojet RF Novi Sad tretman — Sensi Skin (43 karaktera)
  - NOTE: If Yoast requires 50–60 chars, use expanded variant: "Mesojet RF tretman u Novom Sadu — Sensi Skin" (45 chars) or "Mesojet RF Novi Sad — tretman lica bez igala" (44 chars). See full rationale in agent output 2026-06-08.
- **Primary meta description**: Mesojet RF Novi Sad tretman kombinuje radiofrekvenciju i bezigalnu mezoterapiju za vidljivo zategnuću kožu. Zakažite u Sensi Skin studiju. (151 karaktera)
- **Status**: Delivered, pending client implementation in WordPress/Yoast
- **Competitor gap**: SrediMe aggregator and BeautyTech product pages rank for "mesojet radiofrekvencija" — Sensi Skin can outrank with a properly optimized service page targeting booking intent.

### /nega-koze-sensi-skin/ — Skin care philosophy / brand page
- **Focus keyword**: profesionalna nega kože Novi Sad
- **Search intent**: Informational-with-commercial intent (person researching which studio to trust before booking; evaluating expertise and approach)
- **Title tag**: Profesionalna nega kože Novi Sad — Sensi Skin (50 karaktera)
- **Primary meta description**: Profesionalna nega kože Novi Sad uz 20+ godina iskustva. U Sensi Skin studiju tretmani su prilagođeni vašem tipu kože. Zakažite konsultaciju. (151 karaktera)
- **Status**: Delivered, pending client implementation in WordPress/Yoast
- **CRITICAL**: Page currently has 0 words of content. Full Yoast green light requires client to add: minimum 300 words of body text, images with keyword-containing alt attributes, internal links to service pages, and at least one outbound link to an authoritative source.
- **Keyword collision check**: "kozmetološki centar Novi Sad" remains UNASSIGNED — available for homepage or a dedicated about/studio page.

### Previously noted SEO priorities (from audit, jun 2026)
- Sitemap zastareo iz 2018 — Google pretražuje 21 mrtav URL — ADDRESSED in Phase 1
- Nedostaju title tagovi i meta opisi — ADDRESSED in Phase 2 (pending Google re-index)
- Nema LocalBusiness schema markupa — ADDRESSED in Phase 1
- Nema canonical tagova ni alt teksta na slikama — STILL PENDING
- Google Business Profile — status nepoznat, mora se verifikovati — STILL PENDING

### Phase 2 audit findings (June 2026)
- Google search snippets as of June 8, 2026 still display OLD title format ("Kozmeticki salon i salon lepote") on all crawled pages — Phase 2 changes NOT yet indexed
- Old title tag confirmed still visible in Google for: homepage, /epilacija/, /sensi-skin/, /kontakt/, /cenovnik-usluga-2/ and others
- Competitor landscape for "laserska epilacija Novi Sad": Vita Elos, Brana Estetik, K2 Derma, Luftika — all with dedicated content pages. SensiSkin currently not on first page.
- Competitor landscape for "kozmetoloski centar Novi Sad": Soze Beauty, Ceca Skincare, Madam In, VIVA Beauty — SensiSkin not confirmed on first page
- ZERO content on most service pages = title/meta changes cannot produce rankings without content to back them up
- Next highest-impact action: write minimum 300–500 words of real content on the top 3 pages: /hydrafacial-tretmani-lica/, /epilacija/, /nega-lica/

### Keyword targets (pipeline)
- "hydrafacial Novi Sad" — high priority, branded differentiator
- "kozmetološki centar Novi Sad" — broad local anchor (UNASSIGNED — do NOT use on /nega-koze-sensi-skin/, reserved for homepage or about page)
- "laserska epilacija Novi Sad" — high commercial intent
- "aura reality dijagnostika kože" — unique, zero competition, brand-building
- "mesojet RF Novi Sad" — ACTIVE (delivered 2026-06-08, assigned to /mesojet-rf/)
- "profesionalna nega kože Novi Sad" — ACTIVE (delivered 2026-06-08, assigned to /nega-koze-sensi-skin/)
- "saveti za negu kože" — ACTIVE (delivered 2026-06-08, assigned to /blog/)
- "dermokozmetika Novi Sad" — ACTIVE (delivered 2026-06-08, assigned to /proizvodi-sensi-skin-studio/)

## Conversion insights
[cro agent logs A/B test results and winning variants here]

## Ad performance notes
[paid-ads agent logs what's working and what isn't here]

## Email metrics
[email agent tracks open rates, sequence performance here]

## Analytics baselines
[analytics agent records key metric benchmarks here]
