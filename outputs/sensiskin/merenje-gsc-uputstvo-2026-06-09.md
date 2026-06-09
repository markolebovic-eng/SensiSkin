# Sensi Skin — Merenje i verifikacija SEO napretka
## Korak-po-korak playbook za Fazu B i Fazu C
**Datum izrade**: 9. jun 2026.  
**Za**: Vlasnika/vlasnika studija — bez tehničkog predznanja  
**Cilj**: Da možete VIDETI da li Phase B (NAP/direktorijumi) i Phase C (on-page/schema) rade, i da uhvatite probleme pre nego što se nagomilaju.

---

## DEO 0 — SNAPSHOT "DANAS" (snimak pre promena)

Pre nego što krenete sa bilo čim, zabeležite ove brojeve. Bez polazne tačke, ne možete meriti napredak.

### Šta snimiti danas — 9. jun 2026.

1. **Google Search Console — Performance izveštaj**
   - Idite na: search.google.com/search-console
   - Kliknite: "Performance" → "Search results"
   - Promenite period na: poslednjih 3 meseca
   - Zapišite: ukupan broj klikova, ukupan broj impresija, prosečna pozicija
   - Zapišite i top 5 upita (ključnih reči) iz tabele "Queries"

2. **Google Search Console — broj indeksiranih stranica**
   - Kliknite: "Indexing" → "Pages"
   - Zapišite: broj stranica sa statusom "Indexed" (zeleno)
   - Zapišite: broj stranica sa greškama (crveno)

3. **Google Business Profile — Insights**
   - Idite na: business.google.com
   - Kliknite na vaš profil → "Performance" ili "Insights"
   - Zapišite za poslednjih 28 dana: broj prikaza profila, broj poziva, broj zahteva za rutu, broj recenzija i prosečna ocena

4. **Google pretraga — vizuelni snapshot**
   - Otvorite inkognito tab (Ctrl+Shift+N u Chrome-u)
   - Pretražite: `site:sensiskinstudio.com`
   - Zapišite koliko stranica Google prikazuje
   - Pretražite: `"Vojvode Bojovića 5a"` — zapišite da li se stara adresa pojavljuje i gde
   - Pretražite: `sensi skin kozmetički centar novi sad` — zapišite na kojoj ste poziciji

5. **Recenzije**
   - Otvorite Google Maps, pretražite "Sensi Skin Novi Sad"
   - Zapišite: ukupan broj recenzija, prosečna ocena (zvezdice)

> Sačuvajte ove brojeve u kolonu "Baseline (danas)" u tabeli u Delu 3 ovog dokumenta.

---

## DEO 1 — GOOGLE SEARCH CONSOLE (GSC)

Google Search Console je besplatna Google alatka koja vam govori kako Google "vidi" vaš sajt. Mislite na nju kao na izveštaj koji Google šalje vama o vašem sajtu.

Adresa: **search.google.com/search-console**

---

### 1a. Kako potvrditi da je sajt verifikovan

Verifikacija znači da GSC zna da ste vi vlasnik sensiskinstudio.com.

**Korak 1.** Idite na search.google.com/search-console i prijavite se Google nalogom.

**Korak 2.** U gornjem levom uglu vidite naziv imovine (property). Treba da piše `sensiskinstudio.com` ili `sc-domain:sensiskinstudio.com`.

**Korak 3.** Ako vidite dashboard sa grafovima i izveštajima — sajt je verifikovan. Gotovo.

**Korak 4.** Ako ne vidite sajt ili piše "Add a property":
- Kliknite "Add property"
- Unesite `sensiskinstudio.com`
- Izaberite verifikaciju putem "DNS record" — ovo radi vaš hosting provajder (ili pišite nama)

> Ako ste već verifikovani iz prethodnih faza — samo proverite da li dashboard učitava podatke. Ako da, sve je u redu.

---

### 1b. URL Inspection — da li je nova stranica / novi title indeksiran?

Ovo koristite posle svake promene naslova (title taga), meta opisa ili sadržaja stranice.

**Korak 1.** U GSC, u traku za pretragu na vrhu (piše "Inspect any URL in [vaš sajt]"), unesite punu adresu stranice.  
Primer: `https://sensiskinstudio.com/hydrafacial-tretmani-lica-novi-sad/`

**Korak 2.** Sačekajte nekoliko sekundi dok se učita rezultat.

**Korak 3.** Pogledajte šta piše:
- "URL is on Google" = stranica je indeksirana, sve je u redu
- "URL is not on Google" = stranica NIJE u Google indeksu — treba je prijaviti (pogledaj 1c)

**Korak 4.** Kliknite na "View crawled page" → kartica "More info".  
Tražite: "Page title". Proverite da li se ovde vidi VAŠ novi title tag koji ste upisali u Yoast.  
Ako još uvek piše stari naslov — Google nije ponovo prošao kroz stranicu. Vidite 1c.

---

### 1c. Zahtev za re-indeksiranje posle promena na stranici

Svaki put kada promenite title tag, sadržaj ili schema markup na nekoj stranici, recite Googleu da ponovo proveri tu stranicu.

**Korak 1.** Unesite URL stranice u traku za pretragu u GSC (isto kao u 1b).

**Korak 2.** Kliknite dugme "Request indexing" (desno gore ili u sredini ekrana).

**Korak 3.** Pojaviće se točkić (učitavanje) nekoliko sekundi. Kada završi, videćete poruku "Indexing requested".

**Korak 4.** Sačekajte. Google obično re-crawluje stranicu za 3–14 dana. Ne morate da pritiskate više puta — jedanput je dovoljno.

**Korak 5.** Posle 7–10 dana, ponovo uradite korake iz 1b i proverite da li je novi title vidljiv pod "View crawled page".

> Ograničenje: GSC dozvoljava oko 10 URL prijava dnevno. Prioritizujte: Home, HydraFacial, Epilacija, Kontakt.

---

### 1d. Performance izveštaj — impresije i pozicija na ciljnim ključnim rečima

Ovo vam govori: "Koliko puta su vas ljudi videli u Google pretrazi, i na kojoj poziciji?"

**Korak 1.** U levom meniju kliknite "Performance" → "Search results".

**Korak 2.** Na vrhu, kliknite "Date range" i izaberite "Last 3 months" (ili "Compare" da poredite dva perioda).

**Korak 3.** Proverite da su uključena sva 4 polja na vrhu grafikona: Clicks, Impressions, Average CTR, Average position. Kliknite na svako da se upali.

**Korak 4.** Skrolujte dole do tabele "Queries".

**Korak 5.** U polje za pretragu iznad tabele unesite ključnu reč koja vas zanima. Primeri:
- `hydrafacial novi sad`
- `laserska epilacija novi sad`
- `kozmetički centar novi sad`
- `sensi skin`

**Korak 6.** Za svaku ključnu reč zapišite:
- Impressions (impresije) — koliko puta se vaš sajt pojavio u pretrazi
- Clicks (klikovi) — koliko puta su kliknuli
- Position (pozicija) — prosečna pozicija u rezultatima (1 = prvo mesto, 10 = kraj prve stranice)

> Cilj: Posle Phase C, impresije treba da rastu za ciljne ključne reči. Ako su impresije = 0, stranica ili nije indeksirana, ili nema sadržaja.

---

### 1e. Coverage / Pages izveštaj — greške u indeksiranju

Ovo vam pokazuje koje stranice Google ne može da indeksira i zašto.

**Korak 1.** U levom meniju kliknite "Indexing" → "Pages".

**Korak 2.** Videćete pie chart (krug) sa bojama. Zeleno = indeksirano. Ostale boje = problemi.

**Korak 3.** Kliknite na crvenu ili narandžastu sekciju. Pojaviće se lista URL adresa sa greškom.

**Korak 4.** Najčešće greške — šta znači:
- "Crawled — currently not indexed": Google je video stranicu ali odlučio da je ne indeksira. Najčešće zbog previše malog sadržaja (ispod 300 reči). Rešenje: dodajte sadržaj.
- "Not found (404)": Stranica ne postoji. Možda je obrisana ili promenjen URL. Rešenje: proverite da li URL radi u browseru.
- "Redirect error": Stranica preusmjerava na pogrešno mesto. Rešenje: javite web developeru.
- "Excluded by noindex tag": Stranica ima oznaku "ne indeksiraj". Proverite u Yoast da li je greškom uključena opcija "noindex".

**Korak 5.** Mesečno proverite da li se broj grešaka smanjuje (dobro) ili raste (problem).

> Baseline koji treba zapamtiti: Iz ranijeg audita, sajt je imao 21 mrtav URL u sitemapu iz 2018. Proverite da li su ti URL-ovi sada u greškama — treba da nestanu tokom Phase B/C.

---

## DEO 2 — GOOGLE BUSINESS PROFILE INSIGHTS

GBP Insights su brojevi koji pokazuju šta se dešava na vašem Google profilu. Dostupni su na: **business.google.com**

Kliknite na vaš profil → "Performance" (ili "See your profile performance").

---

### Koji brojevi da gledate i šta znače

**Za Phase A i Phase B — ovi brojevi su najvažniji:**

| Metrika | Gde se nalazi | Šta znači | Cilj |
|---|---|---|---|
| Profile views (Prikazi profila) | Performance → Searches | Koliko puta su ljudi videli vaš GBP profil u pretrazi ili Maps | Rast iz meseca u mesec |
| Website clicks (Klikovi na sajt) | Performance → Actions | Koliko je kliknulo da ode na sensiskinstudio.com | Rast > 20% u 60 dana od GBP optimizacije |
| Calls (Pozivi) | Performance → Actions | Koliko je kliknulo na broj telefona direktno sa GBP-a | Baseline → pratite nedeljno |
| Directions (Rute) | Performance → Actions | Koliko je tražilo rutu do studija | Rast posle NAP cleanup-a |
| Review count (Broj recenzija) | Vaš profil | Ukupan broj Google recenzija | Cilj: +4–6 recenzija mesečno |
| Review average (Prosek ocena) | Vaš profil | Prosečna zvezdica ocena | Cilj: 4.8+ zvezde |

**Kako čitati trendove:**
- GBP Insights prikazuje podatke za poslednjih 28 dana. Svake nedelje zabeležite broj u svoju tabelu.
- Ako vidite PORAST u "Searches" i "Actions" posle Phase B (NAP cleanup) — znači da je Google povećao poverenje u vaš profil jer su podaci konzistentni.
- Pozivi i rute su najvažniji signali: direktno se pretvaraju u klijente.
- "Profile views" raste polako (1–2 meseca od promene). "Calls" i "Directions" su brži indikator.

> Napomena o "Searches vs. Views": GBP razlikuje "Business Profile Interactions" (akcije koje je korisnik preduzeo) od "Business Profile Views" (koliko je profil prikazan). Fokusirajte se na Interactions jer su to pravi potencijalni klijenti.

---

## DEO 3 — MESECNA TABELA PRACENJA

Kopirajte ovu tabelu u Google Sheets ili Excel. Popunite kolonu "Baseline (danas)" odmah.

| Metrika | Baseline (9. jun 2026) | Cilj (3 meseca) | Jul 2026 | Avg 2026 | Sep 2026 |
|---|---|---|---|---|---|
| GSC: Ukupni klikovi (90 dana) | ___ | +50% | | | |
| GSC: Ukupne impresije (90 dana) | ___ | +100% | | | |
| GSC: Prosečna pozicija (90 dana) | ___ | ispod 20 | | | |
| GSC: Broj indeksiranih stranica | ___ | 13+ (sve key stranice) | | | |
| GSC: Broj indexing grešaka | ___ | 0 | | | |
| GSC: Impresije za "hydrafacial novi sad" | ___ | 100+/mesec | | | |
| GSC: Impresije za "laserska epilacija novi sad" | ___ | 100+/mesec | | | |
| GSC: Impresije za "kozmetički centar novi sad" | ___ | 200+/mesec | | | |
| GBP: Prikazi profila (28 dana) | ___ | +40% u 60 dana | | | |
| GBP: Klikovi na sajt (28 dana) | ___ | +30% | | | |
| GBP: Pozivi (28 dana) | ___ | +20% | | | |
| GBP: Zahtevi za rutu (28 dana) | ___ | +20% | | | |
| GBP: Broj recenzija (ukupno) | ___ | +12 za 3 meseca | | | |
| GBP: Prosečna ocena | ___ | 4.8+ | | | |
| AI check: Pomenuta u ChatGPT? | Da/Ne | Da, barem 1 od 3 upita | | | |
| AI check: Pomenuta u Perplexity? | Da/Ne | Da, barem 1 od 3 upita | | | |

**Kada popunjavati:** Jednom mesečno, uvek istog dana (npr. prvog u mesecu).

---

## DEO 4 — VERIFIKACIJA PHASE B (NAP/Direktorijumi)

Phase B je uspešna kada: (a) stara adresa "Vojvode Bojovića 5a" više nije vidljiva na webu i (b) svi direktorijumi prikazuju istu, tačnu adresu.

---

### 4a. Proverite da li se stara adresa još uvek pojavljuje

**Korak 1.** Otvorite Chrome u inkognito modu (Ctrl+Shift+N).

**Korak 2.** Pretražite tačno ovo (sa navodnicima):
```
"Vojvode Bojovića 5a" "Sensi Skin"
```

**Korak 3.** Prođite kroz prve dve stranice rezultata. Ako nema rezultata — odlično, Phase B je čist.

**Korak 4.** Ako se pojavljuje neka stranica (npr. mirandre.com, virtualnigrad.com), to su direktorijumi koji još nisu ažurirani. Prijavite se na taj direktorijum i promenite adresu.

**Korak 5.** Iste pretrage ponovite i bez navodnika:
```
Vojvode Bojovića 5a Sensi Skin Novi Sad
```

**Korak 6.** Ponovite ove pretrage svake 4 nedelje dok ne dobijete nula rezultata.

---

### 4b. Proverite NAP konzistentnost na ključnim direktorijumima

Tačan NAP blok koji mora biti identičan svuda:
> **Sensi Skin** / Braće Popović 3, sprat 2, stan 12, 21000 Novi Sad, Srbija / 065/333-8-338 / sensistudio@gmail.com / https://sensiskinstudio.com

**Proverite ove lokacije jednu po jednu:**

| Platforma | URL | Proverite da li NAP odgovara |
|---|---|---|
| Google Business Profile | business.google.com | adresa, telefon, sajt |
| navidiku.rs | navidiku.rs | tražite "Sensi Skin" |
| virtualnigrad.com | virtualnigrad.com | tražite "Sensi Skin" |
| mirandre.com | mirandre.com | tražite "Sensi Skin" |
| ordinacije.info | ordinacije.info | tražite "Sensi Skin" |
| Facebook | facebook.com/sensi.skin.studiozanegulepote | "O firmi" sekcija |
| Instagram | instagram.com/sensi_skin | bio sekcija |

**Za svaki: kliknite na "uredi" ili "predloži izmenu" i unesite tačan NAP.**

> Svaki direktorijum koji prikazuje staru adresu ili pogrešan telefon SMANJUJE vase šanse u lokalnoj pretrazi i u AI preporuci. Konzistentnost = poverenje Googlea.

---

### 4c. Proverite ispravan prikaz u Google Maps

**Korak 1.** Otvorite maps.google.com.

**Korak 2.** Pretražite "Sensi Skin Novi Sad".

**Korak 3.** Proverite da li se prikazuje NOVA adresa (Braće Popović 3) — ne stara.

**Korak 4.** Kliknite na profil. Proverite: adresu, telefon, radno vreme, sajt. Sve treba da odgovara tačnom NAP bloku.

---

## DEO 5 — VERIFIKACIJA PHASE C (On-page/Schema)

Phase C uključuje: ispravne title tagove, meta opise, sadržaj na stranicama i schema markup (strukturirani podaci koji pomažu Googleu da razume šta je vaš studio).

---

### 5a. Kako proveriti da je novi title tag ušao u Google

**Metoda 1 — direktna Google pretraga:**

**Korak 1.** Otvorite inkognito tab.

**Korak 2.** Pretražite naziv stranice ili ključnu reč. Primer: `hydrafacial Novi Sad`.

**Korak 3.** Potražite sensiskinstudio.com u rezultatima. Kliknite na tri tačke pored rezultata (ili pogledajte plavi naslov).

**Korak 4.** Da li plavi naslov odgovara title tagu koji ste uneli u Yoast? Ako da — indeksiran. Ako ne (stari naslov) — koristite GSC Request Indexing (Deo 1c).

**Metoda 2 — GSC URL Inspection (pouzdanije):**

Koristite postupak iz Dela 1b i 1d za svaku stranicu koja je promenjena.

---

### 5b. Validacija schema markup-a — Rich Results Test

Schema markup je "nevidljivi kod" koji Googleu govori: "Ovo je lokalni kozmetički studio, evo adrese, usluga, ocene."

**Korak 1.** Idite na: **search.google.com/test/rich-results**

**Korak 2.** U polje "Enter URL to test" unesite adresu stranice koju proveravate.  
Primer: `https://sensiskinstudio.com/` (homepage za LocalBusiness schema)

**Korak 3.** Kliknite "Test URL".

**Korak 4.** Sačekajte 20–30 sekundi.

**Korak 5.** Videćete listu detected structured data (schema tipovi koji su pronađeni).  
Tražite:
- `LocalBusiness` ili `HealthAndBeautyBusiness` — treba biti na Home i Kontakt stranici
- `Service` — treba biti na svakoj stranici tretmana (HydraFacial, Epilacija, itd.)
- `BreadcrumbList` — treba biti na dubokim stranicama

**Korak 6.** Ako vidite zelenu ikonu pored tipa — schema je validna.

**Korak 7.** Ako vidite žutu ikonu ("Warning") — schema postoji ali ima manjivih problema. Obično nebitno za lokalni biznis.

**Korak 8.** Ako vidite crvenu ikonu ("Error") ili tip uopšte NIJE na listi — schema nije implementirana ili ima grešku. Prosledite ovaj izveštaj web developeru.

> NAPOMENA o FAQ schema (jun 2026): Google je u maju 2026. uklonio vizuelni FAQ prikaz iz pretrage. Međutim, FAQPage schema markup I DALJE ima vrednost za AI pretraživače (ChatGPT, Perplexity). Nemojte je brisati ako je implementirana.

**Alternativna alatka — Schema Markup Validator:**

Za detaljniju tehničku validaciju: **validator.schema.org**  
Unesite URL ili zalepite HTML kod. Prikazuje sve schema.org tipove, bez Google-specifičnih pregleda.

---

### 5c. Proverite meta opis u Google pretrazi

**Korak 1.** Pretražite naziv studija ili ključnu reč u inkognito tabu.

**Korak 2.** Ispod plavog naslova vidite sivi tekst (meta opis ili odlomak iz sadržaja).

**Korak 3.** Da li odgovara opisu koji ste uneli u Yoast? Ako da — sve je u redu.

**Korak 4.** Ako Google prikazuje nešto drugo: Google ponekad sam bira bolji odlomak. To nije greška — to je normalno. Bitno je da je title tag tačan.

---

## DEO 6 — MESECNA AEO/GEO PROVERA (AI pretraživači)

AEO (Answer Engine Optimization) = da li vas AI alati preporučuju kada neko pita za kozmetički studio u Novom Sadu.

Ovu proveru radite jednom mesečno — traje oko 15 minuta.

---

### Koji alati, koji upiti

**Alat 1: ChatGPT** (chat.openai.com)

Upišite ova tri upita jedan po jedan i zapišite odgovor:

1. `Koji su najbolji kozmetički studiji u Novom Sadu?`
2. `Gde mogu da uradim HydraFacial u Novom Sadu?`
3. `Preporuči mi profesionalni salon za negu kože u Novom Sadu`

**Šta zapisujete:** Da li se "Sensi Skin" pojavljuje u odgovoru? Da ili ne. Ako da — koji put je pomenut i da li je adresa tačna?

---

**Alat 2: Perplexity** (perplexity.ai)

Upišite:

1. `Kozmetički studiji Novi Sad preporuke`
2. `HydraFacial tretman Novi Sad`
3. `Nataša Burka kozmetičar Novi Sad`

**Šta zapisujete:** Da li je Sensi Skin pomenut? Koji je izvor citiran (URL)? Da li je informacija tačna (adresa, opis)?

---

**Alat 3: Google AI Overviews**

Ovo se pojavljuje automatski u Google pretrazi iznad organskih rezultata (samo ponekad, ne uvek).

1. Pretražite u inkognito tabu: `kozmetički studio Novi Sad preporuka`
2. Pretražite: `hydrafacial novi sad gde`
3. Pretražite: `laserska epilacija novi sad`

**Šta zapisujete:** Da li se AI Overview pojavljuje (plava kutija na vrhu)? Da li pominje Sensi Skin?

---

### Tabela za AEO mesečni log

| Upit | Alat | Datum | Pomenuta Sensi Skin? | Tačna adresa? | Napomena |
|---|---|---|---|---|---|
| Kozmetički studiji Novi Sad | ChatGPT | _______ | Da/Ne | Da/Ne | |
| HydraFacial Novi Sad | ChatGPT | _______ | Da/Ne | Da/Ne | |
| Preporuka salon Novi Sad | ChatGPT | _______ | Da/Ne | Da/Ne | |
| Kozmetički studiji Novi Sad | Perplexity | _______ | Da/Ne | Da/Ne | |
| HydraFacial Novi Sad | Perplexity | _______ | Da/Ne | Da/Ne | |
| Nataša Burka kozmetičar | Perplexity | _______ | Da/Ne | Da/Ne | |
| Kozmetički studio Novi Sad | Google AI Overview | _______ | Da/Ne | Da/Ne | |

**Zašto ovo raditi?** AI alati kao ChatGPT i Perplexity koriste podatke iz direktorijuma, recenzija i web stranica da bi preporučili biznis. Svaki put kada popravite NAP ili dodate recenziju, poboljšavate šanse da vas AI pomene. Ovaj mesečni check pokazuje da li to funkcioniše.

> Napomena o brzini: AI modeli ažuriraju podatke sporije od Googlea. Tek posle 2–3 meseca od Phase B/C promena možete očekivati pomenute u ChatGPT-u. Perplexity je brži jer pretražuje web u realnom vremenu.

---

## DEO 7 — BRZA REFERENTNA LISTA (sve alatke na jednom mestu)

| Alatka | Adresa | Šta koristiti za |
|---|---|---|
| Google Search Console | search.google.com/search-console | Indeksiranje, greške, ključne reči |
| Rich Results Test | search.google.com/test/rich-results | Validacija schema markup-a |
| Schema Markup Validator | validator.schema.org | Detaljna schema validacija |
| Google Business Profile | business.google.com | Upravljanje profilom, insights |
| Google Maps | maps.google.com | Provera prikaza adrese i podataka |
| ChatGPT | chat.openai.com | AI brand mention check |
| Perplexity | perplexity.ai | AI brand mention check |
| Google pretraga (inkognito) | google.com | SERP snapshot, title provera |

---

## REZIME — Šta raditi i kada

| Period | Akcija | Alatka |
|---|---|---|
| DANAS (9. jun) | Snimiti baseline (Deo 0) | GSC + GBP + Google pretraga |
| Posle svake Phase C promene | Request Indexing za izmenjeni URL | GSC — URL Inspection |
| 7–14 dana posle Phase C | Proveriti da li je novi title indexiran | GSC — URL Inspection |
| Jednom mesečno | Popuniti tabelu praćenja (Deo 3) | GSC + GBP |
| Jednom mesečno | AI brand mention check (Deo 6) | ChatGPT + Perplexity |
| Svake 4 nedelje | Proveriti staru adresu u pretrazi (Deo 4a) | Google inkognito |
| Jednom mesečno | Validacija schema na key stranicama | Rich Results Test |

---

*Dokument izradio: Analytics agent — Sensi Skin SEO project, 9. jun 2026.*  
*Sledeće ažuriranje: kada vlasnik pošalje baseline snapshot — popuniti kolonu "Baseline (danas)" u tabeli u Delu 3.*
