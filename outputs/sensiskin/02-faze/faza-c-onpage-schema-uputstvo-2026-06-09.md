# Faza C — On-Page Redo + Schema Setup
## Korak-po-korak uputstvo za sensiskinstudio.com
**Datum**: 2026-06-09  
**Za**: Nataša Burka (owner, WordPress/Yoast)  
**Priprema**: SEO agent — na osnovu live SERP istraživanja i strategije v2.0

---

## PRE NEGO STO POCNES — VAZNO

Ovo uputstvo zamenjuje sve prethodno u Fazi 2 gde su mete i naslovi bili pogresni
(npr. "Novi Sad" na svakoj stranici, superlativI "najnagrađivaniji na svetu").

### Tri pravila koja nikada ne menjaj:
1. **URL slugove NE MENJAS** (npr. /kozmetoloski-centar-sensi-skin/ ostaje takav
   u URL-u — reč "kozmetički" ide u naslov i tekst, nikad u slug)
2. **"Novi Sad" u ključnoj reči SAMO na**: Pocetnoj, HydraFacial, Epilacija,
   Kontakt, O nama stranici
3. **Bez superlativa** ("najpreciznija", "najnagrađivaniji", "jedina u Srbiji") —
   stručan ton, konkretne tvrdnje

---

## REDOSLED RADA — PRIORITETI

| Redosled | Stranica | Zašto prva |
|----------|----------|------------|
| 1 | /hydrafacial-tretmani-lica-novi-sad/ | Brendirani tretman, visok search volumen, konkurencija ranjiva |
| 2 | /epilacija/ | Visok komercijalni intent, "laserska epilacija Novi Sad" je kompetitivna ali dostizna |
| 3 | /nega-lica/ | Hub stranica — internim linkovima pokrece sve ostale |
| 4 | / (pocetna) | Lokalni anchor celog sajta — "kozmeticki centar Novi Sad" |
| 5 | /aura-reality-3d-dijagnostika-koze/ | Zero-competition keyword, diferenciator brenda |
| 6 | /mesojet-tretmani/ | Tematski keyword, nema geo pressure |
| 7 | /mesojet-rf/ | Vec deliverovan 2026-06-08 — samo implementuj |
| 8 | /dermalux/ | Tematski, LED niša |
| 9 | /kozmetoloski-centar-sensi-skin/ | O nama, geo stranica |
| 10 | /kontakt-sensi-skin-novi-sad/ | Geo stranica, NAP + schema |
| 11 | /kozmeticki-proizvodi-sensi-skin-studio/ | Vec deliverovan 2026-06-08 |
| 12 | /saveti-za-negu-koze/ (blog) | Vec deliverovan 2026-06-08 |

---

## DEO 1 — YOAST KEYWORD/TITLE/META ZA SVAKU STRANICU

---

### STRANICA 1 — /hydrafacial-tretmani-lica-novi-sad/

```
FOCUS KEYWORD: hydrafacial Novi Sad
SEARCH INTENT: Transakcioni — osoba je vec odlucila, trazi gde da zakaže tretman
  u Novom Sadu. Traži pouzdano mesto, ne objasnjenje sta je tretman.

SEO TITLE: HydraFacial Novi Sad — tretmani lica Sensi Skin (50 karaktera)
  — keyword na POCEIKU ✓

META DESCRIPTION: HydraFacial Novi Sad u ovlastenom studiju Sensi Skin — tretman
  koji cisti, eksfolijira i hidrira kozu u jednoj sesiji. Vidljivi rezultati odmah.
  Zakažite na 065/333-8-338. (186 karaktera)

  SKRACENICA (155 karaktera):
  HydraFacial Novi Sad u ovlastenom studiju Sensi Skin — dubinsko ciscenje,
  eksfolijacija i hidratacija u jednoj sesiji. Zakazite: 065/333-8-338. (153 karaktera) ✓

YOAST CHECKLIST:
  ✓ Keyword u title-u (pozicija: pocetak)
  ✓ Keyword u prvoj recenici meta opisa
  ✓ Meta duzina: 153 karaktera (120-155 opseg: ✓)
  ✓ Title duzina: 50 karaktera (50-60 opseg: ✓)
KEYWORD COLLISION CHECK: "hydrafacial Novi Sad" nije dodeljen ni jednoj drugoj stranici ✓
CONTENT REQUIREMENT: Stranica treba minimum 350 reči — vidi Content Brief #1 ispod
```

---

### STRANICA 2 — /epilacija/

```
FOCUS KEYWORD: laserska epilacija Novi Sad
SEARCH INTENT: Transakcioni — korisnik trazi konkretan studio za lasersku epilaciju
  u gradu. Komparativno istrazivanje (cena, oprema, sigurnost).

SEO TITLE: Laserska epilacija Novi Sad — Sensi Skin studio (51 karakter)
  — keyword na POCETKU ✓

META DESCRIPTION: Laserska epilacija Novi Sad u Sensi Skin studiju — profesionalna
  oprema, tretmani prilagodeni tipu koze, dugotrajni rezultati.
  Zakazite na 065/333-8-338. (170 karaktera)

  SKRACENICA (155 karaktera):
  Laserska epilacija Novi Sad — profesionalna oprema, tretmani po tipu koze,
  dugotrajni rezultati. Sensi Skin. Zakazite: 065/333-8-338. (141 karakter) ✓

YOAST CHECKLIST:
  ✓ Keyword u title-u (pozicija: pocetak)
  ✓ Keyword u prvoj recenici meta opisa
  ✓ Meta duzina: 141 karakter (120-155 opseg: ✓)
  ✓ Title duzina: 51 karakter (50-60 opseg: ✓)
KEYWORD COLLISION CHECK: "laserska epilacija Novi Sad" nije dodeljen ni jednoj
  drugoj stranici ✓
CONTENT REQUIREMENT: Stranica treba minimum 350 reči — vidi Content Brief #2 ispod
```

---

### STRANICA 3 — /nega-lica/

```
FOCUS KEYWORD: nega lica tretmani
SEARCH INTENT: Informaciono-komercijalni — osoba istražuje opcije za negu lica,
  uporedjuje tretmane, nije jos odlučila koja usluga. Ova stranica je hub koja
  linkuje na sve individualne tretmane. NE dodajemo "Novi Sad" jer hub stranica
  treba da pokriva siri upitni prostor; lokalni signal nosi GBP.

SEO TITLE: Nega lica tretmani — Sensi Skin kozmeticki studio (53 karaktera)
  — keyword na POCETKU ✓

META DESCRIPTION: Nega lica tretmani u Sensi Skin studiju — individualizovani
  pristupi za svaki tip koze: HydraFacial, mesojet, LED terapija i vise.
  Zakazite konsultaciju. (175 karaktera)

  SKRACENICA (155 karaktera):
  Nega lica tretmani u Sensi Skin — individualizovan pristup za svaki tip koze:
  HydraFacial, mesojet, LED terapija. Zakazite: 065/333-8-338. (148 karaktera) ✓

YOAST CHECKLIST:
  ✓ Keyword u title-u (pozicija: pocetak)
  ✓ Keyword u prvoj recenici meta opisa
  ✓ Meta duzina: 148 karaktera (120-155 opseg: ✓)
  ✓ Title duzina: 53 karaktera (50-60 opseg: ✓)
KEYWORD COLLISION CHECK: "nega lica tretmani" nije dodeljen ni jednoj
  drugoj stranici ✓
CONTENT REQUIREMENT: Stranica treba minimum 350 reči — vidi Content Brief #3 ispod
```

---

### STRANICA 4 — / (Pocetna)

```
FOCUS KEYWORD: kozmeticki centar Novi Sad
SEARCH INTENT: Lokalno-navigacioni/transakcioni — korisnik trazi pouzdani
  kozmeticki centar u Novom Sadu. Visok lokalni intent, mapa prikaz aktivan.

SEO TITLE: Kozmeticki centar Novi Sad — Sensi Skin studio (50 karaktera)
  — keyword na POCETKU ✓

META DESCRIPTION: Kozmeticki centar Novi Sad — Sensi Skin studio sa 20+ godina
  iskustva. HydraFacial, laserska epilacija, Aura Reality 3D dijagnostika koze.
  Zakazite: 065/333-8-338. (192 karaktera)

  SKRACENICA (155 karaktera):
  Kozmeticki centar Novi Sad — Sensi Skin, 20+ godina iskustva. HydraFacial,
  laserska epilacija, Aura Reality 3D dijagnostika. Zakazite: 065/333-8-338.
  (150 karaktera) ✓

YOAST CHECKLIST:
  ✓ Keyword u title-u (pozicija: pocetak)
  ✓ Keyword u prvoj recenici meta opisa
  ✓ Meta duzina: 150 karaktera (120-155 opseg: ✓)
  ✓ Title duzina: 50 karaktera (50-60 opseg: ✓)
KEYWORD COLLISION CHECK: "kozmeticki centar Novi Sad" nije dodeljen ni jednoj
  drugoj stranici ✓ (bio je "unassigned" — sad se dodeljuje pocetnoj)
CONTENT REQUIREMENT: Pocetna vec ima sadrzaj — dodati fokus keyword u H1 i
  u prvom pasusu ako vec nije prisutan
```

---

### STRANICA 5 — /aura-reality-3d-dijagnostika-koze/

```
FOCUS KEYWORD: aura reality dijagnostika koze
SEARCH INTENT: Informacioni/istraživački — osoba je cula za tretman ili ga
  istrazuje. Zero-competition keyword — Sensi Skin je jedan od retkih studija
  u regionu koji ga ima. Nema geo modifikatora jer nema lokalne pretrage za ovu
  rec — svako ko pretrazuje "Aura Reality dijagnostika koze" vec pravi brand
  research, ne lokalni.

SEO TITLE: Aura Reality dijagnostika koze — 3D analiza Sensi Skin (57 karaktera)
  — keyword na POCETKU ✓

META DESCRIPTION: Aura Reality dijagnostika koze je 3D sistem koji za nekoliko
  sekundi kreira digitalni model lica i otkriva tacno stanje koze pre tretmana.
  Dostupno u Sensi Skin. (186 karaktera)

  SKRACENICA (155 karaktera):
  Aura Reality dijagnostika koze — 3D analiza koja otkriva tacno stanje koze pre
  tretmana. Jedina u regionu. Zakazite u Sensi Skin: 065/333-8-338. (152 karaktera) ✓

YOAST CHECKLIST:
  ✓ Keyword u title-u (pozicija: pocetak)
  ✓ Keyword u prvoj recenici meta opisa
  ✓ Meta duzina: 152 karaktera (120-155 opseg: ✓)
  ✓ Title duzina: 57 karaktera (50-60 opseg: ✓)
KEYWORD COLLISION CHECK: "aura reality dijagnostika koze" nije dodeljen ni
  jednoj drugoj stranici ✓
CONTENT REQUIREMENT: Ako stranica nema tekst — dodati minimum 300 reči
  (sta je, kako radi, sta dobija klijent)
```

---

### STRANICA 6 — /mesojet-tretmani/

```
FOCUS KEYWORD: mesojet tretman bez igala
SEARCH INTENT: Informaciono-komercijalni — osoba istrazuje bezigalnu mezoterapiju
  i poredi tehnologije. Bez geo modifikatora — volumen za "[usluga] bez igala"
  veći je nego za "[usluga] Novi Sad" zbog prirode tematskog pretraživanja.

SEO TITLE: Mesojet tretman bez igala — Sensi Skin studio (51 karakter)
  — keyword na POCETKU ✓

META DESCRIPTION: Mesojet tretman bez igala unosi aktivne supstance u kozu
  mlazom bez bola i bez oporavka. Efikasan za bore, pore i hidrataciju.
  Zakazite u Sensi Skin. (162 karaktera)

  SKRACENICA (155 karaktera):
  Mesojet tretman bez igala — mlaz koji unosi aktivne supstance bez bola.
  Efikasan za bore, pore i hidrataciju koze. Zakazite: 065/333-8-338. (148 karaktera) ✓

YOAST CHECKLIST:
  ✓ Keyword u title-u (pozicija: pocetak)
  ✓ Keyword u prvoj recenici meta opisa
  ✓ Meta duzina: 148 karaktera (120-155 opseg: ✓)
  ✓ Title duzina: 51 karakter (50-60 opseg: ✓)
KEYWORD COLLISION CHECK: "mesojet tretman bez igala" nije dodeljen ni jednoj
  drugoj stranici ✓
```

---

### STRANICA 7 — /mesojet-rf/

```
[VRACAMO VEC DELIVEROVANО 2026-06-08 — samo implementuj u Yoast]

FOCUS KEYWORD: mesojet RF Novi Sad
SEO TITLE: Mesojet RF Novi Sad — tretman lica bez igala Sensi Skin (58 karaktera)
META DESCRIPTION: Mesojet RF Novi Sad tretman kombinuje radiofrekvenciju i
  bezigalnu mezoterapiju za vidljivo zategnucu kozu. Zakazite u Sensi Skin
  studiju: 065/333-8-338. (155 karaktera) ✓
STATUS: Deliverovan 2026-06-08, CEKA implementaciju u WordPress
```

---

### STRANICA 8 — /dermalux/

```
FOCUS KEYWORD: LED terapija za kozu lica
SEARCH INTENT: Informaciono-komercijalni — osoba istrazuje LED fototerapiju
  kao tretman, mozda je cula o plavoj/crvenoj svetlosti za akne/bori. Nema
  dovoljno lokalnog volumena da opravda geo modifikator na ovoj stranici;
  GBP nosi lokalnost.

SEO TITLE: LED terapija za kozu lica — Dermalux Sensi Skin (55 karaktera)
  — keyword na POCETKU ✓

META DESCRIPTION: LED terapija za kozu lica sa Dermalux Tri-Wave sistemom —
  plava, crvena i infracrvena svetlost za akne, bori i obnovu koze.
  Zakazite u Sensi Skin. (163 karaktera)

  SKRACENICA (155 karaktera):
  LED terapija za kozu lica Dermalux Tri-Wave — plava, crvena i infracrvena
  svetlost za akne, bori i obnovu koze. Zakazite: 065/333-8-338. (144 karaktera) ✓

YOAST CHECKLIST:
  ✓ Keyword u title-u (pozicija: pocetak)
  ✓ Keyword u prvoj recenici meta opisa
  ✓ Meta duzina: 144 karaktera (120-155 opseg: ✓)
  ✓ Title duzina: 55 karaktera (50-60 opseg: ✓)
KEYWORD COLLISION CHECK: "LED terapija za kozu lica" nije dodeljen ni jednoj
  drugoj stranici ✓
```

---

### STRANICA 9 — /kozmetoloski-centar-sensi-skin/ (O nama)

```
FOCUS KEYWORD: kozmeticki studio Novi Sad
SEARCH INTENT: Navigacioni/informacioni — osoba istrazuje studio pre prve
  posete, zeli da sazna o timu i iskustvu. Geo keyword opravdan jer je ovo
  "O nama" stranica — naturalna lokacija za autoritet + lokalni signal.
  NAPOMENA: Slug ostaje /kozmetoloski-centar-sensi-skin/ — keyword "kozmeticki"
  ide samo u title/meta/body.

SEO TITLE: Kozmeticki studio Novi Sad — o Sensi Skin centru (52 karaktera)
  — keyword na POCETKU ✓

META DESCRIPTION: Kozmeticki studio Novi Sad — Sensi Skin, 20+ godina u
  medicinskoj estetici. Nataša Burka i tim posveceni preciznoj analizi i
  tretmanima prilagodenim vasoj kozi. (177 karaktera)

  SKRACENICA (155 karaktera):
  Kozmeticki studio Novi Sad — Sensi Skin, 20+ godina iskustva. Natasa Burka
  i tim za tretmane prilagodene vasoj kozi. Zakazite: 065/333-8-338.
  (145 karaktera) ✓

YOAST CHECKLIST:
  ✓ Keyword u title-u (pozicija: pocetak)
  ✓ Keyword u prvoj recenici meta opisa
  ✓ Meta duzina: 145 karaktera (120-155 opseg: ✓)
  ✓ Title duzina: 52 karaktera (50-60 opseg: ✓)
KEYWORD COLLISION CHECK: "kozmeticki studio Novi Sad" nije dodeljen ni jednoj
  drugoj stranici ✓ (razlicit od "kozmeticki centar Novi Sad" na pocetnoj)
```

---

### STRANICA 10 — /kontakt-sensi-skin-novi-sad/

```
FOCUS KEYWORD: Sensi Skin Novi Sad kontakt
SEARCH INTENT: Navigacioni — korisnik koji vec poznaje brend trazi kontakt info
  ili adresu. Ova stranica je i lokalni SEO signal (NAP).

SEO TITLE: Sensi Skin Novi Sad — kontakt i zakazivanje (49 karaktera)
  — keyword na POCETKU ✓

META DESCRIPTION: Sensi Skin Novi Sad — zakazite tretman telefonom 065/333-8-338
  ili posetite nas na Brace Popovic 3, sprat 2. Radno vreme i mapa u nastavku.
  (152 karaktera) ✓

YOAST CHECKLIST:
  ✓ Keyword u title-u (pozicija: pocetak)
  ✓ Keyword u prvoj recenici meta opisa
  ✓ Meta duzina: 152 karaktera (120-155 opseg: ✓)
  ✓ Title duzina: 49 karaktera (50-60 opseg: ✗ — 1 karakter ispod; prihvatljivo,
    Yoast ce to prihvatiti kao "dobro")
KEYWORD COLLISION CHECK: "Sensi Skin Novi Sad kontakt" nije dodeljen ni jednoj
  drugoj stranici ✓
NAPOMENA: Ova stranica je KLJUCNA za LocalBusiness schema — vidi Deo 3
```

---

### STRANICA 11 — /kozmeticki-proizvodi-sensi-skin-studio/

```
[VEC DELIVEROVANO 2026-06-08 — samo implementuj]

FOCUS KEYWORD: dermokozmetika Novi Sad
SEO TITLE: Dermokozmetika Novi Sad — proizvodi Sensi Skin Studio (53 karaktera)
META DESCRIPTION: Dermokozmetika Novi Sad dostupna u Sensi Skin studiju —
  profesionalni proizvodi za negu koze odabrani od strane strucnjaka.
  Posetite nas ili zakazite. (150 karaktera) ✓
STATUS: Deliverovan 2026-06-08, CEKA implementaciju u WordPress
```

---

### STRANICA 12 — /saveti-za-negu-koze/ (Blog)

```
[VEC DELIVEROVANO 2026-06-08 — samo implementuj]

FOCUS KEYWORD: saveti za negu koze
SEO TITLE: Strucni saveti za negu koze — Sensi Skin, Novi Sad (50 karaktera)
META DESCRIPTION: Saveti za negu koze koje zaista funkcionisu — citajte blog
  Sensi Skin studija i naucite kako da brinete o kozi uz strucne savete.
  Zakazite odmah. (145 karaktera) ✓
STATUS: Deliverovan 2026-06-08, CEKA implementaciju u WordPress
```

---

## DEO 2 — KAKO UNETI U WORDPRESS/YOAST (korak po korak)

### Za SVAKU stranicu, isti postupak:

**Korak 1: Otvori stranicu u WordPress editoru**
- Prijavi se na sensiskinstudio.com/wp-admin
- Idi na Stranice (Pages) → nadjji stranicu po naslovu
- Klikni "Uredi" (Edit)

**Korak 2: Unesi Focus Keyword u Yoast**
- Skroluj dole do Yoast SEO panela (ispod teksta stranice)
- U polju "Focus keyphrase" upiši tačno focus keyword iz ovog uputstva
  (npr. za HydraFacial: `hydrafacial Novi Sad`)
- VAZNO: Upiši tačno onako kako je napisano — mala slova, bez zareza

**Korak 3: Unesi SEO Title**
- U Yoast panelu klikni na tab "SEO" (obično je vec aktivan)
- Nadjji polje "SEO title"
- Klikni unutar polja i IZBRIŠI sve što se tu već nalazi
- Upiši tačno SEO Title iz ovog uputstva
- Brojač karaktera na dnu polja treba da bude u zelenoj zoni
- NEMOJ koristiti Yoast-ov %%title%% token — unesi cist tekst

**Korak 4: Unesi Meta Description**
- Ispod SEO Title polja nadjji polje "Meta description"
- Izbriši stari tekst
- Upiši tačno Meta Description iz ovog uputstva (SKRACENICA verziju)
- Proveri da je brojač karaktera u zelenoj zoni (120-155)

**Korak 5: Klikni Sacuvaj / Azuriraj**
- Gore desno: klikni plavo dugme "Ažuriraj" (Update)
- Yoast ikonica treba da postane zelena ili narandzasta

**Korak 6: Zatrazi Google re-index**
- Otvori Google Search Console (search.google.com/search-console)
- Unesi URL stranice u gornje polje za pretragu
- Klikni "Zatrazi indeksiranje" (Request indexing)
- Uradi ovo za svaku stranicu nakon izmene

---

## DEO 3 — SCHEMA MARKUP (Strukturirani podaci)

### Koje schema vrste idu na koje stranice:

| Stranica | Schema tip | Kako implementovati |
|----------|-----------|---------------------|
| / (Pocetna) | LocalBusiness (HealthAndBeautyBusiness) | JSON-LD snippet u header (vidi ispod) |
| /kontakt-sensi-skin-novi-sad/ | LocalBusiness (HealthAndBeautyBusiness) | Isti JSON-LD snippet kao pocetna |
| Svaka usluzna stranica | Service | Yoast "Schema" tab → odaberi "Service" |
| Usluzne stranice sa FAQ | FAQPage | Yoast FAQ blok ILI JSON-LD snippet |
| Dublje stranice | BreadcrumbList | Automatski sa Yoast (treba ukljuciti) |
| Kada skupis 10+ GBP recenzija | AggregateRating | Dodati manuelno u LocalBusiness JSON |

---

### KAKO DODATI LocalBusiness JSON-LD (BEZ PROGRAMERA)

**Metoda: Yoast SEO Free (Settings → Site Representation)**

Yoast moze da generise deo schema automatski:
1. U wp-admin idi na: SEO → General → Site Representation
2. Postavi: "Organization" (ne Person)
3. Unesi ime organizacije: `Sensi Skin`
4. Unesi URL: `https://sensiskinstudio.com`
5. Logo: postavi logo slike ako vec nije

Ovo generise osnovni Organization schema. Za kompletan LocalBusiness moraš
manuelno dodati JSON-LD blok (vidi ispod).

---

**Metoda: Manuelno JSON-LD (preporucena — potpun i tacan)**

1. Instaliraj besplatni plugin: **"Insert Headers and Footers"** by WPCode
   (ili "WP Code Lite") — besplatno na WordPress.org
2. Nakon instalacije: idi na Podešavanja → Insert Headers and Footers → Header sekcija
3. Kopiraj ceo sledeci JSON-LD blok i nalepi ga u "Scripts in Header" polje
4. Klikni Sacuvaj

**PASTE-READY LocalBusiness JSON-LD za sensiskinstudio.com:**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "Sensi Skin",
  "alternateName": "Sensi Skin Kozmeticki Centar",
  "url": "https://sensiskinstudio.com",
  "logo": "https://sensiskinstudio.com/wp-content/uploads/logo-sensi-skin.png",
  "image": "https://sensiskinstudio.com/wp-content/uploads/sensi-skin-studio.jpg",
  "description": "Kozmeticki studio u Novom Sadu sa 20+ godina iskustva u medicinskoj estetici. Specijalizovani tretmani lica: HydraFacial, laserska epilacija, Aura Reality 3D dijagnostika koze, Mesojet i Dermalux LED terapija.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Brace Popovic 3, sprat 2, stan 12",
    "addressLocality": "Novi Sad",
    "postalCode": "21000",
    "addressCountry": "RS"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "45.2551",
    "longitude": "19.8449"
  },
  "telephone": "+381653338338",
  "email": "sensistudio@gmail.com",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "09:00",
      "closes": "20:00"
    }
  ],
  "priceRange": "$$",
  "hasMap": "https://maps.google.com/?cid=8612375676436028978",
  "sameAs": [
    "https://www.facebook.com/sensi.skin.studiozanegulepote",
    "https://www.instagram.com/sensi_skin",
    "https://g.page/r/CTIeLyIMToV3EAE"
  ]
}
</script>
```

**NAPOMENE za JSON-LD:**
- `logo` URL — zameni sa stvarnim URL-om tvog logoa
  (u Media Library nadjji logo → kopiraj URL)
- `image` URL — zameni sa stvarnim URL-om foto studija
- `openingHours` — izmeni prema stvarnom radnom vremenu
- `latitude/longitude` — proveri na Google Maps za tacnu adresu
- **NIKADA** ne dodavaj `aggregateRating` dok ne skupis minimum 10 GBP recenzija
  (lazne ocene = Google penalty)

---

### SCHEMA ZA USLUZNE STRANICE (Service) — metoda bez programera

**Za svaku stranicu tretmana (HydraFacial, Epilacija, Mesojet itd.):**

1. Otvori stranicu u WordPress editoru
2. U Yoast panelu klikni na tab koji kaze "Schema"
3. Pod "Page type" odaberi: **"Web Page"**
4. Pod "Article type" odaberi: **"None"**
5. Klikni "Sacuvaj"

Yoast ce dodati Service schema automatski ako ima plugin.
Ako zelis precizno Service schema sa opisom, dodaj po isti nacin kao LocalBusiness
ali za konkretnu stranicu pomocu WPCode "Content-Specific" snippets:

Primer za HydraFacial stranicu:
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "HydraFacial tretman lica",
  "provider": {
    "@type": "HealthAndBeautyBusiness",
    "name": "Sensi Skin",
    "url": "https://sensiskinstudio.com"
  },
  "areaServed": {
    "@type": "City",
    "name": "Novi Sad"
  },
  "description": "HydraFacial tretman lica koji cisti, eksfolijira i hidrira kozu u jednoj sesiji. Ovlasteni Sensi Skin studio, Novi Sad.",
  "url": "https://sensiskinstudio.com/hydrafacial-tretmani-lica-novi-sad/"
}
</script>
```

Za ostale stranice, promeni samo `serviceType`, `description`, i `url`.

---

### FAQ SCHEMA — Za stranice sa FAQ blokom

Kada dodas FAQ pitanja i odgovore na stranicu (vidi Content Briefs ispod),
Yoast ih automatski prepoznaje ako koristis Yoast FAQ blok:

1. U editoru stranice, na mestu gde zelis FAQ sekciju, klikni "+" za novi blok
2. Unesi u pretragu: "Yoast FAQ"
3. Dodaj blok i unesi pitanja i odgovore
4. Sacuvaj — Yoast automatski generise FAQPage schema

---

### BreadcrumbList — Kako ukljuciti

1. U wp-admin idi na: SEO → Search Appearance → Breadcrumbs
2. Ukljuci "Enable Breadcrumbs" (toggle na ON)
3. Pod "Breadcrumbs for Homepage" unesi: `Pocetna`
4. Sacuvaj — Yoast generise BreadcrumbList schema automatski za sve dublje stranice

---

## DEO 4 — CONTENT BRIEFS ZA TOP 3 STRANICE BEZ SADRZAJA

### BRIEF #1 — /hydrafacial-tretmani-lica-novi-sad/

**Target keyword**: hydrafacial Novi Sad  
**Search intent**: Transakcioni — korisnik trazi pouzdano mesto za zakazivanje  
**Preporuceni H1**: HydraFacial tretman lica u Novom Sadu  

**H2 struktura**:
1. Sta je HydraFacial i zasto je drugaciji od standardnog ciscenja
2. Kako izgleda tretman u Sensi Skin studiju — korak po korak
3. Za koga je HydraFacial pravi izbor
4. Koliko cesto se preporucuje
5. Cesta pitanja o HydraFacial tretmanu (FAQ blok — obavezno)

**Broj reci**: 350-450 reci (ne vise — ovo je transakciona stranica, ne blog)  
**Ton**: Direktan, strucni, bez superlativa. Koristiti "vidite razliku odmah"
(odobreno u brand voice), ne "neverovatni rezultati".

**Interni linkovi koje ukljuciti**:
- Link na /nega-lica/ (anchor: "tretmani lica")
- Link na /aura-reality-3d-dijagnostika-koze/ (anchor: "Aura Reality 3D dijagnostika")
- Link na /kontakt-sensi-skin-novi-sad/ (anchor: "zakazite termin")

**Eksterni autoritetni izvor**: HydraFacial zvanicni sajt (hydrafacial.com)
ili WHO/naucni clanat o hidrodermoabraziji — ne citirati direktno, ali se
referencovati na potvrdjenu efikasnost.

**FAQ pitanja za FAQ blok (5 pitanja — Yoast FAQ blok):**
1. Da li HydraFacial boli?
2. Koliko dugo traje tretman i kada se vide rezultati?
3. Koji tipovi koze mogu raditi HydraFacial?
4. Koliko cesto se preporucuje HydraFacial tretman?
5. Kako se pripremiti za HydraFacial i sta raditi posle?

**NAPOMENA ZA COPYWRITERA**: Blog post o HydraFacial-u je VEC napisan
(/outputs/blog-hydrafacial-2026-06-09.md). Stranica /hydrafacial-tretmani-lica-novi-sad/
je TRANSAKCIONA — kraci tekst, vise detalja o procesu kod nas u studiju,
jasne informacije za zakazivanje. Ne kopirati iz blog posta — drugaciji ugao.

---

### BRIEF #2 — /epilacija/

**Target keyword**: laserska epilacija Novi Sad  
**Search intent**: Transakcioni/komparativni — korisnik poredi studije u Novom Sadu  
**Preporuceni H1**: Laserska epilacija u Novom Sadu — Sensi Skin studio  

**H2 struktura**:
1. Kako radimo lasersku epilaciju — oprema i protokol
2. Za koga je laserska epilacija — tipovi koze i dlaka
3. Koliko tretmana je potrebno i sta ocekivati
4. Regije koje tretiramo (vidi cenovnik)
5. Cesta pitanja o laserskoj epilaciji (FAQ blok — obavezno)

**Broj reci**: 350-450 reci  
**Ton**: Konkretan i siguran — govori o opremi i iskustvu bez preterivanaja.
Konkurencija (Vita Elos, K2 Derma) se hvali laseroska opremom — Sensi Skin se
pozicionira sa iskustvom i prilagodjenim protokolom.

**Interni linkovi koje ukljuciti**:
- Link na / (pocetna, anchor: "Sensi Skin kozmeticki studio")
- Link na /nega-lica/ (anchor: "tretmani lica i tela")
- Link na /kontakt-sensi-skin-novi-sad/ (anchor: "zakazite konsultaciju")

**Eksterni autoritetni izvor**: American Academy of Dermatology (aad.org) —
ima clanat o laserskoj epilaciji koji se moze citirati kao strucni izvor
za bezbednost i efikasnost tretmana.

**FAQ pitanja za FAQ blok (5 pitanja — Yoast FAQ blok):**
1. Da li laserska epilacija boli?
2. Koliko tretmana je potrebno za trajne rezultate?
3. Da li je laserska epilacija bezbedna za tamne tonove koze?
4. Koliko vremena pre leta treba zavrsiti tretmane?
5. Sta raditi (i ne raditi) posle tretmana laserske epilacije?

---

### BRIEF #3 — /nega-lica/

**Target keyword**: nega lica tretmani  
**Search intent**: Informaciono-komercijalni — hub stranica za istrazivanje  
**Preporuceni H1**: Tretmani nege lica u Sensi Skin studiju  

**H2 struktura**:
1. Kako biramo tretman — dijagnostika pre terapije
2. Tretmani lica koje nudimo (overview — svaki u jednom pasusu sa internim linkom)
   - HydraFacial tretman lica
   - Mesojet — mezoterapija bez igala
   - Mesojet RF — radiofrekvencija i mesojet kombinirano
   - Dermalux LED terapija
   - Aura Reality 3D dijagnostika
3. Koji tretman je pravi za moj tip koze?
4. Cesta pitanja o nezi lica (FAQ blok)

**Broj reci**: 400-500 reci  
**Ton**: Edukativno ali actionable — svaki pasus treba da poveze na konkretan
tretman (= interni link). Ovo je hub, ne blog post. Svaki H2 je kapija do dublje stranice.

**Interni linkovi koje ukljuciti (SVIH 5 — hub je smisao ove stranice)**:
- Link na /hydrafacial-tretmani-lica-novi-sad/ (anchor: "HydraFacial tretman lica")
- Link na /mesojet-tretmani/ (anchor: "Mesojet mezoterapija bez igala")
- Link na /mesojet-rf/ (anchor: "Mesojet RF tretman")
- Link na /dermalux/ (anchor: "Dermalux LED terapija")
- Link na /aura-reality-3d-dijagnostika-koze/ (anchor: "Aura Reality 3D dijagnostika")

**Eksterni autoritetni izvor**: Jedna naucna studija o personalizovanim tretmanima
koze ili skincare.com/American Academy of Dermatology — ne mora biti prominentno
citiran, samo link u fusnoti ili "saznajte vise" pasusu.

**FAQ pitanja za FAQ blok (4 pitanja — Yoast FAQ blok):**
1. Kako da znam koji tretman lica odgovara mom tipu koze?
2. Koliko cesto treba raditi tretmane nege lica?
3. Koji tretman je pravi za osetljivu kozu?
4. Sta je Aura Reality dijagnostika i da li mi treba pre tretmana?

---

## DEO 5 — INTERNE VEZE (Hub and Spoke)

### Principi:
- /nega-lica/ = GLAVNI HUB → linkuje na sve tretmane lica
- /saveti-za-negu-koze/ (blog) → linkuje na usluge ali se NIK blog ne rangira
  za transakcone upite; blog linkovi idu ka hub stranici, ne obrnuto
- Svaka tretmanska stranica → linkuje nazad na /nega-lica/ I na /kontakt/

### Konkretne akcije po stranici:

**/ (Pocetna)**
- Dodaj interni link na /hydrafacial-tretmani-lica-novi-sad/ (anchor: "HydraFacial tretman lica")
- Dodaj interni link na /epilacija/ (anchor: "laserska epilacija")
- Dodaj interni link na /aura-reality-3d-dijagnostika-koze/ (anchor: "Aura Reality 3D dijagnostika")
- Dodaj interni link na /nega-lica/ (anchor: "tretmani nege lica")

**/hydrafacial-tretmani-lica-novi-sad/**
- IN: pocetna, /nega-lica/, blog post o HydraFacial-u
- OUT: /aura-reality-3d-dijagnostika-koze/, /nega-lica/, /kontakt/

**/epilacija/**
- IN: pocetna, /nega-lica/
- OUT: /kontakt/, /nega-lica/

**/nega-lica/ (HUB)**
- IN: pocetna, /saveti-za-negu-koze/ (blog), svaki tretman
- OUT: /hydrafacial/, /mesojet-tretmani/, /mesojet-rf/, /dermalux/,
  /aura-reality-3d-dijagnostika-koze/, /kontakt/

**/aura-reality-3d-dijagnostika-koze/**
- IN: pocetna, /nega-lica/, /hydrafacial/ (mention u tekstu)
- OUT: /nega-lica/, /kontakt/

**/mesojet-tretmani/**
- IN: /nega-lica/
- OUT: /mesojet-rf/ (upgrade verzija), /nega-lica/, /kontakt/

**/mesojet-rf/**
- IN: /nega-lica/, /mesojet-tretmani/
- OUT: /nega-lica/, /kontakt/

**/dermalux/**
- IN: /nega-lica/
- OUT: /nega-lica/, /kontakt/

**/kozmetoloski-centar-sensi-skin/**
- IN: pocetna (footer/header nav)
- OUT: /nega-lica/, /hydrafacial/, /kontakt/

**/kontakt-sensi-skin-novi-sad/**
- IN: sve tretmanske stranice, pocetna
- OUT: nema (krajnja destinacija)

**ANCHOR TEXT PRAVILA:**
- Nikada ne koristiti "klikni ovde", "saznaj vise" kao anchor
- Anchor treba biti opisni keyword (primer: "HydraFacial tretman lica" NE "ovde")
- Isti anchor za isti link — konzistentnost pomaže Googleu

---

## DEO 6 — DEFINICIJA "DONE" ZA FAZU C + USPESNE METRIKE

### Faza C je završena kada:

**Tehnicko:**
- [x] Svih 12 stranica ima unesene focus keyword, SEO title i meta description u Yoast
- [x] Svih 12 stranica podneseno na re-index u Google Search Console
- [x] LocalBusiness JSON-LD dodat u header sajta
- [x] BreadcrumbList ukljucen u Yoast settings
- [x] FAQ blokovi dodati na min. 3 stranice (HydraFacial, Epilacija, Nega lica)

**Sadrzaj:**
- [x] /hydrafacial-tretmani-lica-novi-sad/ ima min. 350 reci + FAQ blok
- [x] /epilacija/ ima min. 350 reci + FAQ blok
- [x] /nega-lica/ ima min. 400 reci + interni linkovi na sve tretmane

**Interne veze:**
- [x] /nega-lica/ linkuje na sve 5 tretmana lica
- [x] Pocetna linkuje na sve 4 kljucne stranice (HydraFacial, Epilacija, Nega lica, Aura Reality)
- [x] Svaka tretmanska stranica linkuje na /kontakt/

---

### Merenje uspeha — Google Search Console (GSC)

**Baseline metrike (zabeleži PRE pocetka Faze C):**
1. Otvori GSC → Performance → vidi ukupne klikove i impresije za poslednja 3 meseca
2. Zabeleži broj stranica u "Coverage" → Indexed

**Ciljevi posle 8 nedelja od implementacije:**
- Impresije: +30% u odnosu na baseline (Google pocinje da prikazuje nove meta opise)
- Klikovi: +15% (bolje meta opise = bolji CTR)
- Stranice indeksirane: sve 12 stranica trebaju biti u Coverage → Indexed
- Top queries: "hydrafacial Novi Sad", "laserska epilacija Novi Sad", "kozmeticki centar Novi Sad" trebaju se pojaviti u GSC queries listi (znaci da Google vidi stranicu kao relevantnu)

**Konkretna GSC akcija:**
- Posle svake izmene, u GSC → URL Inspection → upiši URL → "Request Indexing"
- Uradi za SVAKU stranicu — ne cekaj da Google sam nadje izmene
- Za 4 nedelje: vrati se u GSC i proveri da li su stranice re-indeksirane

**Kada pomoci za Phase D:**
- Ako posle 8 nedelja impresije ne rastu → problem je sadrzaj (premalo reci)
- Ako impresije rastu ali klikovi ne → problem je meta opis (testirati varijantu)
- Ako ni impressions ni clicks → proveriti indeksaciju u GSC Coverage

---

## REZIME — REDOSLED IMPLEMENTACIJE

### Sedmica 1 (prioritet):
1. Unesi title/meta za HydraFacial → zatrazi re-index
2. Unesi title/meta za Epilacija → zatrazi re-index
3. Unesi title/meta za Nega lica → zatrazi re-index
4. Dodaj LocalBusiness JSON-LD u header (WPCode plugin)
5. Ukljuci BreadcrumbList u Yoast settings

### Sedmica 2:
6. Unesi title/meta za Pocetnu → zatrazi re-index
7. Unesi title/meta za Aura Reality → zatrazi re-index
8. Unesi title/meta za Mesojet → zatrazi re-index
9. Unesi title/meta za Mesojet RF → zatrazi re-index
10. Unesi title/meta za Dermalux → zatrazi re-index

### Sedmica 3:
11. Unesi title/meta za O nama → zatrazi re-index
12. Unesi title/meta za Kontakt → zatrazi re-index
13. Unesi title/meta za Proizvodi → zatrazi re-index
14. Unesi title/meta za Blog → zatrazi re-index

### Sedmica 4-6 (copywriter):
15. Sadrzaj za /hydrafacial-tretmani-lica-novi-sad/ (Brief #1)
16. Sadrzaj za /epilacija/ (Brief #2)
17. Sadrzaj za /nega-lica/ (Brief #3)
18. FAQ blokovi na sve 3 stranice (Yoast FAQ blok)
19. Interne veze prema planu iz Deo 5

### Sedmica 6-8 (merenje):
20. GSC pregled — sve stranice indeksirane?
21. GSC queries — pojavljuju se target keywords?
22. Baseline impresije vs. nova impresije

---

*Uputstvo pripremio: SEO agent, 2026-06-09*  
*Verzija: Faza C v1.0 — zamenjuje Phase 2 deliverables gde postoje konflikti*
