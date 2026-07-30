# Casa Montana — Sveža revizija sajta (2026-07-28)

Sajt: **https://casamontana.rs** (LIVE, HTTP 200, HTTPS ok, GitHub Pages)
Repo: github.com/ognjenzekovic/casa-montana (React 19 + Vite + TS)
Pregledano: živi sajt + kompletan kod na `main` (HEAD 0ac0eba, 8 novih commit-ova od revizije 2026-07-19)
Kontekst: cilj = izdavanje + brend (prodaja nusprodukt uz proviziju agencije); OTA vodi druga agencija; klik ka OTA = naša konverziona metrika; **ništa se ne menja u repou bez Markovog odobrenja**.

---

## 0. Šta je developer REŠIO od prošle revizije (kredit)
- **DNS/domen** — `casamontana.rs` je živ (bio najveći blocker).
- **Galerija popunjena** — sve prostorije + **sauna** i **terase** (praznine koje smo flagovali), sa **dnevnim i noćnim** verzijama (npr. sauna 5/2, terase 8/2, eksterijer 13/4).
- **Specs popunjeni** — `[XXX]` zamenjeni: **200 m² stambeno, 700 m² placa**.
- **Lokalizacija SR/EN** (jezički prekidač).
- **Drugo „prodaja" dugme** + Instagram link + mobilni navbar/galerija + blog skelet.

Ostaje NAŠ posao: ceo SEO/GEO sloj + par sadržajnih/tehničkih doterivanja.

---

## 1. KRITIČNO (P0) — bez ovoga SEO/GEO ne postoji

### 1.1 SPA bez prerender-a → nevidljiv AI/GEO crawlerima
`<div id="root"></div>` je prazan; sav sadržaj ubacuje JS. GPTBot/PerplexityBot/ClaudeBot i deo Google-a ne izvršavaju JS → vide praznu stranicu. Za sajt kome je GEO cilj, ovo je **najveći tehnički problem**. → prerender (vite-react-ssg / react-snap / SSG) da HTML sadrži tekst pre JS-a.

### 1.2 Nema analitike
Nema GA4 ni bilo kakvog trackinga. Naša metrika — **klik ka Booking/Airbnb** — je **nemerljiva**. → GA4 + outbound-click event na OTA dugmad.

### 1.3 Blog = hash-rute (#/blog) + MOCK sadržaj → nula SEO vrednosti
Blog radi na `#/blog` fragmentima (developer i sam u komentaru priznaje SEO tradeoff) — fragmenti se **ne indeksiraju kao zasebne stranice**. Uz to, sadržaj je eksplicitno **placeholder** (`[MOCK]`, 3 lažna posta), a blog kartice **ne vode nikuda** (posts nemaju svoje stranice). Za content/SEO strategiju blog trenutno **ne vredi ništa**: treba (a) prave rute (path-based + prerender), (b) pravi sadržaj, (c) pojedinačne stranice po postu.

### 1.4 Nema robots.txt ni sitemap.xml (oba 404)
### 1.5 Nema JSON-LD scheme (0)
→ `LodgingBusiness`/`VacationRental` + `geo` + `amenityFeature` (sauna, terase, kamin, WiFi, parking) + `aggregateRating` (kad se verifikuje). Najveći GEO dobitak.
### 1.6 og:image je relativna putanja (`./assets/hero.jpeg`) → pokvaren social preview
OG traži **apsolutni** URL. Direktno šteti deljivosti (cilj: da što više ljudi vidi).

---

## 2. SEO on-page (P1)

- **Title/meta i dalje samo prodaja** — „Kuća na Kopaoniku na prodaju" / „for Sale", bez rental/lokalnih ključnih reči. Ljudi daleko više traže „smeštaj/brvnara/vikendica Kopaonik" nego „kuća na prodaju". → title koji hvata i rental i brend + lokalne reči (npr. „Casa Montana — luksuzna brvnara sa saunom na Kopaoniku").
- **Dvojezičnost bez hreflang / bez zasebnih URL-ova** — SR i EN dele **isti URL** (prekidač je localStorage/JS). Google može da indeksira samo jednu verziju → **engleska verzija je nevidljiva pretrazi**. → zasebni URL-ovi po jeziku (`/en/`) + `hreflang` (ide zajedno sa prerender-om).
- **Nema canonical** taga.
- **Slike bez bogatih alt-ova** — galerija koristi generičke alt-ove; propušten keyword/pristupačnost.

---

## 3. Sadržaj / kredibilitet / doterivanje (P2)

- **Copy je već dobar i „human"** (poetičan brend-glas: „Kuća građena za jedan život, ne za jedan izdatak"). Sitno: ta linija (i EN „not a line item") **suptilno omalovažava izdavanje** — a izdavanje je realan prihod; ublažiti.
- **Ocena nekonzistentna** — `Trust` prikazuje **5.0** (ocena) / 14 utisaka / 13 godina, a `Book` kaže **9.8/10**. Verovatno Airbnb (5.0) vs Booking (9.8) — ali bez naznake izvora deluje kontradiktorno. → označiti izvor svake ocene.
- **Video walkthrough** (isporučen 2026-07-17) i dalje **nije ugrađen** na sajt — gotov diferencijator koji stoji neiskorišćen.
- **Kontakt** je `mailto:` (Closer) — treba adresa koja realno prima poštu ili forma.
- **Interno povezivanje** tanko — kad blog dobije pravi sadržaj, povezati početna ↔ blog ↔ OTA (i kartice bloga da vode na pojedinačne postove).

---

## 4. Ko šta radi (mi smo kolaboratori, repo je klijentov)

**Možemo mi kroz PR (uz Markovo odobrenje), manji rizik:**
- robots.txt + sitemap.xml
- JSON-LD schema (LodgingBusiness + geo + amenities + rating)
- og:image apsolutni URL + canonical + title/meta prerada (rental+lokalne reči)
- GA4 + outbound-click tracking
- bogati alt tekstovi galerije
- ubacivanje video walkthrough-a
- copy doterivanje (ublažiti anti-rental liniju, označiti izvore ocena)

**Veći zahvat (arhitektura) — traži plan + verovatno koordinaciju sa developerom:**
- **Prerender** (vite-react-ssg/react-snap) — otključava GEO vidljivost, indeksabilan blog i hreflang odjednom
- **Blog: prave rute + pojedinačne stranice + pravi sadržaj** (mi pišemo content; developer/mi menjamo routing)
- **hreflang + /en/ URL-ovi**

---

## 5. Prioritet za dalje (predlog redosleda)

**Talas 1 (brzo, mi kroz PR, veliki efekat):** GA4+click tracking → og:image+canonical+title/meta → JSON-LD schema → robots.txt+sitemap. (Merenje + osnovna vidljivost + social + AI citati.)
**Talas 2 (arhitektura):** prerender → time se otključavaju indeksabilan blog + hreflang. Uz to blog-routing.
**Talas 3 (sadržaj):** pravi blog postovi (SR/EN) po GEO/lokalnim temama („smeštaj Kopaonik", „šta raditi na Kopaoniku", „brvnara sa saunom"), video embed, doterivanje ocena/kontakta.

*Napomena: ovo je materijal za Markovu odluku, ne lista sprovedenih izmena. Ništa nije menjano u repou.*
