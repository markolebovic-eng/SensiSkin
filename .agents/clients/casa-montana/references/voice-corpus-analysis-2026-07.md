# Casa Montana — Voice Corpus Analysis (2026-07-31)

Dokazna baza iza `brand-voice-script.md`. Ovaj fajl je za proveru/reviziju
tvrdnji, ne za pisanje — pisac koristi glavni dokument.

## Metodologija

3-slojni korpus: Sloj A (globalni chalet/cabin lideri, cilj glasa), Sloj B
(regionalni južnoslovenski most, jezička adaptacija), Sloj C (srpsko tržište,
baseline klišea). Faza 1 (definicija korpusa preko WebSearch, 0 kredita) →
vlasnik potvrdio punu listu → Faza 2 (skrejp preko firecrawl) → Faza 3
(analiza po 9 dimenzija + niša-specifični nalazi a-f).

Izvršilac: `research` agent (Firecrawl CLI arhitektura). Glavna sesija (Claude,
Opus) uradila sintezu u Fazama 4-6.

## Krediti

| Tačka | Stanje |
|---|---|
| Pre Faze 1 (WebSearch, definicija korpusa) | 991/1000 |
| Posle Faze 1 | 991/1000 (nepromenjeno — čist WebSearch) |
| Pre Faze 2 (skrejp) | 991/1000 |
| Posle Faze 2 | 927/1000 |
| **Stvarna potrošnja** | **64 kredita** (procena je bila 55-75 — unutar raspona) |

Napomena: ~14-18 kredita otišlo na `firecrawl map` (istraživanje strukture
sajta pre skrejpa) — u Fazi 1 je ovo pogrešno pretpostavljeno kao besplatno.
Za buduće pokretanje ovog procesa: budžetirati mapiranje kao trošak, ne kao
nulti korak.

## Korpus — finalna lista (posle provere živosti, pre skrejpa)

**Izbačeno pre trošenja kredita** (curl/DNS provera, ~0 kredita):
- Jahorina Luxury Chalets — DNS se razrešava na 127.0.0.1 (mrtav, potvrđeno i
  preko javnog Google DNS-a, nije sandbox artefakt)
- Vila Babin Zub — NXDOMAIN, nema A zapisa
- Postcard Cabins (i journal.postcardcabins.com) — 301 trajno preusmerenje na
  `marriott.com/brands/outdoor-collection/postcard-cabins.mi`. Nezavisan
  urednički sajt više ne postoji — apsorbovan u Marriott Bonvoy brend.

**Živ, ali bez upotrebljivog sadržaja:**
- MonsAlbius (HR, Velebit) — HTTP 200, ali sadržaj = "COMING SOON" placeholder
- Linden Tree Retreat & Ranch (HR) — sadržaj minimalan (samo citati o prirodi,
  JS-render, mapa sajta nije otkrila podstranice)

### Sloj A — Globalni lideri (skrejpovano)

| Brend | URL | Stranice skrejpovane |
|---|---|---|
| Firefly Collection | firefly-collection.com | homepage, opis šalea (Courchevel 1850), About Us, blog post |
| Consensio | consensiochalets.co.uk | homepage, opis šalea (Hameau Alpin), About Us, blog indeks |
| Oxford Ski Company | oxfordski.com | homepage, opis šalea (Chalet Couttet), About Us, blog post |
| Bramble Ski | brambleski.com | homepage, About (opis šalea 404 — URL iz mape zastareo) |
| Unique Homestays | uniquehomestays.com | homepage, opis kuće (Pepper Shack), About Us, Travellers' Tales post |
| Boutique Retreats | boutique-retreats.co.uk | homepage, opis kuće (Nahla 532), blog (About stranica nije nađena u mapi) |
| Juvet Landscape Hotel | juvet.com/en | homepage, opis sobe (Skrivarstova, posle korekcije URL-a), About (Oppdag Juvet), opis restorana (Fjøsen, posle korekcije URL-a) |
| Manshausen | manshausen.no | homepage (na norveškom), Our Cabins & Houses, The History, The Hosts |

### Sloj B — Regionalni most (delimično uspelo — videti ograničenja)

| Brend | URL | Stranice | Napomena |
|---|---|---|---|
| Vila Planinka | vilaplaninka.com/en/ | homepage, Rooms, Our Philosophy | **Skrejpovano na ENGLESKOM (/en/), ne slovenačkom** — Faza 1 je zadala tu putanju, propust otkriven tek u Fazi 3 |

### Sloj C — Srpski baseline (skrejpovano)

| Brend | URL | Stranice | Napomena |
|---|---|---|---|
| Rtanj Kopaonik Eco Resort | rtanj.rs | homepage, akcije/brvnara | — |
| Garden Hill Tara | gardenhilltara.rs | homepage, opis vile (Vila A1) | Najrazvijeniji prozni uzorak na domaćem tržištu u ovom korpusu |
| Konaci Kopaonik | kopaonikkonaci.rs | homepage, apartman (Maglić Premium) | **Javno izložen Joomla debug bar** ($_SESSION/$_COOKIE vidljivi) — bezbednosna napomena za vlasnika Casa Montane (šta izbeći na sopstvenom sajtu), ne copy-nalaz |
| Green House Divčibare | greenhousedivcibare.com | homepage, "Green Story" blog post | Blog post = primer TOTALNOG odsustva uredničke discipline (nasumičan tok svesti o boji zelenoj, pogrešno pripisan citat MLK-u) — drugi tip greške od klišea, vredi zapamtiti kao anti-primer |
| Zlatiborski Mir | zlatibor.rs (agregator) | jedina dostupna stranica | — |

Neuspeli pokušaji (kredit potrošen, stranica nije postojala): Bramble Ski
"the-lodge" (404), Juvet "writers-lodge" i "barn" (stari URL-ovi, ispravljeni
na drugi pokušaj).

**Ukupno: 43 uspešne jedinstvene stranice sa upotrebljivim sadržajem** (od toga
2 vrlo tanke — Linden Tree, MonsAlbius — i 2 degradirane debug-barom — Konaci).

## Nalazi po dimenzijama — ilustrativni citati

Svaki citat ispod je **ILUSTRACIJA OBRASCA**, ne materijal za kopiranje.

**Adresiranje:**
- Sloj A (Boutique Retreats): *"Let us know your requirements"*, *"Speak to
  our experts and let us plan a true experience tailored around you"*
- Sloj C (Garden Hill): *"Vila A1 nije prostor koji se opisuje – to je osećaj
  koji se prepoznaje"*, *"gosti mogu potpuno da se prepuste miru"* — gost kao
  gramatički objekat, ne subjekat, dosledno kroz uzorak.

**Otvaranja:**
- Boutique Retreats, 6/6 hero slajdova ista formula: *"Moments of quiet luxury
  await at our clifftop hideaway for two..."*, *"Escape to a spellbinding
  oceanside sanctuary for six..."*, *"Seek a captivating country escape for
  up to twelve..."*
- Garden Hill, identična formula 3x: *"Vila A1 nije prostor koji se opisuje..."*
  / *"Vila A2 nije samo mesto za dolazak..."* / *"Vila A3 nije samo
  destinacija..."*

**Ritam — Garden Hill (Sloj C), ugnježdene "koji" klauze:**
*"Prostor stvoren za one koji traže više od smeštaja: mir koji ne prolazi,
luksuz koji ne mora da se dokazuje i atmosferu koja briše granice između
boravka i bivanja"* — jedna rečenica, ~28 reči, tri ugnježdena "koji".

**Leksika — Garden Hill:** "svaki detalj"/"svaki trenutak" — 10+ ponavljanja
na samo dve skrejpovane stranice.

**Autoritet — Vila Planinka (Sloj B):** *"...said the hotel's new owner,
Marjan Batagelj"* — ime vlasnika, godina osnivanja (1938), sertifikati (Green
Key, Michelin 2026, SLH). Kontrast sa Sloj C: nula pominjanja vlasnika/porekla
u celom uzorku.

**Luksuz — centralni nalaz (Vila Planinka):**
*"Vila Planinka has redefined the meaning of luxury. It's not about
technological innovations and expensive materials, but about the wealth of
nature."* — eksplicitna redefinicija, najjača formulacija u celom korpusu za
Casa Montanino pozicioniranje.

**Luksuz — kontrast (Garden Hill):** "luksuz koji ne mora da se dokazuje",
"svaki trenutak... luksuza", uključujući štamparsku grešku "**luskuz**" koja
prolazi nezapaženo — znak koliko je reč devalvirana ponavljanjem.

**Formula jutro-popodne-veče (Garden Hill, 3x skoro identično):**
- A1: *"Jutra su spokojna i obojena tišinom, popodneva teku lagano, a večeri
  vraćaju osećaj ravnoteže"*
- A2: *"Jutra su spokojna, popodneva laka, a večeri pružaju osećaj harmonije"*
- A3: *"Jutra započinju spokojno, popodneva nude trenutke za odmor..., a
  večeri donose osećaj ravnoteže"*

**Cena/CTA — paralela zapad/domaće tržište:** Oxford Ski (Chalet Husky) i
Rtanj (luksuzna brvnara) oba kriju cenu za najekskluzivniji proizvod ("Price
on Request" / "Upit na broj...") dok je transparentna za standardne pakete —
ovo NIJE zapadni uvoz, postoji i lokalno kao legitimna taktika za vrh ponude.

## Katalog srpskih turističkih klišea (pun spisak)

Prebačeno u `.claude/skills/stop-slop/references/serbian-hospitality-phrases.md`
(klijent-agnostično, za ponovnu upotrebu kod budućih ugostiteljskih klijenata).

## Ograničenja ovog pokretanja — eksplicitno, ne zaobiđeno

1. **Sloj B nije ispunio svrhu.** Cilj sloja je bio "kako luksuzni ton zvuči na
   južnoslovenskom jeziku" — jezički most. Umesto toga: Vila Planinka je
   pročitana na ENGLESKOM (/en/ putanja, greška u Fazi 1 zadatku), Linden Tree
   i MonsAlbius su dali gotovo prazan sadržaj. **Nalazi o "luksuz kao
   redefinicija" (najjači nalaz celog istraživanja) dolaze sa Vila Planinke,
   ali na engleskom — ne dokazuju kako to zvuči na srodnom jeziku.** Ovo je
   rupa koju Faza 4 (srpska adaptacija) mora da premosti sopstvenim
   rezonovanjem, ne korpusom.
2. **Crna Gora — nula kandidata.** Nijedan premium objekat sa sopstvenim
   uredničkim sajtom nije pronađen (samo agregatorski listinzi). Ako je
   potreban crnogorski uzorak, treba posebna runda pretrage ili predlog
   vlasnika.
3. **Golija — nula kandidata** u Sloju C, iz istog razloga.
4. **Svi brojevi/procenti u analizi su kvalitativne procene sa malog uzorka**
   (43 stranice), ne strogo statistička merenja. Gde je bilo nesigurno, Faza 3
   izveštaj je to eksplicitno naznačio umesto da zaokruži.
5. **Jedan brend nosi najjači pojedinačni zaključak** (odnos prema "luksuzu" —
   Vila Planinka) — vredi ojačati drugim izvorom u budućem pokretanju pre nego
   što se ovaj nalaz tretira kao čvrsto utvrđen obrazac cele niše.

## Preporuka za sledeće pokretanje (ako se korpus obnavlja)

- Skrejpovati `vilaplaninka.com/sl/o-vili/filozofija/` (slovenačka verzija).
- Naći zamenu za Jahorina Luxury Chalets (mrtav domen) — regionalni BiH/CG
  brend sa sopstvenim sajtom, ako postoji.
- Periodično proveriti MonsAlbius (trenutno "coming soon").
- Budžetirati `firecrawl map` kao trošak u proceni kredita, ne kao besplatan
  korak.
