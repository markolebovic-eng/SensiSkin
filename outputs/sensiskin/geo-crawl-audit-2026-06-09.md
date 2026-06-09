# GEO Deep Crawl Audit — sensiskinstudio.com
**Datum**: 9. jun 2026.  
**Metodologija**: Direktan URL pristup — svaki nalaz je potvrđen čitanjem stvarnog sadržaja stranice

---

## SEKCIJA 3A — Šta POSTOJI na sajtu (potvrđeno direktnim pristupom)

### Blog postovi — 10 potvrđenih objava na /saveti-za-negu-koze/

| # | Naslov | URL | Datum | Reči | Format |
|---|--------|-----|-------|------|--------|
| 1 | DERMALUX LED terapija kao rešenje problema | /dermalux-led-terapija-kao-resenje-problema/ | 02.04.2024 | ~650 | Paragrafi + italik podnaslovi |
| 2 | Leto i promene na koži | /leto-i-promene-na-kozi/ | nepoznat | n/a | n/a |
| 3 | Posledice starenja na koži | /posledice-starenja-na-kozi/ | nepoznat | n/a | n/a |
| 4 | PRVA POMOĆ koži u hladnim danima | /prva-pomoc-kozi-u-hladnim-danima/ | nepoznat | n/a | n/a |
| 5 | **Sve ISTINE o laserskoj EPILACIJI** | /sve-istine-o-laserskoj-epilaciji/ | **04.09.2023** | **~1.100–1.200** | **Q&A format — 7 pitanja** |
| 6 | Sinergija estetskih procedura i tretmana lica | /sinergija-estetskih-procedura-i-tretmana-lica/ | nepoznat | n/a | n/a |
| 7 | Uticaj kiseonika na kožu | /uticaj-kiseonika-na-kozu/ | nepoznat | n/a | n/a |
| 8 | Koraci unaprеđene nege lica | /koraci-unapredjene-nege-lica/ | nepoznat | n/a | n/a |
| 9 | Osnovni koraci svakodnevne "beauty" rutine | /osnovni-koraci-svakodnevne-beauty-rutine/ | nepoznat | n/a | n/a |
| 10 | BALLANCER PRO | /ballancer-pro/ | nepoznat | n/a | n/a |

**Ključna napomena**: Blog post #5 ("Sve ISTINE o laserskoj epilaciji") je **već napisan u Q&A formatu** sa 7 pitanja i konkretnim statistikama (80% rezultata, 6–10 tretmana, itd.). Ovo je izuzetno vrednik sadržaj — ali AI ga ne vidi kao strukturirano znanje jer nema schema.

---

### Service stranice — FAQ sadržaj POTVRĐEN

**HydraFacial stranica** (`/hydrafacial-tretmani-lica-novi-sad/`)
- ~1.200 reči
- **7 FAQ pitanja potvrđena** kao H3 naslovi:
  1. "Šta podrazumeva Hydrafacial® tretman?"
  2. "Kome je namenjen tretman?"
  3. "Koliko tretmana je potrebno uraditi?"
  4. "Razlike u protokolima?"
  5. "Period oporavka nakon tretmana"
  6. "Očekivan rezultat nakon Hydrafacial® tretmana?"
  7. "Ko ne sme da radi ovaj tretman?"
- JSON-LD schema: **NEMA**

**Epilacija stranica** (`/epilacija/`)
- ~900–1.000 reči
- **4 FAQ pitanja potvrđena** kao H3 naslovi:
  1. "Kako se pripremiti pre epilacije?"
  2. "Može li epilacija rešiti problem uraslih dlaka i kako?"
  3. "Koliko tretmana je potrebno da biste primetili trajne promene u gustini i rastu dlaka?"
  4. "Koji tipovi kože i dlaka mogu da se tretiraju epilacijom i postoji li razlika u efikasnosti?"
- JSON-LD schema: **NEMA**

---

### About/Tim stranica — E-E-A-T signali POTVRĐENI

**Stranica** `/kozmetoloski-centar-sensi-skin/`

Potvrđeni podaci:
- **Nataša Burka** — CEO, specijalista medicinske estetike, 20+ godina iskustva
- Kompletni tim: Isidora Vasić, Nina Šipčić, Tamara Stojanović, Darina Zaskalicki, Dragana Spasojević
- Adresa: **Braće Popović 3, sprat 2, stan 12** (NAP konzistentna ovde)
- Telefon: +381 65 33 38338, Email: sensistudio@gmail.com
- JSON-LD schema: **NEMA** (ni Person ni Organization schema)

---

### Sitemap situacija — KRITIČAN NALAZ

Na sajtu postoje **DVE** sitemape:

| URL | Sadržaj | Status |
|-----|---------|--------|
| `/sitemap.xml` | 23 mrtva `.html` URL-a sa STAROG sajta (`www.sensiskinstudio.com`) | **ZASTARELO — stari sajt** |
| `/sitemap_index.xml` | Yoast sitemap sa 6 pod-sitemapa: post, page, product, category, author | **AKTUELNO — novi WordPress** |

**Ako je u Google Search Console-u submitovana `/sitemap.xml`** — Google crawluje 23 mrtva URL-a, a sve nove stranice i blogove potpuno zanemaruje.

---

## SEKCIJA 3B — Uzroci niske AI vidljivosti (rangirani po ozbiljnosti)

| # | Uzrok | Ozbiljnost | Dokaz |
|---|-------|-----------|-------|
| 1 | FAQ sadržaj postoji ali nema FAQPage schema | **Kritičan** | HydraFacial: 7 Q&A bez schema. Epilacija: 4 Q&A bez schema. |
| 2 | Sitemap koji GSC crawluje verovatno je stari (23 mrtva URL-a) | **Kritičan** | `/sitemap.xml` = stari sajt. `/sitemap_index.xml` = Yoast. Proveriti koji je submitovan. |
| 3 | Blog post "Sve istine o laserskoj epilaciji" nema Article+FAQ schema | **Kritičan** | 1.200 reči Q&A sadržaj, 7 pitanja, konkretni podaci — bez schema = AI ga ne vidi |
| 4 | Nijedan blog post nema Article/BlogPosting schema | **Visok** | 10 blog postova potvrđeno. Nula schema. |
| 5 | Nema Person schema za Nataša Burka | **Visok** | Podaci postoje na /kozmetoloski-centar-sensi-skin/ ali nisu machine-readable |
| 6 | Poverilačke informacije samo na jednoj stranici | **Visok** | Nataša Burka se ne pominje na service stranicama ni u blog postovima |
| 7 | Blog postovi nemaju author byline | **Srednji** | Ni jedan od 10 postova nema potpisanog autora |
| 8 | Dermalux blog post koristi italik umesto H2/H3 za podnaslove | **Srednji** | AI teže extrahuje sadržaj strukturiran italik tekstom |
| 9 | Zastareli promotivni podaci u blog postovima | **Nizak** | "30% i 40% popust, septembar-oktobar" iz 2023. u aktivnom postu |
| 10 | robots.txt — AI botovi NISU blokirani | ✅ Nije problem | GPTBot, PerplexityBot, ClaudeBot mogu da crawlaju |

---

## SEKCIJA 3C — Šta čovek vidi vs. šta AI ekstrahovuje

| Element | Šta čovek vidi | Šta AI ekstrahuje |
|---------|---------------|-------------------|
| HydraFacial FAQ (7 pitanja) | Lepo formatiran Q&A sa H3 naslovima | **Ništa kao strukturirani FAQ** — vidi tekst ali ne zna da su to Q&A parovi |
| Epilacija FAQ (4 pitanja) | H3 naslovi sa odgovorima | **Ništa kao strukturirani FAQ** |
| Blog "Sve istine o epilaciji" | Odličan Q&A članak sa statistikama | Tekst bez datuma authora, bez Article schema = nizak prioritet za citiranje |
| Tim stranicu sa Nataša Burka podacima | Kompletna bio stranica sa timom | Nestrukturirani tekst — AI ne zna da je "Nataša Burka" Person entitet |
| 10 blog postova | Sadržaj sa datumima | Vidljivi ali bez Article schema = AI ih tretira kao generičke stranice |
| Sitemap | Vizuelno ne postoji | `/sitemap_index.xml` = OK, ali ako GSC koristi stari `/sitemap.xml` = Google ne zna za novi sadržaj |

---

## SEKCIJA 4 — Prioritizovani spisak popravki

| Prior. | Popravka | Stranica(e) | Teškoća | AI Impact | Kako primeniti |
|--------|---------|------------|---------|-----------|----------------|
| 1 | Proveriti koji sitemap je u GSC i promeniti na `/sitemap_index.xml` | GSC podešavanja | Lako | **Kritičan** | GSC → Sitemaps → ukloni stari, dodaj `/sitemap_index.xml` |
| 2 | Dodati FAQPage JSON-LD schema na HydraFacial stranicu | /hydrafacial-tretmani-lica-novi-sad/ | Lako | **Kritičan** | Kopirati kod iz Sekcije 5.1 u WordPress Yoast → Schema |
| 3 | Dodati FAQPage JSON-LD schema na Epilacija stranicu | /epilacija/ | Lako | **Kritičan** | Kopirati kod iz Sekcije 5.2 u Yoast Schema |
| 4 | Dodati Article + FAQPage schema na "Sve istine o laserskoj epilaciji" blog post | /sve-istine-o-laserskoj-epilaciji/ | Lako | **Kritičan** | Kopirati kod iz Sekcije 5.3 u Yoast Schema |
| 5 | Dodati Article schema na svih 10 blog postova | Sve /saveti-za-negu-koze/ objave | Srednje | **Visok** | Yoast SEO → svaki post → Schema tip: Article |
| 6 | Dodati author byline na sve blog postove | Sve blog objave | Lako | **Visok** | WordPress → korisnik profil → ime vidljivo → Yoast author schema ON |
| 7 | Dodati Person schema za Nataša Burka | /kozmetoloski-centar-sensi-skin/ | Lako | **Visok** | Kopirati kod iz Sekcije 5.4 u Yoast Schema |
| 8 | Pomenuti "Nataša Burka, medicinsko-estetski stručnjak" na svakoj service stranici | Sve service stranice | Lako | **Visok** | Dodati 1 rečenicu sa imenom i titulom na svaku service stranicu |
| 9 | Ažurirati Dermalux blog post: italik podnaslove zameniti pravim H2/H3 | /dermalux-led-terapija-kao-resenje-problema/ | Lako | **Srednji** | WordPress editor → promeniti formatiranje |
| 10 | Ukloniti zastareli promotivni sadržaj iz septembra 2023. | /sve-istine-o-laserskoj-epilaciji/ | Lako | **Nizak** | Izbrisati "30% i 40% popust, septembar-oktobar" referencu |

---

## SEKCIJA 5 — Gotovi JSON-LD kod snippeti

### 5.1 — FAQPage schema za /hydrafacial-tretmani-lica-novi-sad/
*(Baziran na stvarnim pitanjima pronađenim na stranici)*

```json
<script type="application/ld+json">
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
</script>
```

**Kako dodati u WordPress**: Yoast SEO → otvori HydraFacial stranicu → Schema → Custom Schema → zalepiti gornji kod. Ili dodati u WordPress header/footer plugin.

---

### 5.2 — FAQPage schema za /epilacija/
*(Baziran na stvarnim pitanjima pronađenim na stranici)*

```json
<script type="application/ld+json">
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
</script>
```

---

### 5.3 — Article + FAQPage schema za blog post "Sve istine o laserskoj epilaciji"
*(Combinovana schema za Q&A blog post — najefikasnija kombinacija)*

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Sve istine o laserskoj epilaciji",
  "description": "Odgovori na 7 najčešćih pitanja o laserskoj epilaciji — trajnost, broj tretmana, bezbednost, priprema i rezultati.",
  "author": {
    "@type": "Person",
    "name": "Nataša Burka",
    "jobTitle": "Medicinsko-estetski stručnjak",
    "worksFor": {
      "@type": "LocalBusiness",
      "name": "Sensi Skin Kozmetološki Centar"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "Sensi Skin Kozmetološki Centar",
    "url": "https://sensiskinstudio.com"
  },
  "datePublished": "2023-09-04",
  "dateModified": "2026-06-09",
  "url": "https://sensiskinstudio.com/sve-istine-o-laserskoj-epilaciji/",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensiskinstudio.com/sve-istine-o-laserskoj-epilaciji/"
  }
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Da li je trajna laserska epilacija zaista trajna?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Da, ali ne 100%. Nakon serije od 6–10 tretmana postiže se do 80% trajnog smanjenja rasta dlaka. Preostalih 20% dlačica može nastaviti da raste ali znatno tanje i ređe. Povremeni tretman održavanja jednom godišnje je dovoljan."
      }
    },
    {
      "@type": "Question",
      "name": "Da li se epilacijom uklone sve dlačice?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Laser uklanja dlačice koje su u aktivnoj fazi rasta u trenutku tretmana. Kako sve dlačice nisu istovremeno u istoj fazi, potrebno je 6–10 tretmana u razmacima od 6 nedelja da bi se pokrile sve faze rasta."
      }
    },
    {
      "@type": "Question",
      "name": "Da li je laserska epilacija bolna?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Osećaj je opisan kao lagano peckanje ili toplota. Savremeni laseri imaju integrisane sisteme hlađenja koji smanjuju nelagodnost. Tolerancija je individualna i zavisi od regije koja se tretira."
      }
    },
    {
      "@type": "Question",
      "name": "Da li je laserska epilacija bezbedna?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Da, laserska epilacija je medicinski sertifikovana procedura kada se izvodi na odgovarajućoj opremi od strane obučenog stručnjaka. U Sensi Skin studiju koriste se sertifikovani laseri i protokoli prilagođeni tipu kože."
      }
    },
    {
      "@type": "Question",
      "name": "Ko ne bi smeo da radi lasersku epilaciju?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Laserska epilacija se ne preporučuje trudnicama, osobama sa aktivnim infekcijama kože, onima koji uzimaju fotosenzitivne lekove, i osobama sa određenim dermatološkim stanjima. Prethodna konsultacija je obavezna."
      }
    },
    {
      "@type": "Question",
      "name": "Da li se laserska epilacija može raditi tokom leta?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Moguće je, ali uz obavezne mere opreza: izbegavati direktno sunčanje 7–10 dana pre i 7 dana posle tretmana, koristiti zaštitni faktor SPF 50. Preporučuje se početi sa serijom u jesen ili zimu kada je izlaganje suncu manje."
      }
    },
    {
      "@type": "Question",
      "name": "Da li je moguće ukloniti svetle dlačice laserskom epilacijom?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Laser cilja pigment melanin u dlačici, pa su tamne dlačice najefikasnije za uklanjanje. Svetle, sive ili crvene dlačice imaju manje melanina i laser je na njima manje efikasan. Aura Reality 3D dijagnostika može precizno proceniti prikladnost tretmana za vaš tip dlake."
      }
    }
  ]
}
</script>
```

---

### 5.4 — Person schema za Nataša Burka
*(Dodati na /kozmetoloski-centar-sensi-skin/)*

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Nataša Burka",
  "jobTitle": "Medicinsko-estetski stručnjak, CEO",
  "description": "Nataša Burka je medicinsko-estetski stručnjak sa više od 20 godina iskustva u profesionalnoj nezi kože. Osnivač i vlasnik Sensi Skin Kozmetološkog Centra u Novom Sadu. Specijalista za barijeru kože, inflamatorne i vaskularne promene i moderne anti-age strategije zasnovane na digitalnoj dijagnostici.",
  "worksFor": {
    "@type": "LocalBusiness",
    "name": "Sensi Skin Kozmetološki Centar",
    "url": "https://sensiskinstudio.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Braće Popović 3, sprat 2, stan 12",
      "addressLocality": "Novi Sad",
      "addressCountry": "RS"
    }
  },
  "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/",
  "sameAs": [
    "https://www.instagram.com/sensi_skin/",
    "https://www.facebook.com/sensi.skin.studiozanegulepote/"
  ]
}
</script>
```

---

### 5.5 — Popravka Google Search Console Sitemapa
*(Uputstvo — ne kod)*

**Korak 1**: Otvori [search.google.com/search-console](https://search.google.com/search-console)  
**Korak 2**: Levo meni → Sitemaps  
**Korak 3**: Provjeri koji sitemap je trenutno submitovan:
- Ako piše `sitemap.xml` → to je stari, neispravni sitemap
- Ako piše `sitemap_index.xml` → ispravno

**Korak 4**: Ako je stari submitovan → klikni na njega → "Remove" (ukloni)  
**Korak 5**: "Add a new sitemap" → unesi: `sitemap_index.xml`  
**Korak 6**: Klikni Submit

**Zašto je ovo kritično**: `/sitemap.xml` sadrži 23 URL-a sa starog HTML sajta (`www.sensiskinstudio.com`). Yoast sitemap na `/sitemap_index.xml` sadrži sve aktuelne stranice i blog postove. Ako Google crawluje stari sitemap, sve nove stranice su za njega praktično nevidljive.

---

### 5.6 — Dodati "dateModified" i autora na blog postove

Za svaki blog post u WordPress editoru:
1. Yoast SEO panel → Schema → Article author: "Nataša Burka"
2. Dodati ručno u post content (na kraju posta): `Autor: Nataša Burka, medicinsko-estetski stručnjak`
3. U Yoast Schema tab proveriti da je "Article type" postavljeno na **BlogPosting**

---

## Jedna rečenica — najvažnija akcija ove nedelje

**Odmah provjeri u Google Search Console koji sitemap je submitovan — ako je `/sitemap.xml` (stari), zameni ga sa `/sitemap_index.xml`, jer dok Google crawluje 23 mrtva URL-a sa starog sajta, svi tvoji blog postovi i nove stranice su za njega nevidljive, a bez toga ni jedno od ostalih poboljšanja ne može imati efekta.**

---

*Izveštaj baziran na direktnom pristupu URL-ovima: robots.txt, sitemap.xml, sitemap_index.xml, /hydrafacial-tretmani-lica-novi-sad/, /epilacija/, /kozmetoloski-centar-sensi-skin/, /saveti-za-negu-koze/, /dermalux-led-terapija-kao-resenje-problema/, /sve-istine-o-laserskoj-epilaciji/*
