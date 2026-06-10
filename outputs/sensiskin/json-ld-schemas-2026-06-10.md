# JSON-LD Schema — sensiskinstudio.com
**Datum**: 10. jun 2026.  
**Format**: Sve scheme su u formatu za Yoast Custom Schema polje (JSON bez `<script>` tagova)

---

## KORAK 0 — Yoast Knowledge Graph (jednom, za ceo sajt)

Ovo je najvažniji korak — konfiguriše LocalBusiness schema koja se automatski dodaje na SVE stranice.

**WordPress → SEO (Yoast) → Opšta podešavanja → Knowledge Graph & Schema**

Popuni ova polja:

| Polje | Vrednost |
|-------|---------|
| Tip organizacije | **LocalBusiness** |
| Ime organizacije | `Sensi Skin Kozmetološki Centar` |
| URL sajta | `https://sensiskinstudio.com` |
| Logo organizacije | uploaduj logo |
| Opis (ako postoji polje) | `Kozmetološki centar u Novom Sadu specijalizovan za tretmane lica i tela, negu kože i anti-age pristup zasnovan na 3D dijagnostici.` |

**Važno**: Nakon ove konfiguracije, Yoast automatski dodaje LocalBusiness schema na svaku stranicu. Nije potrebno ručno dodavati LocalBusiness schema u Custom Schema polje bilo koje stranice.

---

## STRANICA 1 — Početna strana (`/`)

**Kuda**: WordPress → Stranice → Početna → Yoast SEO → Schema → Custom Schema

Ova schema dopunjuje Yoast Knowledge Graph sa WebSite schema i tačnim NAP podacima (Ime, Adresa, Telefon). Lepi u Custom Schema polje:

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
      "@type": "LocalBusiness",
      "name": "Sensi Skin Kozmetološki Centar"
    }
  },
  {
    "@context": "https://schema.org",
    "@type": ["LocalBusiness", "BeautySalon"],
    "@id": "https://sensiskinstudio.com/#organization",
    "name": "Sensi Skin Kozmetološki Centar",
    "url": "https://sensiskinstudio.com",
    "description": "Kozmetološki centar u Novom Sadu specijalizovan za tretmane lica i tela, negu kože i anti-age pristup zasnovan na 3D dijagnostici. Osnovan 2014. godine.",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Braće Popović 3, sprat 2, stan 12",
      "addressLocality": "Novi Sad",
      "postalCode": "21000",
      "addressCountry": "RS"
    },
    "telephone": "+381653338338",
    "email": "sensistudio@gmail.com",
    "foundingDate": "2014",
    "priceRange": "€€",
    "sameAs": [
      "https://www.instagram.com/sensi_skin/",
      "https://www.facebook.com/sensi.skin.studiozanegulepote/"
    ]
  }
]
```

---

## STRANICA 2 — HydraFacial (`/hydrafacial-tretmani-lica-novi-sad/`)

**Kuda**: WordPress → Stranice → HydraFacial → Yoast SEO → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "HydraFacial® tretman lica",
    "description": "HydraFacial® je višefazni tretman lica koji koristi patentiranu VORTEX tehnologiju za istovremeno čišćenje, eksfolijaciju, ekstrakciju i hidrataciju kože. Dostupan u Signature, De Luxe i Platinum protokolu za sve tipove kože od 14. godine.",
    "provider": {
      "@type": "LocalBusiness",
      "name": "Sensi Skin Kozmetološki Centar",
      "url": "https://sensiskinstudio.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Braće Popović 3, sprat 2, stan 12",
        "addressLocality": "Novi Sad",
        "addressCountry": "RS"
      },
      "telephone": "+381653338338"
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

## STRANICA 3 — Epilacija (`/epilacija/`)

**Kuda**: WordPress → Stranice → Epilacija → Yoast SEO → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Laserska epilacija",
    "description": "Trajna laserska epilacija u Novom Sadu — tretman koji eliminiše dlačice na svim delovima tela i rešava problem uraslih dlaka. Serija od 6 do 10 tretmana postiže do 80% trajnog smanjenja rasta dlaka.",
    "provider": {
      "@type": "LocalBusiness",
      "name": "Sensi Skin Kozmetološki Centar",
      "url": "https://sensiskinstudio.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Braće Popović 3, sprat 2, stan 12",
        "addressLocality": "Novi Sad",
        "addressCountry": "RS"
      },
      "telephone": "+381653338338"
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

## STRANICA 4 — Aura Reality 3D dijagnostika (`/aura-reality/`)

**Kuda**: WordPress → Stranice → Aura Reality → Yoast SEO → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Aura Reality 3D dijagnostika kože",
    "description": "Aura Reality je najnapredniji sistem za 3D analizu kože i lica koji pruža objektivne, merljive parametre stanja kože — volumen, tonus, elastičnost, asimetrije i mikropromene teksture — kao osnovu za individualizovane tretmane u Sensi Skin centru.",
    "provider": {
      "@type": "LocalBusiness",
      "name": "Sensi Skin Kozmetološki Centar",
      "url": "https://sensiskinstudio.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Braće Popović 3, sprat 2, stan 12",
        "addressLocality": "Novi Sad",
        "addressCountry": "RS"
      },
      "telephone": "+381653338338"
    },
    "areaServed": {
      "@type": "City",
      "name": "Novi Sad"
    },
    "url": "https://sensiskinstudio.com/aura-reality/"
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

## STRANICA 5 — Mesojet RF (`/mesojet-rf/`)

**Kuda**: WordPress → Stranice → Mesojet RF → Yoast SEO → Schema → Custom Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Mesojet RF tretman — radio-frekventno podmlađivanje",
  "description": "Mesojet RF je jedini uređaj na svetu koji koristi specijalnu keramičku sondu za lice i telo, što osigurava maksimalnu provodljivost radio talasa bez površinskih opekotina. Tretman zagrevanjem kože na 40°C stimuliše regeneraciju kolagena i elastina, pruža nesurgički lifting lica i vidljivo poboljšava tonus i elastičnost kože.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Sensi Skin Kozmetološki Centar",
    "url": "https://sensiskinstudio.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Braće Popović 3, sprat 2, stan 12",
      "addressLocality": "Novi Sad",
      "addressCountry": "RS"
    },
    "telephone": "+381653338338"
  },
  "areaServed": {
    "@type": "City",
    "name": "Novi Sad"
  },
  "url": "https://sensiskinstudio.com/mesojet-rf/"
}
```

---

## STRANICA 6 — Mesojet tretmani (`/mesojet-tretmani/`)

**Kuda**: WordPress → Stranice → Mesojet tretmani → Yoast SEO → Schema → Custom Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Mesojet tretmani — beziglarni mezoterapi",
  "description": "Mesojet koristi patentiranu JET tehnologiju za beziglarnu, neinvazivnu isporuku aktivnih supstanci u dublje slojeve kože komprimovanim vazduhom. Tretman adresira bore, neujednačen ten, akne, hiperpigmentaciju i uvećane pore. Rezultati su vidljivi odmah, bez perioda oporavka.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Sensi Skin Kozmetološki Centar",
    "url": "https://sensiskinstudio.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Braće Popović 3, sprat 2, stan 12",
      "addressLocality": "Novi Sad",
      "addressCountry": "RS"
    },
    "telephone": "+381653338338"
  },
  "areaServed": {
    "@type": "City",
    "name": "Novi Sad"
  },
  "url": "https://sensiskinstudio.com/mesojet-tretmani/"
}
```

---

## STRANICA 7 — Dermalux LED terapija (`/dermalux/`)

**Kuda**: WordPress → Stranice → Dermalux → Yoast SEO → Schema → Custom Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Dermalux LED terapija lica",
  "description": "Dermalux LED terapija koristi tri talasne dužine svetlosti za terapeutske efekte na kožu: crvenu (633nm) za sintezu kolagena i ćelijsku energiju, plavu (415nm) za antibakterijsko dejstvo kod akne, i NIR (830nm) za duboku penetraciju i zarastanje. Neinvazivna, bezbedna i bez perioda oporavka.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Sensi Skin Kozmetološki Centar",
    "url": "https://sensiskinstudio.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Braće Popović 3, sprat 2, stan 12",
      "addressLocality": "Novi Sad",
      "addressCountry": "RS"
    },
    "telephone": "+381653338338"
  },
  "areaServed": {
    "@type": "City",
    "name": "Novi Sad"
  },
  "url": "https://sensiskinstudio.com/dermalux/"
}
```

---

## STRANICA 8 — Tim / O nama (`/kozmetoloski-centar-sensi-skin/`)

**Kuda**: WordPress → Stranice → Tim → Yoast SEO → Schema → Custom Schema

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Nataša Burka",
    "jobTitle": "Medicinsko-estetski stručnjak, CEO",
    "description": "Nataša Burka je medicinsko-estetski stručnjak sa više od 20 godina iskustva u profesionalnoj nezi kože. Osnivač i vlasnik Sensi Skin Kozmetološkog Centra u Novom Sadu. Specijalista za barijeru kože, inflamatorne i vaskularne promene i moderne anti-age strategije zasnovane na 3D digitalnoj dijagnostici.",
    "worksFor": {
      "@type": "LocalBusiness",
      "name": "Sensi Skin Kozmetološki Centar",
      "url": "https://sensiskinstudio.com"
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
    "employee": [
      {
        "@type": "Person",
        "name": "Nataša Burka",
        "jobTitle": "CEO, Medicinsko-estetski stručnjak"
      },
      {
        "@type": "Person",
        "name": "Isidora Vasić"
      },
      {
        "@type": "Person",
        "name": "Nina Šipčić"
      },
      {
        "@type": "Person",
        "name": "Tamara Stojanović"
      },
      {
        "@type": "Person",
        "name": "Darina Zaskalicki"
      },
      {
        "@type": "Person",
        "name": "Dragana Spasojević"
      }
    ]
  }
]
```

---

## BLOG POSTOVI — uputstvo + Article schema

### Korak 1: Yoast podešavanje (za SVE blog postove)

Za svaki blog post u WordPress editoru:

1. Yoast SEO panel → **Schema** tab
2. **Page type**: Veb stranica
3. **Article type**: **BlogPosting** ← ovo je ključno
4. Yoast će automatski generisati Article/BlogPosting schema

Ovo je dovoljno za osnovnu Article schema na svim postovima. Custom Schema polje koristiš samo za FAQPage (vidi dole).

---

### Korak 2: Author (za SVE blog postove)

Ako blog postovi nemaju vidljivog autora, Yoast neće dodati author u Article schema. Fix:

**WordPress → Korisnici → Tvoj profil** → popuni:
- Ime i prezime: `Nataša Burka`
- Biografija: (kratki opis sa titulom)

Zatim na svakom blog postu: **Post author** = Nataša Burka

---

### Korak 3: Custom Schema — samo za postove sa FAQ sadržajem

#### Blog post: "Sve istine o laserskoj epilaciji" (`/sve-istine-o-laserskoj-epilaciji/`)

**Napomena**: Korisnik je već dodao FAQPage schema. Article schema se generiše automatski kroz Yoast (Korak 1). Ova stranica je **završena** ako je Yoast Schema type = Article + BlogPosting.

---

#### Svi ostali blog postovi — NEMA potrebe za Custom Schema

Yoast automatski generiše BlogPosting schema kada podesite Article type = BlogPosting. Custom Schema polje ostaviti prazno za:
- `/dermalux-led-terapija-kao-resenje-problema/`
- `/leto-i-promene-na-kozi/`
- `/posledice-starenja-na-kozi/`
- `/prva-pomoc-kozi-u-hladnim-danima/`
- `/sinergija-estetskih-procedura-i-tretmana-lica/`
- `/uticaj-kiseonika-na-kozu/`
- `/koraci-unapredjene-nege-lica/`
- `/osnovni-koraci-svakodnevne-beauty-rutine/`
- `/ballancer-pro/`

**Jedini task za ove postove**: Yoast → Schema → Article type = BlogPosting + podesi autora (vidi Korak 2).

---

## Redosled implementacije

| Prior. | Stranica | Schema tip | Vreme |
|--------|----------|-----------|-------|
| 1 | Yoast Knowledge Graph | LocalBusiness (sitewide) | 5 min |
| 2 | Početna `/` | WebSite + LocalBusiness | 3 min |
| 3 | HydraFacial | Service + FAQPage (7 pitanja) | 3 min |
| 4 | Epilacija | Service + FAQPage (4 pitanja) | 3 min |
| 5 | Aura Reality | Service + FAQPage (5 pitanja) | 3 min |
| 6 | Tim stranica | Person + Organization | 3 min |
| 7 | Mesojet RF | Service | 2 min |
| 8 | Mesojet tretmani | Service | 2 min |
| 9 | Dermalux | Service | 2 min |
| 10 | Svi blog postovi (9) | Yoast Schema → BlogPosting | 15 min |
| **Ukupno** | | | **~41 min** |

---

## Gde lepiš JSON kod u WordPress

Za **svaku stranicu/post**:
1. WordPress editor → otvori stranicu/post
2. Desno → **Yoast SEO** → klikni na **Schema** tab
3. Skroluj do **Custom Schema** polja
4. Ljepi JSON iz ovog dokumenta (BEZ `<script>` tagova)
5. Klikni **Sačuvaj / Objavi**

**Kada su DVE scheme** (npr. Service + FAQPage), koristi JSON array format koji je već primenjen u ovim primerima: `[{...}, {...}]`

---

*Schema kod generisan na osnovu direktnog crawla svih stranica sensiskinstudio.com — juni 2026.*
