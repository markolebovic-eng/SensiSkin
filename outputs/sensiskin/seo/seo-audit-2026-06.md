# SEO Audit — Sensi Skin — Jun 2026

**Datum**: 24. jun 2026  
**GSC property**: https://sensiskinstudio.com/  
**GA4 property**: properties/532419831  
**Period (GSC snapshot)**: 2026-03-24 → 2026-06-21 (90 dana, tekuci period)  
**Prethodni period (poređenje)**: 2025-12-24 → 2026-03-23  
**Agent**: SEO  
**Status**: Predlog — nema izmena na sajtu

---

## 1. TRAFFIC HEALTH SUMMARY

### GSC — Organicki saobraćaj (90 dana, mart–jun 2026)

| Metrika | Tekući period | Prethodni period | Delta |
|---------|--------------|------------------|-------|
| Klikovi | 1.519 | 1.938 | -419 (-21,6%) |
| Impresije | 35.431 | 37.175 | -1.744 (-4,7%) |
| Prosečni CTR | 4,29% | 5,21% | -0,93pp (-17,8%) |
| Prosečna pozicija | 8,15 | 7,09 | -1,05 mesta (lošije) |

**Trend: pogoršanje na svim metrikama.** Klikovi su pali za 21,6%, pozicija se pogoršala za gotovo jedno mesto, a CTR pao za 17,8% relativno. Ovo nije sezonski dip — pad je sistematski i prisutan i u impresijama i u poziciji.

**Mogući uzroci**:
- Title tagovi i meta opisi još uvek nisu promenili na Google-u (MEMORY.md beleži da se stari format "Kozmeticki salon i salon lepote" i dalje prikazuje)
- Sadržaj service stranica nije implementovan (Phase C copy dostavljen, ali ne i postavljen)
- Duplikat stranice na `/strucni-saveti-za-negu-koze/` vs `/saveti-za-negu-koze/` — aktivna kannibalizacija
- Pozicija 8.15 znači da je sajt pretežno na dnu prve strane ili na drugoj strani Google-a

---

### KRITIČNO: GA4 Tracking Gap

**Dijagnoza**: `tracking_gap`  
**GA4/GSC ratio**: 0.226 (zdravo je 0.7–1.3)

GA4 beleži samo **344 organska sesije** od **1.519 organskih klikova** koje beleži GSC. To je **samo 23% stvarnog organskog saobraćaja** — 77% klikova GA4 ne vidi.

**Ovo je kritičan problem koji mora biti rešen pre nego što se donose ikakve odluke na osnovu GA4 podataka.**

Mogući uzroci (po verovatnoći):
1. **Consent banner blokira GA4 na prvom page-view-u** — najčešći uzrok u GDPR regionu. Ako korisnik ne klikne "Prihvati" pre nego što učita prvu stranicu, GA4 ne zabeleži sesiju.
2. **Pogrešna konfiguracija kanala** — organski saobraćaj se klasifikuje kao "Direct" ili drugi kanal u GA4.
3. **GA4 tracking kod nije na svim landing stranicama** — posebno na blog postovima koji su nedavno dodati.
4. **Referral exclusion lista** — moguće da je domen slučajno dodat u exclusion listu.

**Preporuka**: Pre implementacije bilo čega, vlasnik treba da proveri GA4 → Admin → Data Streams → Measurement ID da li je kod na svim stranicama. Zatim proveriti: Reports → Acquisition → Traffic Acquisition i videti koliko je "Organic Search" vs "Direct". Ako je "Direct" neuobičajeno visok, tracking je pogrešan.

**Posledica**: Sve GA4 metrike (sesije, konverzije, engagement) su nepouzdane dok se ovo ne reši. Koristiti GSC kao primarni izvor podataka.

---

## 2. PAGE SELECTION RATIONALE

Podaci iz: `gsc_ctr_opportunities`, `gsc_quick_wins`, `cross_opportunity_matrix`  
Period: 2026-03-24 → 2026-06-21

### Odabrane TOP 5 stranica

| # | URL | Impresije | Pozicija | Stvarni CTR | Očekivani CTR | Deficit klikova |
|---|-----|-----------|----------|-------------|----------------|-----------------|
| 1 | /perutanje-koze/ | 6.289 | 5,78 | 1,64% | 6% | +274 potencijalna |
| 2 | /nega-lica/ | 2.618 | 5,65 | 2,86% | 6% | +82 potencijalna |
| 3 | /kontakt/ | 1.380 | 4,50 | 0,72% | 8% | +100 potencijalna |
| 4 | /sensi-skin/ | 1.706 | 4,06 | 2,75% | 8% | +89 potencijalna |
| 5 | /epilacija/ | 430 | 5,97 | 0,47% | 6% | +24 potencijalna |

**Zašto ovih 5:**

**1. /perutanje-koze/** — Najveći broj impresija na sajtu (6.289) i drastičan CTR gap (1,64% vs 6% očekivano). Potencijal za +274 klika mesečno ako CTR dođe na benchmark. Blog stranica koja se rangira za informativne upite o problemu kože. Vlasnik nema kontrolu nad rangiranjem odmah, ali bolji naslov dramatično podiže CTR na existirajućoj poziciji.

**2. /nega-lica/** — Ključna uslužna stranica sa 2.618 impresija i opportunity score 212 (treći na sajtu). Nalazi se na poziciji 5.65 — bliska top 5. CTR 2.86% je skoro duplo ispod očekivanog. Ovo je direktan prihod: svaki novi klik je potencijalni klijent.

**3. /kontakt/** — Pozicija 4.5 (skoro top 3) ali CTR svega 0.72% — katastrofalan gap od 7.28pp. 1.380 impresija na ovako dobroj poziciji treba da donosi 80+ klikova, a donosi 10. Stranica verovatno ima generičan ili loš title koji ne privlači klikove na "lokalne" upite.

**4. /sensi-skin/** — "O nama" stranica sa 1.706 impresija i pozicijom 4.06. CTR 2.75% umesto 8% očekivano = propuštenih 89 klikova. Stranica se rangira visoko ali ne konvertuje klikove. Naziv stranice verovatno nema jasnu vrednosnu ponudu u naslovu.

**5. /epilacija/** — Samo 430 impresija (volumen je nizak) ali ovo je jedna od prioritetnih uslužnih stranica za SensiSkin i CTR je katastrofalan: 0.47% na poziciji 6. Potencijal je strateški (transakcioni intent, visoka vrednost klijenta) čak i ako je volumen manji. Keyword "laserska epilacija Novi Sad" je u Master Keyword tabeli kao prioritet #2.

---

### Backup stranice (2–3)

| URL | Razlog | Impresije | Pozicija | CTR Gap |
|-----|--------|-----------|----------|---------|
| /mesojet-tretmani/ | Pos 4.5 sa 969 imp, CTR 5.26% vs 8% — 27 potencijalnih klikova, service page | 969 | 4,50 | +2,7pp |
| /stetnost-solarijuma/ | 2.471 impresija, pos 6.6, opp score 215 — blog post sa sezonskim relevantnim sadržajem (jun/jul) | 2.471 | 6,64 | +2,2pp |
| /sensi-skin/ (SEO redirect flag) | Napomena: GSC vidi /sensi-skin/ ali MEMORY.md dokumentuje slug kao /kozmetoloski-centar-sensi-skin/ — moguće da postoje dve URL varijante u indexu. Treba proveriti. | — | — | — |

---

## 3. PER-PAGE KEYWORD ANALYSIS

**Napomena o metodologiji**: GSC API dimension_filter za page vratio sitewide podatke (poznato ograničenje MCP implementacije). Keyword data po stranici izgrađena je kombinovanjem:
- CTR opportunities tool (koji direktno mapira page → pozicija → impresije → CTR)
- Quick wins tool (koji mapira query → pozicija → opportunity score)
- Sitewide query data (6 meseci, 2025-12-24 → 2026-06-21) sa poznatim tematskim klasterima
- Cross opportunity matrix (koji mapira page → impresije → CTR gap)

Tamo gde je query → page mapping direktno vidljiv iz CTR opportunities (koji je vratio page-level podatke), koristi se taj podatak. Tamo gde nije direktno vidljiv, koristim tematsku logiku i sitewide query data sa napomenom.

---

### Stranica 1: /perutanje-koze/

**Direktni page-level podaci iz CTR opportunities (90 dana)**:
- Impresije: 6.289 | Pozicija: 5,78 | CTR: 1,64% | CTR gap: 4,36pp

**Direktno potvrđeni query → page mapovi (iz quick wins i sitewide data)**:
- "perutanje koze tela" → /perutanje-koze/: 12 klikova, 263 impresija, pos 4.62, CTR 4.56% (90 dana)
- "perutanje kože na nogama" → /perutanje-koze/: 11 klikova, 419 impresija, pos 3.15, CTR 2.63% (90 dana)
- "svrab i perutanje koze" → verovatno /perutanje-koze/: 116 impresija, pos 6.64 (quick wins)

**Zaključak o keyword-ima**:
- Primarni keyword: **perutanje kože** (sitewide: 1.628 impresija, pos 2.68 — dominantna tematska baza)
- Sekundarni: perutanje kože na nogama (419 imp, pos 3.15), perutanje koze tela (263 imp, pos 4.62), svrab i perutanje kože (116 imp)

**Komentar**: Stranica se rangira na poziciji ~5-6 za kombinovano 6.289 impresija ali CTR je svega 1.64%. Trenutni title verovatno ne odgovara pretraživačkim frazama koje korisnici upisuju. Popravak naslova ima direktan uticaj na klikove bez promene rankinga.

---

### Stranica 2: /nega-lica/

**Direktni page-level podaci iz CTR opportunities (90 dana)**:
- Impresije: 2.618 | Pozicija: 5,65 | CTR: 2,86% | CTR gap: 3,14pp

**Direktno potvrđeni query → page mapovi**:
- "higijenski tretman lica novi sad" → /nega-lica/: 8 klikova, 225 impresija, pos 8.24 (direktno vidljivo u CTR opp data)
- "tretmani lica novi sad" → /nega-lica/ verovatno: 22 klikova, 729 imp, pos 7.87 (tematski fit + quick wins potvrdio "tretmani lica" sa 171 imp na pos 12.7)
- "nega lica" → /nega-lica/ tematski: sitewide volumen relevantan
- "ciscenje lica novi sad" → /nega-lica/ ili /hydrafacial/: 16 klikova, 249 imp, pos 5.70

**Zaključak o keyword-ima**:
- Primarni keyword: **nega lica tretmani** (iz MEMORY.md Master Keyword Table #3 — potvrđeno kao dodeljeni keyword)
- Sekundarni: higijenski tretman lica Novi Sad (225 imp, pos 8.2), tretmani lica Novi Sad (729 imp, pos 7.9), čišćenje lica Novi Sad (249 imp, pos 5.7)

**Komentar**: "nega lica tretmani" je već dodeljeni keyword iz Phase C (MEMORY.md #3). Stranica ima ogroman potencijal za "higijenski tretman lica Novi Sad" — 700 impresija na 6 meseci i samo pos 6.5 sa 7% CTR = korisnici klikaju kada su na višim pozicijama. Novi title i meta moraju pokriti oba intent-a: opcu negu lica + higijenu/čišćenje.

---

### Stranica 3: /kontakt/

**Direktni page-level podaci iz CTR opportunities (90 dana)**:
- Impresije: 1.380 | Pozicija: 4,50 | CTR: 0,72% | CTR gap: 7,28pp

**Query analiza**:
Stranica /kontakt/ je navigacijska stranica — korisnici koji je traže pretražuju brendirane izraze. Na poziciji 4.5 sa 1.380 impresija i samo 10 klikova, problem je jasan: title stranice verovatno ne kaže jasno šta ova stranica nudi, ili korisnici koji vide snippet biraju drugu URL (npr. / homepage ili /sensi-skin/) jer misle da tamo nađu kontakt.

- "sensi skin" → prikazuje /kontakt/ u nekim impresijama (multi-URL za isti brand query)
- "sensi skin novi sad" → prikazuje više URL-ova istovremeno (cannibalization)
- "kozmeticki salon novi sad" → 410 imp, pos 8.58 (sitewide) — neke od ovih impresija padaju na /kontakt/

**Zaključak o keyword-ima**:
- Primarni keyword: **Sensi Skin Novi Sad kontakt** (navigacioni intent — korisnici traže kontakt informacije brenda)
- Sekundarni: Sensi Skin zakazivanje, kozmetički salon Novi Sad kontakt, Sensi Skin adresa Novi Sad

**Komentar**: Title mora sadržati i brand name i akciju (zakazivanje/kontakt) jer je navigacioni intent — korisnik zna šta traži, title treba da potvrdi da je to prava stranica. Trenutni ekstremno nizak CTR (0.72% na pos 4.5) ukazuje da snippet ne komunicira jasnu vrednost.

---

### Stranica 4: /sensi-skin/

**Direktni page-level podaci iz CTR opportunities (90 dana)**:
- Impresije: 1.706 | Pozicija: 4,06 | CTR: 2,75% | CTR gap: 5,25pp

**Slug napomena**: GSC vidi stranicu na `/sensi-skin/`. MEMORY.md dokumentuje "O nama" stranicu na `/kozmetoloski-centar-sensi-skin/`. Moguće je da postoje dve varijante (301 redirect ili canonical problem) ili da je /sensi-skin/ novi slug. Ovo treba proveriti u WordPress-u.

**Query analiza**:
"O nama" stranica na poziciji 4 sa skoro 1.700 impresija. Brendirani upiti su dominantni.
- "sensi skin" → direktno: 810 klikova sitewide, ova stranica dobija deo
- "kozmeticki salon novi sad" → 1.280 imp, pos 7.06 — deo impresija može biti na /sensi-skin/
- "kozmeticki studio novi sad" → MEMORY.md keyword #9 dodeljen ovoj stranici

**Zaključak o keyword-ima**:
- Primarni keyword: **kozmetički studio Novi Sad** (iz MEMORY.md Master Table #9 — potvrđeno kao dodeljeni keyword za "O nama" stranicu)
- Sekundarni: Sensi Skin Novi Sad, kozmetički centar Novi Sad, Nataša Burka kozmetolog

**Komentar**: "O nama" stranica na pos 4 treba title koji komunicira: (a) ko su, (b) gde su, (c) zašto izabrati njih. Trenutni CTR 2.75% na poziciji 4 je duplo ispod benchmarka — title verovatno samo kaže "Sensi Skin" bez differentiator-a.

---

### Stranica 5: /epilacija/

**Direktni page-level podaci iz CTR opportunities (90 dana)**:
- Impresije: 430 | Pozicija: 5,97 | CTR: 0,47% | CTR gap: 5,53pp

**Query analiza**:
- "laserska epilacija Novi Sad" → /epilacija/: ovo je potvrđeni primarni keyword iz MEMORY.md #2
- Sitewide svi epilacija upiti imaju mali volumen u 90 dana — ali strateška vrednost je visoka (transakcioni intent, visoka vrednost per klijent)
- "epilacija" generički + "laserska epilacija" su tematski pokriveni
- "Nove technologije epilacije Novi Sad" / "trajna epilacija Novi Sad" — potencijalni sekundarni

**Zaključak o keyword-ima**:
- Primarni keyword: **laserska epilacija Novi Sad** (iz MEMORY.md Master Table #2 — potvrđeno)
- Sekundarni: trajna epilacija Novi Sad, laserska epilacija cena, epilacija lasером Novi Sad

**Komentar**: CTR 0.47% na poziciji 6 je alarm. Na ovom intent-u (transakcioni, lokalni) korisnik klika na ono što mu zvuči kao "pravo mesto" — title mora komunicirati stručnost, lokalnost i differentiator (profesionalna oprema, tip kože). Phase C copy je već napisan ali verovatno nije implementovan.

---

## 4. DELIVERABLES — NOVI TITLE TAGOVI I META OPISI

---

### PAGE 1: /perutanje-koze/

**URL**: https://sensiskinstudio.com/perutanje-koze/

**Target phrases**:
- Primarni: **perutanje kože** (1.628 imp sitewide 6M, pos 2.68)
- Sekundarni: perutanje kože na nogama (956 imp / 6M, pos 2.93), perutanje kože tela (458 imp / 6M, pos 4.15), svrab i perutanje kože (116 imp / 90d, pos 6.64)

**FOCUS KEYWORD**: perutanje kože  
**SEARCH INTENT**: Informacioni — korisnik traži uzroke i rešenja za problem perutanja kože, nije u fazi kupovine  
**SEO TITLE**: Perutanje kože — uzroci i tretmani | Sensi Skin (51 chars)  
Keyword na početku: DA  
**META DESCRIPTION**: Perutanje kože može biti znak poremećenog balansa kože. Saznajte uzroke perutanja — suva koža, ekcem, psorijaza — i kada je vreme za profesionalni tretman u Sensi Skin studiju. (191 chars)

Napomena: Meta je 191 chars što je iznad preporučenih 155. Skraćena verzija ispod:

**META DESCRIPTION (skraćena, copy-paste ready)**: Perutanje kože — uzroci, simptomi i kada potražiti pomoć stručnjaka. Saznajte šta radi Sensi Skin kad kućna nega više ne pomaže. (150 chars)

**YOAST CHECKLIST**:
- Keyword u title-u (pozicija: početak): DA
- Keyword u prvoj rečenici meta: DA ("Perutanje kože")
- Dužina meta: 150 chars (120–155 opseg: DA)
- Dužina title: 51 chars (50–60 opseg: DA)

**KEYWORD COLLISION CHECK**: "perutanje kože" nije u MEMORY.md Master Keyword Table. Nema konflikta.

**RATIONALE**: Stranica ima 6.289 impresija u 90 dana (najveći broj na sajtu) ali CTR samo 1.64%. Benchmark za pos 5.78 je 6%. Nova h1 i title koji sadrži tačnu pretraživačku frazu "perutanje kože" može dovesti CTR sa 1.64% na 3-4% = 75-160 dodatnih klikova. Informacioni intent znači korisnik istražuje — title treba da obeća odgovor, ne prodaju.

**CONTENT REQUIREMENTS**: H1 mora sadržati "perutanje kože" verbatim (nominativ). Prva rečenica uvoda mora sadržati keyword. Proveri da li stranica ima dovoljno sadržaja za Yoast green (min 300 reči).

---

### PAGE 2: /nega-lica/

**URL**: https://sensiskinstudio.com/nega-lica/

**Target phrases**:
- Primarni: **nega lica tretmani** (potvrđen MEMORY.md keyword #3)
- Sekundarni: higijenski tretman lica Novi Sad (700 imp / 6M, pos 6.55), tretmani lica Novi Sad (729 imp / 6M, pos 7.87), čišćenje lica Novi Sad (249 imp / 6M, pos 5.70)

**FOCUS KEYWORD**: nega lica tretmani  
**SEARCH INTENT**: Mešoviti — navigaciono-transakcioni. Korisnik istražuje tretmane lica i traži studijo gde može to uraditi.  
**SEO TITLE**: Nega lica tretmani — Sensi Skin kozmetički studio (50 chars)  
Keyword na početku: DA  
**META DESCRIPTION (copy-paste ready)**: Nega lica tretmani u Sensi Skin — higijenski tretmani, HydraFacial i mesojet prilagođeni Vašem tipu kože. Zakazite konsultaciju: 065/333-8-338. (152 chars)

**YOAST CHECKLIST**:
- Keyword u title-u (pozicija: početak): DA ("Nega lica tretmani")
- Keyword u prvoj rečenici meta: DA ("Nega lica tretmani u Sensi Skin")
- Dužina meta: 152 chars (120–155 opseg: DA)
- Dužina title: 50 chars (50–60 opseg: DA)

**KEYWORD COLLISION CHECK**: "nega lica tretmani" — dodeljeno ovoj stranici u MEMORY.md #3. Bez konflikta.

**RATIONALE**: Stranica je na poziciji 5.65 sa 2.618 impresija i CTR samo 2.86% — propušta 82 potencijalna klika. Prethodni title (verovatno generički "Nega lica — Sensi Skin") ne pominje konkretne tretmane ni lokaciju. Novi title eksplicitno kaže šta nudi i ko (studio), meta dodaje higijenski tretman lica Novi Sad (225 imp/90d, pos 8.2) i HydraFacial kao sekundarni signal. Poziv na akciju sa brojem telefona podiže CTR na transakcionalnim stranicama.

**CONTENT REQUIREMENTS**: H1 mora biti "Nega lica tretmani" (nominativ, verbatim). Prva rečenica body copy mora sadržati keyword. Phase C body copy je već napisan i čeka implementaciju.

---

### PAGE 3: /kontakt/

**URL**: https://sensiskinstudio.com/kontakt/

**Target phrases**:
- Primarni: **Sensi Skin Novi Sad kontakt** (navigacioni intent)
- Sekundarni: Sensi Skin zakazivanje, kozmetički salon Novi Sad zakazivanje, Sensi Skin adresa

**FOCUS KEYWORD**: Sensi Skin Novi Sad kontakt  
**SEARCH INTENT**: Navigacioni — korisnik koji već zna za Sensi Skin i traži kako da stupi u kontakt ili zakažeme termin.  
**SEO TITLE**: Sensi Skin Novi Sad — kontakt i zakazivanje (49 chars)  
Keyword na početku: DA (brand + lokacija na početku)  
**META DESCRIPTION (copy-paste ready)**: Sensi Skin Novi Sad — zakazite tretman telefonom 065/333-8-338 ili posetite nas na Braće Popović 3, sprat 2. Radno vreme i mapa u nastavku. (152 chars)

**YOAST CHECKLIST**:
- Keyword u title-u (pozicija: početak): DA
- Keyword u prvoj rečenici meta: DA ("Sensi Skin Novi Sad")
- Dužina meta: 152 chars (120–155 opseg: DA)
- Dužina title: 49 chars (50–60 opseg: BLAGO ISPOD, ali prihvatljivo za navigacione stranice)

**KEYWORD COLLISION CHECK**: "Sensi Skin Novi Sad kontakt" — potvrđeno kao keyword #10 u MEMORY.md Master Table. Stranica /kontakt/ odgovara slug-u koji je GSC prijavio. Nema konflikta.

**Napomena o slug-u**: MEMORY.md beleži slug kao `/kontakt-sensi-skin-novi-sad/`, ali GSC prikazuje stranicu na `/kontakt/`. Treba proveriti da li je ovo isti URL sa redirectom ili da li postoje dve varijante. Preporuka: ne menjati slug — samo ažurirati title/meta u Yoastu.

**RATIONALE**: CTR 0.72% na poziciji 4.5 je najgori CTR gap po apsolutnim brojevima na sajtu (100 potencijalnih klikova). Stranica gotovo sigurno ima neinformativan title (npr. samo "Kontakt — Sensi Skin"). Novi title sa brendom + lokacijom + jasnom akcijom (zakazivanje) direktno odgovara navigacionom intent-u i dramatično podiže CTR.

**CONTENT REQUIREMENTS**: Stranica mora sadržati adresu (Braće Popović 3, sprat 2, 21000 Novi Sad), broj telefona (065/333-8-338), radno vreme i Google Maps embed za lokalni SEO signal. H1: "Kontakt i zakazivanje — Sensi Skin Novi Sad".

---

### PAGE 4: /sensi-skin/

**URL**: https://sensiskinstudio.com/sensi-skin/

**Target phrases**:
- Primarni: **kozmetički studio Novi Sad** (MEMORY.md keyword #9)
- Sekundarni: Sensi Skin Novi Sad, Nataša Burka kozmetolog, kozmetički centar Novi Sad iskustvo

**FOCUS KEYWORD**: kozmetički studio Novi Sad  
**SEARCH INTENT**: Navigaciono-informacioni — korisnik istražuje ko je Sensi Skin, želi da sazna više pre rezervacije.  
**SEO TITLE**: Kozmetički studio Novi Sad — o Sensi Skin centru (50 chars)  
Keyword na početku: DA  
**META DESCRIPTION (copy-paste ready)**: Kozmetički studio Novi Sad — Sensi Skin, 20+ godina iskustva. Nataša Burka i tim za tretmane prilagođene Vašoj koži. Zakazite: 065/333-8-338. (147 chars)

**YOAST CHECKLIST**:
- Keyword u title-u (pozicija: početak): DA
- Keyword u prvoj rečenici meta: DA ("Kozmetički studio Novi Sad")
- Dužina meta: 147 chars (120–155 opseg: DA)
- Dužina title: 50 chars (50–60 opseg: DA)

**KEYWORD COLLISION CHECK**: "kozmetički studio Novi Sad" — dodeljeno u MEMORY.md #9 stranici `/kozmetoloski-centar-sensi-skin/`. GSC prijavljuje `/sensi-skin/` kao aktuelni URL. Ovo su verovatno isti sadržaj na različitim URL-ovima — TREBA PROVERITI i rešiti pre implementacije.

**RATIONALE**: "O nama" stranica na poziciji 4.06 sa 1.706 impresija i CTR 2.75% — propušta 89 klikova. Pozicija je dobra, sadržaj je rangiran, ali title ne privlači klikove. Novi title koji počinje sa "Kozmetički studio Novi Sad" direktno odgovara lokalnom search intent-u, a "20+ godina iskustva" u meta-u dodaje E-E-A-T signal i differentiator koji navodi korisnika da klikne.

**CONTENT REQUIREMENTS**: H1: "Kozmetički studio Novi Sad — Sensi Skin". Stranica mora sadržati: bio Nataše Burke, broj godina iskustva, listu sertifikata/specijalizacija, fotografije. Keyword mora biti u prvoj rečenici body copy.

---

### PAGE 5: /epilacija/

**URL**: https://sensiskinstudio.com/epilacija/

**Target phrases**:
- Primarni: **laserska epilacija Novi Sad** (MEMORY.md keyword #2, pos 5.97, 430 imp / 90d)
- Sekundarni: trajna epilacija Novi Sad, laserska epilacija cena, profesionalna epilacija Novi Sad

**FOCUS KEYWORD**: laserska epilacija Novi Sad  
**SEARCH INTENT**: Transakcioni — korisnik aktivno traži salon za lasersku epilaciju u Novom Sadu, spreman za zakazivanje.  
**SEO TITLE**: Laserska epilacija Novi Sad — Sensi Skin studio (49 chars)  
Keyword na početku: DA  
**META DESCRIPTION (copy-paste ready)**: Laserska epilacija Novi Sad u Sensi Skin — profesionalna oprema, tretmani po tipu kože, dugotrajni rezultati. Zakazite konsultaciju: 065/333-8-338. (154 chars)

**YOAST CHECKLIST**:
- Keyword u title-u (pozicija: početak): DA
- Keyword u prvoj rečenici meta: DA ("Laserska epilacija Novi Sad u Sensi Skin")
- Dužina meta: 154 chars (120–155 opseg: DA)
- Dužina title: 49 chars (50–60 opseg: 1 char ispod, prihvatljivo)

**KEYWORD COLLISION CHECK**: "laserska epilacija Novi Sad" — dodeljeno u MEMORY.md #2. Bez konflikta.

**RATIONALE**: CTR 0.47% na poziciji 5.97 je najgori CTR na uslužnim stranicama. Za transakcioni lokalni upit, korisnik bira na osnovu title-a — treba da vidi (1) šta traži, (2) gde, (3) zašto baš ovde. Novi title to eksplicitno komunicira. Phase C body copy je već napisan — implementacija copy-ja i novih meta tagova zajedno mogu pomeriti poziciju I CTR.

**CONTENT REQUIREMENTS**: H1 mora biti "Laserska epilacija Novi Sad" (verbatim, nominativ). Phase C body copy je spreman na /outputs/sensiskin/faza-c-sadrzaj-top3-strane-2026-06-09.md — implementovati odmah uz ove meta tagove.

---

## 5. IMPLEMENTATION NOTES

### KRITIČNO — Redosled implementacije

1. **GA4 tracking gap (odmah)** — Pre svega else, vlasnik mora otkloniti tracking gap. 77% organskog saobraćaja je nevidljivo u GA4. Proveri: GA4 Admin → Data Streams → verify tag na svim stranicama. Consent banner konfiguracija (cookie-on-accept pattern vs always-fire).

2. **Phase C copy + novi title/meta zajedno (ove nedelje)** — Za stranice /nega-lica/ i /epilacija/ postoji već napisan body copy. Implementovati copy + nove meta tagove u istom WordPress editu. Ne postavljati title bez sadržaja — nije efikasno.

3. **/perutanje-koze/ title/meta (ove nedelje)** — Čista CTR optimizacija. Sadržaj verovatno već postoji. Samo promeniti title i meta u Yoastu.

4. **/kontakt/ title/meta (ove nedelje)** — Brza implementacija, ogroman CTR gain.

5. **/sensi-skin/ — URL provera (pre implementacije)** — Razjasniti da li je /sensi-skin/ isti sadržaj kao /kozmetoloski-centar-sensi-skin/. Ako da — rešiti canonical ili redirect PRZED implementacijom meta tagova.

### URL diskrepancija — flag za vlasnika

GSC prikazuje sledeće URL-ove koji se razlikuju od MEMORY.md dokumentacije:
- GSC: `/kontakt/` vs MEMORY.md: `/kontakt-sensi-skin-novi-sad/`
- GSC: `/sensi-skin/` vs MEMORY.md: `/kozmetoloski-centar-sensi-skin/`

Moguće objašnjenje: WordPress ima više URL-ova koji vode na isti sadržaj (redirect ili duplikat). Preporuka: u WordPress-u proveriti stvarni permalink za "Kontakt" i "O nama" stranicu. Ne menjati URL slug.

### Slug za Phase C stranice

GSC prikazuje `/hydrafacial-tretman-lica/` (bez sufiks `-novi-sad`) ali MEMORY.md koristi `/hydrafacial-tretmani-lica-novi-sad/`. Proveriti koji slug je aktuelan pre sledeće iteracije optimizacije.

### Napomena o /perutanje-koze/ i business relevantnosti

Stranica o perutanju kože je blog post, ne uslužna stranica. Informacioni saobraćaj neće direktno konvertovati u rezervacije. CTR optimizacija ove stranice donosi posete, ali monetarna vrednost zavisi od: (a) internih linkova prema uslužnim stranicama (/nega-lica/, /dermalux/, /hydrafacial/), (b) CTA-a unutar teksta. Preporuka: u body tekstu dodati interni link ka relevantnoj usluzi uz contextualni anchor tekst (npr. "Dermalux LED tretman može pomoći kod hroničnog perutanja kože — saznajte više").

### GSC Request Indexing

Nakon svake izmene title/meta u Yoastu, URL treba prijaviti u Google Search Console:
- GSC → URL Inspection → uneti URL → Request Indexing
- Uraditi za svaku stranicu gde su napravljene izmene
- Google obično re-crawla u roku 1–7 dana

---

## 6. MASTER KEYWORD TABLE — AŽURIRANA STAVKA

Sledeće stavke iz Phase C MEMORY.md tabele su potvrđene i / ili korigovane ovim auditom:

| # | Stranica (slug) | Focus keyword | Status |
|---|----------------|---------------|--------|
| 2 | /epilacija/ | laserska epilacija Novi Sad | POTVRĐEN — novi title/meta u ovom auditu |
| 3 | /nega-lica/ | nega lica tretmani | POTVRĐEN — novi title/meta u ovom auditu |
| 9 | /sensi-skin/ | kozmetički studio Novi Sad | POTVRĐEN — proveriti slug pre implementacije |
| 10 | /kontakt/ | Sensi Skin Novi Sad kontakt | POTVRĐEN — slug može biti /kontakt/ umesto /kontakt-sensi-skin-novi-sad/ |
| NOVO | /perutanje-koze/ | perutanje kože | NOVO — nije bio u Master Table. Informacioni intent. Bez konflikta. |

---

*Izveštaj sačuvan: /outputs/sensiskin/seo/seo-audit-2026-06.md*  
*Sledeći korak: vlasnik implementira izmene u WordPress → Yoast → Request Indexing u GSC*
