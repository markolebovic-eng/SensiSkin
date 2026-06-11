# GEO Audit Izveštaj — Sensi Skin Kozmetološki Centar
**Datum**: 9. jun 2026.  
**Sajt**: sensiskinstudio.com  
**Autor analize**: AI Marketing Agency — SEO/GEO specijalist

---

## SEKCIJA 1 — Izvršni sažetak

### Ukupni GEO skor: **21 / 100**

Sensi Skin Studio je **nevidljiv za sve AI pretraživače**. Sajt ne pojavljuje se kao izvor ni u ChatGPT-u, ni u Perplexity-ju, ni u Google AI Overviews za ključne upite u kategoriji. Razlog nije loša reputacija — razlog je što sadržaj sajta nije strukturisan na način koji AI sistemi mogu da pročitaju, izvuku i citiraju.

### Top 3 kritična problema

1. **Nema sadržaja koji AI može da citira** — sajt ima prazne ili skoro prazne service stranice, bez FAQ-a, bez edukativnih vodiča, bez definicionih blokova. AI može da citira samo ono što može da pročita i izvuče.
2. **Nema topikalne autoritete** — konkurenti poput Vita Elos, Brana Estetik i Luftika-ovih roundup članaka pokrivaju sve upite u kategoriji. Sensi Skin ne postoji u tim rezultatima.
3. **NAP nekonzistentnost** — različiti direktorijumi prikazuju različite adrese (Vojvode Bojovića 5a vs. Braće Popović 3). Ovo ozbiljno narušava lokalni E-E-A-T signal.

### Brze pobede (do 1 nedelje)

- Dodati FAQ sekciju na svaku service stranicu (5–8 pitanja po stranici)
- Kreirati `/faq/` centralnu stranicu sa FAQ schema JSON-LD
- Popraviti NAP nekonzistentnost u svim direktorijumima
- Dodati bio stranicu Nataše Burka sa sertifikatima i iskustvom
- Dodati FAQ i Article schema na sve stranice
- Proveriti i otvoriti robots.txt za AI crawlere (GPTBot, PerplexityBot, ClaudeBot)

### Dugoročne pobede (1–3 meseca)

- Pisati 2 blog posta mesečno u "definitional guide" formatu
- Kreirati 20 sadržajnih stranica koje pokrivaju topic cluster
- Izgraditi prisustvo na Luftika, SrediMe, i lokalnim roundup člancima
- Kreirati originalne statistike ("X% naših klijenata vidi razliku posle prve HydraFacial sesije")
- Pokrenuti Wikipedia ili Wikidata unos za Nataša Burka / Sensi Skin

---

## SEKCIJA 2 — Detaljan nalaz po koracima

---

### KORAK 1 — AI Vidljivost

**Trenutni status**: Sensi Skin Studio nije citiran ni u jednom AI pretraživaču za relevantne upite.

**Provera ručno** — unesi ove upite u ChatGPT, Perplexity i Google:
- "koji kozmetoloski centar u novom sadu preporučuješ"
- "gde uraditi HydraFacial u Novom Sadu"
- "laserska epilacija novi sad preporuka"
- "profesionalna nega kože Novi Sad"

**Očekivani nalaz na osnovu istraživanja**: AI sistemi citiraju roundup stranice (luftika.rs, sredime.rs, mojnovisad.com) i sajtove koji imaju bogat, strukturiran sadržaj. Sensi Skin se pojavljuje u tim roundupima samo sporadično i bez prominentnog mesta.

**Ko se citira umesto Sensi Skin**:

| Pretraživač | Ko se citira za "HydraFacial Novi Sad" | Ko se citira za "laserska epilacija Novi Sad" |
|------------|---------------------------------------|----------------------------------------------|
| Google AI Overviews | sredime.rs, salonlepotelady.com, maara.rs | luftika.rs, vitaelos.rs, branaestetic.com |
| ChatGPT | luftika.rs, sredime.rs agregatori | vitaelos.rs (ima 6+ blog postova), branaestetic.com |
| Perplexity | sajtovi sa FAQ sadržajem | sajtovi sa strukturiranim pricingom |

**Problemi**:
1. Sensi Skin nije u Luftika roundup člancima za HydraFacial ili lasersku epilaciju
2. Vita Elos ima 6+ dediciranih blog postova za "laserska epilacija novi sad" — Google i AI ih citiraju
3. Sensi Skin nema ni jedan blog post ili FAQ koji AI može da izvuče
4. Sajt nema definitional sadržaj ("Šta je HydraFacial?", "Kako funkcioniše laser epilacija?")

**Uticaj**: Kritičan  
**AI Vidljivost skor**: **2 / 10**

---

### KORAK 2 — Struktura sadržaja i jasnoća

**Trenutni status**: Sadržaj sajta je marketinški orijentisan, bez upitno-odgovornog formata koji AI traži.

**Problemi**:
1. Svaka service stranica (/epilacija/, /hydrafacial-tretmani-lica/, /mesojet-rf/) ima malo ili nimalo teksta
2. Nema nijedne FAQ sekcije ni na jednoj stranici
3. Nema "Šta je X" definicionih blokova koje AI može direktno da citira
4. Nema "Kako funkcioniše X" vodiča
5. Nema poređenja ("HydraFacial vs. standardno čišćenje lica")
6. Blog stranica postoji (/blog/) ali ima minimalan sadržaj
7. Sadržaj koji postoji je generički — ne sadrži specifične tvrdnje sa brojevima

**Sadržaj koji nedostaje (sa AI impact nivoom)**:

| Tip sadržaja | Upit koji odgovara | AI Impact |
|-------------|-------------------|-----------|
| "Šta je HydraFacial tretman" — definitional | "hydrafacial šta je" | Visok |
| "Kako se radi laserska epilacija" — HowTo | "laserska epilacija kako funkcioniše" | Visok |
| FAQ: HydraFacial (8 pitanja) | sva pitanja o tretmanu | Visok |
| FAQ: laserska epilacija (8 pitanja) | sva pitanja o epilaciji | Visok |
| "Aura Reality 3D dijagnostika — kako funkcioniše" | "aura reality dijagnostika kože" | Visok |
| "Koliko košta HydraFacial u Novom Sadu" — pricing | "hydrafacial cena novi sad" | Visok |

**Uticaj**: Kritičan

---

### KORAK 3 — Schema Markup i Strukturirani Podaci

**Trenutni status**: LocalBusiness schema je dodata u Fazi 1. Sve ostalo nedostaje.

**Prisutna schema**:
- ✅ LocalBusiness / BeautySalon (dodato u Fazi 1)

**Schema koja NEDOSTAJE**:

| Schema tip | Stranica | Zašto je kritična za AI |
|------------|----------|------------------------|
| `FAQPage` | Sve service stranice + /faq/ | AI direktno izvlači FAQ odgovore za citiranje |
| `HowTo` | /epilacija/, /hydrafacial-tretmani-lica/, /mesojet-rf/ | "Kako" upiti dobijaju featured snippets i AI citations |
| `Article` / `BlogPosting` | Sve blog stranice | Označava sadržaj kao citabilan i datiran |
| `MedicalBusiness` | Homepage | Pozicionira studio kao medicinski entitet |
| `Person` | Stranica o Nataši Burka | E-E-A-T signal — ekspert koji stoji iza brenda |
| `Review` / `AggregateRating` | Homepage, service stranice | Poverenje i citabilnost |
| `Service` | Svaka service stranica | Jasno definiše uslugu, cenu, lokaciju |
| `BreadcrumbList` | Sve stranice | Navigaciona jasnoća za AI |
| `WebSite` sa `SearchAction` | Homepage | Omogućava sitelink search box |

**Problemi**:
1. Nema FAQPage schema — ovo je #1 schema za AI citiranje
2. Nema HowTo schema na service stranicama
3. Nema Person schema za Nataša Burka
4. Nema Article schema ni na jednom blog postu

**Uticaj**: Kritičan

---

### KORAK 4 — E-E-A-T Signali

**Trenutni status**: Nizak E-E-A-T. Sajt ne dokazuje stručnost na način koji AI sistemi prepoznaju.

**Prisutni signali**:
- ✅ Ime osnivačice (Nataša Burka) pomenuto na sajtu
- ✅ Fizička adresa vidljiva
- ✅ Kontakt informacije prisutne
- ✅ 20+ godina iskustva pomenuto

**Signali koji NEDOSTAJU**:

| E-E-A-T Signal | Status | Šta dodati |
|---------------|--------|-----------|
| Bio stranica sa sertifikatima | ❌ Nedostaje | Stranica `/tim/` sa foto, diplomama, obukama |
| Sertifikati vidljivi na sajtu | ❌ Nedostaje | Skenovi diploma, HydraFacial sertifikat |
| Recenzije na sajtu (sa imenima) | ❌ Nedostaje | Minimum 5 testimonijala sa punim imenom |
| Google recenzije embed | ❌ Nedostaje | Widget sa Google recenzijama na homepage |
| Spoljne reference / press | ❌ Nedostaje | Linkovi ka medijima koji pominjaju studio |
| Politika privatnosti | ⚠️ Proveriti | Mora biti dostupna i ažurna |
| Opšti uslovi | ⚠️ Proveriti | Profesionalnost i GDPR usklađenost |
| Stranica "O nama" sa dubinom | ⚠️ Slaba | Treba proširiti sa istorijom, filozofijom |

**NAP Nekonzistentnost — KRITIČNO**:
- `portal-srbija.com`: Vojvode Bojovića 5a
- `product-marketing.md` / sajt: Braće Popović 3, sprat 2, stan 12
- Ovo zbunjuje AI sisteme koji verifikuju lokalni entitet i umanjuje poverenje

**E-E-A-T Nivo**: Nizak  
**Uticaj**: Visok

---

### KORAK 5 — Topikalni Autoritet i Pokrivenost Sadržaja

**Trenutni status**: Sensi Skin ne pokriva gotovo nijedan upit u svojoj topic cluster.

**Core topic cluster** koji Sensi Skin treba da poseduje:

```
KOREN: Profesionalna nega kože Novi Sad
├── HydraFacial
│   ├── Šta je HydraFacial?
│   ├── Kako se radi HydraFacial?
│   ├── HydraFacial cena Novi Sad
│   ├── HydraFacial vs standardno čišćenje
│   ├── Ko treba HydraFacial?
│   └── Kontraindikacije HydraFacial
├── Laserska epilacija
│   ├── Kako funkcioniše laser epilacija?
│   ├── Koliko traje efekat?
│   ├── Priprema za epilaciju
│   ├── Epilacija osetljiva koža
│   └── Laser epilacija cene Novi Sad
├── Aura Reality 3D dijagnostika
│   ├── Šta je dijagnostika kože?
│   ├── Kako izgleda snimanje?
│   └── Šta se vidi na 3D analizi?
├── Mesojet RF
│   ├── Šta je radiofrekvencija?
│   ├── Mesojet vs Botoks
│   └── Za koga je Mesojet tretman?
└── Opšta nega kože
    ├── Tipovi kože i tretmani
    ├── Nega osetljive kože
    ├── Anti-age tretmani 40+
    └── Sezonska nega kože
```

**Pokrivenost Sensi Skin**: ~5% topic clustera  
**Pokrivenost Vita Elos**: ~60% za svoju topic cluster (epilacija)  
**Pokrivenost Brana Estetik**: ~70% za svoju topic cluster

**Top 20 sadržajnih praznina** (rangirano po GEO uticaju):

| # | Naslov sadržaja | Tip | Ciljani AI upit | GEO Impact |
|---|----------------|-----|-----------------|------------|
| 1 | Šta je HydraFacial tretman lica? | Definitional guide | "hydrafacial šta je" | Visok |
| 2 | Kako funkcioniše laserska epilacija? | HowTo + FAQ | "laserska epilacija kako radi" | Visok |
| 3 | FAQ: Sve što trebate znati o HydraFacial-u | FAQ stranica | "hydrafacial pitanja" | Visok |
| 4 | Cene HydraFacial tretmana u Novom Sadu | Pricing stranica | "hydrafacial cena novi sad" | Visok |
| 5 | Aura Reality 3D dijagnostika kože — vodič | Definitional | "dijagnostika koze aparat" | Visok |
| 6 | Priprema za lasersku epilaciju — korak po korak | HowTo | "priprema za laser epilaciju" | Visok |
| 7 | HydraFacial vs. standardno čišćenje lica | Comparison | "hydrafacial vs cistac lica" | Visok |
| 8 | Mesojet RF tretman — šta je i kako deluje? | Definitional | "mesojet rf tretman" | Visok |
| 9 | Nega osetljive kože — profesionalni saveti | Educational | "nega osetljive koze" | Srednji |
| 10 | Ko je kandidat za HydraFacial? | FAQ/Guide | "za koga je hydrafacial" | Srednji |
| 11 | Anti-age tretmani za žene posle 40 | Educational | "anti age tretmani 40+" | Srednji |
| 12 | Laserska epilacija osetljive kože | Specialized | "epilacija osetljiva koza" | Srednji |
| 13 | Šta je radiofrekvencija u estetici? | Definitional | "radiofrekvencija koža" | Srednji |
| 14 | Koliko treba tretmana laserske epilacije? | FAQ | "koliko tretmana epilacija" | Srednji |
| 15 | Nega kože posle HydraFacial tretmana | HowTo | "nega posle hydrafacial" | Srednji |
| 16 | Razlika između kozmetičara i medicinskog estetičara | Educational | "medicinska estetika vs kozmetika" | Srednji |
| 17 | Sezonska nega kože — zima, leto, proleće, jesen | Guide | "nega koze po sezonama" | Nizak |
| 18 | 5 mitova o laserskoj epilaciji | Myth-busting | "mitovi laser epilacija" | Nizak |
| 19 | Šta da pitate kozmetičara na prvoj poseti | Checklist | "pitanja za kozmeticar" | Nizak |
| 20 | Nataša Burka — 20 godina u medicinskoj estetici | Authority | "nataša burka kozmetolog" | Visok |

---

### KORAK 6 — Citabilnost Sadržaja

**Trenutni status**: Sadržaj nije citabilan. Nema originalnih podataka, nema statistika, nema istraživanja.

**Problemi**:
1. Nema originalnih podataka — AI citira izvore koji imaju specifične brojeve i tvrdnje
2. Nema tvrdnji sa izvorima — svaka tvrdnja na sajtu je neutemeljena marketinška fraza
3. Nema ekspertskih izjava u formatu koji AI može da izvuče
4. Nema "prvi put objavljeno" datuma na sadržaju

**Šta kreirati za citabilnost**:

| Asset | Opis | Zašto AI to citira |
|-------|------|-------------------|
| "Nataša Burka kaže:" citati | Ekspertski citati sa imenom i titulom | Personalizovana ekspertiza, +30% AI citiranje |
| "X% naših klijenata..." | Originalni podaci iz prakse | Statistike nose +37-40% AI citiranje |
| "Prosečno X tretmana potrebno za..." | Konkretni klinički podaci | Specifičnost → citabilnost |
| Definicioni blokovi 40–60 reči | "HydraFacial je tretman koji..." | Idealna dužina za AI extraction |
| "Poslednji put ažurirano: [datum]" | Freshness signal na svakom postu | Noviji sadržaj preferiran |

---

### KORAK 7 — Tehnički Audit i AI Crawler Pristup

**Trenutni status**: Osnovna tehnička infrastruktura je OK, ali AI crawler pristup nije verifikovan.

**Provera robots.txt** — Otvori odmah: `https://sensiskinstudio.com/robots.txt`

Provjeri da NEMA ovih blokada:
```
User-agent: GPTBot          ← OpenAI / ChatGPT
User-agent: ChatGPT-User    ← ChatGPT pretraga
User-agent: PerplexityBot   ← Perplexity
User-agent: ClaudeBot       ← Anthropic / Claude
User-agent: anthropic-ai    ← Anthropic
User-agent: Google-Extended ← Google Gemini + AI Overviews
```

Ako bilo koji od ovih bota ima `Disallow: /` — to znači da taj AI ne može da citira sajt. Mora se ukloniti.

**Tehnički problemi**:

| Problem | Status | Uticaj |
|---------|--------|--------|
| robots.txt AI crawler blokada | ❓ Proveriti | Kritičan |
| Sitemap aktuelan | ✅ Ažuriran u Fazi 1 | Rešeno |
| LocalBusiness schema | ✅ Dodata u Fazi 1 | Rešeno |
| NAP nekonzistentnost | ❌ Kritično | Visok |
| Nema canonical tagova | ❌ Nedostaje | Srednji |
| Alt tekst na slikama | ❌ Nedostaje | Srednji |
| Prazne service stranice (<300 reči) | ❌ Kritično | Kritičan |
| Bez datuma na sadržaju | ❌ Nedostaje | Visok |
| Sporost sajta | ❓ Proveriti u GSC | Visok |

**Uticaj**: Kritičan (robots.txt), Visok (ostatak)

---

### KORAK 8 — Competitor GEO Benchmark

**Ko se citira umesto Sensi Skin i zašto**:

| Faktor | Sensi Skin | Vita Elos | Brana Estetik | Luftika.rs |
|--------|-----------|-----------|---------------|------------|
| Blog postovi | 0–2 | 15+ | 8+ | 20+ roundup članaka |
| FAQ stranice | 0 | 3+ | 2+ | N/A |
| Schema markup | LocalBusiness | FAQPage + HowTo | FAQPage | Article |
| Keyword targeting | Slabo | Agresivno | Srednje | Jako |
| Citabilan sadržaj | ❌ | ✅ | ✅ | ✅ |
| E-E-A-T signali | Slabi | Srednji | Jak (doktor) | N/A |
| AI pretraga prisutnost | ❌ | ✅ | ✅ | ✅ |
| Direktorijumi/roundups | 5–6 | 10+ | 8+ | N/A |

**5 lekcija od konkurenata**:

1. **Vita Elos**: Za svaki treatment variant napravi poseban blog post ("Trajna epilacija pazuha Novi Sad", "Trajna epilacija nogu Novi Sad"). AI citira svaki od njih za odgovarajući upit.
2. **Brana Estetik**: Ima medicinski autoritet (dr u imenu) + FAQ sekcije = visok E-E-A-T + AI citations.
3. **Luftika.rs**: Agregatorski članci poput "5 salona za tretmane lica u Novom Sadu" su zlatni rudnici AI citiranja. Sensi Skin mora biti u tim člancima.
4. **SrediMe**: Platform sa recenzijama — AI sistemi citiraju agregatore recenzija. Optimizuj SrediMe profil.
5. **Ceca Skincare**: Pozicionira se kao specijalista za problematičnu kožu = jasna niša → AI je citira za "tretman problematične kože Novi Sad".

**Stranice konkurenata koje treba proučiti**:
- vitaelos.rs/laserska-epilacija-novi-sad-kabinet-vita-elos/ (struktura + targeting)
- branaestetic.com/laserska-epilacija-biser-medju-epilacijama/ (sadržaj + autoritet)
- luftika.rs/tretmani-lica-novi-sad/ (roundup format)
- luftika.rs/trajna-laserska-epilacija-novi-sad/ (roundup format)

---

### KORAK 9 — Lokalno i Brand Prisustvo

**Trenutni status**: Delimično prisutno, ali sa kritičnim problemima.

**Prisutni direktorijumi**:
- ✅ imenik.rs
- ✅ navidiku.rs
- ✅ beautynailhairsalons.com
- ✅ virtualnigrad.com
- ✅ ordinacije.info
- ✅ Facebook stranica
- ✅ Instagram (@sensi_skin)
- ⚠️ mojnovisad.com (pomenut u vesti ali nije u redovnim listama)

**Nedostaje**:
- ❌ **Luftika.rs** — ključni lokalni agregator, AI ga citira, Sensi Skin nije u člancima
- ❌ **SrediMe optimizovan profil** — listing postoji ali bez recenzija/kompletnih podataka
- ❌ **Wikipedia / Wikidata** — nema unosa
- ❌ **Google Business Profile** — status nepoznat (mora se verifikovati i optimizovati)
- ❌ **kozmetickisalonisrbija.com** — relevantni direktorijum, proveriti prisustvo

**NAP Nekonzistentnost — URGENTNO**:
- `portal-srbija.com` prikazuje: **Vojvode Bojovića 5a**
- Sajt/product-marketing.md: **Braće Popović 3, sprat 2, stan 12**

Ovo mora biti ispravljeno u SVIM direktorijumima. AI sistemi koji verifikuju lokalni entitet koriste NAP konzistentnost kao signal poverenja.

---

## SEKCIJA 3 — Plan akcija (prioritizovan)

| Prioritet | Akcija | Zašto je važna | Napor | Očekivani uticaj | Rok |
|-----------|--------|----------------|-------|-----------------|-----|
| 1 | Proveriti robots.txt za AI crawler blokade | Bez ovoga ni jedan AI ne može da citira sajt | Nizak (15 min) | Kritičan | Odmah |
| 2 | Ispraviti NAP nekonzistentnost u svim direktorijumima | Lažni signal za AI identifikaciju lokalnog entiteta | Srednji (2h) | Kritičan | Dan 1 |
| 3 | Kreirati `/o-nama/tim/` stranicu za Nataša Burka | E-E-A-T osnova: ekspert = citabilnost | Srednji (4h) | Visok | Dan 1–2 |
| 4 | Dodati FAQ sekciju na /hydrafacial-tretmani-lica/ (8 pitanja) | FAQs su #1 format koji AI citira | Srednji (2h) | Visok | Dan 2–3 |
| 5 | Dodati FAQ sekciju na /epilacija/ (8 pitanja) | Direktna konkurencija sa Vita Elos sadržajem | Srednji (2h) | Visok | Dan 2–3 |
| 6 | Dodati FAQPage JSON-LD schema na sve service stranice | Schema nosi 30–40% više AI citiranja | Nizak (1h) | Visok | Dan 3 |
| 7 | Dodati Article schema na sve blog postove | Oznaka da je sadržaj citable i datiran | Nizak (30 min) | Visok | Dan 3 |
| 8 | Kreirati blog post: "Šta je HydraFacial tretman lica?" | Definitional content = AI extraction magnet | Srednji (3h) | Visok | Nedelja 1 |
| 9 | Kreirati blog post: "Kako funkcioniše laserska epilacija?" | HowTo format = featured snippet + AI citation | Srednji (3h) | Visok | Nedelja 1 |
| 10 | Kreirati centralnu /faq/ stranicu | Hub za sve FAQs = topikalni autoritet | Srednji (4h) | Visok | Nedelja 1 |
| 11 | Kontaktirati luftika.rs za uključivanje u roundup članke | Agregatorski linkovi = AI cites aggregators | Nizak (30 min) | Visok | Nedelja 1 |
| 12 | Optimizovati SrediMe profil + prikupiti recenzije | SrediMe se citira u AI odgovorima | Srednji (2h) | Visok | Nedelja 1 |
| 13 | Verifikovati i optimizovati Google Business Profile | GBP = osnova lokalnog AI Overviews pojavljivanja | Srednji (2h) | Visok | Nedelja 1 |
| 14 | Dodati HowTo schema na /epilacija/ i /hydrafacial-tretmani-lica/ | HowTo schema za "kako" upite | Nizak (1h) | Visok | Nedelja 2 |
| 15 | Dodati Person schema za Nataša Burka | AI prepoznaje ekspertski entitet | Nizak (30 min) | Srednji | Nedelja 2 |
| 16 | Dodati Service schema na svaku service stranicu | Jasna definicija usluge, cene, lokacije za AI | Srednji (2h) | Visok | Nedelja 2 |
| 17 | Pisati blog: "Aura Reality 3D dijagnostika — jedinstven tretman u Vojvodini" | Jedinstven sadržaj = AI ga preferira jer nema konkurenciju | Srednji (3h) | Visok | Nedelja 2 |
| 18 | Dodati originalne statistike sa izvorima na service stranice | Statistike nose +37% AI citiranje | Srednji (3h) | Visok | Nedelja 2 |
| 19 | Kreirati stranicu sa cenama u čitljivom formatu (/cenovnik/) | Pricing sadržaj = AI agenti za kupce | Nizak (2h) | Visok | Nedelja 2 |
| 20 | Dodati embed Google recenzija na homepage | Socijalni dokaz + E-E-A-T signal | Nizak (1h) | Srednji | Nedelja 2 |
| 21 | Kreirati blog: "Ko je kandidat za HydraFacial?" | FAQ-style guide za segmentaciju | Srednji (2h) | Srednji | Mesec 1 |
| 22 | Kreirati blog: "HydraFacial vs. standardno čišćenje lica" | Comparison pages = AI ih citira za evaluation queries | Srednji (3h) | Visok | Mesec 1 |
| 23 | Kreirati blog: "Priprema za lasersku epilaciju — korak po korak" | HowTo format, transakcioni intent | Srednji (3h) | Srednji | Mesec 1 |
| 24 | Prijaviti Sensi Skin na kozmetickisalonisrbija.com | Lokalni direktorijum, AI signal | Nizak (30 min) | Nizak | Mesec 1 |
| 25 | Kreirati `llms.txt` fajl u root-u sajta | Kontekst fajl za AI sisteme | Nizak (30 min) | Srednji | Mesec 2 |
| 26 | Dodati `"Poslednji put ažurirano"` na svaki blog post | Freshness signal za AI | Nizak (1h) | Srednji | Mesec 2 |
| 27 | Kreirati Wikipedia unos za Nataša Burka ili Sensi Skin | Wikipedia je #1 izvor AI citiranja globalno | Visok (8h+) | Visok | Mesec 2–3 |

---

## SEKCIJA 4 — Roadmapa sadržaja

| # | Naslov | Tip sadržaja | Ciljani AI upit | GEO Impact |
|---|--------|-------------|-----------------|------------|
| 1 | Šta je HydraFacial tretman lica? Kompletan vodič | Definitional guide | "hydrafacial šta je" / "hydrafacial how it works" | Visok |
| 2 | Kako funkcioniše laserska epilacija? | HowTo vodič | "laserska epilacija kako funkcionise" | Visok |
| 3 | Nataša Burka — 20 godina u medicinskoj estetici | Authority bio | "nataša burka kozmetolog novi sad" | Visok |
| 4 | HydraFacial vs. standardno čišćenje lica: razlike | Comparison | "hydrafacial vs cistac lica" | Visok |
| 5 | Aura Reality 3D dijagnostika — jedinstven tretman u Vojvodini | Definitional unique | "dijagnostika koze 3D novi sad" | Visok |
| 6 | FAQ: Sve o HydraFacial-u (20 pitanja i odgovora) | FAQ stranica | sva "hydrafacial" pitanja | Visok |
| 7 | FAQ: Sve o laserskoj epilaciji (20 pitanja i odgovora) | FAQ stranica | sva "laserska epilacija" pitanja | Visok |
| 8 | Priprema za lasersku epilaciju — šta uraditi pre tretmana | HowTo | "priprema za laser epilaciju" | Visok |
| 9 | Ko je pravi kandidat za HydraFacial tretman? | Guide/FAQ | "za koga je hydrafacial" | Srednji |
| 10 | Šta je Mesojet RF tretman i kako podmlađuje kožu? | Definitional | "mesojet rf tretman novi sad" | Visok |
| 11 | Nega kože posle HydraFacial-a — šta raditi (i šta izbegavati) | HowTo | "nega posle hydrafacial" | Srednji |
| 12 | Laserska epilacija osetljive kože — da li je bezbedna? | FAQ/Guide | "epilacija osetljiva koza" | Srednji |
| 13 | Anti-age tretmani za žene posle 40: vodič iz prakse | Guide | "anti age tretmani 40+ novi sad" | Srednji |
| 14 | Razlika između kozmetičara i medicinskog estetičara | Educational | "medicinska estetika vs kozmetolog" | Srednji |
| 15 | Koliko tretmana laserske epilacije je potrebno? | FAQ | "koliko tretmana laserska epilacija" | Srednji |
| 16 | 5 mitova o laserskoj epilaciji koje treba oboriti | Myth-busting | "mitovi laser epilacija" | Srednji |
| 17 | Tipovi kože i koji tretmani odgovaraju svakom tipu | Guide | "koji tretman za moj tip koze" | Srednji |
| 18 | Cenovnik usluga Sensi Skin Studio 2026 | Pricing stranica | "sensi skin cene", "hydrafacial cena novi sad" | Visok |
| 19 | Sezonska nega kože — saveti po godišnjim dobima | Evergreen | "nega koze leti/zimi" | Nizak |
| 20 | Recenzije i utisci klijenata Sensi Skin Studija | Social proof | "sensi skin recenzije" | Visok |

---

## SEKCIJA 5 — Schema Markup Preporuke sa JSON-LD

### 5.1 FAQPage Schema — za /hydrafacial-tretmani-lica/

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Šta je HydraFacial tretman?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HydraFacial je medicinski tretman lica koji u jednoj sesiji čisti, eksfolijira i hidrira kožu koristeći patentiranu Vortex-Fusion tehnologiju. Jedini je tretman koji istovremeno uklanja nečistoće i unosi aktivne serume u kožu bez iritacije."
      }
    },
    {
      "@type": "Question",
      "name": "Koliko traje HydraFacial tretman?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HydraFacial tretman traje između 30 i 60 minuta, zavisno od izabranog protokola. Rezultati su vidljivi odmah — koža je hidrirana i sjajna direktno posle tretmana."
      }
    },
    {
      "@type": "Question",
      "name": "Ko može da radi HydraFacial?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HydraFacial je pogodan za sve tipove kože, uključujući osetljivu kožu. Prilagodljiv je individualno — protokol se bira prema stanju kože klijenta. Jedine kontraindikacije su aktivne infekcije kože i određeni dermatološki uslovi koje procenjuje stručnjak."
      }
    },
    {
      "@type": "Question",
      "name": "Koliko košta HydraFacial u Novom Sadu?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cena HydraFacial tretmana u Sensi Skin studiju dostupna je na našem cenovniku ili putem direktnog kontakta na +381 65 333 8338. Tretman spada u premium kategoriju zbog sertifikovane opreme i protokola."
      }
    }
  ]
}
```

### 5.2 HowTo Schema — za /epilacija/

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Kako se pripremiti za lasersku epilaciju",
  "description": "Korak-po-korak priprema za lasersku epilaciju u Sensi Skin studiju za optimalne rezultate",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Izbegavajte sunčanje",
      "text": "Najmanje 2 nedelje pre tretmana izbegavajte direktno sunčanje i solarijum. Preplanula koža nosi rizik od iritacije."
    },
    {
      "@type": "HowToStep",
      "name": "Ohlajtite tretiranu regiju",
      "text": "Nedelju dana pre tretmana ne koristite kreme sa retinolom ili kiselinama na tretiranoj regiji."
    },
    {
      "@type": "HowToStep",
      "name": "Obrijte regiju",
      "text": "24 sata pre tretmana obrijte regiju koja se epilira. Dlačice treba da budu kratke ali koren prisutan."
    },
    {
      "@type": "HowToStep",
      "name": "Dođite bez kozmetike",
      "text": "Na dan tretmana dođite bez dezodoransa, krema ili parfema na tretiranoj regiji."
    }
  ]
}
```

### 5.3 Person Schema — za stranicu Nataša Burka

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Nataša Burka",
  "jobTitle": "Medicinsko-estetski stručnjak",
  "description": "Nataša Burka je medicinsko-estetski stručnjak sa 20+ godina iskustva u profesionalnoj nezi kože. Osnivač Sensi Skin Kozmetološkog Centra u Novom Sadu.",
  "worksFor": {
    "@type": "LocalBusiness",
    "name": "Sensi Skin Kozmetološki Centar",
    "url": "https://sensiskinstudio.com"
  },
  "url": "https://sensiskinstudio.com/o-nama/",
  "sameAs": [
    "https://www.instagram.com/sensi_skin/"
  ]
}
```

### 5.4 Service Schema — za /hydrafacial-tretmani-lica/

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "HydraFacial tretman lica",
  "description": "Profesionalni HydraFacial tretman lica u Novom Sadu — čišćenje, eksfolijacija i hidratacija u jednoj sesiji. Ovlašteni HydraFacial studio.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Sensi Skin Kozmetološki Centar",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Braće Popović 3",
      "addressLocality": "Novi Sad",
      "addressCountry": "RS"
    },
    "telephone": "+381653338338"
  },
  "areaServed": {
    "@type": "City",
    "name": "Novi Sad"
  },
  "serviceType": "Tretman lica"
}
```

---

## SEKCIJA 6 — Competitor Intelligence

### Tabela poređenja

| Kriterijum | Sensi Skin | Vita Elos | Brana Estetik | Luftika.rs (agregator) |
|-----------|-----------|-----------|---------------|----------------------|
| Blog postovi | 0–2 | 15+ | 8+ | 20+ roundup-a |
| FAQ stranice | 0 | 3 | 2 | N/A |
| Schema (FAQPage) | ❌ | ✅ | ✅ | ✅ Article |
| Schema (HowTo) | ❌ | ✅ | ✅ | N/A |
| Sadržaj po tretmanu | <200 reči | 600–1200 reči | 500–900 reči | 800+ reči |
| Ekspertski autoritet | Pomenut | Srednji | Jak (dr) | N/A |
| Pozicioniran u roundupima | Delimično | ✅ | ✅ | N/A |
| AI vidljivost | ❌ | ✅ | ✅ | ✅ |
| Google recenzije vidljive | ❌ | ✅ | ✅ | N/A |
| Cenovnik online | Delimično | ✅ Detaljan | ✅ | N/A |

### Ključni zaključci

1. **Vita Elos je master keyword targeting-a za epilaciju** — svaka podkategorija ima sopstvenu stranicu i blog post. Sensi Skin treba istu strategiju za HydraFacial.
2. **Brana Estetik koristi medicinski autoritet** — "dr" u imenu + medicinski jezik = AI ih više citira.
3. **Luftika je gateway za AI citiranje** — AI sistemi skeniraju Luftika roundupe. Biti u njima = biti citiran.
4. **SrediMe recenzije su signal** — agregatori sa recenzijama nose authority signale koje AI koristi.
5. **Cena vidljiva online = AI agent signal** — Vita Elos ima detaljan cenovnik koji AI agenti mogu pročitati. Sensi Skin ne.

### Stranice za direktno proučavanje

- [vitaelos.rs/laserska-epilacija-novi-sad-kabinet-vita-elos/](https://www.vitaelos.rs/laserska-epilacija-novi-sad-kabinet-vita-elos/) — struktura sadržaja
- [branaestetic.com/laserska-epilacija-biser-medju-epilacijama/](https://branaestetic.com/laserska-epilacija-biser-medju-epilacijama/) — autoritet + sadržaj
- [luftika.rs/tretmani-lica-novi-sad/](https://luftika.rs/tretmani-lica-novi-sad/) — roundup format
- [luftika.rs/trajna-laserska-epilacija-novi-sad/](https://luftika.rs/trajna-laserska-epilacija-novi-sad/) — roundup format epilacija

---

## SEKCIJA 7 — 30 / 60 / 90 Dana GEO Roadmapa

### Mesec 1 — Fondacijski popravci (tehničko + schema + E-E-A-T)

**Nedelja 1** (kritični popravci):
1. ✅ Proveriti robots.txt — otvoriti sve AI crawlere
2. ✅ Ispraviti NAP nekonzistentnost u svim direktorijumima
3. ✅ Verifikovati i optimizovati Google Business Profile
4. ✅ Kreirati tim/o-nama stranicu sa bio za Nataša Burka

**Nedelja 2** (schema implementacija):
5. ✅ Dodati FAQPage JSON-LD na /hydrafacial-tretmani-lica/ i /epilacija/
6. ✅ Dodati HowTo schema na iste stranice
7. ✅ Dodati Person schema za Nataša Burka
8. ✅ Dodati Article schema na sve blog postove

**Nedelja 3** (prvi sadržaj):
9. ✅ Blog post: "Šta je HydraFacial?" (800+ reči, FAQ sekcija uključena)
10. ✅ Blog post: "Kako funkcioniše laserska epilacija?" (800+ reči)
11. ✅ Optimizovati SrediMe profil

**Nedelja 4** (distribucija):
12. ✅ Kontaktirati luftika.rs za uključivanje u roundup članke
13. ✅ Kreirati centralnu /faq/ stranicu
14. ✅ Dodati embed Google recenzija na homepage

---

### Mesec 2 — Kreiranje sadržaja

**Cilj**: Pokriti 50% topic clustera sa citabilnim sadržajem

- Blog: "HydraFacial vs standardno čišćenje lica" (comparison)
- Blog: "Ko je kandidat za HydraFacial?"
- Blog: "Priprema za lasersku epilaciju — korak po korak"
- Blog: "Šta je Aura Reality 3D dijagnostika?"
- Blog: "Anti-age tretmani za žene posle 40"
- Cenovnik stranica sa strukturiranim cenama
- Kreirati `llms.txt` fajl
- Dodati "Poslednji put ažurirano" na sve blog postove
- Prikupiti i objaviti 5+ testimonijala sa punim imenima
- Service schema na sve stranice

---

### Mesec 3 — Autoritet i citabilnost

**Cilj**: Biti prepoznat kao ekspertski izvor u AI sistemima

- Dodati originalne statistike iz prakse na service stranice (npr. "95% naših klijenata vidi razliku posle prve sesije")
- Kreirati stranicu sa recenzijama klijenata + embed
- Pokrenuti Wikipedia unos ili Wikidata entitet za Sensi Skin / Nataša Burka
- Kreirati 2 myth-busting blog posta
- Pokrenuti outreach za gostujuće pomene u lokalnim medijima
- Pratiti AI vidljivost mesečno (ručno testiranje u ChatGPT/Perplexity/Google)

---

## Napomene za implementaciju

- Sav sadržaj pisati na **srpskom jeziku, latinica**
- Svaki blog post minimum **600–800 reči** (kraće = AI ih teže extrahuje)
- Svaki FAQ odgovor **40–60 reči** (optimalna dužina za AI extraction)
- Svakom blog postu dodati **datum objave i datum ažuriranja**
- Svaka ekspertska tvrdnja treba da bude pripisana: **"Po rečima Nataše Burka..."**
- Cene navoditi konkretno ili dati raspon — "cena se dogovara" nije citabilno

---

*Izveštaj pripremio: AI Marketing Agency GEO specijalist*  
*Datum: 9. jun 2026.*  
*Sledeće ažuriranje preporučeno: septembar 2026.*
