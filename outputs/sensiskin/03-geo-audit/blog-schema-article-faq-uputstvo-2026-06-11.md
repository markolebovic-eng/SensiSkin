# Blog schema — Article + FAQPage (gotov JSON + Yoast podešavanje)

**Datum:** 11. jun 2026. · **Za:** ~30 blog postova na sensiskinstudio.com
**Cilj:** dodati `Article` + `datePublished` + `author` na SVE postove, i `FAQPage` na one sa pitanjima.
**Stanje (crawl 11. jun):** 0/29 postova ima Article schema, 0/29 ima datum u schemi, 2/29 ima FAQPage.

---

## ⚡ NAJVAŽNIJE: Article se rešava JEDNIM podešavanjem (ne post po post)

Yoast automatski generiše `Article` schema za sve postove — sa tačnim `datePublished`, `dateModified`, `author` i `publisher` — **ako je uključen pravi tip**. Pošto crawl pokazuje 0/29, kod vas je verovatno isključen ili postavljen na „Web Page". Ovo je razlog #1 i popravlja svih 30 postova odjednom.

### Yoast podešavanje (preporučeno — uradi prvo ovo)

1. WordPress admin → **Yoast SEO → Search Appearance (Izgled u pretrazi)** → tab **Content Types (Tipovi sadržaja)**
2. Nađi sekciju **„Posts / Objave"** → otvori pod-tab **„Schema"**
3. Postavi:
   - **Page type / Tip stranice:** `Web Page`
   - **Article type / Tip članka:** `Article`  ← **OVO je ključno (verovatno je sad „None"/„Web Page")**
4. **Save changes.**

Time Yoast na SVAKI post automatski dodaje:
```
Article → headline, datePublished, dateModified, author (Person), publisher (Organization), image, mainEntityOfPage
```

### Da author (Nataša Burka) bude ispravan
1. **Users (Korisnici)** → otvori nalog koji je autor postova
2. Popuni **Biographical Info (Biografija)** (2–3 rečenice: „Nataša Burka, medicinsko-estetski stručnjak, 20+ godina…") i postavi avatar.
3. Idealno: svi blog postovi treba da imaju istog autora (Nataša Burka) radi konzistentnog E-E-A-T signala.

### Da publisher/logo bude ispravan
**Yoast → Search Appearance → General → Knowledge Graph & site name:** Organization, ime „Sensi Skin", postavljen logo. (Već imate MedicalOrganization na početnoj — samo proveriti da je logo tu.)

### Provera (posle podešavanja)
Otvori bilo koji post → **validator.schema.org** → mora da prikaže `Article` sa `datePublished` i `author`. Ako prikazuje → gotovo za svih 30.

---

## REZERVA: ručni Article JSON-LD (samo ako Yoast auto nije moguć)

Koristi **samo ako** ne možeš da uključiš Yoast Article tip (npr. zbog page-buildera). Lepi se preko WPCode/Custom Schema, **po jedan po postu**, menjajući 5 polja. NE koristi istovremeno sa Yoast auto (duplirao bi schema).

### Šablon (zameni `{...}` poljima konkretnog posta)
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{NASLOV POSTA}",
  "description": "{kratak opis posta, 1 rečenica}",
  "image": "{URL glavne slike posta}",
  "datePublished": "{YYYY-MM-DD}",
  "dateModified": "{YYYY-MM-DD}",
  "author": {
    "@type": "Person",
    "name": "Nataša Burka",
    "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Sensi Skin",
    "logo": {
      "@type": "ImageObject",
      "url": "https://sensiskinstudio.com/{putanja-do-logoa}.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{PUN URL POSTA}"
  }
}
```

### Popunjen primer — post „Vrste akni"
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vrste akni — kako da prepoznate i tretirate svaki tip",
  "description": "Pregled neupalnih i upalnih vrsta akni i pristup tretmanu za svaki tip kože.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/vrste-akni.jpg",
  "datePublished": "2025-03-12",
  "dateModified": "2026-06-11",
  "author": {
    "@type": "Person",
    "name": "Nataša Burka",
    "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Sensi Skin",
    "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/logo.png" }
  },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/vrste-akni/" }
}
```
> `datePublished` mora biti **stvarni datum objave posta** (vidi u WP listi objava). Zato je Yoast auto bolji — sam povlači tačan datum.

---

## FAQPage schema (po stranici)

FAQ ide samo na postove koji **odgovaraju na konkretna pitanja**. Dva načina:

### Način 1 (najlakši): Yoast FAQ blok (Gutenberg)
1. Otvori post u editoru → dodaj blok **„Yoast FAQ"**
2. Ukucaj pitanja i odgovore (vidljivo na strani)
3. Yoast **automatski** generiše `FAQPage` schema. Gotovo — bez koda.

### Način 2 (ručno): JSON-LD preko WPCode / Yoast Custom Schema
Ako koristite page-builder bez Gutenberg blokova, lepite JSON-LD ispod (isti princip kao za service strane).

---

### Gotovi FAQPage blokovi za ključne postove

Niže su **stvarna pitanja i tačni, umereni odgovori** (40–60 reči, bez preuveličavanja, u tonu brenda) za 8 najvrednijih postova. Za svaki: zameni `@id` URL-om posta ako se razlikuje.

#### 1) `/vrste-akni/`
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Koje vrste akni postoje?",
      "acceptedAnswer": { "@type": "Answer", "text": "Akne se dele na neupalne (komedoni — mitiseri i bele tačkice) i upalne (papule, pustule, noduli i ciste). Tip akni određuje koja nega i tretman odgovaraju vašoj koži." } },
    { "@type": "Question", "name": "Da li se sve vrste akni tretiraju isto?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ne. Blage, neupalne akne dobro reaguju na pravilnu kućnu negu i profesionalne tretmane čišćenja, dok upalne i cistične forme zahtevaju stručno vođen pristup, a ponekad i saradnju sa dermatologom." } },
    { "@type": "Question", "name": "Da li istiskivanje akni pomaže?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ne preporučuje se. Istiskivanje može da pogorša upalu i ostavi ožiljke i pigmentacije. Bolje je akne rešavati ciljanim tretmanima i odgovarajućom svakodnevnom negom." } }
  ]
}
```

#### 2) `/melazma/`
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Šta je melazma?",
      "acceptedAnswer": { "@type": "Answer", "text": "Melazma je oblik hiperpigmentacije koji se javlja kao tamnije mrlje, najčešće na licu. Povezuje se sa hormonskim promenama i izlaganjem suncu." } },
    { "@type": "Question", "name": "Da li melazma može trajno da se ukloni?",
      "acceptedAnswer": { "@type": "Answer", "text": "Melazma je sklona ponavljanju i traži strpljenje. Kombinacija dosledne zaštite od sunca, odgovarajuće nege i profesionalnih tretmana može značajno da je ublaži i drži pod kontrolom." } },
    { "@type": "Question", "name": "Koliko je važna zaštita od sunca kod melazme?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ključna je. Bez svakodnevne SPF zaštite melazma se brzo vraća, bez obzira na primenjene tretmane." } }
  ]
}
```

#### 3) `/rozacea-kako-da-ublazite-simptome/`
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Šta je rozacea?",
      "acceptedAnswer": { "@type": "Answer", "text": "Rozacea je hronično stanje kože koje se ispoljava crvenilom, proširenim kapilarima i ponekad papulama, najčešće na centralnom delu lica." } },
    { "@type": "Question", "name": "Šta pogoršava rozaceu?",
      "acceptedAnswer": { "@type": "Answer", "text": "Česti okidači su sunce, nagle promene temperature, ljuta hrana, alkohol, stres i agresivna kozmetika. Prepoznavanje ličnih okidača je važan deo kontrole stanja." } },
    { "@type": "Question", "name": "Kako se ublažava rozacea?",
      "acceptedAnswer": { "@type": "Answer", "text": "Blagom, umirujućom negom, doslednom zaštitom od sunca i ciljanim profesionalnim tretmanima koji smiruju crvenilo. Za izraženije forme savetuje se i konsultacija sa dermatologom." } }
  ]
}
```

#### 4) `/da-li-je-serum-zaista-potreban/`
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Da li mi je serum zaista potreban?",
      "acceptedAnswer": { "@type": "Answer", "text": "Serum nije obavezan, ali je koristan: sadrži veću koncentraciju aktivnih sastojaka od krema i cilja konkretne potrebe kože — hidrataciju, pigmentaciju ili znake starenja." } },
    { "@type": "Question", "name": "Kada se nanosi serum?",
      "acceptedAnswer": { "@type": "Answer", "text": "Posle čišćenja, a pre kreme. Ujutru se često bira serum sa antioksidansima, a uveče onaj sa regenerativnim sastojcima." } }
  ]
}
```

#### 5) `/da-li-vas-plase-hemijski-pilinzi/`
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Da li su hemijski pilinzi bezbedni?",
      "acceptedAnswer": { "@type": "Answer", "text": "Kada ih radi obučen stručnjak i prilagodi tipu i stanju kože, hemijski pilinzi su bezbedan i efikasan tretman. Ključ su pravilan izbor jačine i nega posle tretmana." } },
    { "@type": "Question", "name": "Da li se koža obavezno ljušti posle pilinga?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ne nužno. Vidljivo ljuštenje zavisi od vrste i jačine pilinga; mnogi blagi pilinzi obnavljaju kožu bez izraženog perutanja." } }
  ]
}
```

#### 6) `/stetnost-solarijuma/`
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Da li je solarijum štetan za kožu?",
      "acceptedAnswer": { "@type": "Answer", "text": "Da. UV zračenje iz solarijuma ubrzava starenje kože, izaziva pigmentacije i povećava rizik od oštećenja kože. Za ten bez rizika bolji su samopotamneli preparati." } },
    { "@type": "Question", "name": "Da li solarijum „priprema" kožu za sunce?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ne na bezbedan način. Tamnija boja iz solarijuma ne pruža pravu zaštitu, a dodatno UV opterećenje koži šteti. Zaštita od sunca (SPF) je prava priprema." } }
  ]
}
```

#### 7) `/predeo-oko-ociju-kako-negovati-ovu-osetljvu-regiju/`
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Zašto koža oko očiju zahteva posebnu negu?",
      "acceptedAnswer": { "@type": "Answer", "text": "Koža oko očiju je najtanja i najosetljivija na licu, sa manje lojnih žlezda, pa je sklonija suvoći, finim linijama i otocima." } },
    { "@type": "Question", "name": "Kada početi sa kremom za predeo oko očiju?",
      "acceptedAnswer": { "@type": "Answer", "text": "Preventivno već u dvadesetim, posebno ako postoji suvoća ili rane fine linije. Bira se nežna formula prilagođena potrebama te regije." } }
  ]
}
```

#### 8) `/menopauza-i-pravilna-nega-koze/`
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Kako se koža menja u menopauzi?",
      "acceptedAnswer": { "@type": "Answer", "text": "Pad estrogena dovodi do gubitka kolagena, suvoće, tanjenja kože i gubitka čvrstine. Promene su postepene, ali vremenom vidljive." } },
    { "@type": "Question", "name": "Kako negovati kožu u menopauzi?",
      "acceptedAnswer": { "@type": "Answer", "text": "Naglasak je na hidrataciji, obnovi barijere i stimulaciji kolagena — kombinacijom odgovarajuće kućne nege i profesionalnih tretmana, uz obaveznu zaštitu od sunca." } }
  ]
}
```

### FAQPage šablon (za ostale postove)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "{PITANJE 1 — kako ga ljudi stvarno pišu}",
      "acceptedAnswer": { "@type": "Answer", "text": "{Odgovor 40–60 reči, jasan i tačan, bez preuveličavanja.}" } },
    { "@type": "Question", "name": "{PITANJE 2}",
      "acceptedAnswer": { "@type": "Answer", "text": "{Odgovor.}" } }
  ]
}
```
> **Pravilo:** tekst odgovora u schemi mora da postoji i kao **vidljiv tekst** na strani (Google ne dozvoljava „skriveni" FAQ). Ako koristiš Yoast FAQ blok — to je automatski ispunjeno.

---

## Redosled rada (preporuka)

1. **Yoast Article tip = „Article"** (1 podešavanje → svih 30 postova dobije Article + datum + autor). ✅ najveći efekat
2. Popuni **autor bio** (Nataša Burka) + proveri **logo** u Knowledge Graph.
3. Dodaj **FAQ** (Yoast FAQ blok ili JSON gore) na 8 postova iznad → pa postepeno na ostale koji imaju pitanja.
4. **Validacija:** svaki post kroz **validator.schema.org** → mora `Article` (+ `FAQPage` gde si dodala).
5. U **GSC → URL Inspection → Request indexing** za izmenjene postove.

## Koji postovi NE moraju FAQ
Postovi koji su priča/saveti bez jasnih pitanja (npr. „Jesenji režim nege", „Šta ćete spakovati u beauty kofer") — njima je dovoljan **Article + datum**. FAQ dodaj samo gde prirodno postoje pitanja i odgovori.

---

*Pripremio: AI Marketing Agency — SEO/GEO · 11. jun 2026.*
*Povezano: geo-audit-izvestaj-2026-06-11.md (nalaz 0/29 Article), json-ld-schema-kompletno-2026-06-10.md (schema za service strane).*
