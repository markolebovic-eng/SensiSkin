# GEO Audit — RE-EVALUACIJA (posle implementacije) — Sensi Skin

**Datum:** 11. jun 2026.
**Sajt:** sensiskinstudio.com
**Tip:** Ponovljeni audit nakon popravki (poređenje sa izveštajem od 9. juna)
**Metod:** Verifikacija UŽIVO — direktan crawl renderovanog DOM-a (Chrome) za 10 ključnih strana + robots.txt, **+ naknadni pun crawl svih ~30 blog postova** (vidi DOPUNU). Sve ocene su zasnovane na onome što je stvarno objavljeno, ne na pretpostavci.

---

## SEKCIJA 1 — Izvršni sažetak

### Novi GEO skor: **64 / 100**  ⬆️ (sa 21/100 — napredak +43)

> **Dopuna 11. jun (posle PUNOG crawl-a bloga):** prvobitni nalaz je bio 62, sa „topikalni autoritet 4/10 / malo blogova". Korigovano na **64** nakon što sam crawl-ovao svih ~30 blog postova — sadržajni klaster je znatno jači nego što je prvi (nepotpun) crawl pokazao. Detalji u sekciji „DOPUNA — pun crawl bloga".

Ovo je veliki, stvaran skok. Temelji koje AI pretraga zahteva — otvoren pristup botovima, schema, FAQ, dubina sadržaja, E-E-A-T signal autora — sada **postoje na sajtu**, što sam potvrdio direktnim pregledom koda strana. Pre mesec dana sajt je bio praktično nečitljiv za AI; sada je čitljiv i delom citabilan.

Ali **nije „sve gotovo"** — i red je da ti to kažem otvoreno, jer si tražila iskrenu ocenu. Tri stvari za koje misliš da su urađene, a nisu (vidi „Šta još nije gotovo").

### Šta je VERIFIKOVANO kao popravljeno ✅

| Stavka | Status 9. jun | Status 11. jun (uživo) |
|--------|---------------|------------------------|
| **robots.txt — AI botovi** | ❓ nepoznato (kritično) | ✅ **Otvoreno.** Nema blokade za GPTBot, ClaudeBot, PerplexityBot, Google-Extended. Blokirani su samo cart/parametri — ispravno. |
| **NAP doslednost (na sajtu)** | ❌ stara adresa | ✅ **Sve strane** prikazuju „Braće Popović" — nigde više „Vojvode Bojović". |
| **Schema — početna** | samo LocalBusiness | ✅ BeautySalon + **MedicalOrganization** + **WebSite** + ContactPoint + ImageObject |
| **FAQPage schema** | ❌ nigde | ✅ HydraFacial (7 pitanja), Epilacija (4), „Sve istine o laserskoj epilaciji" (7) |
| **Service schema** | ❌ | ✅ HydraFacial, Epilacija, Nega lica, Mesojet RF, Dermalux |
| **Person schema (Nataša Burka)** | ❌ | ✅ Na strani „O nama" (E-E-A-T autor signal) |
| **Article schema** | ❌ | ✅ Na „Sve istine o laserskoj epilaciji" |
| **Sadržaj na service stranama** | prazne (<200 reči) | ✅ Realan sadržaj: HydraFacial ~1.300, Nega lica ~1.900, Epilacija ~950 reči tela |
| **„Sve istine o laserskoj epilaciji"** | — | ✅ **Najbolja strana na sajtu** — Article + FAQPage + LocalBusiness + Person + WebPage. Ovo je šablon za sve ostale. |

### ⚠️ Šta još NIJE gotovo (iskreno)

1. **🔴 Novi blog post „Razlika profesionalna i drogerijska kozmetika" NIJE objavljen.** URL `/saveti-za-negu-koze/razlika-profesionalna-i-drogerijska-kozmetika/` vraća **404 „Stranica nije pronađena"**. Tekst je napisan i spreman, ali nije postavljen na sajt.
2. **🟠 FAQ + FAQPage schema fali na pola service strana** — nema na: Nega lica, Mesojet RF, Dermalux, (i verovatno Aura Reality — nije bila u ovom crawl-u, proveriti). FAQ je #1 format koji AI citira.
3. **🟠 Nema AggregateRating / Review schema** nigde (ni na početnoj). To su „zvezdice" i social-proof signal koji AI rado citira — i dalje nedostaje.
4. **🟡 Nema BreadcrumbList schema** ni na jednoj strani (bilo preporučeno).
5. **🟡 Kanibalizacija bloga i dalje stoji** — blog hub linkuje i `/saveti-za-negu-koze/` i `/strucni-saveti-za-negu-koze/`. Druga još nije repozicionirana u „U medijima".
6. **🟡 Nema HowTo schema** (FAQ je delom pokrio tu ulogu — prihvatljivo, ali HowTo bi pomogao za „kako" upite).

### Šta NISAM mogao da proverim odavde (zahteva tvoju proveru)
- **Direktorijumi van sajta** (mirandre.com, navidiku.rs, ordinacije.info…) — NAP je čist NA SAJTU, ali off-site čišćenje (Faza B) ne mogu da potvrdim crawl-om sajta.
- **Google Business Profile, Luftika/SrediMe prisustvo** — off-site.
- **Stvarne AI citacije uživo** (ChatGPT/Perplexity/AI Overviews) — temelji su tek postavljeni; citiranje se pojavljuje nedeljama nakon što Google/AI ponovo iscrawluju sajt. Ovo se meri ručno za 3–6 nedelja (vidi merenje-gsc-uputstvo).

---

## DOPUNA — pun crawl bloga (svih ~30 postova, 11. jun)

U prvom prolazu crawl-ovao sam samo blog **hub** + 2 članka (`sve-istine-o-laserskoj-epilaciji` = Article+FAQPage; novi `razlika…` = 404). Naknadno sam crawl-ovao **svih 29 postojećih blog postova** sa strana 1–4. Nalaz:

| Metrika | Rezultat |
|---------|----------|
| Broj edukativnih blog postova | **~30** (serum, hemijski pilinzi, melazma, rozacea, vrste akni, menopauza, predeo oko očiju, štetnost solarijuma, tipovi kože, dnevna rutina, alopecija…) |
| Dužina | solidna — ~700–1700 reči tela po postu |
| **Article / BlogPosting** schema | **0 / 29** ❌ |
| **FAQPage** schema | **2 / 29** (`nega-lica-sta-je-u-rukama-kozmeticara…`, `tretmani-lica-sta-primeniti…`) |
| **datePublished** u schemi | **0 / 29** ❌ |

**Posledica po ocenu:** sadržajni klaster je realno jak — zato **ispravljam „topikalni autoritet" sa 4 na 7/10**. ALI sloj strukturisanih podataka na blogu je prazan: bez `Article` schema, bez datuma objave, skoro bez `FAQPage`. AI zato teže prepoznaje te članke kao citabilne i datirane. Takođe ovo malo spušta „Schema markup" (8 → 7) jer service strane jesu dobre, ali 29 blog strana je praktično bez schema.

**Nova prioritetna akcija (visok uticaj, mali napor):** masovno dodati `Article` + `datePublished`/`dateModified` (+ `author` = Nataša Burka) na svih ~30 postova, i `FAQPage` na one koji imaju pitanja. Sadržaj već postoji — fali samo markup. U WordPress/Yoast ovo ide preko Yoast podešavanja za tip „Post" (globalno) + Custom Schema gde treba.

---

## SEKCIJA 2 — Ocene po dimenzijama (staro → novo)

| # | Dimenzija | 9. jun | 11. jun | Komentar (verifikovano uživo) |
|---|-----------|:------:|:-------:|-------------------------------|
| 1 | **AI vidljivost** | 2/10 | **5/10** | Temelji postavljeni; stvarne citacije zahtevaju re-crawl (nedelje). Skor će rasti sam ako se sadržaj indeksira. |
| 2 | **Struktura sadržaja** | kritično | **7/10** | Service strane imaju realan sadržaj + FAQ na ključnima. Minus: FAQ fali na 3–4 strane, blog 404. |
| 3 | **Schema markup** | kritično | **7/10** | Service strane odlične (FAQPage, Service, Person, Article, MedicalOrganization, WebSite). Minus: **0/29 blog postova ima Article schema**, nema Breadcrumb, AggregateRating, HowTo. |
| 4 | **E-E-A-T** | nizak | **6/10** | Person schema (Nataša Burka) + dubina sadržaja + dosledan NAP. Minus: nema vidljivih recenzija/sertifikata sa schema. |
| 5 | **Topikalni autoritet** | ~5% | **7/10** ⬆ | **ISPRAVKA posle punog crawl-a:** sajt ima ~30 kvalitetnih blog postova (širok klaster). Minus: novi post 404; postovi bez Article schema/datuma. |
| 6 | **Citabilnost** | kritično | **5/10** | Definicioni + FAQ blokovi postoje. Minus: nema originalnih statistika („X% klijenata…"), nema datuma ažuriranja. |
| 7 | **Tehnički / crawler** | kritično | **8/10** | robots.txt otvoren za AI, NAP čist, schema renderovana u DOM-u. |
| 8 | **Lokalno / brand** | problemi | **5/10** | NAP na sajtu čist; off-site (direktorijumi, GBP, Luftika) neproveren + strucni duplikat stoji. |

**Ponderisani skor:** 64/100 (revidirano sa 62 posle punog crawl-a bloga).

---

## SEKCIJA 3 — Šta uraditi sledeće (prioritet, posle ovog audita)

| # | Akcija | Zašto | Napor | Prioritet |
|---|--------|-------|-------|-----------|
| 1 | **Objaviti blog „Razlika profesionalna i drogerijska kozmetika"** (sad je 404) | Tekst je gotov, samo nije postavljen — najlakša pobeda | 30 min | 🔴 odmah |
| 2 | **Dodati FAQ + FAQPage schema** na: Nega lica, Mesojet RF, Dermalux, Aura Reality | FAQ = #1 AI-citat format; pola strana ga nema | 2–3 h | 🔴 visok |
| 2b | **Masovno dodati `Article` + `datePublished` + `author` na svih ~30 blog postova** (Yoast „Post" tip globalno) | Sadržaj već postoji; 0/29 ima Article schema → AI ih ne vidi kao citabilne članke | 1–2 h | 🔴 visok |
| 3 | **Dodati AggregateRating/Review schema** (povezano sa stvarnim Google recenzijama) | „Zvezdice" + social proof za AI i SERP | 1 h | 🟠 visok |
| 4 | **Rešiti duplikat bloga** — repozicionirati `/strucni-saveti-za-negu-koze/` u „U medijima/Iz štampe" | Gasi kanibalizaciju | 1–2 h | 🟠 srednji |
| 5 | **Dodati BreadcrumbList schema** na sve dublje strane | Navigaciona jasnoća za AI | 1 h | 🟡 srednji |
| 6 | **Originalne statistike** iz prakse na service strane („X% klijenata…", „prosečno N tretmana…") | Statistike nose +37% AI citiranja | 2–3 h | 🟡 srednji |
| 7 | **Off-site (Faza B):** potvrditi NAP ispravku na mirandre/navidiku/ordinacije + GBP | Ne mogu da verifikujem odavde — tvoja provera | po playbook-u | 🟠 visok |
| 8 | **Za 3–6 nedelja:** ručno testirati AI citacije (ChatGPT/Perplexity/AI Overviews) | Tek tada se vidi stvarni rezultat schema rada | 30 min/mesečno | 🟡 praćenje |
| 9 | Dodati „Poslednji put ažurirano" + datume na blogove; razmotriti `llms.txt` | Freshness + AI kontekst | 1 h | 🟢 nisko |

---

## SEKCIJA 4 — Metodologija (transparentnost)

Verifikovano 11. juna 2026. direktnim crawl-om renderovanog DOM-a (Chrome headless `--dump-dom`) za:
`/`, `/hydrafacial-tretmani-lica-novi-sad/`, `/epilacija/`, `/nega-lica/`, `/mesojet-rf/`, `/dermalux/`, `/kozmetoloski-centar-sensi-skin/`, `/kontakt-sensi-skin-novi-sad/`, `/saveti-za-negu-koze/`, `/sve-istine-o-laserskoj-epilaciji/`, `/robots.txt`.
Za svaku stranu provereni: JSON-LD `@type` vrednosti, prisustvo vidljivog FAQ-a, NAP adresa, dubina sadržaja. Strana `razlika-profesionalna-i-drogerijska-kozmetika` i `/tim/` vraćaju 404 (potvrđeno preko `<title>Stranica nije pronađena`).

**Naknadno (dopuna):** crawl-ovano i svih **29 postojećih blog postova** (sa hub strana 1–4) — provereni Article/BlogPosting schema, FAQPage, datePublished, dužina. Rezultat: 0/29 Article, 2/29 FAQPage, 0/29 datePublished. Vidi sekciju „DOPUNA".

---

## Zaključak

Za mesec dana ste otišli sa **21 → 64**. To je ozbiljan, merljiv napredak i najteži deo (schema + sadržaj + E-E-A-T temelji) je urađen kvalitetno — strana „Sve istine o laserskoj epilaciji" je primer kako sve treba da izgleda. Pun crawl bloga je pokazao i veliku skrivenu prednost: ~30 kvalitetnih edukativnih postova koji samo čekaju Article/datum schema. Da bi prešli 75+, fokus je: (1) objaviti blog koji je 404, (2) **Article+datum schema na svih ~30 blog postova**, (3) FAQ schema na preostale service strane, (4) recenzije/AggregateRating, (5) potvrditi off-site NAP + GBP. Stvarne AI citacije će se pojaviti tek kad AI motori ponovo iscrawluju sajt — to merimo za 3–6 nedelja.

*Pripremio: AI Marketing Agency — GEO/SEO specijalist · 11. jun 2026.*
*Prethodni izveštaj: geo-audit-izvestaj-2026-06-09.md (skor 21/100).*
