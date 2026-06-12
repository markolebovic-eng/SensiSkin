# SensiSkin — Shared Agent Memory

This file is read and updated by all agents. It acts as the project's 
persistent memory across sessions.

## Last updated
2026-06-12 — Social copy delivered: HydraFacial pre/posle Instagram + Facebook post (Nataša's voice). Article schema resolved via SASWP. See notes below.

## ▶ ARTICLE SCHEMA — SASWP (2026-06-12, RESOLVED)
Site uses TWO schema plugins simultaneously: **Yoast SEO** (handles service pages) and **SASWP** (Schema & Structured Data for WP & AMP, handles blog posts + navigation). This was the root cause of 0/29 Article schema on blog posts despite Yoast "Article type" being set correctly — SASWP was overriding Yoast output on posts.
FIX APPLIED: Configured SASWP → Add New Schema → Article → assigned to Post type. Verified: Article schema now appears on ALL blog posts (confirmed via validator.schema.org and page source).
IMPORTANT FOR FUTURE AGENTS: Do NOT tell user to configure Article schema in Yoast for blog posts. SASWP handles schema for posts. Yoast Custom Schema field still works for service pages (Pages post type). Manual JSON-LD in /outputs/sensiskin/03-geo-audit/blog-article-json-svi-postovi-2026-06-11.md is now OBSOLETE — do not use (would duplicate SASWP output).
STATUS: Article schema = ✅ LIVE on all 29 blog posts as of 2026-06-12.

## ▶ BLOG CRAWL CORRECTION (2026-06-11) — read with re-audit
Full crawl of all ~29 existing blog posts (initial re-audit only crawled the hub + 2 articles). Findings: site has ~30 quality educational posts (serum, hemijski pilinzi, melazma, rozacea, vrste akni, menopauza, predeo oko ociju, stetnost solarijuma, tipovi koze, dnevna rutina, alopecija…), each ~700–1700 body words. BUT: 0/29 have Article/BlogPosting schema, only 2/29 have FAQPage, 0/29 have datePublished in schema. => Topical authority corrected 4→7/10; Schema 8→7/10; overall 62→64. NEW HIGH-PRIORITY ACTION: bulk-add Article + datePublished/dateModified + author(Nataša Burka) schema to all ~30 posts (Yoast global "Post" type), FAQPage where Q&A exists. Content already exists — only markup missing.

## ▶ RE-AUDIT FINDINGS (2026-06-11, verified live via Chrome --dump-dom)
VERIFIED FIXED: robots.txt open to all AI bots (GPTBot/ClaudeBot/PerplexityBot/Google-Extended not blocked); on-site NAP consistent (Braće Popović everywhere, no Vojvode Bojovića); schema live = home(MedicalOrganization+WebSite+BeautySalon+ContactPoint), HydraFacial(FAQPage 7Q+Service), Epilacija(FAQPage 4Q+Service), Nega lica(Service+OfferCatalog), Mesojet RF/Dermalux(Service), O nama(Person — Nataša Burka), sve-istine-o-laserskoj-epilaciji(Article+FAQPage+LocalBusiness+Person+WebPage = best page); service pages now have real content.
STILL NOT DONE: (1) 🔴 blog "razlika-profesionalna-i-drogerijska-kozmetika" returns 404 — NOT published yet (text ready, just not posted). (2) FAQ/FAQPage missing on Nega lica, Mesojet RF, Dermalux, (Aura Reality unchecked). (3) No AggregateRating/Review schema anywhere. (4) No BreadcrumbList. (5) /strucni-saveti-za-negu-koze/ duplicate still live (cannibalization). (6) No HowTo.
NOT VERIFIABLE FROM SITE CRAWL: off-site directory NAP (Faza B), GBP, Luftika/SrediMe, real AI citations (need re-crawl, measure in 3–6 weeks).
Per-dimension scores: AI vis 5/10, content 7, schema 8, E-E-A-T 6, topical 4, citability 5, technical 8, local 5.

## Last updated (prior)
2026-06-10 — GEO audit (2-phase) + complete JSON-LD schema for all 48 URLs delivered. Blog post body copy for "razlika profesionalna i drogerijska kozmetika" written (copywriter). Keyword #13 status updated to COPY WRITTEN.

## Active campaigns
- Local SEO re-strategy for sensiskinstudio.com (in progress).
- GEO/AI search optimization: schema layer being implemented.

## ▶ WHERE WE LEFT OFF (2026-06-10) — read this first next session
State: Complete JSON-LD schema code delivered for ALL pages on sensiskinstudio.com. Ready to paste into Yoast Custom Schema fields. GEO audit identified dual sitemap as critical issue (owner may have already fixed this).
Delivered so far (all sessions):
  1. /outputs/gbp-recenzije-vodic-2026-06-09.html — GBP + reviews guide (priority #1)
  2. /outputs/seo-restrategija-pregled-2026-06-09.md — half-page re-strategy overview (PRIOR VERSION, kept)
  3. /outputs/qr-recenzije-sensiskin-2026-06-09.png — static review QR (link: https://g.page/r/CTIeLyIMToV3EAE/review)
  4. /outputs/blog-hydrafacial-2026-06-09.md — edukativni blog post o HydraFacial tretmanu (Q&A format, ~800 words, SEO paket uključen)
  5. /outputs/sensiskin/seo-restrategija-2026-06-09.md — full SEO re-strategy v2.0
  6. /outputs/sensiskin/merenje-gsc-uputstvo-2026-06-09.md — measurement & verification playbook for Phase B/C
  7. /outputs/sensiskin/faza-c-onpage-schema-uputstvo-2026-06-09.md — Phase C execution playbook
  8. /outputs/sensiskin/faza-b-nap-direktorijumi-uputstvo-2026-06-09.md — Phase B NAP playbook
  9. /outputs/sensiskin/faza-c-sadrzaj-top3-strane-2026-06-09.md — kompletni body copy za 3 prioritetne stranice (/hydrafacial/, /epilacija/, /nega-lica/)
  10. /outputs/sensiskin/blog-kucna-nega-SEO-brief-2026-06-09.md — SEO brief za blog post keyword #13
  11. /outputs/sensiskin/blog-kucna-nega-vs-profesionalna-2026-06-09.md — blog post body copy za keyword #13 (~960 reči, Yoast-ready)
  12. /outputs/sensiskin/geo-audit-izvestaj-2026-06-09.md — GEO audit phase 1 (WebSearch based)
  13. /outputs/sensiskin/geo-crawl-audit-2026-06-09.md — GEO deep crawl audit (direct fetch, definitive)
  14. /outputs/sensiskin/json-ld-schema-kompletno-2026-06-10.md — KORISTITI OVAJ: kompletan JSON-LD schema za svih 48 URL-ova (stariji json-ld-schemas- fajl ima pogrešan Aura Reality URL)
Client decision: do the GBP guide IN PRACTICE first, before we write more docs.
NEXT SESSION — pick up with:
  - OWNER ACTION (SCHEMA — HIGHEST PRIORITY): Paste JSON-LD schemas from /outputs/sensiskin/json-ld-schema-kompletno-2026-06-10.md into Yoast Custom Schema. Order: (1) Yoast Knowledge Graph settings, (2) Početna strana, (3) HydraFacial, (4) Epilacija, (5) Aura Reality, (6) Kontakt, (7) Tim, (8) Mesojet RF, (9) Mesojet tretmani, (10) Dermalux, (11) Cenovnik, (12) 5 blog FAQPage posts.
  - OWNER ACTION (Phase B): Execute directory cleanup — mirandre.com, navidiku.rs, ordinacije.info, virtualnigrad.com, Apple Business, Bing Places, 011info.com, planplus.rs. Playbook: /outputs/sensiskin/faza-b-nap-direktorijumi-uputstvo-2026-06-09.md.
  - OWNER ACTION (Phase C — UNBLOCKED): Implement body copy from /outputs/sensiskin/faza-c-sadrzaj-top3-strane-2026-06-09.md into WordPress. Priority: HydraFacial → Epilacija → Nega lica. Use Yoast FAQ blok for FAQ sections.
  - OWNER ACTION (Phase D — UNBLOCKED): Implement blog post from /outputs/sensiskin/blog-kucna-nega-vs-profesionalna-2026-06-09.md into WordPress under /saveti-za-negu-koze/.
  - OWNER ACTION: Request indexing in GSC for each changed page after content is added.
  - CONFIRMED DONE (owner confirmed): FAQPage schema for /sve-istine-o-laserskoj-epilaciji/ already added via Yoast Custom Schema.
  - Also pending: fix the GBP guide's step-4 wording (services can't hold clickable links — use Google Posts instead). HTML guide still needs edit.
  - PENDING FROM OWNER: baseline snapshot capture.
Tone reminder: client is hands-on, asks "correct me if I'm wrong," prefers honest pushback over yes-manning. All deliverables in Serbian (Latin).

## Key decisions made
- 2026-06-09 | PHASE B PLAYBOOK DELIVERED. Live research confirmed: mirandre.com has "Vojvode Bojovića 5a" (listing URL: /kozmeticki-salon-sensi-skin). navidiku.rs has staru adresu + poseban URL podlistinga sa starom adresom. ordinacije.info listing + blog postovi imaju staru adresu. virtualnigrad.com listing nepoznat + blog post iz 2021 ima staru adresu. 011info.com, Apple Maps, Bing Places: ne postoje listinzi — treba kreirati. Playbook pokriva 13 platformi, redosled izvršenja po danima, tabelu za praćenje, definiciju "gotovo". Saved to /outputs/sensiskin/faza-b-nap-direktorijumi-uputstvo-2026-06-09.md.
- 2026-06-09 | PHASE C DELIVERED. Full execution playbook at /outputs/sensiskin/faza-c-onpage-schema-uputstvo-2026-06-09.md. Covers: (1) 12-page work-order with priority ranking; (2) all keyword/title/meta in Yoast-ready Serbian format; (3) step-by-step Yoast entry instructions; (4) LocalBusiness JSON-LD block (HealthAndBeautyBusiness, real NAP pre-filled), Service schema, FAQPage (Yoast FAQ blok), BreadcrumbList setup; (5) 3 content briefs for copywriter; (6) hub-and-spoke internal linking map; (7) Phase C "done" checklist + 8-week GSC success metrics. All Phase 2 errors corrected (superlatives removed, "Novi Sad" geo rule enforced, real slugs used).
- 2026-06-09 | PHASE C BODY COPY WRITTEN. All 3 service pages written per briefs. Word counts: /hydrafacial/ ~405 reči, /epilacija/ ~410 reči, /nega-lica/ ~455 reči. All within brief targets. Each page has: H1 with focus keyword (verbatim, nominative), H2 structure matching brief, 5 FAQ items (/hydrafacial/, /epilacija/) and 4 FAQ items (/nega-lica/) as Yoast-ready blocks, CTA with exact phone number format, internal link tables with descriptive anchor text. Saved to /outputs/sensiskin/faza-c-sadrzaj-top3-strane-2026-06-09.md.
- 2026-06-09 | COPYWRITING DECISIONS: (a) Transactional angle for /hydrafacial/ clearly separated from blog post angle — service page focuses on "ovlašćeni studio, dijagnostika pre tretmana, protokol prilagođen Vašoj koži", blog covers educational "šta je, kako radi, za koji tip kože". No content duplication. (b) Competitor positioning on /epilacija/ done indirectly — "standardni protokol koji svi rade na isti način" frames differentiation without naming rivals. (c) Aura Reality 3D dijagnostika appears on all 3 pages but in different contexts — not as a forced badge. (d) "20+ godina iskustva" appears only on /epilacija/ (most natural context: protocol oversight by Nataša Burka) — not on all three pages to avoid badge-nabbing. (e) /nega-lica/ contains zero instances of "Novi Sad" in body text — GBP carries local signal as planned.
- 2026-06-09 | KEYWORD MODEL FINALIZED (replaces Phase 2 partial/incorrect assignments). GEO keywords on geo pages only. Thematic pages get treatment+problem keywords. Full assignment table in SEO targets section below.
- 2026-06-09 | SEO RE-STRATEGY UPGRADED to v2.0 (/outputs/sensiskin/seo-restrategija-2026-06-09.md). Revision, not rewrite. Kept: phase A–E model, ranking-lever order, geo-vs-thematic keyword logic + both keyword tables, "Potvrđene odluke". FIXED: "kozmetički" not "kozmetološki" in copy/keywords; added missing real slugs (Proizvodi /kozmeticki-proizvodi-sensi-skin-studio/, Mesojet RF /mesojet-rf/); flagged Ballancer Pro has NO page (don't optimize); GBP "Services" can't hold links (use Google Posts); NAP old address "Vojvode Bojovića 5a" must be corrected. Decided to KEEP existing slugs unchanged (incl. /kozmetoloski-centar-sensi-skin/) to avoid losing ranking — "kozmetički" goes in title/meta/body, not the slug. ADDED (gaps filled): schema layer (LocalBusiness/Service/FAQPage/BreadcrumbList/AggregateRating per page), AEO/GEO AI-search section, per-phase KPIs, concrete Phase B directory list + NAP block, FAQ angle, internal-linking plan, timeline/effort estimate.
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
- 2026-06-09 | BLOG KEYWORD #13 ASSIGNED: keyword "razlika profesionalna i drogerijska kozmetika" → slug /saveti-za-negu-koze/razlika-profesionalna-i-drogerijska-kozmetika/ | INFORMATIONAL intent | no geo modifier | no cannibalization with any of 12 service/hub page keywords | SEO brief delivered to copywriter at /outputs/sensiskin/blog-kucna-nega-SEO-brief-2026-06-09.md
- 2026-06-09 | BLOG POST #13 BODY COPY WRITTEN. ~960 reči (body), 6x FAQ Yoast-ready blok, 5x interni link sa anchor tekstom, 4x alt tekst predlog. SEO paket na vrhu fajla. Saved to /outputs/sensiskin/blog-kucna-nega-vs-profesionalna-2026-06-09.md.
- 2026-06-08 | Focus keyword for /mesojet-rf/ page: "mesojet RF Novi Sad" — chosen over "mesojet radiofrekvencija Novi Sad" because locals abbreviate RF, and competitor pages that rank use the "mesojet RF" short form. Transactional (booking) intent confirmed.
- 2026-06-08 | Title tag and meta description finalized for /mesojet-rf/ — Yoast green-light criteria met (keyword in first sentence of meta, 120–155 chars, CTA included, 50–60 char title).
- 2026-06-08 | Focus keyword for /nega-koze-sensi-skin/ page: "profesionalna nega kože Novi Sad" — chosen over "nega kože Novi Sad" (too broad/generic, high homepage-level competition) and "kozmetološki centar nega kože" (unnatural phrasing, low local search volume). "Profesionalna" qualifier narrows intent to service-seekers, not DIY skincare browsers, and matches the brand's positioning as a medical-aesthetic studio. This keyword is NOT duplicated — the homepage pipeline keyword "kozmetološki centar Novi Sad" remains available for the homepage.
- 2026-06-08 | Title tag and meta description finalized for /nega-koze-sensi-skin/ — Yoast green-light criteria met for the three elements delivered. Page requires significant content additions (minimum 300 words, images with alt text, internal and outbound links) before full Yoast green light is achievable.
- 2026-06-08 | Focus keyword for /blog/ page: "saveti za negu kože" — chosen over "blog o nezi kože" (weak search intent, people don't search for a blog, they search for advice) and "nega kože saveti Novi Sad" (awkward word order in Serbian, low natural-language match). "Saveti za negu kože" is the most natural informational query Novi Sad users type when looking for skincare guidance content. No local geo-modifier added because blog index pages target broad informational intent — adding "Novi Sad" would narrow audience and reduce reach for an already-local domain. Keyword is NOT duplicated — no other page uses this phrase.
- 2026-06-08 | Focus keyword for /proizvodi-sensi-skin-studio/ page: "dermokozmetika Novi Sad" — chosen over "kozmetički proizvodi Novi Sad" (too broad, attracts mass-market shoppers not aligned with premium studio positioning), "profesionalni proizvodi za negu kože" (too long, low search volume as exact phrase), and "prirodna kozmetika Novi Sad" (does not reflect the clinical/professional nature of studio-grade products). "Dermokozmetika" is the exact term informed consumers and professionals use for clinic-grade skincare; it attracts high-intent buyers who already understand the category and are ready to purchase or inquire. Clear commercial/transactional intent. No duplication with any assigned keyword.
- 2026-06-08 | Title tag and meta description finalized for /proizvodi-sensi-skin-studio/ — Yoast green-light criteria met for the three elements delivered. Page currently has 0 words of content and no meta description at all. Full Yoast green light requires client to add: minimum 300 words of body text, images with keyword-containing alt attributes, internal links to service pages, outbound links.
- 2026-06-08 | Phase 2 SEO Audit completed — Google search results as of June 2026 still show OLD title tags ("Kozmeticki salon i salon lepote — Sensi Skin") on all pages. Phase 2 changes have NOT yet propagated to Google index. Either: (a) changes were implemented too recently and Google has not re-crawled, or (b) changes were not saved correctly in Yoast. Client must verify in WordPress Yoast that all title tags are saved, then submit pages to GSC for re-indexing. Phase 2 honest SEO score: 5.5/10 — technically the right inputs are in, but ranking impact is ZERO until Google re-crawls and until content is added.

## Completed tasks log
- 2026-06-12 | SOCIAL (skills: social, copywriting) | HydraFacial pre/posle — Instagram + Facebook post | Nataša Burka's first-person voice; Instagram: scroll-stopping hook, Aura Reality 3D dijagnostika angle, fair-balance on home care, 5 branded/local hashtags, 2x Stories frames; Facebook: longer "why" format covering vortex mechanism, home care fair-balance, ovlašćeni studio + dijagnostika both woven in, full explanation of personalization protocol; approved credibility device used once per post; CTA exact format; no superlatives, no price mentions, "Novi Sad" appears once per post naturally | saved to /outputs/sensiskin/09-social/hydrafacial-pre-posle-social-2026-06-12.md
- 2026-06-10 | SEO (skills: schema, ai-seo) | JSON-LD schema KOMPLETNO v2 | Fresh sitemap crawl: 14 stranica + 34 blog posta = 48 URL-ova. KRITIČAN ISPRAVAK: Aura Reality URL bio /aura-reality/ (POGREŠNO) — tačno je /aura-reality-3d-dijagnostika-koze/. Nijedno "already done" schema nije live na sajtu (sve 4 verifikovane URL-ove vraćaju NO JSON-LD). 5 blog FAQPage schema napisano sa verbatim Q&A (Ballancer Pro, Serum, Melazma, Tretmani pre/posle letovanja, Nega lica+kozmetičar). Article schema šablon + tabela za svih 29 Article-only postova. Cenovnik ItemList schema sa 13 tretmana i cenama. SEO meta tabela za svih 34 blog posta (focus keyphrase + meta opis). | saved to /outputs/sensiskin/json-ld-schema-kompletno-2026-06-10.md (KORISTITI OVAJ — stariji fajl json-ld-schemas- ima pogrešan Aura Reality URL)
- 2026-06-09 | SEO (skills: seo-audit, ai-seo) | GEO audit — 2 faze: broad research + deep crawl | KRITIČNI NALAZI: (1) Dual sitemap — /sitemap.xml ima 23 mrtva URL-a sa starog sajta, /sitemap_index.xml je Yoast sa aktuelnim sadržajem. (2) FAQPage schema potpuno nedostaje na svim stranicama sa FAQ sadržajem. (3) Blogs nema Article schema. GEO score: 21/100. | saved to /outputs/sensiskin/geo-audit-izvestaj-2026-06-09.md + /outputs/sensiskin/geo-crawl-audit-2026-06-09.md
- 2026-06-04 | orchestrator→copywriter | Homepage headline + subheadline | 3 variations delivered | saved to /outputs/homepage-headline-2026-06-04.md
- 2026-06-08 | SEO agent | Yoast-ready focus keyword + title tag + meta description for /mesojet-rf/ | Delivered in agent response (no file output required)
- 2026-06-08 | SEO agent | Yoast-ready focus keyword + title tag + meta description for /nega-koze-sensi-skin/ | Delivered in agent response (no file output required)
- 2026-06-08 | SEO agent | Yoast-ready focus keyword + title tag + meta description for /blog/ | Delivered in agent response (no file output required)
- 2026-08 | SEO agent | Yoast-ready focus keyword + title tag + meta description for /proizvodi-sensi-skin-studio/ | Delivered in agent response (no file output required)
- 2026-06-08 | SEO agent | Full Phase 2 SEO audit completed | Delivered as agent response text
- 2026-06-09 | SEO | GBP + Reviews guide (priority #1 deliverable) | covers profile optimization + systematic review generation, brand-voice templates | saved to /outputs/gbp-recenzije-vodic-2026-06-09.html
- 2026-06-09 | SEO | Re-strategy OVERVIEW (half-page, for direction confirmation) | saved to /outputs/seo-restrategija-pregled-2026-06-09.md
- 2026-06-09 | SEO | Review QR code (static, never-expires PNG) | saved to /outputs/qr-recenzije-sensiskin-2026-06-09.png | client confirmed plan: do GBP guide in practice first.
- 2026-06-09 | COPYWRITING | HydraFacial edukativni blog post | Q&A format (~800 reči), SEO paket uključen (title tag, meta opis, URL slug, 4x alt tekst) | saved to /outputs/blog-hydrafacial-2026-06-09.md
- 2026-06-09 | SEO (skills: seo-audit, directory-submissions, site-architecture, schema, ai-seo) | REVISED + upgraded SEO re-strategy to full v2.0 | fixed kozmetički/slugs/Ballancer/GBP-links/NAP; added schema layer, AEO/GEO, per-phase KPIs, directory list + NAP block, FAQ angle, internal-linking plan, timeline | saved to /outputs/sensiskin/seo-restrategija-2026-06-09.md (prior version /outputs/seo-restrategija-pregled-2026-06-09.md kept)
- 2026-06-09 | ANALYTICS | Measurement & verification playbook for Phase B/C | GSC step-by-step, GBP Insights guide, monthly tracking table, NAP verification, schema validation (Rich Results Test), AEO/GEO monthly check (ChatGPT/Perplexity/Google AI Overviews), baseline snapshot instructions | saved to /outputs/sensiskin/merenje-gsc-uputstvo-2026-06-09.md
- 2026-06-09 | SEO (skills: seo-audit, schema) | PHASE C EXECUTION PLAYBOOK delivered | 12-page keyword/title/meta assignments, WordPress/Yoast entry instructions, LocalBusiness JSON-LD block, Service/FAQPage/BreadcrumbList schema guide, 3 content briefs (HydraFacial/Epilacija/Nega lica), hub-and-spoke internal linking map, Phase C "done" checklist + 8-week GSC success metrics | saved to /outputs/sensiskin/faza-c-onpage-schema-uputstvo-2026-06-09.md
- 2026-06-09 | SEO (skill: directory-submissions) | PHASE B EXECUTION PLAYBOOK | NAP konzistentnost + cleanup starih direktorijuma — korak-po-korak za vlasnika koji izvršava sam | Live research potvrdio staru adresu na: mirandre.com, navidiku.rs, ordinacije.info, virtualnigrad.com (blog post) | Pokriva: kanonski NAP blok, 5 Google pretraga za audit, 8 direktorijuma + Apple/Bing + socijalne mreže, redosled po danima (3 dana), 13-stavčanu tracking tabelu, definiciju "gotovo" + KPI | saved to /outputs/sensiskin/faza-b-nap-direktorijumi-uputstvo-2026-06-09.md
- 2026-06-09 | COPYWRITING | Phase C body copy — top 3 service pages | /hydrafacial/ (~405 reči), /epilacija/ (~410 reči), /nega-lica/ (~455 reči) | All pages: H1+H2 structure per brief, FAQ blokovi (5/5/4 pitanja), CTA sa tačnim formatom telefona, tabele internih linkova sa anchor tekstovima | No content duplicated from blog post | saved to /outputs/sensiskin/faza-c-sadrzaj-top3-strane-2026-06-09.md
- 2026-06-09 | SEO (skill: seo-audit) | BLOG SEO BRIEF — "razlika profesionalna i drogerijska kozmetika" | keyword #13 assigned, slug confirmed, H2 structure (5 odeljaka), 6x FAQ, 5x interni link, word count 850–1000 reči | No cannibalization confirmed vs. all 12 service/hub keywords | Predan copywriteru | saved to /outputs/sensiskin/blog-kucna-nega-SEO-brief-2026-06-09.md
- 2026-06-09 | COPYWRITING | BLOG POST — "razlika profesionalna i drogerijska kozmetika" | Owner's authentic voice (Nataša Burka), ~960 reči body + 6x FAQ Yoast-ready blok + 5x interni link sa anchor tekstom + 4x alt tekst predlog + SEO paket | No superlatives, no overclaiming, fair treatment of home care role, all brief H2s followed, focus keyword in H1 + first paragraph, "Novi Sad" appears once naturally, Aura Reality + individualan pristup woven in (not forced), CTA with exact phone number | saved to /outputs/sensiskin/blog-kucna-nega-vs-profesionalna-2026-06-09.md

## GBP / local data (2026-06-09)
- Google listing CID (ludocid): 8612375676436028978 — permanent business ID. Feature ID hex: 0x475b11b33766c78d:0x77854e0c222f1e32.
- OFFICIAL REVIEW LINK (clean, permanent — use in SMS/email templates + QR): https://g.page/r/CTIeLyIMToV3EAE/review
- (also valid long form: https://www.google.com/search?...&ludocid=8612375676436028978&...&laa=merchant-review-solicitation)
- NAP INCONSISTENCY FOUND: current address = Braće Popović 3, but old address "Vojvode Bojovića 5a" still appears in directories (mirandre.com etc). Must fix in Phase B. Local directories to clean/claim: navidiku.rs, virtualnigrad.com, mirandre.com, ordinacije.info. Social: facebook.com/sensi.skin.studiozanegulepote (~4,237 likes), instagram.com/sensi_skin (~12k followers).
- PASTE-READY NAP BLOCK (canonical, use verbatim everywhere): "Sensi Skin / Braće Popović 3, sprat 2, stan 12, 21000 Novi Sad, Srbija / Telefon: 065/333-8-338 (+381 65 333 8338) / Email: sensistudio@gmail.com / Sajt: https://sensiskinstudio.com"
- CORRECTION logged: GBP "Services" descriptions can't hold clickable links. Link specific pages via Google Posts (button + URL), the main website field, and the booking/appointment link. (Guide wording to be fixed — documented in strategy doc; HTML guide itself still pending edit.)

## Phase B — NAP / Directory Status (as of 2026-06-09)
- PLAYBOOK DELIVERED: /outputs/sensiskin/faza-b-nap-direktorijumi-uputstvo-2026-06-09.md
- EXECUTION STATUS: Pending — owner (Nataša Burka) to execute
- CONFIRMED WRONG ADDRESS CITATIONS (live-researched 2026-06-09):
  - mirandre.com/kozmeticki-salon-sensi-skin — "Vojvode Bojovića 5a" CONFIRMED
  - navidiku.rs/firme/kozmeticki-saloni-novi-sad/sensi-skin-kozmeticki-studio — "Vojvode Bojovića 5a" CONFIRMED + stari podlisting URL
  - ordinacije.info/kozmeticki-saloni-novi-sad-kozmeticki-salon-sensi-skin/ — "Vojvode Bojovića 5A" CONFIRMED
  - virtualnigrad.com/2021/04/nega-koze-u-prolece/ — blog post sa "Vojvode Bojovića 5A" CONFIRMED
  - virtualnigrad.com/item/kozmeticki-salon-sensi-skin/ — adresa u listingu NEPROVERENA direktno (verovatno stara)
- LISTINGS TO CREATE (ne postoje):
  - 011info.com — nema listinga
  - Apple Maps / Apple Business (businessconnect.apple.com) — nema listinga
  - Bing Places for Business (bingplaces.com) — nema listinga
  - planplus.rs — nema potvrde o listingu, treba proveriti
- DEFINITION OF DONE for Phase B: (1) Google pretraga "Vojvode Bojovića 5a" + "Sensi Skin" vraća 0 aktivnih rezultata; (2) svih 5 direktorijuma prikazuju "Braće Popović 3"; (3) Apple Maps listing potvrđen; (4) Bing listing potvrđen; (5) FB + IG kontakt podaci ispravni
- KPI: min 7/13 stavki "Gotovo" u 30 dana

## Confirmed strategic decisions (2026-06-09)
- NAMING: keep official business name "Sensi Skin" as-is for NAP/GBP consistency. Use word "kozmetički" (NOT "kozmetološki") in SEO copy + keywords — higher search volume in Serbia. Client preference + better SEO.
- KEYWORD MODEL: do NOT append "Novi Sad" to every page. Concentrate local/geo keywords ONLY on high-volume/high-intent pages: Home, HydraFacial, Epilacija, Kontakt, O nama. Niche/thematic pages (Nega lica, Aura Reality, Mesojet, Mesojet RF, Dermalux) target TREATMENT + PROBLEM it solves (e.g. "mezoterapija bez igala", "LED terapija za akne", "tretman za akne") — NOT "[service] Novi Sad" (near-zero volume + spammy). GBP carries local signal for those.
- SLUGS: keep existing URL slugs unchanged (already SEO-good) — incl. /kozmetoloski-centar-sensi-skin/ — to avoid losing ranking. "kozmetički" goes in title/meta/body, not the slug.
- SCHEMA: add LocalBusiness (HealthAndBeautyBusiness) on Home+Kontakt; Service on each treatment page; FAQPage on service-page FAQ blocks + Q&A blog posts; BreadcrumbList on deep pages; AggregateRating/Review tied to real GBP reviews (no fabrication).
- AEO/GEO: not a separate phase — emerges from A–D. Targets: 5–8 natural-language FAQ per key service; entity-consistent "O nama"; monthly manual check of ChatGPT/Perplexity/Google AI Overviews for brand mentions.
- BLOG: main blog /saveti-za-negu-koze/ = content hub (keep). Magazine section /strucni-saveti-za-negu-koze/ (only 3 PDF articles) = reposition as "Sensi Skin u medijima / Iz štampe" (authority signal) + transcribe PDFs to real text. Resolves cannibalization.
- PHASE ORDER (corrected): A=GBP+reviews (done), B=NAP+local directories (PLAYBOOK DELIVERED, pending execution), C=on-page redo (PLAYBOOK + COPY DELIVERED, pending implementation), D=content+FAQ, E=links.

## ▶ INSTAGRAM VOICE — REAL EXAMPLES (2026-06-12, verified from live posts)
Analyzed 5 real posts from @sensi_skin. Key patterns to replicate:

TONE: Warmer and more casual than previously documented. Mix of "Vi" (formal) and "ti" (informal) — switches freely, even within the same caption. Not strict.
STRUCTURE: Short paragraphs, 1-3 sentences each. Line breaks between every paragraph. No walls of text.
EMOJI USE: Light but present — 🌷✨💉📞 — functional, not decorative. One or two per post, usually at end of sentence.
HOOKS used in real posts: "Koliko nas troši novac na skupe preparate..." (frustration hook), "Da li ste znali da se koža obnavlja..." (curiosity/education hook), "Šta je Mesojet tretman i zašto ga svi vole?" (direct question hook).
CTA: Always ends with phone number 065 3338 338 (not 065/333-8-338 as previously documented — real format uses spaces). Sometimes "Pišite na @sensi_skin". Sometimes "Vaš Sensi Skin 🌷" sign-off.
PRICE MENTION: One post explicitly mentions price (5.000 din / 3.500 din with tretman) — price mentions ARE allowed on Instagram, contrary to previous rule. Rule applies to blog/web, not IG.
EDUCATION POSTS: Longer, step-by-step, explain the science simply. "Tokom tog procesa dolazi do smene ćelija..." — educational but not clinical.
RESULTS POSTS (before/after): Very short caption. "Dubina bora je manja, tonus kože podignut, ten ujednačen, a jedrina vraćena — to su rezultati koje možete videti odmah nakon tretmana kada se koži pruži upravo ono što joj je u tom trenutku najpotrebnije ✓" — one paragraph, phone, done.
HIGHEST PERFORMING POST (1413 likes, 2696 sends): Written by influencer/klijent (@masakupresanin), not Sensi Skin — UGC performs 10-40x better than brand posts. Priority: encourage/repost client content.
SIGN-OFF patterns: "Vaš Sensi Skin 🌷" or just phone number. No formal closing.
WHAT TO AVOID on IG: Long intros, "Posetite nas", corporate tone, hashtag spam. Real posts use NO hashtags or very few.
NOTE: Real IG posts use significantly fewer hashtags than recommended (often zero). Brand relies on reach from content quality + saves/shares, not hashtag discovery.

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
- SERVICE PAGE vs BLOG COPY separation rule (locked 2026-06-09): Service page = transactional angle (who we are, how we do it HERE, booking CTA, studio-specific protocol). Blog post = educational angle (what is X, how does it work, FAQ). No paragraph should be copied between the two — different intent, different user.
- COMPETITOR POSITIONING ON SERVICE PAGES: Never name competitors directly. Use indirect framing — "standardni protokol koji svi rade na isti način" to establish differentiation without naming rivals. Keeps brand voice clean and avoids reputation risks.
- DIFFERENTIATOR DISTRIBUTION RULE (locked 2026-06-09): Do not badge-nail all differentiators on every page. Each page gets the ONE differentiator most relevant to its service context. "20+ godina iskustva" lands strongest on /epilacija/ (safety/protocol trust). "Aura Reality 3D dijagnostika" lands strongest on /hydrafacial/ and /nega-lica/ (personalization angle). "Ovlašteni studio" lands strongest on /hydrafacial/ (branded protocol). Use the others as supporting context only.
- TRANSACTIONAL PAGES — word count ceiling: 350-450 reči for booking-intent pages (/hydrafacial/, /epilacija/). Going over dilutes the transactional signal and pushes the page toward informational. Hub pages (/nega-lica/) can go to 500 because their job is exploration, not immediate booking.
- BLOG EDUCATIONAL POSTS — approved "credibility without overclaiming" device (locked 2026-06-09): Phrase "Ovo nije marketinška fraza. Razlika je tehnička i merljiva." (or equivalent) is an approved pattern for Nataša's voice when making a factual claim about apparatus/professional results that could sound like marketing. Use sparingly — once per post maximum.
- BLOG FAIR-BALANCE RULE (locked 2026-06-09): Educational blog posts must honestly acknowledge what home care CAN do before explaining its limits. Opening a blog post by dismissing home care entirely violates Nataša's authentic, balanced voice and risks reader trust. Pattern confirmed effective: "Kućna nega i dalje ima svoju ulogu" → then explain the ceiling → then professional value.
- SOCIAL COPY RULE (locked 2026-06-12): Same fair-balance and credibility-device rules apply to Instagram/Facebook captions as to blog posts. "Ovo nije reklamna fraza. Razlika je tehnička i merljiva." is the approved device for social too — once per post. Instagram captions must complement the visual (add why/science/reassurance), not describe it. Facebook posts can run longer to explain the mechanism — FB audience expects more context.

## SEO targets

### MASTER KEYWORD TABLE — Phase C + Blog (2026-06-09) — ALL ASSIGNMENTS ACTIVE

| # | Stranica (slug) | Focus keyword | SEO Title | Chars | Meta (shortened) | Chars | Status |
|---|----------------|---------------|-----------|-------|------------------|-------|--------|
| 1 | /hydrafacial-tretmani-lica-novi-sad/ | hydrafacial Novi Sad | HydraFacial Novi Sad — tretmani lica Sensi Skin | 50 | HydraFacial Novi Sad u ovlastenom studiju Sensi Skin — dubinsko ciscenje, eksfolijacija i hidratacija u jednoj sesiji. Zakazite: 065/333-8-338. | 153 | COPY WRITTEN — pending WordPress implementation |
| 2 | /epilacija/ | laserska epilacija Novi Sad | Laserska epilacija Novi Sad — Sensi Skin studio | 51 | Laserska epilacija Novi Sad — profesionalna oprema, tretmani po tipu koze, dugotrajni rezultati. Sensi Skin. Zakazite: 065/333-8-338. | 141 | COPY WRITTEN — pending WordPress implementation |
| 3 | /nega-lica/ | nega lica tretmani | Nega lica tretmani — Sensi Skin kozmeticki studio | 53 | Nega lica tretmani u Sensi Skin — individualizovan pristup za svaki tip koze: HydraFacial, mesojet, LED terapija. Zakazite: 065/333-8-338. | 148 | COPY WRITTEN — pending WordPress implementation |
| 4 | / (pocetna) | kozmeticki centar Novi Sad | Kozmeticki centar Novi Sad — Sensi Skin studio | 50 | Kozmeticki centar Novi Sad — Sensi Skin, 20+ godina iskustva. HydraFacial, laserska epilacija, Aura Reality 3D dijagnostika. Zakazite: 065/333-8-338. | 150 | ACTIVE — keyword was unassigned, now confirmed here |
| 5 | /aura-reality-3d-dijagnostika-koze/ | aura reality dijagnostika koze | Aura Reality dijagnostika koze — 3D analiza Sensi Skin | 57 | Aura Reality dijagnostika koze — 3D analiza koja otkriva tacno stanje koze pre tretmana. Jedina u regionu. Zakazite u Sensi Skin: 065/333-8-338. | 152 | ACTIVE |
| 6 | /mesojet-tretmani/ | mesojet tretman bez igala | Mesojet tretman bez igala — Sensi Skin studio | 51 | Mesojet tretman bez igala — mlaz koji unosi aktivne supstance bez bola. Efikasan za bore, pore i hidrataciju koze. Zakazite: 065/333-8-338. | 148 | ACTIVE |
| 7 | /mesojet-rf/ | mesojet RF Novi Sad | Mesojet RF Novi Sad — tretman lica bez igala Sensi Skin | 58 | Mesojet RF Novi Sad tretman kombinuje radiofrekvenciju i bezigalnu mezoterapiju za vidljivo zategnucu kozu. Zakazite: 065/333-8-338. | 141 | ACTIVE — previously delivered 2026-06-08 |
| 8 | /dermalux/ | LED terapija za kozu lica | LED terapija za kozu lica — Dermalux Sensi Skin | 55 | LED terapija za kozu lica Dermalux Tri-Wave — plava, crvena i infracrvena svetlost za akne, bori i obnovu koze. Zakazite: 065/333-8-338. | 144 | ACTIVE |
| 9 | /kozmetoloski-centar-sensi-skin/ | kozmeticki studio Novi Sad | Kozmeticki studio Novi Sad — o Sensi Skin centru | 52 | Kozmeticki studio Novi Sad — Sensi Skin, 20+ godina iskustva. Natasa Burka i tim za tretmane prilagodene vasoj kozi. Zakazite: 065/333-8-338. | 145 | ACTIVE — slug kept unchanged per decision |
| 10 | /kontakt-sensi-skin-novi-sad/ | Sensi Skin Novi Sad kontakt | Sensi Skin Novi Sad — kontakt i zakazivanje | 49 | Sensi Skin Novi Sad — zakazite tretman telefonom 065/333-8-338 ili posetite nas na Brace Popovic 3, sprat 2. Radno vreme i mapa u nastavku. | 152 | ACTIVE |
| 11 | /kozmeticki-proizvodi-sensi-skin-studio/ | dermokozmetika Novi Sad | Dermokozmetika Novi Sad — proizvodi Sensi Skin Studio | 53 | Dermokozmetika Novi Sad dostupna u Sensi Skin studiju — profesionalni proizvodi za negu koze odabrani od strane strucnjaka. Posetite nas ili zakazite. | 150 | ACTIVE — previously delivered 2026-06-08 |
| 12 | /saveti-za-negu-koze/ | saveti za negu koze | Strucni saveti za negu koze — Sensi Skin, Novi Sad | 50 | Saveti za negu koze koje zaista funkcionisu — citajte blog Sensi Skin studija i naucite kako da brinete o kozi uz strucne savete. Zakazite odmah. | 145 | ACTIVE — previously delivered 2026-06-08 |
| 13 | /saveti-za-negu-koze/razlika-profesionalna-i-drogerijska-kozmetika/ | razlika profesionalna i drogerijska kozmetika | Razlika profesionalna i drogerijska kozmetika — Sensi Skin | 55 | Razlika profesionalna i drogerijska kozmetika nije samo cena — u pitanju su koncentracija, prodiranje u kozu i strucna dijagnoza. Saznajte sta kucna nega moze, a sta ne. | 153 | COPY WRITTEN — pending WordPress implementation. File: /outputs/sensiskin/blog-kucna-nega-vs-profesionalna-2026-06-09.md |

**COLLISION CHECK**: All 13 keywords are unique. No two pages share a focus keyword.
**GEO RULE COMPLIANCE**: "Novi Sad" in keyword only on pages 1, 2, 4, 7, 9, 10, 11 (geo pages). Pages 3, 5, 6, 8, 12, 13 are thematic — no geo modifier.
**BLOG CANNIBALIZATION CHECK**: Page #13 is informational; all service pages (1–11) are transactional/local. Zero overlap in keyword intent or phrasing. Slug is a subpage of blog hub #12, not a service page slug.

---

### Content briefs ready for copywriter (Phase C, 2026-06-09)
- Brief #1 — /hydrafacial-tretmani-lica-novi-sad/: EXECUTED. Copy at /outputs/sensiskin/faza-c-sadrzaj-top3-strane-2026-06-09.md
- Brief #2 — /epilacija/: EXECUTED. Copy at /outputs/sensiskin/faza-c-sadrzaj-top3-strane-2026-06-09.md
- Brief #3 — /nega-lica/: EXECUTED. Copy at /outputs/sensiskin/faza-c-sadrzaj-top3-strane-2026-06-09.md

### Blog content briefs (Phase D, 2026-06-09)
- Brief #4 — /saveti-za-negu-koze/razlika-profesionalna-i-drogerijska-kozmetika/: EXECUTED. Copy at /outputs/sensiskin/blog-kucna-nega-vs-profesionalna-2026-06-09.md. ~960 reči body + 6x FAQ + 5x interni link + 4x alt tekst. Pending WordPress implementation.

---

### Schema implementation status (updated 2026-06-10)
- COMPLETE SCHEMA FILE: /outputs/sensiskin/json-ld-schemas-2026-06-10.md — ready-to-paste JSON for ALL pages
- LocalBusiness + WebSite: Homepage Custom Schema — JSON ready. ALSO configure Yoast Knowledge Graph settings first.
- Service + FAQPage: HydraFacial (7 Q), Epilacija (4 Q), Aura Reality (5 Q) — JSON ready in schema file.
- Service only: Mesojet RF, Mesojet tretmani, Dermalux — JSON ready in schema file.
- Person + Organization: Tim stranica (/kozmetoloski-centar-sensi-skin/) — JSON ready in schema file. Includes all 6 team members.
- BlogPosting (Article): set Yoast Schema tab → Article type = BlogPosting for all 10 blog posts. No Custom Schema needed.
- FAQPage on blog: /sve-istine-o-laserskoj-epilaciji/ — ALREADY DONE by owner (confirmed).
- BreadcrumbList: Enable in Yoast → SEO → Search Appearance → Breadcrumbs.
- AggregateRating: DO NOT add until 10+ real GBP reviews collected.
- IMPLEMENTATION TIME ESTIMATE: ~41 minutes for all pages per schema file table.

---

### Previously delivered (pre-Phase C) — still pending implementation
- /mesojet-rf/: delivered 2026-06-08 — see master table row 7
- /kozmeticki-proizvodi-sensi-skin-studio/: delivered 2026-06-08 — see master table row 11
- /saveti-za-negu-koze/ (blog): delivered 2026-06-08 — see master table row 12
- /nega-koze-sensi-skin/ (OLD slug, now corrected to /nega-lica/): previous delivery superseded by Phase C assignment. Use row 3 of master table.

### Previously noted SEO priorities (from audit, jun 2026)
- Sitemap zastareo iz 2018 — Google pretražuje 21 mrtav URL — ADDRESSED in Phase 1
- Nedostaju title tagovi i meta opisi — ADDRESSED in Phase C (all 12 pages assigned)
- Nema LocalBusiness schema markupa — JSON-LD block delivered in Phase C playbook
- Nema canonical tagova ni alt teksta na slikama — STILL PENDING
- Google Business Profile — status nepoznat, mora se verifikovati — STILL PENDING

### Phase 2 audit findings (June 2026)
- Google search snippets as of June 8, 2026 still display OLD title format ("Kozmeticki salon i salon lepote") on all crawled pages — Phase C will replace all of these
- Competitor landscape for "laserska epilacija Novi Sad": Vita Elos, Studio LiliuM, K2 Derma, Dr. Jelena Glavinić Clinic — all with dedicated content pages. SensiSkin not on first page.
- Competitor landscape for "kozmetoloski centar Novi Sad": Soze Beauty, Ceca Skincare, Madam In, VIVA Beauty — SensiSkin not confirmed on first page
- ZERO content on most service pages = title/meta changes cannot produce rankings without content to back them up
- HydraFacial competitive landscape: SrediMe aggregator, Rea Medika, Beauty&Me ranking — SensiSkin has advantage as authorized studio
- Aura Reality: SensiSkin is cited on lepotaizdravlje.rs — strong brand authority signal for this keyword

## Conversion insights
[cro agent logs A/B test results and winning variants here]

## Ad performance notes
[paid-ads agent logs what's working and what isn't here]

## Email metrics
[email agent tracks open rates, sequence performance here]

## Analytics baselines
- STATUS (2026-06-09): Measurement playbook delivered — /outputs/sensiskin/merenje-gsc-uputstvo-2026-06-09.md
- BASELINE SNAPSHOT: PENDING from owner. Owner must open GSC + GBP + Google today (9. jun 2026) and record the numbers from Deo 0 of the playbook. Until this is done, no before/after comparison is possible.
- TRACKING CONFIGURED: None yet (no GA4 events, no GTM tags). Current measurement relies entirely on free native tools: Google Search Console, Google Business Profile Insights, Google Search (incognito), Rich Results Test, and manual AI checks (ChatGPT, Perplexity).
- METRICS THE OWNER MUST CAPTURE TODAY (baseline):
  1. GSC: total clicks (last 90 days)
  2. GSC: total impressions (last 90 days)
  3. GSC: average position (last 90 days)
  4. GSC: number of indexed pages (Pages report, green)
  5. GSC: number of indexing errors (Pages report, red/orange)
  6. GSC: impressions for "hydrafacial novi sad", "laserska epilacija novi sad", "kozmetički centar novi sad" (each separately)
  7. GBP: profile views (last 28 days)
  8. GBP: website clicks (last 28 days)
  9. GBP: calls (last 28 days)
  10. GBP: direction requests (last 28 days)
  11. GBP: total review count + average star rating
  12. Google search (inkognito): does "Vojvode Bojovića 5a" + "Sensi Skin" return any results? (Yes/No)
  13. AI check: Is Sensi Skin mentioned in ChatGPT and Perplexity for "kozmetički studiji Novi Sad"? (Yes/No)
- KNOWN BASELINE SIGNAL (from prior audit): As of June 8, 2026, all GSC-visible title tags still show OLD format "Kozmeticki salon i salon lepote" — Phase 2 changes NOT yet indexed. This is the confirmed pre-Phase-C baseline for title tag state.
- FAQ SCHEMA NOTE (jun 2026): Google deprecated FAQPage rich results in May 2026 (visual dropdowns gone from SERP). FAQPage schema markup remains valid and should be kept — it has AEO/AI citation value. Rich Results Test will lose FAQ check in June 2026; use validator.schema.org as fallback for FAQ schema validation.
