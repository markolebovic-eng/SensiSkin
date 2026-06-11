# JSON-LD Schema — Kompletna implementacija
## sensiskinstudio.com | Jun 2026 | Fresh crawl na osnovu sitemap_index.xml

---

## ⚠️ KRITIČNI NALAZI PRE IMPLEMENTACIJE

### 1. Pogrešan URL za Aura Reality u prethodnom fajlu
- **PRETHODNI (POGREŠAN) URL**: `/aura-reality/`
- **TAČAN URL** (iz sitemap): `/aura-reality-3d-dijagnostika-koze/`
- Sve prethodne schema koje su koristile `/aura-reality/` moraju se popraviti.

### 2. Nijadan "already done" schema nije live na sajtu
WebFetch detekcija pokazuje **NO JSON-LD** na svim stranicama:
- `/hydrafacial-tretmani-lica-novi-sad/` — NEMA live schema
- `/epilacija/` — NEMA live schema
- `/aura-reality-3d-dijagnostika-koze/` — NEMA live schema
- `/sve-istine-o-laserskoj-epilaciji/` — NEMA live schema

> Napomena: Yoast Custom Schema se renderuje server-side i trebalo bi biti vidljivo. Ako misliš da si dodao — verifikuj odmah na: **search.google.com/test/rich-results** (upiši URL stranice). Ako test prikaže schema → WebFetch ga nije video. Ako NE prikaže → schema nije sačuvana.

### 3. Sajt ima 34 blog posta, ne 10
Prethodni audit je pronašao samo najnovijih 10 (sa blog index stranice). Pravi broj: **34 blog posta** u post-sitemap.xml, od 2020 do 2026.

---

## ENTITETSKA ARHITEKTURA (koristiti konzistentno u svim schemama)

```
Organization @id:    https://sensiskinstudio.com/#organization
Person @id:          https://sensiskinstudio.com/#natasa-burka
WebSite @id:         https://sensiskinstudio.com/#website
LocalBusiness type:  ["LocalBusiness", "BeautySalon"]
```

---

## INVENTAR — Sve stranice i blog postovi

### A) Stranice (Pages)

| # | URL | Naslov | Schema potrebna | Status |
|---|-----|--------|----------------|--------|
| 1 | `/` | Početna | WebSite + LocalBusiness | ❌ Generisati |
| 2 | `/hydrafacial-tretmani-lica-novi-sad/` | HydraFacial | Service + FAQPage (7 Q) | ⚠️ Proveriti live |
| 3 | `/epilacija/` | Epilacija | Service + FAQPage (4 Q) | ⚠️ Proveriti live |
| 4 | `/aura-reality-3d-dijagnostika-koze/` | Aura Reality (**ispravljen URL**) | Service + FAQPage (5 Q) | ⚠️ URL bio pogrešan, ispraviti |
| 5 | `/nega-lica/` | Nega lica | Service | ❌ Generisati |
| 6 | `/mesojet-tretmani/` | Mesojet tretmani | Service | ❌ Generisati |
| 7 | `/mesojet-rf/` | Mesojet RF | Service | ❌ Generisati |
| 8 | `/dermalux/` | Dermalux | Service | ❌ Generisati |
| 9 | `/kozmetoloski-centar-sensi-skin/` | Tim / O nama | Person + Organization | ❌ Generisati |
| 10 | `/kontakt-sensi-skin-novi-sad/` | Kontakt | LocalBusiness (NAP) | ❌ Generisati |
| 11 | `/cenovnik-kozmetickih-tretmana-novi-sad/` | Cenovnik | ItemList (OfferCatalog) | ❌ Generisati |
| 12 | `/kozmeticki-proizvodi-sensi-skin-studio/` | Proizvodi | WebPage + Organization | ❌ Generisati |
| 13 | `/strucni-saveti-za-negu-koze/` | Stručni saveti | WebPage | Nizak prioritet |
| 14 | `/moj-nalog-sensi-skin-studio/` | Moj nalog | PRESKOČITI (WooCommerce) | N/A |

### B) Blog postovi (34 total — 5 FAQPage + 29 Article only)

| # | URL slug | Naslov | Datum | Schema tip |
|---|----------|--------|-------|-----------|
| 1 | `/sve-istine-o-laserskoj-epilaciji/` | Sve ISTINE o laserskoj EPILACIJI | 2023-09-04 | ⚠️ Proveriti live (Article+FAQPage) |
| 2 | `/ballancer-pro/` | BALLANCER PRO | 2023-02-27 | Article + FAQPage ← PUNO |
| 3 | `/da-li-je-serum-zaista-potreban/` | Da li je SERUM zaista potreban? | 2023-02-15 | Article + FAQPage ← PUNO |
| 4 | `/melazma/` | Melazma | 2022-09-24 | Article + FAQPage ← PUNO |
| 5 | `/tretmani-lica-sta-primeniti-pre-a-sta-posle-letnjeg-odmora/` | Tretmani lica: šta pre, šta posle letnjeg odmora? | 2022-08-10 | Article + FAQPage ← PUNO |
| 6 | `/nega-lica-sta-je-u-rukama-kozmeticara-a-sta-je-do-vas/` | Nega lica: šta je do kozmetičara, šta do vas? | 2022-08-02 | Article + FAQPage ← PUNO |
| 7 | `/dermalux-led-terapija-kao-resenje-problema/` | DERMALUX LED terapija kao rešenje problema | 2024-04-02 | Article only |
| 8 | `/leto-i-promene-na-kozi/` | Leto i promene na koži | 2024-08-02 | Article only |
| 9 | `/posledice-starenja-na-kozi/` | Posledice starenja na koži | 2024-01-10 | Article only |
| 10 | `/prva-pomoc-kozi-u-hladnim-danima/` | PRVA POMOĆ koži u hladnim danima | 2023-12-04 | Article only |
| 11 | `/sinergija-estetskih-procedura-i-tretmana-lica/` | Sinergija estetskih procedura i tretmana lica | 2023-05-09 | Article only |
| 12 | `/uticaj-kiseonika-na-kozu/` | Uticaj kiseonika na kožu | 2023-04-26 | Article only |
| 13 | `/koraci-unapredjene-nege-lica/` | Koraci unapredjene nege lica | 2023-03-24 | Article only |
| 14 | `/osnovni-koraci-svakodnevne-beauty-rutine/` | Osnovni koraci svakodnevne "beauty" rutine | 2023-03-21 | Article only |
| 15 | `/faktori-rasta-u-borbi-protiv-starenja-koze/` | Faktori rasta u borbi protiv starenja kože | 2023-01-31 | Article only |
| 16 | `/obuzdati-se-i-ne-dirati-akne-kako/` | Obuzdati se i ne dirati akne. Kako? | 2023-01-17 | Article only |
| 17 | `/pojava-osetljivosti-koze-tokom-zimskih-dana/` | Pojava osetljivosti kože tokom zimskih dana | 2022-12-28 | Article only |
| 18 | `/da-li-vas-plase-hemijski-pilinzi/` | Da li vas plaše hemijski pilinzi? | 2022-12-06 | Article only |
| 19 | `/perutanje-koze/` | Perutanje kože – najčešći uzroci i rešenja | 2022-10-31 | Article only |
| 20 | `/dermatolog-ili-esteticar/` | Dermatolog ili estetičar – kome i kada? | 2022-10-14 | Article only |
| 21 | `/jesenji-rezim-nege/` | Jesenji režim nege | 2022-09-19 | Article only |
| 22 | `/rozacea-kako-da-ublazite-simptome/` | Rozacea: kako da ublažite simptome? | 2022-09-09 | Article only |
| 23 | `/tipovi-i-stanje-koze-u-cemu-je-razlika-i-kako-da-ih-odredite/` | Tipovi i stanje kože – u čemu je razlika? | 2022-08-30 | Article only |
| 24 | `/promene-na-kozi-kao-posledica-suncanja/` | Promene na koži kao posledica sunčanja | 2022-08-22 | Article only |
| 25 | `/vrste-akni/` | Vrste akni | 2022-08-19 | Article only |
| 26 | `/tretmani-lica-sta-primeniti-pre-a-sta-posle-letnjeg-odmora/` | *(u tabeli gore, red 5)* | — | — |
| 27 | `/sta-cete-spakovati-u-svoj-beauty-kofer/` | Šta ćete spakovati u svoj beauty kofer? | 2022-07-07 | Article only |
| 28 | `/predeo-oko-ociju-kako-negovati-ovu-osetljvu-regiju/` | Predeo oko očiju – kako negovati? | 2022-07-18 | Article only |
| 29 | `/menopauza-i-pravilna-nega-koze/` | Menopauza i pravilna nega kože | 2022-06-20 | Article only |
| 30 | `/gubitak-kose-i-androgena-alopecija/` | Gubitak kose i androgena alopecija | 2022-06-27 | Article only |
| 31 | `/stetnost-solarijuma/` | Štetnost solarijuma | 2022-06-14 | Article only |
| 32 | `/pravilna-dnevna-rutina-za-negu-koze-lica/` | Pravilna dnevna rutina za negu kože lica | 2022-06-09 | Article only |
| 33 | `/mesojet-hy-po-rf/` | MesoJet HY-PO RF | 2022-03-14 | Article only |
| 34 | `/pure-lift-pro/` | Pure Lift Pro | 2020-03-10 | Article only |

---

## SCHEMA BLOKOVI — Stranice

---

### BLOK 0 — Yoast Knowledge Graph podešavanja (jednom, sitewide)

**WordPress → SEO → Opšta podešavanja → Knowledge Graph & Schema**

| Polje | Vrednost |
|-------|---------|
| Tip organizacije | LocalBusiness |
| Ime | `Sensi Skin Kozmetološki Centar` |
| URL | `https://sensiskinstudio.com` |
| Logo | uploaduj logo |

Ovo konfigurišeš jednom i Yoast ga automatski uključuje na svim stranicama.

---

### STRANICA 1 — Početna (`/`)

**Gde**: WordPress → Stranice → Početna → Yoast → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": "https://sensiskinstudio.com/#website",
    "url": "https://sensiskinstudio.com",
    "name": "Sensi Skin Kozmetološki Centar",
    "description": "Tretmani lica i tela, nega kože i anti-age pristup koji čuva prirodan balans i donosi dugoročne rezultate.",
    "publisher": {
      "@id": "https://sensiskinstudio.com/#organization"
    }
  },
  {
    "@context": "https://schema.org",
    "@type": ["LocalBusiness", "BeautySalon"],
    "@id": "https://sensiskinstudio.com/#organization",
    "name": "Sensi Skin Kozmetološki Centar",
    "url": "https://sensiskinstudio.com",
    "description": "Kozmetološki centar u Novom Sadu osnovan 2014. godine. Specijalizovan za tretmane lica i tela, negu kože i anti-age pristup zasnovan na 3D dijagnostici.",
    "foundingDate": "2014",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Braće Popović 3, sprat 2, stan 12",
      "addressLocality": "Novi Sad",
      "postalCode": "21000",
      "addressCountry": "RS"
    },
    "telephone": "+381653338338",
    "email": "sensistudio@gmail.com",
    "priceRange": "€€",
    "sameAs": [
      "https://www.instagram.com/sensi_skin/",
      "https://www.facebook.com/sensi.skin.studiozanegulepote/"
    ]
  }
]
```

---

### STRANICA 2 — HydraFacial (`/hydrafacial-tretmani-lica-novi-sad/`)

**⚠️ VERIFIKUJ ŽIVU SCHEMA**: https://search.google.com/test/rich-results → unesi URL  
**Gde**: Yoast → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "@id": "https://sensiskinstudio.com/hydrafacial-tretmani-lica-novi-sad/#service",
    "name": "HydraFacial® tretman lica",
    "description": "HydraFacial® je višefazni tretman lica koji koristi patentiranu VORTEX tehnologiju za istovremeno čišćenje, eksfolijaciju, ekstrakciju i hidrataciju kože. Dostupan u Signature, De Luxe i Platinum protokolu za sve tipove kože od 14. godine.",
    "provider": {
      "@id": "https://sensiskinstudio.com/#organization"
    },
    "areaServed": {
      "@type": "City",
      "name": "Novi Sad"
    },
    "url": "https://sensiskinstudio.com/hydrafacial-tretmani-lica-novi-sad/"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Šta podrazumeva HydraFacial® tretman?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "HydraFacial® tretman obuhvata 6 različitih faza: limfnu drenažu, čišćenje i eksfolijaciju, hemijski piling, ekstrakciju, hidrataciju i LED svetlosnu terapiju. Koristi patentiranu VORTEX tehnologiju u 60 protokola. Jedini je tretman koji istovremeno čisti i hidrira kožu bez iritacije."
        }
      },
      {
        "@type": "Question",
        "name": "Kome je namenjen HydraFacial® tretman?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "HydraFacial® je namenjen svim tipovima kože, od uzrasta 14 godina. Protokol se individualno prilagođava stanju kože svakog klijenta."
        }
      },
      {
        "@type": "Question",
        "name": "Koliko HydraFacial® tretmana je potrebno uraditi?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Može se raditi kao jednokratni tretman ili kao nedeljne serije zavisno od potrebe kože. Za zdravu kožu preporučuje se mesečno održavanje. Dostupna su tri protokola: Signature, De Luxe i Platinum."
        }
      },
      {
        "@type": "Question",
        "name": "Koje su razlike između HydraFacial® protokola?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Signature protokol je osnovna verzija, De Luxe dodaje LED svetlosnu terapiju, a Platinum uključuje svih 6 faza sa koncentrovanim boosterima. Izbor zavisi od tipa kože i godina klijenta."
        }
      },
      {
        "@type": "Question",
        "name": "Koliki je period oporavka nakon HydraFacial® tretmana?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Nakon HydraFacial® tretmana nema perioda oporavka. Normalne aktivnosti se nastavljaju odmah nakon tretmana."
        }
      },
      {
        "@type": "Question",
        "name": "Kakav rezultat se može očekivati nakon HydraFacial® tretmana?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Rezultat je sjajna koža ujednačenog tena, meka na dodir, sa vidljivo rafiniranijim porama i povećanom hidratacijom. Rezultati su vidljivi odmah nakon tretmana."
        }
      },
      {
        "@type": "Question",
        "name": "Ko ne sme da radi HydraFacial® tretman?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "HydraFacial® tretman ne preporučuje se osobama obolelim od kancera, trudnicama i dojiljama, kao i osobama sa akutnom upalnom reakcijom na koži."
        }
      }
    ]
  }
]
```

---

### STRANICA 3 — Epilacija (`/epilacija/`)

**⚠️ VERIFIKUJ ŽIVU SCHEMA** prvo  
**Gde**: Yoast → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "@id": "https://sensiskinstudio.com/epilacija/#service",
    "name": "Laserska epilacija",
    "description": "Trajna laserska epilacija u Novom Sadu — tretman koji eliminiše dlačice na svim delovima tela i rešava problem uraslih dlaka. Serija od 6 do 10 tretmana postiže do 80% trajnog smanjenja rasta dlaka.",
    "provider": {
      "@id": "https://sensiskinstudio.com/#organization"
    },
    "areaServed": {
      "@type": "City",
      "name": "Novi Sad"
    },
    "url": "https://sensiskinstudio.com/epilacija/"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Kako se pripremiti pre laserske epilacije?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Obrijte regiju 24 sata pre tretmana. Izbegavajte voskanje 2–3 nedelje pre tretmana jer laser cilja folikul dlake na nivou kože. Ne koristite kreme sa retinolom nedelju dana pre tretmana i izbegavajte sunčanje 7–10 dana pre."
        }
      },
      {
        "@type": "Question",
        "name": "Može li laserska epilacija rešiti problem uraslih dlaka?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Da. Laserska epilacija cilja koren dlake, postepeno smanjuje rast i zatvara folikule, čime sprečava nastanak uraslih dlaka. Ovo je jedna od najtraženih prednosti tretmana pored trajnog uklanjanja dlačica."
        }
      },
      {
        "@type": "Question",
        "name": "Koliko tretmana laserske epilacije je potrebno za trajne promene?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Potrebna je serija od 6 do 10 tretmana za trajno smanjenje rasta dlaka. Broj tretmana zavisi od individualnih faktora: boje i debljine dlačice, tipa kože i faze rasta dlake."
        }
      },
      {
        "@type": "Question",
        "name": "Koji tipovi kože i dlaka se mogu tretirati laserskom epilacijom?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Laserska epilacija je najefikasnija na tamnijim, grubljim dlačicama. Optimalni rezultati postižu se kod svetlije kože sa tamnijim dlačicama. Tretman je moguć na različitim tipovima kože uz prilagođavanje parametara lasera."
        }
      }
    ]
  }
]
```

---

### STRANICA 4 — Aura Reality (`/aura-reality-3d-dijagnostika-koze/`) ← ISPRAVLJEN URL

**⚠️ KRITIČNO**: Prethodni fajl imao je POGREŠAN URL `/aura-reality/`. Ovde je tačan URL.  
**Gde**: Yoast → Schema → Custom Schema na stranici `/aura-reality-3d-dijagnostika-koze/`

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "@id": "https://sensiskinstudio.com/aura-reality-3d-dijagnostika-koze/#service",
    "name": "Aura Reality 3D dijagnostika kože",
    "description": "Aura Reality je najnapredniji sistem za 3D analizu kože i lica koji pruža objektivne, merljive parametre stanja kože — volumen, tonus, elastičnost, asimetrije i mikropromene teksture — kao osnovu za individualizovane tretmane u Sensi Skin centru.",
    "provider": {
      "@id": "https://sensiskinstudio.com/#organization"
    },
    "areaServed": {
      "@type": "City",
      "name": "Novi Sad"
    },
    "url": "https://sensiskinstudio.com/aura-reality-3d-dijagnostika-koze/"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Kako izgleda Aura Reality pregled?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Pregled je potpuno bezbolan i traje svega nekoliko minuta. Klijent se pozicionira ispred uređaja koji vrši 3D snimanje lica, a softver analizira više parametara kože i prikazuje ih kao detaljan digitalni model sa svim izmerenim vrednostima."
        }
      },
      {
        "@type": "Question",
        "name": "Šta se tačno analizira Aura Reality dijagnostikom?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Analiziraju se volumen lica, tonus, elastičnost, asimetrije i mikropromene teksture kože. Svi parametri su merljivi i mogu se pratiti tokom vremena, što omogućava objektivnu procenu rezultata svakog tretmana."
        }
      },
      {
        "@type": "Question",
        "name": "Da li je Aura Reality pregled bezbedan?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Dijagnostika je potpuno bezbedna — bez zračenja i bez kontakta sa kožom. Nema iritacije, nelagodnosti ni perioda oporavka. Prikladna je za sve tipove kože."
        }
      },
      {
        "@type": "Question",
        "name": "Za koga je Aura Reality dijagnostika namenjena?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Dijagnostika je namenjena svima koji žele preciznu procenu stanja kože pre odabira tretmana, klijentima anti-age programa i svima koji žele objektivno da prate napredak tokom serije tretmana."
        }
      },
      {
        "@type": "Question",
        "name": "Zašto je dijagnostika važna pre tretmana?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Dijagnostika omogućava tretman jasno definisanih problema umesto pretpostavki. Objektivni podaci osiguravaju ciljane tretmane sa merljivim napretkom i dugoročnim rezultatima umesto generičkih protokola."
        }
      }
    ]
  }
]
```

---

### STRANICA 5 — Nega lica (`/nega-lica/`) ← NOVA STRANICA

**Gde**: Yoast → Schema → Custom Schema  
**Napomena**: Stranica nema FAQ sekciju — samo Service schema.

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://sensiskinstudio.com/nega-lica/#service",
  "name": "Nega lica — kozmetički tretmani",
  "description": "Kompletna nega lica u Sensi Skin centru — od higijenskog klasičnog tretmana kao osnove pravilne nege, preko bioloških specijalnih tretmana sa kombinacijom profesionalnih preparata, aparata i masaže, do terapijskih tretmana za aknoznu kožu. Svaki protokol se planira prema realnim potrebama kože.",
  "provider": {
    "@id": "https://sensiskinstudio.com/#organization"
  },
  "areaServed": {
    "@type": "City",
    "name": "Novi Sad"
  },
  "url": "https://sensiskinstudio.com/nega-lica/",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Tretmani nege lica",
    "itemListElement": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Karboksi terapija"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Tretman očne zone"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Dermapen 4™"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "PRX Kraljevski piling"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Hemijski piling"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Biorevitalizacija"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Cabine concept tretman"}}
    ]
  }
}
```

---

### STRANICA 6 — Mesojet tretmani (`/mesojet-tretmani/`)

**Gde**: Yoast → Schema → Custom Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://sensiskinstudio.com/mesojet-tretmani/#service",
  "name": "Mesojet tretmani — beziglarni mezoterapi",
  "description": "Mesojet koristi patentiranu JET tehnologiju za beziglarnu, neinvazivnu isporuku aktivnih supstanci u dublje slojeve kože komprimovanim vazduhom. Tretman adresira bore, neujednačen ten, akne, hiperpigmentaciju i uvećane pore. Rezultati su vidljivi odmah, bez perioda oporavka.",
  "provider": {
    "@id": "https://sensiskinstudio.com/#organization"
  },
  "areaServed": {
    "@type": "City",
    "name": "Novi Sad"
  },
  "url": "https://sensiskinstudio.com/mesojet-tretmani/"
}
```

---

### STRANICA 7 — Mesojet RF (`/mesojet-rf/`)

**Gde**: Yoast → Schema → Custom Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://sensiskinstudio.com/mesojet-rf/#service",
  "name": "Mesojet RF tretman — radio-frekventno podmlađivanje",
  "description": "Mesojet RF je jedini uređaj na svetu koji koristi specijalnu keramičku sondu za lice i telo, što osigurava maksimalnu provodljivost radio talasa bez površinskih opekotina. Tretman zagrevanjem kože na 40°C stimuliše regeneraciju kolagena i elastina. Standardna serija: 6–8 nedeljnih tretmana.",
  "provider": {
    "@id": "https://sensiskinstudio.com/#organization"
  },
  "areaServed": {
    "@type": "City",
    "name": "Novi Sad"
  },
  "url": "https://sensiskinstudio.com/mesojet-rf/"
}
```

---

### STRANICA 8 — Dermalux (`/dermalux/`)

**Gde**: Yoast → Schema → Custom Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://sensiskinstudio.com/dermalux/#service",
  "name": "Dermalux LED fototerapija",
  "description": "Dermalux LED terapija koristi tri talasne dužine svetlosti: crvenu (633nm) za sintezu kolagena i ćelijsku energiju, plavu (415nm) za antibakterijsko dejstvo kod akne, i NIR (830nm) za duboku penetraciju i zarastanje kože. Neinvazivna, bezbedna, bez perioda oporavka.",
  "provider": {
    "@id": "https://sensiskinstudio.com/#organization"
  },
  "areaServed": {
    "@type": "City",
    "name": "Novi Sad"
  },
  "url": "https://sensiskinstudio.com/dermalux/"
}
```

---

### STRANICA 9 — Tim / O nama (`/kozmetoloski-centar-sensi-skin/`)

**Gde**: Yoast → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "@id": "https://sensiskinstudio.com/#natasa-burka",
    "name": "Nataša Burka",
    "jobTitle": "CEO — Strukovni estetičar, specijalista medicinske estetike",
    "description": "Nataša Burka je strukovni estetičar i specijalista medicinske estetike sa više od 20 godina iskustva u profesionalnoj nezi kože. Osnivač i tehnički direktor Sensi Skin Kozmetološkog Centra u Novom Sadu.",
    "worksFor": {
      "@id": "https://sensiskinstudio.com/#organization"
    },
    "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/",
    "sameAs": [
      "https://www.instagram.com/sensi_skin/"
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": "https://sensiskinstudio.com/#organization",
    "name": "Sensi Skin Kozmetološki Centar",
    "url": "https://sensiskinstudio.com",
    "foundingDate": "2014",
    "description": "Kozmetološki centar u Novom Sadu specijalizovan za tretmane lica i tela, negu kože i anti-age pristup zasnovan na 3D dijagnostici.",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Braće Popović 3, sprat 2, stan 12",
      "addressLocality": "Novi Sad",
      "postalCode": "21000",
      "addressCountry": "RS"
    },
    "telephone": "+381653338338",
    "email": "sensistudio@gmail.com",
    "employee": [
      {
        "@type": "Person",
        "@id": "https://sensiskinstudio.com/#natasa-burka",
        "name": "Nataša Burka",
        "jobTitle": "CEO, Specijalista medicinske estetike"
      },
      {
        "@type": "Person",
        "name": "Isidora Vasić",
        "jobTitle": "Kozmetički tehničar, Menadžer"
      },
      {
        "@type": "Person",
        "name": "Nina Šipčić",
        "jobTitle": "Strukovni kozmetičar-estetičar"
      },
      {
        "@type": "Person",
        "name": "Tamara Stojanović",
        "jobTitle": "Strukovni kozmetičar-estetičar"
      },
      {
        "@type": "Person",
        "name": "Darina Zaskalicki",
        "jobTitle": "Kozmetički tehničar"
      },
      {
        "@type": "Person",
        "name": "Dragana Spasojević",
        "jobTitle": "Koordinator brige o klijentima"
      }
    ]
  }
]
```

---

### STRANICA 10 — Kontakt (`/kontakt-sensi-skin-novi-sad/`)

**Gde**: Yoast → Schema → Custom Schema  
**⚠️ NEEDS VERIFICATION**: radno vreme nije dostupno na stranici — popuni polje `openingHoursSpecification` kada znaš radno vreme.

```json
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "BeautySalon"],
  "@id": "https://sensiskinstudio.com/#organization",
  "name": "Sensi Skin Kozmetološki Centar",
  "url": "https://sensiskinstudio.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Braće Popović 3, sprat 2, stan 12",
    "addressLocality": "Novi Sad",
    "postalCode": "21000",
    "addressCountry": "RS"
  },
  "telephone": "+381653338338",
  "email": "sensistudio@gmail.com",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "20:00"
    }
  ],
  "hasMap": "https://maps.google.com/?cid=8612375676436028978"
}
```

> **Popuni radno vreme**: izmeni `opens`/`closes` vrednosti i `dayOfWeek` niz po stvarnom radnom vremenu. Subota/nedelja: dodaj novi `openingHoursSpecification` objekat nizu ako rade.

---

### STRANICA 11 — Cenovnik (`/cenovnik-kozmetickih-tretmana-novi-sad/`)

**Gde**: Yoast → Schema → Custom Schema  
**Napomena**: ItemList schema čini cene čitljivim za AI motore.

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Cenovnik kozmetičkih tretmana — Sensi Skin",
  "description": "Cenovnik tretmana lica, tela i dijagnostike u Sensi Skin kozmetološkom centru u Novom Sadu.",
  "url": "https://sensiskinstudio.com/cenovnik-kozmetickih-tretmana-novi-sad/",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Service",
        "name": "HydraFacial Signature",
        "offers": {"@type": "Offer", "price": "14000", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Service",
        "name": "HydraFacial Deluxe",
        "offers": {"@type": "Offer", "price": "17000", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "Service",
        "name": "HydraFacial Platinum",
        "offers": {"@type": "Offer", "price": "21000", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 4,
      "item": {
        "@type": "Service",
        "name": "Klasični tretman lica",
        "offers": {"@type": "Offer", "price": "4500", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 5,
      "item": {
        "@type": "Service",
        "name": "Dermapen 4",
        "offers": {"@type": "Offer", "price": "18000", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 6,
      "item": {
        "@type": "Service",
        "name": "PRX Glow",
        "offers": {"@type": "Offer", "price": "8000", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 7,
      "item": {
        "@type": "Service",
        "name": "Mesojet tretman lica",
        "offers": {"@type": "Offer", "price": "12000", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 8,
      "item": {
        "@type": "Service",
        "name": "RF Lifting lica",
        "offers": {"@type": "Offer", "price": "4700", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 9,
      "item": {
        "@type": "Service",
        "name": "Laserska epilacija — noge (pune)",
        "offers": {"@type": "Offer", "price": "12000", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 10,
      "item": {
        "@type": "Service",
        "name": "Laserska epilacija — ruke",
        "offers": {"@type": "Offer", "price": "7500", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 11,
      "item": {
        "@type": "Service",
        "name": "Aura Reality 3D dijagnostika",
        "offers": {"@type": "Offer", "price": "5000", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 12,
      "item": {
        "@type": "Service",
        "name": "Ballancer Pro",
        "offers": {"@type": "Offer", "price": "3000", "priceCurrency": "RSD"}
      }
    },
    {
      "@type": "ListItem",
      "position": 13,
      "item": {
        "@type": "Service",
        "name": "Dermalux LED terapija",
        "offers": {"@type": "Offer", "price": "2000", "priceCurrency": "RSD"}
      }
    }
  ]
}
```

---

### STRANICA 12 — Proizvodi (`/kozmeticki-proizvodi-sensi-skin-studio/`)

**Gde**: Yoast → Schema → Custom Schema  
**Napomena**: WooCommerce stranica — osnovna schema referenca.

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Kozmetički proizvodi — Sensi Skin Studio",
  "description": "Profesionalni kozmetički i dermokozmetički proizvodi za negu kože dostupni u Sensi Skin kozmetološkom centru. Formulisano bez parabena i mineralnih ulja.",
  "url": "https://sensiskinstudio.com/kozmeticki-proizvodi-sensi-skin-studio/",
  "isPartOf": {
    "@id": "https://sensiskinstudio.com/#website"
  },
  "provider": {
    "@id": "https://sensiskinstudio.com/#organization"
  }
}
```

---

## BLOG POSTOVI — Article + FAQPage (5 puna schema)

---

### BLOG 1 — Ballancer Pro (`/ballancer-pro/`)

**Schema verdikt**: Article + FAQPage — eksplicitne Q&A sekcije sa tretmanskim pitanjima.  
**Gde**: Yoast → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "@id": "https://sensiskinstudio.com/ballancer-pro/#article",
    "headline": "BALLANCER PRO",
    "description": "Ballancer Pro je FDA-odobren uređaj za pneumatsku presoterapiju koji stimuliše limfni sistem. Saznajte kako funkcioniše, ko su idealni kandidati i kontraindikacije.",
    "datePublished": "2023-02-27",
    "dateModified": "2023-02-27",
    "author": {
      "@id": "https://sensiskinstudio.com/#natasa-burka"
    },
    "publisher": {
      "@id": "https://sensiskinstudio.com/#organization"
    },
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://sensiskinstudio.com/ballancer-pro/"
    },
    "url": "https://sensiskinstudio.com/ballancer-pro/"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Kako funkcioniše Ballancer Pro?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "U toku tretmana koristi se posebno formulisano odelo sa 24 vazdušne komore, koje stimulišu pokretanje limfe. Jednokratne pantalone koje dobijate prilikom tretmana obezbeđuju maksimalnu higijenu. Tretman je potpuno bezbolan, komforan i izrazito prijatan."
        }
      },
      {
        "@type": "Question",
        "name": "Koliko traje Ballancer Pro tretman?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Tretman traje od 30 do 40 minuta."
        }
      },
      {
        "@type": "Question",
        "name": "Koliko često se rade Ballancer Pro tretmani?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Kao prevencija: 1x mesečno nakon odradjene detox serije. DETOX protokol: 2x nedeljno u trajanju od 3–5 nedelja. Cellulite protokol: 2x nedeljno kao dodatak drugim tretmanima."
        }
      },
      {
        "@type": "Question",
        "name": "Za koga je Ballancer Pro idealan tretman?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Ballancer Pro je idealan za: osobe sa limfedemom, pri padu imuniteta, osobe sa osećajem teških i umornih nogu, osobe sa oteklim donjim ekstremitetima usled dugog sedenja, za detoksikaciju organizma, kod bolova u mišićima i zglobovima, kod gojaznih u cilju smanjenja telesne mase, kod celulita, i kao tretman relaksacije kod osoba pod stresom."
        }
      },
      {
        "@type": "Question",
        "name": "Koje su kontraindikacije za Ballancer Pro?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Ballancer Pro tretman se ne preporučuje u sledećim slučajevima: trudnoća, malignitet, tromboza, kardiovaskularna oboljenja i autoimune bolesti."
        }
      }
    ]
  }
]
```

---

### BLOG 2 — Serum (`/da-li-je-serum-zaista-potreban/`)

**Schema verdikt**: Article + FAQPage — direktan Q&A format sa pitanjima i odgovorima.  
**Gde**: Yoast → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "@id": "https://sensiskinstudio.com/da-li-je-serum-zaista-potreban/#article",
    "headline": "Da li je SERUM zaista potreban?",
    "description": "Odgovori na najčešća pitanja o serumima za lice — da li je serum zaista neophodan, može li zameniti kremu i kako i kada se pravilno koristi.",
    "datePublished": "2023-02-15",
    "dateModified": "2023-02-15",
    "author": {
      "@id": "https://sensiskinstudio.com/#natasa-burka"
    },
    "publisher": {
      "@id": "https://sensiskinstudio.com/#organization"
    },
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://sensiskinstudio.com/da-li-je-serum-zaista-potreban/"
    },
    "url": "https://sensiskinstudio.com/da-li-je-serum-zaista-potreban/"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Da li je serum zaista potreban ako krema već sadrži aktivne supstance?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Da, serum je potreban. Serumi spadaju u kozmetičke preparate koji imaju visok procenat aktivne supstance, njihov zadatak je da prodiru brže i bolje u dublje slojeve kože. Krema deluje na površini i pruža zaštitu, dok serum cilja specifične probleme kože na dubljim nivoima."
        }
      },
      {
        "@type": "Question",
        "name": "Da li serum može zameniti kremu za lice?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Odgovor je NE. Serumi nemaju zaštitne i lipidne komponente koje krema pruža. Serum i krema imaju komplementarne uloge u rutini nege kože i ne treba ih menjati jednu za drugu."
        }
      },
      {
        "@type": "Question",
        "name": "Koliko seruma naneti i kada ga koristiti?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Serum se nanosi nakon čišćenja i toniranja kože, a pre hidratantne kreme. Princip je 'manje je više' — dovoljno je jedna pipeta ili količina veličine zrna graška. Nanosi se laganim tapkanjem, ne trljanjem."
        }
      },
      {
        "@type": "Question",
        "name": "Koji je pravilan redosled rutine kada koristimo serum?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Pravilan redosled je: (1) Čišćenje lica, (2) Tonik, (3) Serum, (4) Hidratantna krema, (5) SPF zaštita ujutru. Uvek se nanese od najtanje do najgušće teksture preparata."
        }
      }
    ]
  }
]
```

---

### BLOG 3 — Melazma (`/melazma/`)

**Schema verdikt**: Article + FAQPage — Q&A struktura sa pitanjima o uzrocima i tretmanu.  
**Gde**: Yoast → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "@id": "https://sensiskinstudio.com/melazma/#article",
    "headline": "Melazma",
    "description": "Šta je melazma, kako se manifestuje, koji su uzroci i kako se leči? Stručno objašnjenje i pregled profesionalnih tretmana za hiperpigmentaciju.",
    "datePublished": "2022-09-24",
    "dateModified": "2022-09-24",
    "author": {
      "@id": "https://sensiskinstudio.com/#natasa-burka"
    },
    "publisher": {
      "@id": "https://sensiskinstudio.com/#organization"
    },
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://sensiskinstudio.com/melazma/"
    },
    "url": "https://sensiskinstudio.com/melazma/"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Kako se manifestuje melazma?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Melazma se pojavljuje kao pigmentne promene na koži lica koje variraju od braon do plavih i sivih tonova, zavisno od toga koji sloj kože je zahvaćen. Najčešće se javlja na obrazima, čelu, nosu i gornjoj usni."
        }
      },
      {
        "@type": "Question",
        "name": "Koji su uzroci melazme?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Uzroci melazme su višestruki: hormonalni disbalans, nedovoljno UV zaštite, određene terapije lekovima, starenje kože i različiti upalni procesi. Hormoni estrogen i progesteron igraju ključnu ulogu, pa je melazma česta kod žena."
        }
      },
      {
        "@type": "Question",
        "name": "Da li melazma nastaje u trudnoći?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Da — više od 50% trudnica razvija melazmu tokom trudnoće ili posle porođaja zbog dejstva hormona progesterona. Stanje se naziva 'maska trudnoće' i može se poboljšati nakon porođaja uz stručan tretman."
        }
      },
      {
        "@type": "Question",
        "name": "Kako se leči melazma?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Tretman melazme je dugotrajan i složen proces. Kućna nega zahteva doslednu rutinu sa aktivnim supstancama kao što su azelainska kiselina, vitamin C i retinol. Profesionalni tretmani uključuju MESOJET, Mela White Green Peel, hemijski piling, Nanopore i PRX kraljevski piling."
        }
      }
    ]
  }
]
```

---

### BLOG 4 — Tretmani pre/posle letovanja (`/tretmani-lica-sta-primeniti-pre-a-sta-posle-letnjeg-odmora/`)

**Schema verdikt**: Article + FAQPage — direktna pitanja o tretmanima.  
**Gde**: Yoast → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "@id": "https://sensiskinstudio.com/tretmani-lica-sta-primeniti-pre-a-sta-posle-letnjeg-odmora/#article",
    "headline": "Tretmani lica: šta primeniti pre, a šta posle letnjeg odmora?",
    "description": "Koji kozmetički tretmani su preporučeni pre letovanja i zašto treba posjetiti kozmetičara po povratku sa odmora? Stručni saveti Sensi Skin centra.",
    "datePublished": "2022-08-10",
    "dateModified": "2022-08-10",
    "author": {
      "@id": "https://sensiskinstudio.com/#natasa-burka"
    },
    "publisher": {
      "@id": "https://sensiskinstudio.com/#organization"
    },
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://sensiskinstudio.com/tretmani-lica-sta-primeniti-pre-a-sta-posle-letnjeg-odmora/"
    },
    "url": "https://sensiskinstudio.com/tretmani-lica-sta-primeniti-pre-a-sta-posle-letnjeg-odmora/"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Da li je potrebno otići na tretman lica pre letovanja?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Da. Lice treba dobro pripremiti za izlaganje suncu, slanoj vodi ili hloru i promenu klime. Pravilna priprema osigurava da koža ostane hidratisana i ojačana tokom odmora. Preporučeni tretmani pre letovanja: higijensko čišćenje, intenzivna hidratacija, HydraFacial i Mesojet tretmani."
        }
      },
      {
        "@type": "Question",
        "name": "Zašto treba da posetite kozmetičara nakon letovanja?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Nagomilavanje odumrlih ćelija kože, pojava bubuljica i dehidratacija su skoro neizbežne pojave po povratku sa letovanja. Izlaganje suncu, slanoj vodi i SPF preparatima ostavlja vidljivo oštećenje. Foto-oštećenja zahtevaju specijalizovane tretmane — preporučujemo Intense Hydra, tretman oksigenacije, PRX kraljevski piling, biorevitalizaciju i Sensi umirujući tretman."
        }
      }
    ]
  }
]
```

---

### BLOG 5 — Nega lica i kozmetičar (`/nega-lica-sta-je-u-rukama-kozmeticara-a-sta-je-do-vas/`)

**Schema verdikt**: Article + FAQPage — pitanja o svakodnevnim navikama nege kože.  
**Gde**: Yoast → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "@id": "https://sensiskinstudio.com/nega-lica-sta-je-u-rukama-kozmeticara-a-sta-je-do-vas/#article",
    "headline": "Nega lica: šta je u rukama kozmetičara, a šta je do vas?",
    "description": "Koji deo nege kože je odgovornost kozmetičara, a koji vaša? Odgovori na pitanja o svakodnevnim navikama koje direktno utiču na stanje kože.",
    "datePublished": "2022-08-02",
    "dateModified": "2022-08-02",
    "author": {
      "@id": "https://sensiskinstudio.com/#natasa-burka"
    },
    "publisher": {
      "@id": "https://sensiskinstudio.com/#organization"
    },
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://sensiskinstudio.com/nega-lica-sta-je-u-rukama-kozmeticara-a-sta-je-do-vas/"
    },
    "url": "https://sensiskinstudio.com/nega-lica-sta-je-u-rukama-kozmeticara-a-sta-je-do-vas/"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Koliko često je prihvatljivo zaspati sa šminkom na licu?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Nikada — ovo je greška koja direktno šteti koži. Kada ostane šminka na licu tokom noći, pore ostaju začepljene i dolazi do upale kože, posebno u predelu očiju. Micelarna voda je efikasno i nežno sredstvo za skidanje šminke pre spavanja."
        }
      },
      {
        "@type": "Question",
        "name": "Da li treba imati poseban peškir za lice?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Da — poseban peškir za lice je obavezan. Na zajedničkim peškirima se akumuliraju bakterije koje mogu izazvati iritaciju i akne, čime se poništava efekat svakog kozmetičkog preparata koji koristite. Menjajte peškir za lice redovno, barem jednom sedmično."
        }
      },
      {
        "@type": "Question",
        "name": "Koliko često treba čistiti sunđere i četkice za šminkanje?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sve što dodiruje lice mora biti detaljno očišćeno. Sunđeri i četkice skupljaju bakterije, ostatke preparata i ulje kože — ako se koriste svakodnevno, treba ih čistiti jednom nedeljno specijalnim sredstvima ili 70% alkoholom. Prljavi alati za šminkanje direktno uzrokuju upale i akne."
        }
      }
    ]
  }
]
```

---

## BLOG POSTOVI — Article only (29 postova)

### Šablon za kopiranje (zameni naznačena polja)

**Gde**: Svaki blog post → Yoast → Schema → Custom Schema  
**Zameni**: `NASLOV`, `URL-SLUG`, `DATUM-OBJAVE`, `DATUM-IZMENE`, `OPIS`

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "https://sensiskinstudio.com/URL-SLUG/#article",
  "headline": "NASLOV",
  "description": "OPIS (1-2 rečenice o čemu je članak)",
  "datePublished": "DATUM-OBJAVE",
  "dateModified": "DATUM-IZMENE",
  "author": {
    "@id": "https://sensiskinstudio.com/#natasa-burka"
  },
  "publisher": {
    "@id": "https://sensiskinstudio.com/#organization"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensiskinstudio.com/URL-SLUG/"
  },
  "url": "https://sensiskinstudio.com/URL-SLUG/"
}
```

### Tabela vrednosti za svih 29 Article-only postova

| URL slug | Naslov | datePublished | dateModified |
|----------|--------|--------------|-------------|
| `/dermalux-led-terapija-kao-resenje-problema/` | DERMALUX LED terapija kao rešenje problema | 2024-04-02 | 2026-04-06 |
| `/leto-i-promene-na-kozi/` | Leto i promene na koži | 2024-08-02 | 2026-03-31 |
| `/posledice-starenja-na-kozi/` | Posledice starenja na koži | 2024-01-10 | 2024-01-10 |
| `/prva-pomoc-kozi-u-hladnim-danima/` | PRVA POMOĆ koži u hladnim danima | 2023-12-04 | 2023-12-04 |
| `/sinergija-estetskih-procedura-i-tretmana-lica/` | Sinergija estetskih procedura i tretmana lica | 2023-05-09 | 2023-05-09 |
| `/uticaj-kiseonika-na-kozu/` | Uticaj kiseonika na kožu | 2023-04-26 | 2023-04-26 |
| `/koraci-unapredjene-nege-lica/` | Koraci unapredjene nege lica | 2023-03-24 | 2023-03-24 |
| `/osnovni-koraci-svakodnevne-beauty-rutine/` | Osnovni koraci svakodnevne "beauty" rutine | 2023-03-21 | 2023-03-21 |
| `/faktori-rasta-u-borbi-protiv-starenja-koze/` | Faktori rasta u borbi protiv starenja kože | 2023-01-31 | 2023-01-31 |
| `/obuzdati-se-i-ne-dirati-akne-kako/` | Obuzdati se i ne dirati akne. Kako? | 2023-01-17 | 2023-01-17 |
| `/pojava-osetljivosti-koze-tokom-zimskih-dana/` | Pojava osetljivosti kože tokom zimskih dana | 2022-12-28 | 2022-12-28 |
| `/da-li-vas-plase-hemijski-pilinzi/` | Da li vas plaše hemijski pilinzi? | 2022-12-06 | 2022-12-06 |
| `/perutanje-koze/` | Perutanje kože – najčešći uzroci i rešenja | 2022-10-31 | 2022-10-31 |
| `/dermatolog-ili-esteticar/` | Dermatolog ili estetičar – kome i kada se obratiti? | 2022-10-14 | 2022-10-14 |
| `/jesenji-rezim-nege/` | Jesenji režim nege | 2022-09-19 | 2022-09-19 |
| `/rozacea-kako-da-ublazite-simptome/` | Rozacea: kako da ublažite simptome? | 2022-09-09 | 2022-09-09 |
| `/tipovi-i-stanje-koze-u-cemu-je-razlika-i-kako-da-ih-odredite/` | Tipovi i stanje kože – u čemu je razlika i kako da ih odredite | 2022-08-30 | 2022-08-30 |
| `/promene-na-kozi-kao-posledica-suncanja/` | Promene na koži kao posledica sunčanja | 2022-08-22 | 2022-08-22 |
| `/vrste-akni/` | Vrste akni | 2022-08-19 | 2022-08-19 |
| `/sta-cete-spakovati-u-svoj-beauty-kofer/` | Šta ćete spakovati u svoj beauty kofer? | 2022-07-07 | 2022-07-07 |
| `/predeo-oko-ociju-kako-negovati-ovu-osetljvu-regiju/` | Predeo oko očiju – kako negovati ovu osetljivu regiju? | 2022-07-18 | 2022-07-18 |
| `/menopauza-i-pravilna-nega-koze/` | Menopauza i pravilna nega kože | 2022-06-20 | 2022-06-20 |
| `/gubitak-kose-i-androgena-alopecija/` | Gubitak kose i androgena alopecija | 2022-06-27 | 2022-06-27 |
| `/stetnost-solarijuma/` | Štetnost solarijuma | 2022-06-14 | 2022-06-14 |
| `/pravilna-dnevna-rutina-za-negu-koze-lica/` | Pravilna dnevna rutina za negu kože lica | 2022-06-09 | 2022-06-09 |
| `/mesojet-hy-po-rf/` | MesoJet HY-PO RF | 2022-03-14 | 2022-03-14 |
| `/pure-lift-pro/` | Pure Lift Pro | 2020-03-10 | 2020-03-10 |
| `/obuzdati-se-i-ne-dirati-akne-kako/` | Obuzdati se i ne dirati akne. Kako? | 2023-01-17 | 2023-01-17 |
| `/sve-istine-o-laserskoj-epilaciji/` | Sve ISTINE o laserskoj EPILACIJI | 2023-09-04 | 2026-06-09 |

> **Napomena za `/sve-istine-o-laserskoj-epilaciji/`**: Korisnik je dodao FAQPage schema (prema potvrdi). Ovde samo Article/BlogPosting schema — FAQPage je već u polju, koristi JSON array `[{...Article...}, {...FAQPage...}]`.

---

## SEO META TABELA — Svi blog postovi

| URL slug | SEO Title | Fokusni izraz | Meta opis (maks. 155 znakova) |
|----------|-----------|--------------|-------------------------------|
| `/ballancer-pro/` | Ballancer Pro tretman — šta je i kako funkcioniše | ballancer pro tretman | Saznajte šta je Ballancer Pro, kako funkcioniše, ko su idealni kandidati i koliko traje tretman. Zakazite u Sensi Skin: 065/333-8-338. |
| `/da-li-je-serum-zaista-potreban/` | Da li je serum zaista potreban? — odgovori | da li je serum potreban | Da li serum zaista treba? Saznajte razliku između seruma i kreme, kada i kako se nanosi i zašto je bitan korak u rutini. |
| `/melazma/` | Melazma — uzroci, simptomi i tretman | melazma tretman | Šta je melazma, kako nastaje i kako se leči? Stručni saveti i pregled profesionalnih tretmana za hiperpigmentaciju kože. |
| `/tretmani-lica-sta-primeniti-pre-a-sta-posle-letnjeg-odmora/` | Tretmani lica pre i posle letovanja — saveti | tretmani lica pre letovanja | Koji tretmani lica su preporučeni pre letovanja i koji posle? Stručni saveti kozmetičara za pripremu i obnovu kože. |
| `/nega-lica-sta-je-u-rukama-kozmeticara-a-sta-je-do-vas/` | Nega lica: šta je do kozmetičara, a šta do vas? | nega lica saveti | Koji deo nege kože obezbeđuje kozmetičar, a šta je vaša odgovornost? Saveti o peškiru, šminci i higijeni. |
| `/dermalux-led-terapija-kao-resenje-problema/` | Dermalux LED terapija — za koga i koliko tretmana | dermalux LED terapija | DERMALUX LED terapija kao rešenje za problematičnu, aknoznu i reaktivnu kožu — kako svetlost leči i koliko tretmana treba. |
| `/leto-i-promene-na-kozi/` | Leto i promene na koži — prva pomoć i tretmani | promene na koži posle leta | Kako sunce menja kožu i koji tretmani pomažu obnovi kože posle letovanja? LED terapija, Mesojet i Karboksi terapija. |
| `/posledice-starenja-na-kozi/` | Posledice starenja na koži — prevencija i tretmani | posledice starenja na koži | Koji su prvi znaci starenja kože i koji tretmani ih usporavaju? Stručni vodič Sensi Skin centra za anti-age negu. |
| `/prva-pomoc-kozi-u-hladnim-danima/` | Prva pomoć koži u hladnim danima — zimska nega | zimska nega kože | Kako obnoviti kožnu barijeru tokom zime? Korak-po-korak vodič za hladne dane i preporučeni tretmani u Sensi Skin. |
| `/sinergija-estetskih-procedura-i-tretmana-lica/` | Sinergija estetskih procedura i tretmana lica | estetske procedure i tretmani lica | Kako kombinovati injekcione estetske procedure sa tretmanima lica? Šta se sme, šta ne i koliko treba čekati. |
| `/uticaj-kiseonika-na-kozu/` | Uticaj kiseonika na kožu — oksigenacija kože | oksigenacija kože | Zašto koža stari brže kada joj nedostaje kiseonik i kako CO2 tretman vraća svežinu i sijaj koži. |
| `/koraci-unapredjene-nege-lica/` | Koraci unapredjene nege lica — serumi, maske, piling | unapređena nega lica | Dodajte serume, maske i piling u svoju rutinu nege lica. Vodič za pravilnu primenu i redosled preparata. |
| `/osnovni-koraci-svakodnevne-beauty-rutine/` | Osnovna beauty rutina — jutarnja i večernja nega | osnovna beauty rutina | Koji su obavezni koraci jutarnje i večernje nege lica? Stručni vodič za osnovu koja daje vidljive rezultate. |
| `/faktori-rasta-u-borbi-protiv-starenja-koze/` | Faktori rasta u borbi protiv starenja kože | faktori rasta kože | Šta su faktori rasta u kozmetologiji i kako pomažu kolagenu i elastinu? EGF, FGF, IGF i primena u tretmanima. |
| `/obuzdati-se-i-ne-dirati-akne-kako/` | Obuzdati se i ne dirati akne — kako to uspeti? | ne dirati akne | Zašto je diranje akni štetno i šta da radite umesto toga? Saveti i SOS gel kao rešenje za problematičnu kožu. |
| `/pojava-osetljivosti-koze-tokom-zimskih-dana/` | Osetljivost kože zimi — uzroci i tretmani | osetljiva koža zimi | Koji su znaci upozorenja kada koža postane osetljiva tokom zime i koji tretmani vraćaju kožnu barijeru? |
| `/da-li-vas-plase-hemijski-pilinzi/` | Hemijski pilinzi — kako funkcionišu i da li su bezbedni | hemijski piling | Da li vas plaše hemijski pilinzi? Saznajte kako funkcionišu, šta se dešava na koži i zašto su bezbedni. |
| `/perutanje-koze/` | Perutanje kože — uzroci i rešenja | perutanje kože uzroci | Najčešći uzroci perutanja kože i efikasna rešenja za kućnu negu i profesionalne tretmane u Sensi Skin. |
| `/dermatolog-ili-esteticar/` | Dermatolog ili estetičar — kome se obratiti? | dermatolog ili estetičar | Kome da se obratite — dermatologu ili kozmetičaru-estetičaru? Razlike u ulogi i kada je ko pravi izbor. |
| `/jesenji-rezim-nege/` | Jesenji režim nege kože — vodič za jesen | jesenji režim nege kože | Kako prilagoditi rutinu nege kože jesenjem periodu? SPF, retinol, hidratacija i tretmani preporučeni za jesen. |
| `/rozacea-kako-da-ublazite-simptome/` | Rozacea — simptomi, uzroci i nega kože | rozacea nega kože | Šta je rozacea, koji su simptomi i kako da ublažite crvenilo i iritaciju? Stručni saveti i profesionalni tretmani. |
| `/tipovi-i-stanje-koze-u-cemu-je-razlika-i-kako-da-ih-odredite/` | Tipovi i stanje kože — u čemu je razlika? | tipovi kože razlika | Kako da razlikujete tip kože od stanja kože i zašto je ta razlika važna za pravilnu negu? Stručni vodič. |
| `/promene-na-kozi-kao-posledica-suncanja/` | Promene na koži od sunca — fleke i hiperpigmentacija | fleke od sunca na licu | Kako sunce uzrokuje hiperpigmentaciju i fleke na licu? Uzroci, tipovi i efikasni tretmani za uklanjanje. |
| `/vrste-akni/` | Vrste akni — tipovi i razlike | vrste akni | Koje su vrste akni i čime se razlikuju? Od komedona do nodulo-cistične akne — stručni vodič za pravilno tretiranje. |
| `/sta-cete-spakovati-u-svoj-beauty-kofer/` | Beauty kofer za letovanje — šta spakovati | beauty kofer za letovanje | Koji preparati su neophodni za letnji beauty kofer? Saveti za negu lica, tela i kose na odmoru. |
| `/predeo-oko-ociju-kako-negovati-ovu-osetljvu-regiju/` | Nega predela oko očiju — koža kapaka i podočnjaci | nega oko očiju | Kako negovati osetljivu kožu oko očiju? Uzroci podočnjaka, pravi preparati i profesionalni tretmani. |
| `/menopauza-i-pravilna-nega-koze/` | Menopauza i nega kože — promene i rešenja | nega kože u menopauzi | Kako menopauza utiče na kožu i koji su pravi kozmetički preparati i tretmani za žene u menopauzi? |
| `/gubitak-kose-i-androgena-alopecija/` | Gubitak kose i androgena alopecija — uzroci i tretmani | androgena alopecija tretman | Zašto dolazi do gubitka kose i šta je androgena alopecija? Uzroci, simptomi i metode lečenja. |
| `/stetnost-solarijuma/` | Štetnost solarijuma — zašto je opasno | štetnost solarijuma | Zašto je solarijum štetan za kožu i organizam? UV zračenje, rizik od melanoma i bezbedne alternative. |
| `/pravilna-dnevna-rutina-za-negu-koze-lica/` | Pravilna dnevna rutina za negu kože lica | dnevna rutina nega kože lica | Koji su koraci pravilne dnevne rutine za negu kože lica? Čišćenje, serum, krema i profesionalni tretmani. |
| `/mesojet-hy-po-rf/` | MesoJet HY-PO RF tretman — šta je i kako radi | mesojet hy po rf | MesoJet HY-PO RF — beziglarni tretman koji kombinuje hidrodermoabraziju, piling i transdermalnu isporuku aktivnih supstanci. |
| `/pure-lift-pro/` | Pure Lift Pro — neinvazivni lifting lica | pure lift pro tretman | Pure Lift Pro koristi TRIPLE WAVE tehnologiju za stimulaciju mišića lica i produkciju kolagena — bez igala i bola. |
| `/sve-istine-o-laserskoj-epilaciji/` | Sve istine o laserskoj epilaciji — FAQ | sve istine o laserskoj epilaciji | 7 najčešćih pitanja o laserskoj epilaciji: trajnost, bol, broj tretmana, bezbednost i ljetnja primena. |

---

## MASTER TABELA — Sve stranice i postovi

| URL | Tip | Tekući schema status | Potrebna schema | Status |
|-----|-----|---------------------|----------------|--------|
| `/` | Home | ❌ Nema | WebSite + LocalBusiness | Generisati |
| `/hydrafacial-tretmani-lica-novi-sad/` | Service | ⚠️ Proveriti (prethodni fajl ima schema) | Service + FAQPage (7 Q) | Verifikovati live |
| `/epilacija/` | Service | ⚠️ Proveriti | Service + FAQPage (4 Q) | Verifikovati live |
| `/aura-reality-3d-dijagnostika-koze/` | Service | ⚠️ URL bio pogrešan | Service + FAQPage (5 Q) | Ispraviti URL, verifikovati |
| `/nega-lica/` | Service | ❌ Nema | Service | Generisati |
| `/mesojet-tretmani/` | Service | ❌ Nema | Service | Generisati |
| `/mesojet-rf/` | Service | ❌ Nema | Service | Generisati |
| `/dermalux/` | Service | ❌ Nema | Service | Generisati |
| `/kozmetoloski-centar-sensi-skin/` | About | ❌ Nema | Person + Organization | Generisati |
| `/kontakt-sensi-skin-novi-sad/` | Contact | ❌ Nema | LocalBusiness + Radno vreme | Generisati ⚠️ |
| `/cenovnik-kozmetickih-tretmana-novi-sad/` | Price list | ❌ Nema | ItemList (cenovnik) | Generisati |
| `/kozmeticki-proizvodi-sensi-skin-studio/` | Products | ❌ Nema | WebPage ref | Generisati |
| `/sve-istine-o-laserskoj-epilaciji/` | Blog | ⚠️ Proveriti live | Article + FAQPage | Verifikovati |
| `/ballancer-pro/` | Blog | ❌ Nema | Article + FAQPage | Generisano ✅ |
| `/da-li-je-serum-zaista-potreban/` | Blog | ❌ Nema | Article + FAQPage | Generisano ✅ |
| `/melazma/` | Blog | ❌ Nema | Article + FAQPage | Generisano ✅ |
| `/tretmani-lica-sta-primeniti-pre-a-...` | Blog | ❌ Nema | Article + FAQPage | Generisano ✅ |
| `/nega-lica-sta-je-u-rukama-...` | Blog | ❌ Nema | Article + FAQPage | Generisano ✅ |
| Svih 29 ostalih blog postova | Blog | ❌ Nema | BlogPosting Article | Šablon + tabela ✅ |
| `/moj-nalog-sensi-skin-studio/` | WooCommerce | N/A | PRESKOČITI | N/A |

---

## REDOSLED IMPLEMENTACIJE

| Prior. | Stranica | Akcija | Vreme |
|--------|---------|--------|-------|
| 1 | Yoast Knowledge Graph | Podesite Organization jednom (sitewide) | 5 min |
| 2 | Početna `/` | Nalepi WebSite + LocalBusiness | 3 min |
| 3 | Aura Reality | Nalepi schema na **ispravnu** stranicu `/aura-reality-3d-dijagnostika-koze/` | 3 min |
| 4 | HydraFacial | Verifikuj via Rich Results Test → ako nema, nalepi | 3 min |
| 5 | Epilacija | Verifikuj via Rich Results Test → ako nema, nalepi | 3 min |
| 6 | Nega lica | Nova service schema | 2 min |
| 7 | Mesojet RF, Mesojet, Dermalux | Po jedna service schema | 6 min |
| 8 | Tim stranica | Person + Organization | 3 min |
| 9 | Kontakt | LocalBusiness + radno vreme | 3 min |
| 10 | Cenovnik | ItemList schema | 3 min |
| 11 | 5 blog FAQPage postova | Ballancer, Serum, Melazma, Letovanje, Nega+kozmetičar | 15 min |
| 12 | Ostali blog postovi (29) | Article šablon, popuni vrednosti iz tabele | 30 min |
| **UKUPNO** | | | **~80 min** |

---

## VERIFIKACIJA POSLE IMPLEMENTACIJE

Za **svaku stranicu** posle implementacije:
1. **Google Rich Results Test**: https://search.google.com/test/rich-results → unesi URL
2. **Schema validacija**: https://validator.schema.org/ → unesi URL
3. **GSC Request Indexing**: u GSC → URL Inspection → Request Indexing

---

*Generisano na osnovu direktnog crawla post-sitemap.xml i page-sitemap.xml — jun 2026.*
*Ukupno: 14 stranica + 34 blog posta = 48 URL-ova pokriveno.*
