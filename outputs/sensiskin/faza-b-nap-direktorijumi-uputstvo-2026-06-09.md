# Faza B — NAP konzistentnost i čišćenje lokalnih direktorijuma
## Sensi Skin, Novi Sad — Korak po korak uputstvo
**Datum**: 9. jun 2026.  
**Za**: Nataša Burka (vlasnica, izvršava sama)  
**Status**: Spreman za izvršenje

---

## Zašto je ovo bitno — jedan paragraf

Google rangira lokalne biznise delimično na osnovu toga koliko su konzistentni podaci o njima po celom internetu. Trenutno na najmanje 4 sajta stoji stara adresa "Vojvode Bojovića 5a" koja ne postoji više. Google to vidi kao signal da poslovni podaci nisu pouzdani. Kada se svuda uskladi isti NAP blok (Naziv + Adresa + Telefon), lokalni signal jača, a šanse za pojavu na prvoj stranici pretrage i u Google Maps-u rastu.

---

## Korak 0 — Kanonski NAP blok (zlatni standard)

Ovaj tekst mora biti isti svuda, slovo po slovo. Kopiraj ga jednom u notes/beležnicu, pa ga odatle lepi na svako mesto — nikad ne kucaj ručno jer se uvlače greške.

```
Naziv:    Sensi Skin
Adresa:   Braće Popović 3, sprat 2, stan 12, 21000 Novi Sad, Srbija
Telefon:  065/333-8-338
          (+381 65 333 8338)
Email:    sensistudio@gmail.com
Sajt:     https://sensiskinstudio.com
```

**Pravila koja se ne smeju kršiti:**
- Naziv uvek: **Sensi Skin** (dve reči, bez "Studio", bez "Kozmetički centar" u samom imenu)
- Adresa uvek: **Braće Popović 3, sprat 2, stan 12, 21000 Novi Sad, Srbija** (ne "Braće Popovića", ne bez poštanskog broja)
- Telefon: uvek oba formata — lokalni **065/333-8-338** i međunarodni **(+381 65 333 8338)**
- Sajt: uvek sa **https://** (ne http://, ne bez www ako to nije vaša konfiguracija)

---

## Deo A — Pronalaženje svih citata sa starom adresom

Ovo radi jednom, pre nego što počneš da menjaš bilo šta. Cilj: napraviti kompletnu listu mesta gde treba da se pojavi ispravna adresa.

### A1 — Google pretraga sa operatorima (uradi ovo ručno)

Otvori Google i ukucaj svaku od ovih pretraga. Za svaki rezultat koji sadrži staru adresu — zabeleži URL u tracking tabelu (Deo F).

**Pretraga 1 — pronalaženje po staroj adresi:**
```
"Vojvode Bojovića 5a" "Sensi Skin"
```

**Pretraga 2 — šira pretraga (bez navodnika):**
```
Vojvode Bojovića Sensi Skin Novi Sad
```

**Pretraga 3 — provjera svakog direktoriuma posebno:**
```
site:navidiku.rs "Sensi Skin"
site:mirandre.com "Sensi Skin"
site:virtualnigrad.com "Sensi Skin"
site:ordinacije.info "Sensi Skin"
site:011info.com "Sensi Skin"
site:planplus.rs "Sensi Skin"
```

**Pretraga 4 — stara adresa bez naziva firme (može biti na sajtovima koji je ne imenuju):**
```
"Vojvode Bojovića 5a" "Novi Sad" kozmetički
```

### A2 — Šta su pretrage pokazale (stanje na dan 9. jun 2026.)

Ove podatke je agent već proverio:

| Sajt | Stanje | Adresa trenutno prikazana |
|------|--------|--------------------------|
| mirandre.com | POGRESNA ADRESA — treba popraviti | Vojvode Bojovića 5a |
| navidiku.rs | POGRESNA ADRESA — treba popraviti | Vojvode Bojovića 5a |
| virtualnigrad.com (listing) | NEPOZNATA — treba proveriti direktno | Verovatno stara adresa |
| virtualnigrad.com (blog postovi) | POGRESNA ADRESA u tekstu | Vojvode Bojovića 5A (2021. post) |
| ordinacije.info | POGRESNA ADRESA — treba popraviti | Vojvode Bojovića 5A |
| 011info.com | NE POSTOJI LISTING — treba dodati | N/A |
| planplus.rs | NEMA POTVRDE — treba proveriti | Nepoznato |
| Apple Maps | NE POSTOJI LISTING — treba dodati | N/A |
| Bing Places | NE POSTOJI LISTING — treba dodati | N/A |

---

## Deo B — Direktorijumi koje treba popraviti (po prioritetu)

Prioritet je određen po uticaju na lokalni SEO i po tome koliko je lako napraviti izmenu.

---

### B1 — mirandre.com
**Prioritet: Visok** | **Vreme: 20–30 minuta** | **Teškoća: Srednja**

**Zašto je bitno:** mirandre.com je jedan od najposećenijih direktorijuma kozmetičkih salona u Srbiji, ima visok autoritet i pojavljuje se u prvim rezultatima pretrage za "Sensi Skin Novi Sad". Trenutno prikazuje staru adresu.

**Stanje:** Listing POSTOJI na https://www.mirandre.com/kozmeticki-salon-sensi-skin — ali sa adresom "Vojvode Bojovića 5a".

**Kako popraviti:**
1. Idi na https://www.mirandre.com/kozmeticki-salon-sensi-skin
2. Potraži dugme "Preuzmi profil", "Vlasnik si?", ili "Uredi poslovni profil" (obično je u dnu listinga ili uz naziv firme)
3. Klikni — tražiće ti da se registruješ ili prijaviš
4. Registruj se sa emailom sensistudio@gmail.com
5. Potvrdi vlasništvo (obično ti pošalju email sa linkom za potvrdu)
6. Nakon potvrde, uđi u upravljačku tablu i promeni adresu na kanonski NAP blok
7. Proveri i ostala polja: telefon, sajt, opis, radno vreme
8. Sačuvaj izmene

**Pazi na:** mirandre.com može imati i stare recenzije i komentare gde se pominje stara adresa — te ne možeš direktno menjati (komentari klijenata), ali listing treba biti ispravan.

**Šta uneti u polje opisa (kratka verzija, do 500 karaktera):**
> Sensi Skin je kozmetički studio u Novom Sadu sa 20+ godina iskustva u medicinskoj estetici. Vlasnica Nataša Burka, spec. medicinske estetike, nudi individualizovane tretmane lica i tela: HydraFacial, lasersku epilaciju, Aura Reality 3D dijagnostiku kože, Mesojet tretmane i profesionalnu negu kože. Studio se nalazi u centru Novog Sada — Braće Popović 3, sprat 2.

---

### B2 — navidiku.rs
**Prioritet: Visok** | **Vreme: 30–45 minuta** | **Teškoća: Srednja-teška**

**Stanje:** Listing POSTOJI na https://www.navidiku.rs/firme/kozmeticki-saloni-novi-sad/sensi-skin-kozmeticki-studio — prikazuje staru adresu "Vojvode Bojovića 5a".

**Napomena:** navidiku.rs ima i poseban URL za mapu sa starom adresom: `.../vojvode-bojovica-5a-novi-sad` — taj URL postoji kao zaseban "podlisting". Oba treba rešiti.

**Kako popraviti:**

**Opcija 1 — Vlasnikov nalog (preferred):**
1. Idi na https://www.navidiku.rs/firme/dodaj-firmu
2. Prijavna forma za vlasnike obično sadrži i opciju "imam već listing, prijavljujem se kao vlasnik"
3. Registruj se sa sensistudio@gmail.com ili preuzmite Business Admin aplikaciju (dostupna na Google Play i App Store pod "Navidiku.rs - business admin")
4. Kroz aplikaciju možeš menjati sve podatke u realnom vremenu
5. Promeni adresu, potvrdi telefon, dodaj sajt i email

**Opcija 2 — Direktni kontakt:**
1. Idi na https://www.navidiku.rs i potraži link "Kontakt" u footer-u
2. Pošalji poruku: "Ja sam vlasnica firme Sensi Skin, naš listing na vašem sajtu prikazuje staru adresu. Nova adresa je: Braće Popović 3, sprat 2, stan 12, 21000 Novi Sad. Molim da ažurirate."
3. Priloži fotografiju fasade ili nekakav dokaz vlasništva ako traže

**Pazi na:** URL sa starom adresom (`/vojvode-bojovica-5a-novi-sad`) — zatraži od tima navidiku.rs da ga uklone ili preusmere na ispravni listing.

---

### B3 — ordinacije.info
**Prioritet: Visok** | **Vreme: 20–30 minuta** | **Teškoća: Laka-srednja**

**Stanje:** Listing POSTOJI na https://www.ordinacije.info/kozmeticki-saloni-novi-sad-kozmeticki-salon-sensi-skin/ — prikazuje adresu "Vojvode Bojovića 5A". Sajt ima i više blog postova sa Sensi Skin sadržajem.

**Napomena:** ordinacije.info izgleda kao direktori koji prihvata i PR tekstove. Sensi Skin je tu opisana detaljno sa više objava — to je dobro (autoritet), ali adresa u opisu treba da bude ispravna.

**Kako popraviti:**
1. Idi na https://www.ordinacije.info/kozmeticki-saloni-novi-sad-kozmeticki-salon-sensi-skin/
2. Potraži link "Kontakt", "Uredi profil" ili "Vlasnik si?" na stranici ili u footeru
3. Ako ne postoji samoposluživanje, pošalji email na kontakt adresu sajta (pronađi je u footeru)
4. Tekst emaila:

```
Predmet: Ispravka podataka — Kozmetički salon Sensi Skin, Novi Sad

Poštovani,

Vlasnica sam kozmetičkog salona Sensi Skin u Novom Sadu. Na vašem sajtu 
su navedeni stari podaci o adresi. 

Molim da ažurirate sledeće:
STARA ADRESA: Vojvode Bojovića 5A, Novi Sad
NOVA ADRESA: Braće Popović 3, sprat 2, stan 12, 21000 Novi Sad, Srbija
TELEFON: 065/333-8-338 (+381 65 333 8338)
SAJT: https://sensiskinstudio.com
EMAIL: sensistudio@gmail.com

Hvala unapred.
S poštovanjem,
Nataša Burka, vlasnica Sensi Skin
```

5. Isti email pošalji i za svaki od blog postova na ordinacije.info koji sadrže staru adresu (pogledaj listu URL-ova sa pretrage)

---

### B4 — virtualnigrad.com
**Prioritet: Srednji** | **Vreme: 20–40 minuta** | **Teškoća: Srednja**

**Stanje:** 
- Listing na https://www.virtualnigrad.com/item/kozmeticki-salon-sensi-skin/ — adresa nije potvrđena, ali verovatno stara
- Blog post iz 2021 na https://www.virtualnigrad.com/2021/04/nega-koze-u-prolece/ — sadrži "Vojvode Bojovića 5A"

**Kako popraviti:**
1. Idi na https://www.virtualnigrad.com/kontakt (potraži stranicu za kontakt)
2. Pošalji isti email kao za ordinacije.info (prilagodi naziv sajta)
3. U emailu navedi oba URL-a: listing i blog post
4. Zatraži izmenu adrese i na listingu i u tekstu blog posta

**Ako nema kontakt forme:** potraži email ili Facebook stranicu virtualnigrad.com i pošalji poruku tamo.

---

### B5 — 011info.com
**Prioritet: Srednji** | **Vreme: 15–20 minuta** | **Teškoća: Laka**

**Stanje:** Listing NE POSTOJI — treba kreirati od nule.

**Napomena:** 011info.com je uglavnom Beogradski direktorijum (ime govori — 011 je pozivni broj Beograda), ali indeksira i firme iz Novog Sada. Prisutnost tu nije kritična, ali je besplatna i korisna za NAP signale.

**Kako dodati:**
1. Idi na https://www.011info.com
2. Potraži opciju "Dodaj firmu" ili "Registruj biznis" (obično u gornjem meniju ili footeru)
3. Popuni formu sa kanonskim NAP blokom
4. Kategorija: Kozmetički saloni / Salon lepote
5. Opis: koristi kratak opis iz B1 (prilagoditi ako traže drugačiji format)
6. Potvrdi listanje emailom

---

### B6 — planplus.rs
**Prioritet: Srednji** | **Vreme: 20–30 minuta** | **Teškoća: Srednja**

**Stanje:** Pretraga nije potvrdila listing sa Sensi Skin imenom direktno — ali planplus.rs je mapa/direktorijum koji pokriva celu Srbiju i vredi biti prisutan.

**Kako dodati/proveriti:**
1. Idi na https://www.planplus.rs
2. U pretrazi ukucaj "Sensi Skin" + "Novi Sad" — ako listing postoji, potražiće opciju za claim/preuzimanje
3. Ako ne postoji — potraži "Dodaj firmu" ili "Add business" opciju
4. Registruj se i dodaj kanonski NAP blok
5. Kategorija: Kozmetički salon / Beauty salon

---

## Deo C — Novi platformi koje treba kreirati od nule

---

### C1 — Apple Business (Apple Maps)
**Prioritet: Visok** | **Vreme: 30–45 minuta** | **Teškoća: Laka**

**Zašto:** iPhone korisnici koriste Apple Maps, ne Google Maps. Svaka žena u Novom Sadu koja ima iPhone i traži "kozmetički salon" — vidi Apple Maps rezultate. Besplatno, a povećava vidljivost.

**Korak po korak:**
1. Na računaru ili iPhoneu idi na https://businessconnect.apple.com
2. Klikni "Get Started" ili "Prijavite se"
3. Prijaviti se sa Apple ID nalogom (ako nemaš, kreirati besplatno na appleid.apple.com)
4. Klikni "Add a Place" ili "Claim your business"
5. Ukucaj "Sensi Skin" i "Novi Sad" — proveri da li listing već postoji
6. Ako postoji — klikni "Claim" i prođi verifikaciju
7. Ako ne postoji — klikni "Add New Place" i popuni formu

**Šta uneti:**
- Naziv: Sensi Skin
- Kategorija: Beauty Salon / Kozmetički salon
- Adresa: Brace Popovic 3, floor 2, apt 12, Novi Sad 21000, Serbia (uneti na engleskom — sistem to zahteva)
- Telefon: +381 65 333 8338
- Sajt: https://sensiskinstudio.com
- Radno vreme: Ponedeljak–Petak 10:00–21:00, Subota 09:00–17:00

**Verifikacija:** Apple šalje SMS ili poziv na telefonski broj koji si navela. Odgovori na poziv ili unesi SMS kod.

**Vreme do objave:** 1–3 dana nakon verifikacije.

---

### C2 — Bing Places for Business
**Prioritet: Srednji** | **Vreme: 25–35 minuta** | **Teškoća: Laka**

**Zašto:** Bing ne dominira u Srbiji, ali ga koriste Windows korisnici (Edge browser) i ChatGPT koristi Bing kao izvor podataka za lokalne biznise. To znači da ispravan Bing listing direktno pomaže da Sensi Skin bude citiran kada neko pita ChatGPT "koji je dobar kozmetički salon u Novom Sadu".

**Korak po korak:**
1. Idi na https://www.bingplaces.com
2. Klikni "Get Started"
3. Prijavi se sa Microsoft nalogom (ako nemaš — outlook.com nalog je besplatan, kreira se za 2 minuta)
4. U pretraži ukucaj "Sensi Skin" i "Novi Sad" — proveri da li listing već postoji
5. Ako postoji — klikni "Claim Business" pored naziva
6. Ako ne postoji — klikni "Create New Business"
7. Popuni sve podatke sa kanonskim NAP blokom
8. Kategorija: Beauty Salon / Spa & Beauty

**Šta uneti:**
- Naziv: Sensi Skin
- Adresa: Brace Popovic 3, Novi Sad, Serbia, 21000 (uneti na engleskom ili srpskom — oba rade)
- Telefon: +381 65 333 8338
- Sajt: https://sensiskinstudio.com
- Opis: kratki opis od 1–2 rečenice sa kanonskim NAP blokom

**Verifikacija:** Bing nudi verifikaciju telefonom (SMS), emailom ili poštom. Izaberi SMS — najbrže, gotovo u minuti.

**Pazi na:** Ako postoji stari listing bez vlasnika — preuzmi ga ("claim") pre nego što praviš novi. Duplikat listinzi zbunjuju Google i Bing.

**Vreme do objave:** 7–14 dana nakon verifikacije.

---

## Deo D — Provera i usklađivanje naloga na socijalnim mrežama

Socijalni profili nisu klasični direktorijumi, ali Google ih indeksira i uzima NAP podatke sa njih kao signal.

### D1 — Facebook: facebook.com/sensi.skin.studiozanegulepote

**Koraci:**
1. Idi na profil stranicu
2. Klikni "Uredi stranicu" → "O stranici" → "Lokacija"
3. Proveri unesenu adresu — ažuriraj na: Braće Popović 3, sprat 2, stan 12, Novi Sad
4. Proveri telefon: 065/333-8-338
5. Proveri sajt: https://sensiskinstudio.com
6. Proveri kategoriju: "Kozmetički salon" ili "Salon lepote"
7. Sačuvaj

**Napomena:** Na Facebook-u je adresa u sekciji "O nama" — vidljiva je korisnicima ali i Google-u kada indeksira javne Facebook stranice.

### D2 — Instagram: instagram.com/sensi_skin

**Koraci:**
1. Otvori profil → Edit Profile (Uredi profil)
2. U polju "Bio" dodaj adresu u kompaktnom formatu ako nije tu: "Braće Popović 3, sp. 2, Novi Sad"
3. U polju "Website": https://sensiskinstudio.com
4. U sekciji "Contact" (Kontakt): unesite email sensistudio@gmail.com i telefon 065/333-8-338
5. Kategorija profila: "Kozmetički salon" ili "Health/beauty"

**Napomena:** Instagram bio je ograničen na 150 karaktera — nije potrebno pisati punu adresu, ali telefon i sajt moraju biti tačni.

---

## Deo E — Šta da uradiš SA SVAKIM NOVIM LISTINGOM (checklist za svaki sajt)

Svaki put kada popunjavaš formu na novom sajtu, prođi kroz ovu listu:

- [ ] Naziv: tačno "Sensi Skin" (proverite da ne piše "Sensi Skin Studio" ili "SensiSkin" bez razmaka)
- [ ] Adresa: "Braće Popović 3, sprat 2, stan 12, 21000 Novi Sad, Srbija"
- [ ] Telefon: oba formata — lokalni i međunarodni
- [ ] Email: sensistudio@gmail.com
- [ ] Sajt: https://sensiskinstudio.com (sa https)
- [ ] Kategorija: Kozmetički salon (ne "spa", ne "medicinska klinika")
- [ ] Opis: varijacija od kratkog opisa (ne isti tekst na svakom mestu — menjaj prvu rečenicu)
- [ ] Radno vreme: Pon–Pet 10:00–21:00 / Sub 09:00–17:00 / Ned: zatvoreno
- [ ] Logo i fotografije: dodati gde god postoji opcija (smanjuje šansu da te pogrešno kategorizuju)
- [ ] Napraviti screenshot potvrdne stranice ili emaila za evidenciju

---

## Deo F — Tabela za praćenje (ticked off checklist)

Štampaj ili kopiraj u Excel/Google Sheets. Označi svaki korak čim ga završiš.

| # | Direktorijum / Platforma | Status | Akcija | Datum završetka | Napomena |
|---|--------------------------|--------|--------|-----------------|----------|
| 1 | mirandre.com | Treba popraviti | Claim + izmena adrese | | |
| 2 | navidiku.rs (listing) | Treba popraviti | Claim/kontakt + izmena adrese | | |
| 3 | navidiku.rs (URL sa starom adresom) | Treba ukloniti | Email/kontakt tim | | |
| 4 | ordinacije.info (listing) | Treba popraviti | Email za izmenu adrese | | |
| 5 | ordinacije.info (blog postovi sa st. adresom) | Treba popraviti | Email za izmenu teksta | | |
| 6 | virtualnigrad.com (listing) | Proveriti | Kontakt/email za izmenu | | |
| 7 | virtualnigrad.com (blog post 2021) | Treba popraviti | Email za izmenu teksta | | |
| 8 | 011info.com | Treba kreirati | Dodati novi listing | | |
| 9 | planplus.rs | Proveriti/kreirati | Claim ili dodati novi | | |
| 10 | Apple Business (Apple Maps) | Treba kreirati | Registracija + verifikacija | | |
| 11 | Bing Places for Business | Treba kreirati | Registracija + verifikacija | | |
| 12 | Facebook (O stranici) | Proveriti adresu | Ažurirati adresu u podešavanjima | | |
| 13 | Instagram (bio/kontakt) | Proveriti | Ažurirati sajt i kontakt | | |
| 14 | Google pretraga — provjera po završetku | Re-audit | Ponoviti pretrage iz Dela A | | |

**Statusi koji se koriste:**
- "Treba popraviti" — listing postoji, adresa je pogrešna
- "Treba kreirati" — listing ne postoji, treba ga dodati
- "Proveriti" — nepoznato stanje, otvoriti stranicu i videti
- "Gotovo" — izmena potvrđena (dobijen email ili vidljivo na sajtu)
- "Čekanje" — poslat zahtev, čeka se odgovor/verifikacija

---

## Deo G — Preporučeni redosled izvršenja

Ne raditi sve odjednom. Ovaj redosled optimizuje vreme i rezultate:

**Dan 1 (oko 90 minuta):**
1. Kopiraj kanonski NAP blok u beležnicu (Korak 0)
2. Uradi sve Google pretrage iz Dela A — zabeleži nova mesta sa greškom ako ih nađeš
3. Klikni na mirandre.com listing → počni claim proces (B1)
4. Klikni na navidiku.rs listing → preuzmi Business Admin aplikaciju (B2)
5. Pošalji email za ordinacije.info (B3) — 5 minuta

**Dan 2 (oko 60 minuta):**
6. Pošalji email za virtualnigrad.com (B4) — 5 minuta
7. Kreiraj Apple Business nalog i listing (C1) — 30 minuta
8. Ažuriraj Facebook "O stranici" (D1) — 10 minuta
9. Ažuriraj Instagram bio/kontakt (D2) — 5 minuta

**Dan 3 (oko 45 minuta):**
10. Kreiraj Bing Places listing (C2) — 25 minuta
11. Dodaj listing na 011info.com (B5) — 15 minuta
12. Proveri planplus.rs (B6) — 10 minuta

**Nedelja 2 — provera:**
13. Proveri inbox za odgovore od direktorijuma kojima si pisala
14. Proveri da li su Apple i Bing listinzi prošli verifikaciju
15. Ako nisi dobila odgovor od nekog direktoriuma za 7 dana — pošalji podsetnik

**2–4 nedelje nakon završetka — re-audit (Deo A ponovo):**
16. Ponoviti sve Google pretrage iz Dela A
17. Proveriti da li se negde još uvek pojavljuje stara adresa
18. Ažurirati tabelu — označiti "Gotovo"

---

## Deo H — Definicija "Gotovo" za Fazu B

Faza B je završena kada su ispunjeni SVI sledeći uslovi:

1. Google pretraga `"Vojvode Bojovića 5a" "Sensi Skin"` ne vraća nijedan aktivni (ne-arhiviran) rezultat
2. Svih 5 direktorijuma (mirandre.com, navidiku.rs, ordinacije.info, virtualnigrad.com, planplus.rs) prikazuju ispravnu adresu "Braće Popović 3"
3. Apple Maps prikazuje listing sa ispravnom adresom (proveriti na iPhone u Maps aplikaciji — ukucati "Sensi Skin Novi Sad")
4. Bing Maps prikazuje listing sa ispravnom adresom (proveriti na https://www.bing.com/maps → ukucati "Sensi Skin Novi Sad")
5. Facebook i Instagram imaju ispravne kontakt podatke i sajt link

**Merilo uspeha (KPI za Fazu B):**
- Minimalno 7 od 13 stavki u tabeli ima status "Gotovo" u roku od 30 dana
- Nula aktivnih rezultata za staru adresu u Google pretrazi
- Apple Maps listing potvrđen (provjeri na iPhoneu)

---

## Napomene i pitanja na kojima Nataša treba da donese odluku

Postoje tri stvari gde agent ne može da odluči umesto vlasnice:

**Odluka 1 — Nalog za direktorijume:**
Za navidiku.rs, mirandre.com i ostale treba email adresa za registraciju. Preporučujem da koristiš sensistudio@gmail.com dosledno svuda (lakše za praćenje). Da li ti odgovara, ili preferiraš poseban email za poslovne platforme?

**Odluka 2 — Apple ID:**
Za Apple Business treba Apple ID. Ako ga nemaš, kreiraš ga besplatno. Ako ga imaš (za iPhone), bolje je koristiti isti nalog — sve je na jednom mestu. Proveri koji Apple ID je vezan za tvoj iPhone pre nego što počneš.

**Odluka 3 — Radno vreme:**
Svuda unosiš radno vreme. Proveriti da li je tačno: **Pon–Pet 10:00–21:00 / Sub 09:00–17:00 / Ned: zatvoreno.** Ako se promenilo, koristi ažurirano vreme dosledno na svim platformama.

---

*Dokument pripremio: SEO agent za Sensi Skin, 9. jun 2026.*  
*Sledeća faza: Faza C — On-page optimizacija (title tagovi, meta opisi, schema markup).*
