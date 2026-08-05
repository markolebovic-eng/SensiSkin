# Stojanov Auto — Generalni audit (baseline)

**Datum:** 2026-08-05
**Sajt:** https://stojanovauto.rs
**Obim:** onboarding discovery + tehnički/on-page/GEO baseline
**NIJE uključeno:** keyword strategija, quick wins i prioritizacija po prihodu — za to je
potreban GSC/GA4 pristup (klijent za sada ne daje). Vidi „Šta ovaj audit ne može da vidi".

**Ukupna ocena: 4/10**

Sajt je tehnički zdrav (nema pokvarenih linkova, brz odgovor servera, uredan sitemap,
Rank Math postavljen) ali **marketinški neaktiviran**. Ponaša se kao katalog za nekoga
ko već zna ko je Stojanov Auto. Za nekoga ko traži „gde da uradim tehnički u Novom Sadu",
sajt ne postoji.

---

## 1. Najveći nalaz: sajt ne targetira Novi Sad

Ovo je najskuplji problem i vredi ga izdvojiti iznad svega ostalog.

Firma zarađuje od lokalnih usluga sa jakom namerom — servis, tehnički pregled,
registracija, šlep, gume. Svi ti upiti su lokalni. **Nijedan title tag na sajtu
ne sadrži reč „Novi Sad".**

Svi naslovi imaju isti oblik: `Usluga - Stojanov Auto`.

| Trenutni title | Problem |
|---|---|
| `STOJANOV AUTO - Stojanov Auto` (naslovna) | Ime ponovljeno dvaput, nula ključnih reči |
| `Servis - Stojanov Auto` | Ne kaže koji brend, ni koji grad, ni da je ovlašćeni |
| `Tehnički pregled - Stojanov Auto` | Konkuriše za upit koji ima „novi sad" u sebi, bez „novi sad" u naslovu |
| `Pomoć na putu - Šlep služba 24h - Stojanov Auto` | Jedini iole upotrebljiv naslov na sajtu |
| `Polovna vozila - Stojanov Auto` | Identičan naslov na dve različite stranice |

A demand postoji i merljiv je. Google autocomplete za Novi Sad (izvor: `trends.google_suggest`, 2026-08-05):

- `tehnicki pregled novi sad` → + `cena`, `radno vreme`, `najjeftiniji`, `temerinska`, `sajlovo`, `heroja pinkija`, `wolf`
- `slep sluzba novi sad` → + `cena`, `24 7`, `klisa`, i 6 imenovanih konkurenata
- `renault servis novi sad` → + `renault ovlasceni servis novi sad`
- `polovna vozila novi sad` → + `na kredit`, `na lizing`, `i okolina`, `autokomerc`

Autocomplete izlistava konkurente po imenu — Wolf, S&G tim, Atlas, Leven, Autokomerc.
To su firme koje su zauzele mentalni i pretraživački prostor koji Stojanov Auto,
kao ovlašćeni centar sa celim lancem usluga, ima svako pravo da uzme.

**Predložene izmene naslova** (spremno za Rank Math):

| Stranica | Novi title |
|---|---|
| `/` | Stojanov Auto Novi Sad — ovlašćeni Renault, Dacia i Nissan diler i servis |
| `/servis/` | Ovlašćeni Renault, Dacia i Nissan servis — Novi Sad \| Stojanov Auto |
| `/usluge/tehnicki-pregled/` | Tehnički pregled i registracija vozila — Novi Sad, Zrenjaninski put |
| `/usluge/pomoc-na-putu/` | Šlep služba Novi Sad 24h — pomoć na putu \| Stojanov Auto |
| `/usluge/hotel-za-gume/` | Hotel za gume — čuvanje guma u Novom Sadu \| Stojanov Auto |
| `/polovna-vozila/` | Polovna vozila Novi Sad — provereni automobili \| Stojanov Auto |
| `/prodaja/komercijalna-vozila/` | Komercijalna vozila Renault PRO+ — Novi Sad \| Stojanov Auto |

---

## 2. Kritični problemi (P0 — rešiti prvo)

### 2.1 Naslovna stranica nema H1
Naslovna ima 28 H2 elemenata i **nijedan H1**. Isto važi za `/renault/`, `/akcije-old/`,
`/naslovna-old/`. Za najvažniju stranicu na domenu, Google nema glavni signal o čemu je stranica.

**Fix:** H1 na naslovnoj koji nosi i uslugu i lokaciju, npr.
*„Ovlašćeni Renault, Dacia i Nissan centar u Novom Sadu"*.

### 2.2 Schema je pogrešnog tipa i nepotpuna
Trenutno: `Organization`. Za firmu koja prodaje i servisira automobile to je premalo.

Nedostaje:
- **`AutoDealer`** (ili `AutomotiveBusiness` + `AutoRepair` za servisni deo) umesto golog `Organization`
- **`addressLocality: "Novi Sad"`** — grad je zaglavljen unutar `streetAddress` kao slobodan tekst.
  Google ga tako ne parsira pouzdano.
- `addressCountry` je `"Srbija"` — treba ISO kod `"RS"`
- **`openingHoursSpecification`** — radno vreme postoji na sajtu, ali ne u schemi
- **`telephone`** na nivou `Place`/`LocalBusiness`
- **`aggregateRating`** — na `/o-nama/` postoji sekcija „Šta kažu naše mušterije", ali bez schema
- `sameAs` navodi samo Facebook i Twitter, a firma ima i **Instagram, YouTube i LinkedIn**
- `priceRange`

**Suvišno i štetno:** naslovna nosi `Article` schema sa `author: "Sanja Pena"`.
Naslovna dilerskog salona nije članak. Isti `Article` tip se ponavlja i na
`/servis/`, `/polovna-vozila/`, `/prodaja/nova-vozila/`, `/renault/`, `/dacia/`, `/nissan/`.
Ovo je Rank Math default koji nikad nije podešen — treba ga isključiti za stranice
i zameniti odgovarajućim tipovima (`Service`, `AutoRepair`, `AutoDealer`).

### 2.3 Duplirane stranice
`/polovna-vozila/` i `/prodaja/polovna-vozila/` — isti title, isti H1, ista dužina teksta (418 reči),
obe self-canonical, obe u sitemapu, obe indeksabilne. Klasična kanibalizacija: Google mora
da bira, i verovatno bira pogrešnu.

**Fix:** izabrati jednu kao kanonsku (predlog: `/polovna-vozila/` — kraći URL),
301 sa druge. Plugin Redirection je već instaliran.

### 2.4 Stare stranice žive u indeksu
`/naslovna-old/` i `/akcije-old/` — obe `index, follow`, obe u sitemapu.
`/naslovna-old/` ima **istu meta description kao prava naslovna**, tj. direktno se takmiči s njom.

**Fix:** 301 na aktuelne verzije, ili `noindex` + izbaciti iz sitemapa.
Plugin „Duplicate Page" je aktivan — verovatno je tako i nastalo; vredi proveriti ima li još kopija.

### 2.5 Mrtav Universal Analytics se i dalje učitava
`UA-179394377-1` je i dalje u kodu. Google Analytics Universal je ugašen jula 2023 —
ovo je čisto trošenje performansi i pravi zabunu. Postoji GA4 (`G-SFXW7G5GZC`) i GTM (`GTM-PCJ3KQ69`).

**Fix:** ukloniti UA tag.

---

## 3. Ozbiljni problemi (P1)

### 3.1 Ne postoji nijedna stranica pojedinačnog vozila
Cela zaliha stoji na jednoj stranici — `/odmah-dostupna-vozila/`, **378 KB HTML-a**,
28 vozila, 78 slika, 197 internih linkova. U sitemapu nema nijednog custom post type-a za vozila.

Posledica: sajt ne može da rangira ni za jedan upit tipa `renault austral techno novi sad`
ili `polovni renault clio novi sad`. To je dugi rep koji kod dilera nosi većinu organskog saobraćaja,
i trenutno je nula.

**Fix (veći zahvat, najveći dugoročni povraćaj):** custom post type „Vozilo",
jedna stranica po vozilu, sa `Vehicle`/`Car` + `Offer` schema (cena, kilometraža,
godište, gorivo, menjač). Ovo je i preduslov da vozila uđu u Google Vehicle Listings
i da ih AI asistenti mogu citirati.

### 3.2 Nijedna cena nije objavljena
Ni tehnički pregled, ni šlep, ni servisni paketi, ni vozila. A `cena` je najčešći
modifikator u lokalnim upitima za obe te usluge.

Ovo je istovremeno CRO problem (posetilac odlazi da traži cenu drugde) i GEO problem
(AI asistent koji odgovara na „koliko košta tehnički pregled u Novom Sadu" nema šta da citira,
pa citira Wolf ili nekog ko je cenu napisao).

**Fix:** objaviti bar cenu tehničkog pregleda po kategoriji vozila i polaznu cenu šlepa
u gradu. Ako je cena promenljiva — objaviti opseg, ne ništa.

### 3.3 Alt tekstovi na slikama
Oko polovine slika nema alt atribut:

| Stranica | Slika ukupno | Bez alt-a |
|---|---|---|
| `/` | 104 | **80** |
| `/odmah-dostupna-vozila/` | 78 | 38 |
| `/akcije-old/` | 46 | 36 |
| `/naslovna-old/` | 42 | 32 |
| `/nissan/` | 36 | 26 |
| `/usluge/*` | 25 | 15 |
| `/o-nama/` | 28 | 12 |

Za auto sajt slike su sadržaj — Google Images za `renault austral novi sad` je realan izvor saobraćaja.

### 3.4 Meta description — nedostaju ili su auto-generisane
- **Nedostaju potpuno:** `/polovna-vozila/`, `/prodaja/polovna-vozila/`, `/renault/`, `/dacia/`
- **Prazna:** `/usluge/pomoc-na-putu/`
- **Auto-generisane iz prvog pasusa, besmislene kao opis:**
  - `/prodaja/nova-vozila/` → „Izdvajamo iz ponude"
  - `/odmah-dostupna-vozila/` → „RENAULT AUSTRAL Techno"
  - `/nissan/` → „Elektrificirani porodični crossover sa 5 ili 7 sedišta..."

### 3.5 Tri jezika na jednoj stranici
`/usluge/pomoc-na-putu/` sadrži srpsku, englesku i nemačku verziju teksta u istom telu stranice
(H2 na sva tri jezika). Nema `hreflang` na sajtu. Google ne zna koji je jezik stranice.

**Fix:** ostaviti srpski kao glavni; ako su EN/DE potrebni zbog stranaca u kvaru na auto-putu
(što je legitimno za šlep službu), razdvojiti u zasebne URL-ove sa `hreflang`.

### 3.6 Tanak sadržaj na brend stranicama
`/renault/` i `/dacia/` imaju ~415 reči ukupno u HTML-u — a to uključuje meni, footer i
boilerplate. Stvarnog sadržaja ima svega nekoliko rečenica. `/renault/` nema ni H1 ni ijedan H2.

---

## 4. AI pretraga / GEO

| Provera | Rezultat |
|---|---|
| AI botovi u robots.txt | **16 od 16 dozvoljeno** (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Google-Extended...) — dobro, ništa nije slučajno blokirano |
| `llms.txt` | **404 — ne postoji** |
| `llms-full.txt` | **404 — ne postoji** |
| Struktuirani podaci koje AI može da citira | Slabi — nema cena, nema radnog vremena u schemi, nema FAQ, nema ocena |

Zaključak: **vrata su otvorena, ali kuća je prazna.** AI asistenti smeju da čitaju sajt,
ali na njemu nema nijedne činjenice koju bi vredelo citirati — ni cene, ni radnog vremena
u mašinski čitljivom obliku, ni odgovora na konkretna pitanja.

**Fix, redosledom vrednosti:**
1. `openingHoursSpecification` + `telephone` + `AutoDealer` schema (činjenice koje AI najčešće traži)
2. FAQ sekcije sa `FAQPage` schema na `/usluge/tehnicki-pregled/`, `/servis/`, `/usluge/pomoc-na-putu/`
   — pitanja preuzeti direktno iz autocomplete modifikatora (cena, radno vreme, koliko traje, šta treba poneti)
3. Objaviti cene
4. `llms.txt` sa listom ključnih stranica

---

## 5. Tehnički nalazi

**Šta je dobro — ne dirati:**
- **0 pokvarenih internih linkova** od 308 proverenih na 7 stranica
- Sitemap uredan i prijavljen u `robots.txt` (Rank Math, 3 sitemapa)
- HTTPS ispravan, kanonski tagovi postoje na svim stranicama
- `lang="sr-RS"` ispravno postavljen, latinica preko plugina
- Meta robots direktive u redu (`max-image-preview:large` postavljen)
- Server odgovara 200 na sve UA-ove uključujući Googlebot i AI botove — nema slučajnog blokiranja

**Šta zabrinjava:**
- **Težina stranica:** naslovna 253 KB čistog HTML-a, `/odmah-dostupna-vozila/` **378 KB**.
  Elementor Pro + Slider Revolution + 9 eksternih skripti.
- **Duplirani pluginovi za forme:** Contact Form 7 **i** Forminator su oba aktivni.
  Dvostruko opterećenje, jedan treba ugasiti.
- **Nema plugina za optimizaciju slika.** Autoptimize radi CSS/JS, ali slike nisu obrađene —
  a sajt ih ima na stotine.
- **`Duplicate Page` plugin je aktivan** i verovatno je izvor `-old` stranica.

**Nije izmereno:** Core Web Vitals i Lighthouse SEO score — Google PageSpeed API
je vratio 429 (dnevna kvota potrošena, `project_number:583797351490`). Ponoviti sutra.
Na osnovu težine HTML-a i broja skripti, očekivanje je slab LCP na mobilnom, ali to je
procena, ne merenje.

**Nedostupno:** live SERP provera (`serp_check`) — nema DataForSEO kredencijala u MCP-u.
Zbog toga ne mogu da potvrdim ko trenutno rangira za ciljne upite ni da li se pojavljuje AI Overview.

---

## 6. Sadržaj i blog

136 objava u `post-sitemap.xml`, aktivno se objavljuje (poslednja: 30.06.2026).

Problem nije količina nego ugao. Objave su uglavnom prepričane fabričke promocije —
„Renault Clio V", „Nissan Qashqai Acenta", „Renault Symbioz — upoznajte ga iz prve ruke",
sajamske ponude, praznične čestitke. Taj sadržaj već postoji na renault.rs i nissan.rs
u boljoj verziji, sa jačim domenom. Stojanov Auto ne može da pobedi fabriku na fabričkoj temi.

Ono što Stojanov Auto može, a fabrika ne: **lokalno i uslužno**.
- „Koliko košta tehnički pregled u Novom Sadu 2026 — po kategorijama vozila"
- „Šta poneti na tehnički pregled i registraciju"
- „Kada Renault mora u ovlašćeni servis da bi garancija ostala važeća"
- „Cena servisa Dacia Sandero — šta ulazi u mali, a šta u veliki servis"
- „Šlep služba u Novom Sadu — kada zvati, koliko košta, šta pokriva osiguranje"

Ovo su teme sa lokalnom namerom i komercijalnom vrednošću, na kojima nema konkurencije
od strane fabrike.

Izuzetak koji vredi pohvaliti: „U sećanje na Branka Stojanova" (jan 2026) — jedini
autentično lokalni, ljudski sadržaj na sajtu.

---

## 7. Šta ovaj audit ne može da vidi

Bez GSC i GA4 pristupa nedostaju:

- koje stranice već donose saobraćaj (dakle koje ne smemo dirati pri izmenama)
- ključne reči na pozicijama 5–15 — najisplativije brze pobede
- stvarni CTR po stranici i gde naslovi gube klikove
- koliko organskog saobraćaja uopšte ima i da li konvertuje
- da li postoji pad saobraćaja i od kada
- indeksacioni status — koliko od 176 URL-ova je uopšte u indeksu

Zbog toga je prioritizacija u ovom dokumentu rađena po **veličini problema**,
a ne po **veličini gubitka** — što je slabija osnova. GA4 već postoji na sajtu
(`G-SFXW7G5GZC`), pa je pristup pitanje jednog klika kod klijenta kada bude spreman.

Dodatno: **Google Business Profile nije proveren** — a za ovaj biznis je to verovatno
kanal broj jedan, jer local pack stoji iznad organskih rezultata za sve ciljne upite.
Ovo treba uraditi u sledećem koraku bez obzira na GSC/GA4.

---

## 8. Predloženi redosled rada

**Faza 1 — brzo, u WP-u, bez rizika (1–2 dana)**
1. Naslovi i meta description za 12 ključnih stranica (Rank Math)
2. H1 na naslovnu, `/renault/`, `/dacia/`
3. 301 redirekcije: `/prodaja/polovna-vozila/`, `/naslovna-old/`, `/akcije-old/` (Redirection plugin)
4. Ukloniti UA-179394377-1
5. Alt tekstovi na naslovnoj (80 slika) i `/odmah-dostupna-vozila/` (38)

**Faza 2 — schema i GEO (2–3 dana)**
6. `AutoDealer` + `AutoRepair` schema sa punom adresom, radnim vremenom, telefonom, `sameAs`
7. Isključiti `Article` schema na stranicama
8. FAQ sekcije + `FAQPage` schema na 3 uslužne stranice
9. `llms.txt`

**Faza 3 — sadržaj i konverzija**
10. Objaviti cene tehničkog pregleda i šlepa
11. Prepisati `/servis/`, `/usluge/tehnicki-pregled/`, `/polovna-vozila/` sa lokalnim uglom
12. Google Business Profile audit i optimizacija
13. Blog preusmeriti sa fabričkih tema na lokalne uslužne

**Faza 4 — veći razvoj**
14. Custom post type za vozila, stranica po vozilu, `Vehicle`/`Offer` schema
15. Optimizacija performansi (slike, gašenje jednog form plugina)

**Kada stigne GSC/GA4** — prioritizacija se revidira po stvarnom saobraćaju,
pa se dodaje sloj quick wins, kanibalizacije i content decay analize.

---

*Baseline audit, bez GSC/GA4 podataka. Izvori: skrejp sajta 2026-08-05,
WP REST API, `aeo_ai_bots_robots_audit`, `aeo_llms_txt_check`, `schema_extract_url`,
`migration_broken_internal_links`, `google_suggest` (hl=sr, gl=RS).*
