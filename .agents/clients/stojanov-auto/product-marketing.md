# Stojanov Auto — Product Marketing Context

> Popunjeno 2026-08-05 iz discovery skrejpa sajta + WP REST API.
> Oznaka **[POTVRDITI]** = pretpostavka izvedena iz sajta, treba je potvrditi sa klijentom.
> Oznaka **[NEDOSTAJE]** = podatak nije nigde javno dostupan, tražiti od klijenta.

## Jezik / Language
Sav sadržaj za korisnike mora biti na **srpskom jeziku, latinica**.
Sajt je `lang="sr-RS"` i koristi plugin „Serbian in Latin Script".
Izuzetak: stranica `/usluge/pomoc-na-putu/` ima i EN i DE verziju u istom telu stranice
(vidi audit — to je problem koji treba rešiti, ne obrazac koji treba ponavljati).

---

## Brend / Brand overview
**Stojanov Auto DOO** je ovlašćeni prodavac i serviser **Renault, Dacia i Nissan** vozila
u Novom Sadu — servisno-prodajni centar sa salonom, servisom i tehničkim pregledom na istoj lokaciji.

- **Sajt**: https://stojanovauto.rs (WordPress + Elementor Pro, Rank Math SEO)
- **Adresa**: Zrenjaninski put 12, 21000 Novi Sad
- **Geo**: 45.289371, 19.853069
- **Telefon (centrala)**: +381 21 21 00 488
- **Email**: office@stojanovauto.rs
- **Šlep služba 24h**: 021/548-285, 064/64 65 153, 063/512 073
- **Prodaja (direktni kontakti)**: Aleksandar +381 64 643 2547 · Zoran +381 64 643 2549 ·
  Valentina +381 64 643 2550 · Vladimir +381 64 646 5152 · Bogdan +381 64 643 2551
- **Radno vreme — salon**: pon–pet 08:00–18:00, sub 08:00–12:30
- **Radno vreme — servis**: pon–pet 08:00–16:00, sub 08:00–12:30
- **Kontakt osoba za marketing**: Vanja Borić +381 60 9553 009
- **Godine iskustva**: [NEDOSTAJE] — nigde na sajtu nije navedeno. Ovo je propuštena
  poluga poverenja; firma ima post „U sećanje na Branka Stojanova" (jan 2026), što ukazuje
  na porodičnu firmu sa istorijom. Tražiti godinu osnivanja.

**Pristupi / nalozi**
- WP admin: DA — `.env` ključevi `WP_SITE_URL_STOJANOVAUTO`, `WP_USERNAME_STOJANOVAUTO`,
  `WP_APP_PASSWORD_STOJANOVAUTO` (proveren 2026-08-05, REST vraća 200)
- GA4: postoji na sajtu (`G-SFXW7G5GZC`), ali **agencija nema pristup nalogu**
- GTM: `GTM-PCJ3KQ69`
- Universal Analytics: `UA-179394377-1` — **mrtav od jula 2023, i dalje se učitava**
- Meta Pixel: aktivan (`fbq`)
- Google Search Console: **agencija nema pristup**
- Napomena: klijent je (avgust 2026) rekao da za sada NE traži GSC/GA4 pristup

---

## Šta je Stojanov Auto — za koga, koji problem rešava

Stojanov Auto pokriva **ceo životni ciklus vozila na jednom mestu** za vlasnike Renault,
Dacia i Nissan vozila u Novom Sadu i Južnoj Bačkoj: kupovina (novo, polovno, komercijalno),
ovlašćeni servis sa originalnim delovima, tehnički pregled i registracija, čuvanje guma,
i šlep služba 24h.

Klijenti dolaze jer: 
- Ovlašćeni servis = garancija vozila ostaje validna, originalni delovi, fabrička dijagnostika
- Sve na jednoj lokaciji — kupovina, servis, tehnički, registracija (nema vožnje po gradu)
- Direktan kontakt sa imenovanim prodavcem, ne sa call centrom
- Šlep 24h kao sigurnosna mreža za postojeće klijente

**Misija**: [NEDOSTAJE — sajt nema formulisanu misiju osim generičkog „poštujući potrebe
i očekivanja korisnika naših proizvoda i usluga"]

---

## Usluge / Services

| Usluga | Opis | Pozicioniranje | Postojeća stranica |
|--------|------|----------------|--------------------|
| **Prodaja novih vozila** | Renault, Dacia, Nissan — ovlašćeni prodavac | Zvanični diler, fabrička garancija | `/prodaja/nova-vozila/`, `/renault/`, `/dacia/`, `/nissan/` |
| **Odmah dostupna vozila** | Zaliha na stanju, bez čekanja na porudžbinu | Brzina isporuke | `/odmah-dostupna-vozila/` |
| **Polovna vozila** | Polovni program | Provereni polovnjaci od ovlašćenog dilera | `/polovna-vozila/` + duplikat `/prodaja/polovna-vozila/` |
| **Komercijalna vozila** | Renault PRO+ program, dostavna/teretna | B2B, zanatlije i firme | `/prodaja/komercijalna-vozila/`, `/odmah-dostupna-komercijalna-vozila/` |
| **Ovlašćeni servis** | Redovno održavanje i popravke, fabrička dijagnostika, originalni delovi | Ovlašćeni za 3 brenda | `/servis/` |
| **Tehnički pregled i registracija** | Tehnički pregled + registracija vozila | Sve na jednom mestu | `/usluge/tehnicki-pregled/` |
| **Hotel za gume** | Čuvanje vansezonskih guma za redovne klijente | Retencija postojećih klijenata | `/usluge/hotel-za-gume/` |
| **Pomoć na putu / šlep 24h** | Šlep služba dostupna 24 sata | Hitna intervencija | `/usluge/pomoc-na-putu/` |

**Nedostaje na sajtu**: finansiranje / kredit / lizing nije nigde objašnjeno, iako
`polovna vozila na kredit novi sad` i `polovna vozila na lizing novi sad` postoje kao
Google autocomplete upiti za Novi Sad. **[POTVRDITI da li nude finansiranje]**

---

## Ciljana publika / Target audience
**[CEO ODELJAK POTVRDITI — POTVRDJENO]**

**Primarna publika — B2C, kupci vozila**
- Novi Sad + Južnobački okrug, 30–60 godina
- Kupuju u srednjem cenovnom rangu (Dacia = vrednost za novac, Renault = porodično, Nissan = crossover)
- Porodice koje menjaju auto na 5–8 godina
- Racionalni kupci — porede cenu, garanciju i troškove održavanja

**Primarna publika — servisni klijenti**
- Postojeći vlasnici Renault/Dacia/Nissan vozila u garanciji (moraju u ovlašćeni servis)
- Vlasnici van garancije koji biraju ovlašćeni servis zbog originalnih delova
- **Ovo je najvredniji segment za SEO** — ponavljajuća zarada, visoka marža, lokalna namera

**Sekundarna publika — B2B**
- Zanatlije, mala preduzeća, dostavne službe → Renault PRO+ komercijalni program
- Firme sa voznim parkom (održavanje flote) **[POTVRDITI da li rade fleet - POTVRDJENO]**

**Bolne tačke publike** (u njihovim rečima, izvedeno iz Google autocomplete za Novi Sad):
- „koliko košta tehnički pregled" — `tehnicki pregled novi sad cena`, `najjeftiniji tehnicki pregled novi sad`
- „kad rade" — `tehnicki pregled novi sad radno vreme`
- „gde je najbliži ovlašćeni servis" — `renault ovlasceni servis novi sad`
- „koliko košta šlep" — `slep sluzba novi sad cena`
- „mogu li na kredit" — `polovna vozila na kredit novi sad`

---

## Pozicioniranje / Positioning

**Pozicioniranje** (predlog, izveden iz sajta — **[POTVRDITI sa klijentom]**):
> Jedini servisno-prodajni centar u Novom Sadu gde Renault, Dacia i Nissan vozilo
> kupite, servisirate, registrujete i prezimite gume — na jednoj adresi, kod ljudi
> koje znate po imenu.

**Ključni differentiators**:
1. Ovlašćeni diler i serviser za **tri brenda** odjednom (Renault + Dacia + Nissan)
2. Kompletan ciklus na jednoj lokaciji — prodaja, servis, tehnički pregled, registracija, gume, šlep
3. Šlep služba 24h u sopstvenoj režiji
4. Porodična firma sa imenovanim kontakt osobama, ne bezlični salon

**Trenutni problem pozicioniranja**: ništa od gore navedenog nije napisano nigde na sajtu
kao poruka. Naslovna nema ni H1. Sajt je katalog, ne argument.

---

## Ton glasa / Tone of voice
**[POTVRDITI — predlog na osnovu postojećeg sadržaja]**

- **Ton**: Stručan, pouzdan, bez pompe. Ovo je kupovina od 15.000–40.000 EUR i servis
  od koga zavisi bezbednost — ton mora da nosi kompetenciju, ne uzbuđenje.
- **Stil**: Konkretno i brojčano. Cene, rokovi, radno vreme, šta je uključeno.
  Kratke rečenice. Direktno obraćanje („Zakažite", „Proverite").
- **Izbegavati**: marketinški prazan hod („vrhunski kvalitet", „zadovoljstvo klijenata",
  „tim stručnjaka"), uzvičnike, CAPS LOCK naslove (trenutno se koriste: „ODMAH DOSTUPNA VOZILA"),
  bukvalno prevedene fabričke slogane koji ne znače ništa na srpskom
  (npr. „Potražite elektrificirane supermoći kod Nissan vozila")
- **Koristiti**: imena ljudi i njihove brojeve, tačne cene i rokove, lokalne orijentire
  (Zrenjaninski put), reč „ovlašćeni" gde god je tačna — to je glavni argument

---

## Kanali / Key channels

| Kanal | Prioritet | Stanje | Upotreba |
|-------|-----------|--------|----------|
| **Organski / lokalni SEO** | **Visok** | Slabo iskorišćen | Glavni kanal — servis, tehnički, šlep imaju jaku lokalnu nameru |
| **Google Business Profile** | **Visok** | [NEDOSTAJE — nije verifikovano] | Local pack za „tehnicki pregled novi sad", „renault servis novi sad" |
| **Sajt / blog** | Srednji | 136 objava, uglavnom fabričke promocije | Trenutno prepričava Renault press materijale; nema lokalnog ugla |
| **Facebook** | Srednji | Aktivan profil | facebook.com/Stojanov-AUTO-1710079632592948 |
| **Instagram** | Srednji | Postoji | instagram.com/stojanovauto |
| **YouTube** | Nizak | Postoji kanal | youtube.com/channel/UCqLRzot7MqBUD4FlztvMMnQ |
| **LinkedIn** | Nizak | Lični profil, ne firmi | linkedin.com/in/stojanovauto-novi-sad-03a405125 |
| **Twitter/X** | Nizak | twitter.com/stojanovauto — [POTVRDITI da li je živ] | Verovatno ugasiti ili ukloniti iz schema |
| **Meta Ads** | ? | Pixel je postavljen | [NEDOSTAJE — da li se trenutno vrte kampanje] |

---

## Konkurencija / Competitors
**[POTVRDITI — imena izvučena iz Google autocomplete za Novi Sad, nije rađena puna analiza]**

**Konkurencija za tehnički pregled u Novom Sadu** (pojavljuju se u autocomplete):
- Wolf tehnički pregled
- Tehnički pregled Temerinska / Sajlovo / Heroja Pinkija (lokacijski konkurenti)

**Konkurencija za šlep službu u Novom Sadu**:
- S&G tim 24/7, Atlas, Leven, Božić, Velja, „Goran"

**Konkurencija za polovna vozila**:
- Autokomerc, Porsche Novi Sad

**Konkurencija za nova vozila**: ostali ovlašćeni dileri Renault/Dacia/Nissan grupacije
u Vojvodini **[NEDOSTAJE — tražiti od klijenta ko im je stvarni konkurent]**

**Naša prednost vs. konkurencija**:
- Nezavisni tehnički pregledi i šlep službe nemaju servis ni salon — Stojanov ima ceo lanac
- Nezavisni servisi nemaju ovlašćenje ni originalne delove ni fabričku dijagnostiku
- Ali: konkurenti su verovatno bolje optimizovani za lokalne upite, jer Stojanov
  trenutno ne targetira nijedan lokalni upit u naslovima stranica

---

## Cene / Pricing

- **Cenovni opseg**: $$ (srednji) — Dacia/Renault/Nissan je mainstream segment
- **Pozicioniranje cene**: ovlašćeni servis je skuplji od nezavisnog; argument nije cena
  nego garancija, originalni delovi i fabrička dijagnostika
- **Kritično**: **nijedna cena nije objavljena na sajtu** — ni tehnički pregled, ni šlep,
  ni servisni paketi, ni cene vozila. A `cena` je najčešći modifikator u lokalnim upitima
  (`tehnicki pregled novi sad cena`, `slep sluzba novi sad cena`). Ovo je najveći
  jednostruki propust u konverziji i u AI pretrazi.

---

## Customer journey (put kupca)

1. **Svesnost**: Google pretraga sa lokalnom namerom („renault servis novi sad"),
   Google Maps, preporuka, fabrički Renault/Nissan sajt koji upućuje na dilera
2. **Razmatranje**: gleda ponudu, poredi cene i rokove — **ovde sajt trenutno pada**,
   jer nema cena, nema pojedinačnih stranica vozila, nema odgovora na pitanja
3. **Konverzija**: telefonski poziv ili forma („Zakažite prvi slobodan termin",
   „Zahtev za ponudu"). Dominantno telefon. **[NEDOSTAJE — koliko leadova stiže kojim kanalom]**
4. **Povratak**: redovan servis, tehnički pregled jednom godišnje, sezonska zamena guma
   — ovo je najjača retenciona poluga koju firma ima
5. **Lojalnost**: hotel za gume i program lojalnosti (Renault/Dacia loyalty postovi
   iz jan 2026) — postoji, ali nije marketinški iskorišćen

---

## Ključni KPI-jevi / Key metrics
**[POTVRDITI ciljeve sa klijentom — trenutno nema baseline jer nema GA4/GSC pristupa]**

- Pozivi i forme sa organskog saobraćaja (cilj: [TBD])
- Pozicija u local packu za „tehnicki pregled novi sad" i „renault servis novi sad" (cilj: top 3)
- Zakazani servisni termini preko sajta (cilj: [TBD])
- Broj i prosečna ocena Google recenzija (cilj: [TBD])

---

## Tekući SEO status

**SEO ocena: 4/10** (baseline audit 2026-08-05 — bez GSC/GA4 podataka)

**Kritični problemi** (pun spisak u `/outputs/stojanov-auto/`):
1. Naslovna stranica **nema H1**; title je „STOJANOV AUTO - Stojanov Auto" — bez ključne reči, bez lokacije
2. **Nijedan title ne sadrži „Novi Sad"** — lokalni SEO praktično neaktiviran
3. Schema je `Organization`, **ne `AutoDealer`/`AutoRepair`**; `addressLocality` nedostaje;
   nema radnog vremena, telefona ni ocena u schemi
4. Duplikat: `/polovna-vozila/` i `/prodaja/polovna-vozila/` — identične, obe indeksirane
5. `/naslovna-old/` i `/akcije-old/` — stare stranice indeksirane i u sitemapu
6. ~50% slika bez alt teksta (naslovna: 80 od 104)
7. Nema pojedinačnih stranica vozila — celokupna zaliha je jedna stranica od 378 KB
8. Nema nijedne cene na sajtu
9. Mrtav Universal Analytics (`UA-179394377-1`) se i dalje učitava
10. `llms.txt` ne postoji; AI botovi su svi dozvoljeni (dobro), ali nema šta da pročitaju
