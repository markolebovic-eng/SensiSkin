# Casa Montana — Revizija sajta (SEO/GEO/konverzija/sadržaj)

Datum: 2026-07-19
Sajt: http://ognjenzekovic.github.io/casa-montana/
Repo: github.com/ognjenzekovic/casa-montana (React 19 + Vite + TS, GitHub Pages)
Pregledano: živi sajt (HTTP 200) + kompletan kod na `main` (HEAD 3286936)

Kontekst projekta (iz product-marketing.md / MEMORY.md), presudan za ovu reviziju:
- **Cilj: izdavanje + podizanje brenda 99%, prodaja nusprodukt 1%.**
- OTA oglase (Booking/Airbnb) vodi **druga agencija** — van našeg obima.
- Sajt **ne podržava direktnu rezervaciju** — funneluje ka OTA; **klik ka OTA je naša konverziona metrika.**
- Cena se **nikad ne objavljuje.**
- Postoji gotov **video walkthrough** (isporučen 2026-07-17) i **66 fotografija**.
- Pozicioniranje: "chalet u Alpima, ali na Kopaoniku."

---

## ODLUKE (Marko, 2026-07-19) — OVO JE TRENUTNO FINALNI PLAN i ima prednost nad nalazima ispod

Ovaj dokument je od 2026-07-19 usvojen kao **trenutno finalni plan** za rad na sajtu Casa Montane. Sledeće odluke koriguju pojedine nalaze ispod:

1. **Balans prodaja/izdavanje — NE preokretati agresivno na izdavanje.** Bitna korekcija ranije pretpostavke: **prodaja je finansijski bitna AGENCIJI** (dobijamo procenat kad se kuća proda preko nas), a izdavanje je plus za klijenta (isto dobro). **Trenutni dvojni balans na sajtu je prihvatljiv i ostaje.** Planira se dodavanje **još jednog dugmeta koje vodi na "prodaju"**. Znači: cilj NIJE rental-only sajt; zadržavamo i prodajni i rental put. (Ovo koriguje nalaz 1.3 i P0 stavku 3 — svedeno na: NE omalovažavati izdavanje u copy-ju + ubaciti pozicionu liniju, ali bez preokretanja celog tona.)
2. **Ovlašćenje za izmene: NIŠTA se ne menja na sajtu/repou bez Markovog eksplicitnog odobrenja.** Za SVAKU izmenu prvo pitati Marka; tek po odobrenju izvršiti (npr. kroz PR na `ognjenzekovic/casa-montana`).
3. **GA4: pravi se NOVI property** (ne postoji postojeći nalog za povezivanje).
4. **Podaci koji fale** (kvadratura, placa, ocene, email, IG, koordinate) — vlasnik/klijent će ih **pravovremeno dodeliti**; do tada ostaju otvoreni.
5. **Domen:** čeka se **redovan domen** (casamontana.rs); do tada sajt živi na github.io URL-u. Canonical/og:url/email finalizovati tek kad domen bude poznat.

Svaki agent koji radi na ovom klijentu/sajtu treba da pročita ove odluke + ceo izveštaj pre rada.

---

## 0. Top-line verdikt

Sajt je **vizuelno i inženjerski solidan** (čist dizajn, prava galerija po prostorijama sa lazy-loadingom, dobra tipografija, dodat `Book` sekcija sa OTA dugmadima, relativni asset path-ovi rade na github.io subpath-u). Ali za NAŠ posao ima dva ozbiljna problema:

1. **Strateška neusklađenost:** ceo sajt je napisan kao **prodajni** ("na prodaju", "pre kupovine", "posed", "zakažite obilazak"), a naš cilj je 99% **izdavanje/brend**. Sajt trenutno optimizuje za 1%.
2. **Tehnički je slab za SEO/GEO:** SPA bez prerender-a (sadržaj nevidljiv AI crawlerima), nema schema markup, nema robots.txt ni sitemap, naslov/meta prodajno orijentisani, nema analitike (ne merimo klik ka OTA). Za sajt čija je svrha "što više ljudi da vidi" — trenutno je najslabiji baš na tome.

Dobra vest: skoro sve je popravljivo na nivou koda, a mi smo kolaboratori na repou.

---

## 1. KRITIČNI nalazi (P0 — blokiraju cilj)

### 1.1 SPA bez prerender-a — sadržaj nevidljiv za AI/GEO
Build daje prazan `<div id="root">` (~1.4KB HTML), sav sadržaj ubacuje JavaScript. Google ume da renderuje JS, ali **AI crawleri (GPTBot, PerplexityBot, Google-Extended, ClaudeBot) često ne izvršavaju JS** — vide skoro prazну stranicu. Pošto je GEO/AEO eksplicitno interes klijenta, ovo je **najveći pojedinačni tehnički problem**: pozicioniranje, galerija, priča — ništa od toga ne postoji za ne-JS crawlere.
→ Rešenje: prerender jedne stranice u statički HTML (npr. `vite-plugin-prerender`, `react-snap`, ili prerendered build), ili minimalno SSR. Sadržaj mora da bude u HTML-u pre JS-a.

### 1.2 Nema analitike — ne merimo NIŠTA (ni klik ka OTA)
U `<head>` su samo fontovi. Nema GA4, nema event trackinga. Naša dogovorena konverziona metrika — **klik ka Booking/Airbnb** — trenutno je **nemerljiva**. Bez ovoga letimo naslepo i ne možemo da dokažemo efekat marketinga.
→ Rešenje: GA4 + outbound click event na sva OTA dugmad (`Book` i `Nav`). Ovo je preduslov za sve ostalo.

### 1.3 Strateška neusklađenost: prodajni ton umesto izdavanje/brend
Konkretno u kodu:
- `<title>`: "Casa Montana — Kuća na Kopaoniku **na prodaju**"
- Hero badge: "**Na prodaju**"; lead "Jedna kuća, jedan posed"
- Intro: "Kuća građena za jedan život, ne **za jedan izdatak**" (direktno omalovažava izdavanje!)
- `Book`: "**Pre kupovine** / Prenoćite pre nego što odlučite [da kupite]"
- `Closer`: "Retko se ovakav **posed** pojavi... **Zakažite obilazak**"

**REVIDIRANO odlukom 2026-07-19 (vidi vrh dokumenta):** dvojni balans OSTAJE — prodaja je bitna agenciji (procenat), izdavanje je plus klijentu; planira se i dodatno "prodaja" dugme. Ne preokreće se ceo ton.
→ Preostali stvarni zadatak (svedeno): (a) ispraviti JEDNU liniju koja omalovažava izdavanje — Intro "ne za jedan izdatak" (i u dvojnom modelu ne želimo da vređamo rental upotrebu); (b) **ubaciti pozicionu liniju "chalet u Alpima, ali na Kopaoniku"** (trenutno je NEMA na sajtu). Ovo više NIJE P0 preokret tona.

---

## 2. SEO — tehnički nalazi

| Nalaz | Stanje | Preporuka |
|---|---|---|
| `<title>` | Prodajni, bez rental/lokalnih ključnih reči | "Casa Montana — luksuzna brvnara sa saunom na Kopaoniku \| izdavanje" tipa; ključne reči napred |
| Meta description | Prodajni fokus | Preusmeriti na boravak/izdavanje + pozicija |
| **Schema (JSON-LD)** | **0 — ne postoji** | `LodgingBusiness`/`VacationRental` + `geo` + `amenityFeature` (sauna, terase, parking, WiFi, kamin) + `aggregateRating` (kad se verifikuje). **Najveći GEO win.** |
| **robots.txt** | **404** | Dodati; eksplicitno dozvoliti AI botove (GPTBot, PerplexityBot, Google-Extended, ClaudeBot); linkovati sitemap |
| **sitemap.xml** | **404** | Dodati (makar jednu stranicu + sekcije); prijaviti u GSC |
| Canonical tag | Nema | Dodati `<link rel="canonical">` (bitno pri budućem prelasku na casamontana.rs da se izbegne duplikat) |
| `lang="sr"` | ✓ postoji | OK |
| Viewport | ✓ postoji | OK |
| **og:image** | `./assets/hero.jpeg` (relativna) | **OG zahteva APSOLUTNI URL** — social preview slika je trenutno pokvarena pri deljenju. Direktno šteti cilju "što više ljudi da vidi/deli". Staviti pun `https://...` URL |
| Favicon | `./favicon.svg` — radi (200 na subpath-u) | OK (Vite prepisuje na relativno u build-u) |
| GSC/sitemap prijava | — | Prijaviti sajt u Google Search Console čim se odluči finalni domen |

---

## 3. GEO / AEO nalazi

- Kombinacija **SPA bez prerender-a (1.1) + nema schema (2)** znači da je sajt trenutno **skoro nevidljiv za AI odgovore** ("koje luksuzne brvnare sa saunom ima na Kopaoniku"). Za klijenta koji hoće GEO, ovo je prioritet.
- Nema `llms.txt` (opciono, ali jeftin GEO signal).
- Pozicija i spoljna reputacija (J2Ski, "među vodećim chaletima") nisu ni u HTML-u ni u schema — a to su tačno činjenice koje AI voli da citira. Ubaciti ih u tekst + schema `description`.

---

## 4. Konverzija / funnel ka OTA

**Dobro:** `Book` sekcija sa jasnim Booking + Airbnb dugmadima (brendirane ikone), plus `Nav` "Rezervišite boravak" link ka `#book`. Ovo je tačno funnel-ka-OTA model koji smo dogovorili. ✓

**Problemi:**
- **Nema merenja klika** (vidi 1.2) — ne znamo da li iko klikne.
- `Book` framing je prodajni ("Pre kupovine") — treba rental-first ("Rezervišite boravak", "Proverite dostupnost").
- **Ocena nekonzistentna:** `Trust` prikazuje "**5.0** prosečna ocena / 14 utisaka", a `Book` kaže "**9.8/10**". Verovatno Airbnb (5.0) vs Booking (9.8) — ali bez naznake izvora deluje kontradiktorno i podriva poverenje. Označiti izvor svake ocene.
- `Closer` CTA je `mailto:info@casamontana.rs` — **taj domen ne radi (DNS se ne razrešava)**, pa mejl verovatno ne stiže nigde. Za 1% prodaje OK, ali mora da bude adresa koja realno prima poštu.

---

## 5. Sadržaj / brand voice / kredibilitet

- **Pozicione linije "chalet u Alpima, ali na Kopaoniku" NEMA nigde na sajtu** — a to je naša glavna, odobrena formulacija (koristi se u GBP opisu). Ubaciti.
- **`Specs` ima žive `[XXX] m²` placeholdere** za stambeni prostor i placa — **to je trenutno vidljivo na živom sajtu**. Neprofesionalno; popuniti pravim brojkama ili privremeno sakriti te dve stavke.
- **`Trust` statistike (5.0 / 14 / 13 godina) su neverifikovane** (flag iz ranije revizije) — proveriti spram stvarnih Booking/Airbnb podataka pre nego što ostanu.
- **Galerija — praznina baš na diferencijatorima:** kategorija **"terase" nema nijednu sliku** (prikazuje placeholder), a **saune nema kao kategoriju uopšte** — a sauna + terase na oba sprata su nam TOP diferencijatori. Trenutno: eksterijer 7, dnevni boravak 6, kupatila 3, spavaće 3, kuhinja 2, terase 0, sauna 0. Dodati terase i saunu (imamo 66 fotki na raspolaganju).
- **Instagram link u `Footer` vodi na `https://instagram.com`** (generički, mrtav) — pravi profil ili ukloniti.
- Google Maps koordinate (43.2801, 20.8123) — **proveriti da su tačna lokacija kuće**, ne placeholder.

---

## 6. Prilike vezane za NAŠE usluge (lako, visok efekat)

1. **Ubaciti video walkthrough na sajt** — isporučen 2026-07-17, a nigde nije na sajtu. Diferencijator koji nijedan lokalni konkurent nema (Kežman/Rtanj/Villa Prive). Embed + kao pinned na social. Nizak trud, visok efekat.
2. **Galerija je već tu** — samo dopuniti terase + saunu iz postojećih 66 fotki.
3. **Schema + prerender** (P0 gore) su tačno SEO/GEO usluge koje mi pružamo — možemo ih izvršiti direktno u repou.
4. **3D/rotacija kuće** (tvoja ranija ideja) — ako se realizuje preko Luma/Polycam, sajt je spreman da to primi (React, lako se ugrađuje `model-viewer`/embed).
5. **GBP ↔ sajt usklađivanje** — GBP opis je odobren; sajt treba da nosi istu priču/činjenice (konzistentnost je i lokalni SEO signal).

---

## 7. Van našeg obima (samo evidentirati / eskalirati vlasniku)

- **Booking/Airbnb oglasi** — vodi druga agencija. Ako je ocena 9.8/10 i 5.0 realna, super; ali listing SEO (naslov, 20+ fotki, amenity tagovi) je njihov posao — eskalirati vlasniku kao pitanje.
- **DNS / domen `casamontana.rs`** — i dalje se ne razrešava; sajt živi na github.io URL-u. Vlasnik/registrar treba da reši ako se želi brendirani domen (utиče i na email i na canonical).
- **Dev code quality** (React arhitektura, scroll merge logika) — van marketinškog obima, izgleda uredno.

---

## 8. Prioritizovan akcioni plan

**P0 (preduslovi — bez ovoga ostalo nema smisla):**
1. GA4 (NOVI property) + outbound click tracking na OTA dugmad (merenje konverzije)
2. Prerender stranice u statički HTML (GEO vidljivost)
3. ~~Preokrenuti ton~~ → REVIDIRANO: zadržati dvojni balans + dodati "prodaja" dugme; ispraviti liniju koja omalovažava izdavanje + ubaciti pozicionu liniju (nije više preokret tona)
4. Ukloniti/popuniti `[XXX]` placeholdere (podaci: čeka se od vlasnika)

**P1 (SEO/GEO jezgro — mi izvršavamo u repou):**
5. JSON-LD schema (LodgingBusiness + geo + amenities + rating)
6. robots.txt + sitemap.xml + AI botovi dozvoljeni
7. Naslov/meta/description preraditi (rental + ključne reči)
8. og:image apsolutni URL; canonical tag
9. Ubaciti video walkthrough

**P2 (sadržaj/kredibilitet):**
10. Galerija: dodati terase + saunu
11. Uskladiti/označiti ocene (5.0 Airbnb / 9.8 Booking); verifikovati Trust brojke
12. Popraviti Instagram link; email koji realno radi; proveriti mapu koordinate

---

## 9. Otvorena pitanja / odluke za tebe (Marko)

1. **Ton:** koliko agresivno preokrećemo na izdavanje? Predlog: izdavanje kao glavni narativ, prodaja kao jedna diskretna linija/sekcija — potvrdi.
2. **Šta smemo da menjamo u klijentovom repou sami** (mi smo kolaboratori) vs šta ide preko vlasnika/developera? Predlog: tehnički SEO/GEO (schema, robots, meta, og, prerender, GA4, video embed) radimo mi kroz PR; sadržajne brojke (kvadratura, ocene, email, IG) traže vlasnikove podatke.
3. **GA4 nalog** — postoji li već, ili pravimo novi property?
4. **Realni podaci** koji nedostaju: kvadratura kuće + placa, tačna lokacija/koordinate, radni email, Instagram handle, potvrda ocena (5.0 / 9.8 / 14 / 13 god).
5. **Finalni domen** — ostajemo na github.io za sad ili se čeka casamontana.rs (utiče na canonical, og:url, email)?

---

*Napomena o metodu: ovo je revizija za tvoju odluku, ne lista već sprovedenih izmena. Ništa na sajtu/repou nije menjano ovom prilikom.*
