# GSC Indeksiranje i Vidljivost — Kompletan Audit
**Sensi Skin Kozmetološki Centar — sensiskinstudio.com**
**Datum: 2026-07-06 | Izvor: Google Search Console (siteFullUser), 90–180 dana podataka**

---

## 0. Rezime (Executive Summary)

Sajt ima **48 zvanično deklarisanih URL-ova** u aktivnom sitemap-u (14 stranica + 34 blog posta), od kojih je **44 indeksirano (91.7%)** a **4 nisu indeksirana (8.3%)**. Sam sitemap je tehnički čist (55/55 URL-ova vraća 200, 0 grešaka, 0 upozorenja u GSC-u).

Najveći problem NIJE trenutni sitemap — najveći problem su **stari/napušteni URL-ovi van sitemap-a** koji i dalje generišu istoriju klikova u GSC-u, a tri od njih su **potvrđeno mrtvi (404) upravo sada**, uključujući URL koji je bio **DRUGI najklikovaniji URL na celom sajtu** (560 klikova u 6 meseci). Ovo je aktivan, merljiv gubitak saobraćaja koji traje.

**Ključne brojke:**
- Ukupno URL-ova sa podacima u GSC (page dimenzija, 01.01–05.07.2026): ~115 jedinstvenih URL-ova (uključuje sitemap stranice, WooCommerce shop/product/category, PDF-ove, autor arhive i **stare napuštene URL-ove**)
- Sitemap URL-ovi: 48 ukupno → 44 indeksirano / 4 nije indeksirano / 0 grešaka
- Van-sitemap URL-ovi provereni (13 kandidata sa istorijskim saobraćajem): **7 potvrđenih 404 grešaka**, 5 ispravnih 301 redirekcija (Google ih već prepoznaje i konsoliduje), 1 blank
- Kritični problemi pronađeni: **10** (detaljno ispod)
- Direktne akcije izvršene ovom sesijom: sitemap status proveren i POTVRĐEN ISPRAVNIM (nije bilo potrebno ponovo predati — vidi Odeljak 4)
- GSC API kvota: NIJE dostignuta (ukupno ~63 URL Inspection poziva ovom sesijom, well within 2000/dan limit)

---

## 1. Pun inventar stranica

### 1.1 Sitemap struktura (verifikovano uživo)
`https://sensiskinstudio.com/sitemap_index.xml` (Yoast SEO generisan, jedini sitemap registrovan u GSC-u):
- `post-sitemap.xml` → 34 blog posta
- `page-sitemap.xml` → 14 stranica (početna, servisne stranice, kontakt, cenovnik, proizvodi)
- `product-sitemap.xml` → 3 URL-a (proizvodi stranica + 2 WooCommerce proizvoda — vrlo mali broj u odnosu na broj proizvoda viđenih u GSC podacima, videti 3.5)
- `category-sitemap.xml` → 2 URL-a
- `product_cat-sitemap.xml`, `author-sitemap.xml` → nisu detaljno provereni ovom sesijom

`gsc_list_sitemaps` potvrđuje: `sitemap_index.xml` registrovan, poslednji put preuzet 2026-07-04, **0 grešaka, 0 upozorenja**, 55 web URL-ova prijavljeno (ukupno svih pod-sitemapa).

**NAPOMENA o "indexed": 0 polju** — GSC Sitemaps API je vratio `"indexed": "0"` za web i image tip. Ovo polje je poznato po nepouzdanosti u GSC API-ju (često prikazuje 0 čak i kada su URL-ovi stvarno indeksirani — što potvrđuje 44/48 pojedinačnih URL Inspection provera koje pokazuju "Submitted and indexed"). **Ne tretirati ovo kao stvarni signal problema** — pojedinačna URL inspekcija je pouzdaniji izvor istine.

### 1.2 KRITIČAN NALAZ — stari sitemap.xml i dalje živ
`https://sensiskinstudio.com/sitemap.xml` (BEZ "_index") **je i dalje dostupan uživo** i sadrži **21 URL iz 2018. godine**, generisan eksternim alatom (check-domains.com), sa `lastmod` datumima iz oktobra 2018. Ovo je isti "dual sitemap" problem identifikovan u GEO auditu od 2026-06-09 — **NIJE u potpunosti rešen**, samo delimično (novi sitemap_index.xml je ono što je registrovano u GSC-u, ali stari fajl nije uklonjen sa servera).

- NIJE trenutno registrovan u GSC Sitemaps izveštaju (samo sitemap_index.xml je registrovan) — pa Google ga verovatno ne koristi kao primarni izvor
- ALI je i dalje javno dostupan i može ga otkriti Bing, drugi search engine, ili neko ko ručno pokuša `/sitemap.xml`
- Rizik: konfuzija za botove, potencijalno starih/mrtvih URL-ova ponovo uvučenih u crawl red

### 1.3 GSC page-dimenzija vs. sitemap — najveće razlike
Top URL-ovi sa GSC podacima koji **NISU u trenutnom sitemap-u**, sortirano po klikovima (90–180 dana):

| URL | Klikovi | Impresije | Status (provereno) |
|---|---|---|---|
| /cenovnik-usluga-2/ | 560 | 2.832 | **404 — POTVRĐENO MRTAV** |
| /hydrafacial-tretman-lica/ | 215 | 3.508 | **404 — POTVRĐENO MRTAV** |
| /sensi-skin/ | 115 | 3.663 | **404 — POTVRĐENO MRTAV** |
| /cenovnik/ | 108 | 988 | 301 redirekcija → /cenovnik-kozmetickih-tretmana-novi-sad/ (ISPRAVNO) |
| /shop/ | 60 | 2.497 | WooCommerce shop arhiva (nije u sitemap-u, ali je legitimna CPT arhiva) |
| /shop-2/ | 36 | 1.102 | **404 — POTVRĐENO MRTAV**, i dalje linkovan interno sa /blog/ |
| /kontakt/ | 30 | 2.576 | 301 redirekcija → /kontakt-sensi-skin-novi-sad/ (ISPRAVNO) |
| /green-peel/ | 24 | 373 | **404 — POTVRĐENO MRTAV** |
| /hydrafacial-tretmani-lica/ | 7 | 103 | 301 redirekcija → /hydrafacial-tretmani-lica-novi-sad/ (ISPRAVNO) |
| /nega-tela/ | 12 | 342 | **404 — POTVRĐENO MRTAV** |
| /aura-reality/ | 4 | 103 | 301 redirekcija → /aura-reality-3d-dijagnostika-koze/ (ISPRAVNO) |
| /dermalux-led-terapija/ | 13 | 548 | 301 redirekcija → /dermalux-led-terapija-kao-resenje-problema/ (ISPRAVNO) |
| /tekstovi-iz-casopisa/ | 5 | 90 | **404 — POTVRĐENO MRTAV**, linkovan sa POČETNE STRANE |

**Zaključak**: 5 od ovih redirekcija RADE ISPRAVNO — Google ih je prepoznao (`coverageState: "Page with redirect"`, `googleCanonical` pokazuje na ispravnu novu stranicu). Ovo je dobra vest — konsolidacija je uspela za te URL-ove. Ali **7 URL-ova su i dalje potpuno mrtvi (404)**, i tri od njih nose ozbiljnu istorijsku (a možda i tekuću) SERP vidljivost.

---

## 2. Status indeksiranja po URL-u (svih 48 sitemap URL-ova + 13 van-sitemap kandidata)

### 2.1 Sitemap stranice (page-sitemap, 14/14 provereno)

| URL | Status | Poslednji crawl | Google canonical |
|---|---|---|---|
| / | Indeksirano | 2026-07-05 | self |
| /cenovnik-kozmetickih-tretmana-novi-sad/ | Indeksirano | 2026-07-05 | self |
| /strucni-saveti-za-negu-koze/ | **Discovered — nije indeksirano** | — | — |
| /moj-nalog-sensi-skin-studio/ | **Discovered — nije indeksirano** | — | — |
| /hydrafacial-tretmani-lica-novi-sad/ | Indeksirano | 2026-07-05 | self |
| /epilacija/ | Indeksirano | 2026-06-29 | self |
| /aura-reality-3d-dijagnostika-koze/ | Indeksirano | 2026-06-29 | self |
| /nega-lica/ | Indeksirano | 2026-06-21 | self |
| /mesojet-tretmani/ | Indeksirano | 2026-06-21 | self |
| /mesojet-rf/ | Indeksirano | 2026-06-11 | self |
| /dermalux/ | Indeksirano | 2026-06-21 | self |
| /kozmetoloski-centar-sensi-skin/ | Indeksirano | 2026-06-24 | self |
| /kontakt-sensi-skin-novi-sad/ | Indeksirano | 2026-06-30 | self |
| /kozmeticki-proizvodi-sensi-skin-studio/ | Indeksirano | 2026-07-05 | self |

### 2.2 Blog postovi (post-sitemap, 34/34 provereno)

Svi indeksirani OSIM:
- `/faktori-rasta-u-borbi-protiv-starenja-koze/` — **Discovered — nije indeksirano** (Google još nije crawlovao)
- `/pojava-osetljivosti-koze-tokom-zimskih-dana/` — **Crawled — nije indeksirano** (Google JESTE crawlovao 2026-02-04, ali odlučio da ne indeksira — ovo je signal kvaliteta sadržaja, ne tehnički problem)

Ostalih 32 blog posta: svi `Submitted and indexed`, poslednji crawl datumi u rasponu 2026-04-24 do 2026-07-05 (zdrav, redovan re-crawl).

### 2.3 Van-sitemap "duh" URL-ovi (13 provereno)

| URL | Nalaz |
|---|---|
| /sensi-skin/ | **404** |
| /cenovnik-usluga-2/ | **404** |
| /hydrafacial-tretman-lica/ | **404** |
| /shop-2/ | **404** (interno linkovan sa /blog/) |
| /green-peel/ | **404** |
| /nega-tela/ | **404** |
| /tekstovi-iz-casopisa/ | **404** (interno linkovan sa POČETNE) |
| /kontakt/ | 301 → /kontakt-sensi-skin-novi-sad/ (ispravno) |
| /cenovnik/ | 301 → /cenovnik-kozmetickih-tretmana-novi-sad/ (ispravno) |
| /hydrafacial-tretmani-lica/ | 301 → /hydrafacial-tretmani-lica-novi-sad/ (ispravno) |
| /dermalux-led-terapija/ | 301 → /dermalux-led-terapija-kao-resenje-problema/ (ispravno) |
| /aura-reality/ | 301 → /aura-reality-3d-dijagnostika-koze/ (ispravno) |

**Kvota napomena**: ukupno 63 URL Inspection poziva izvršeno ovom sesijom (48 sitemap + 13 van-sitemap + 2 dodatna). Nema signala ograničenja kvote — dnevni limit (obično ~2.000) nije ni približno dostignut.

---

## 3. Top 10 kritičnih problema (sortirano po očekivanom uticaju na vidljivost)

### #1 — TRI potvrđena 404 na URL-ovima sa najvećom istorijskom vidljivošću (KRITIČNO)
`/cenovnik-usluga-2/` (560 klikova/2.832 impresija u 6 meseci — **drugi najklikovaniji URL na celom sajtu, odmah iza početne strane**), `/hydrafacial-tretman-lica/` (215 klikova/3.508 impresija), `/sensi-skin/` (115 klikova/3.663 impresija). `gsc_traffic_drops` potvrđuje aktivan kolaps: /cenovnik-usluga-2/ je palo sa 551 klika (prethodnih 90 dana) na **1 klik** (poslednjih 90 dana) — pad od 99.8%. /hydrafacial-tretman-lica/ palo sa 197 na 6 klikova.
**Uticaj**: Google i dalje prikazuje ove URL-ove u SERP-u (ili ih je nedavno prestao prikazivati zbog 404), a korisnici koji kliknu sada dobijaju "stranica nije pronađena". Ovo je direktan, merljiv gubitak saobraćaja koji se dešava upravo sada.
**OWNER ACTION (ne mogu izvršiti — nema WordPress/FTP pristupa)**: Postaviti 301 redirekcije: `/cenovnik-usluga-2/` → `/cenovnik-kozmetickih-tretmana-novi-sad/`; `/hydrafacial-tretman-lica/` → `/hydrafacial-tretmani-lica-novi-sad/`; `/sensi-skin/` → `/kozmetoloski-centar-sensi-skin/`. Ovo su iste ciljne stranice na koje su već ispravno redirektovane slične varijante slugova (videti 2.3).

### #2 — Stari sitemap.xml (2018, 21 mrtav URL) i dalje živ na serveru
Ne samo da postoji istorija problema iz juna (delimično rešeno) — fajl je i dalje pristupačan uživo, generisan eksternim alatom, sa lastmod iz 2018. Nije registrovan u GSC-u (dobra vest), ali predstavlja rizik za druge crawlere.
**OWNER ACTION**: Ukloniti ili preusmeriti (410 ili 301 ka sitemap_index.xml) fajl `/sitemap.xml` na WordPress strani. Van mog dosega — nema FTP/WP pristupa.

### #3 — 4 dodatna potvrđena 404, uzrok ispravljen (CORRECTION 2026-07-06, posle objave izveštaja)
`/shop-2/`, `/tekstovi-iz-casopisa/`, `/green-peel/`, `/nega-tela/` — svi vraćaju 404. **Ispravka prethodnog nalaza**: direktan uvid u sirov HTML (`curl` na `/` i `/blog/`) pokazuje da `/shop-2/` i `/tekstovi-iz-casopisa/` NISU linkovani u stvarnom, renderovanom navigacionom meniju (i mobilni i desktop `<nav>` su potpuno čisti i koriste ispravne, žive URL-ove — "Sensi Skin"→`/kozmetoloski-centar-sensi-skin/`, "Tekstovi iz časopisa"→`/strucni-saveti-za-negu-koze/`, "Proizvodi"→`/kozmeticki-proizvodi-sensi-skin-studio/`). Mrtvi URL-ovi se pojavljuju ISKLJUČIVO u auto-generisanoj JSON-LD `SiteNavigationElement` schema oznaci (verovatno Blocksy tema), koja je zastarela/kеширана i ne odražava trenutno stanje menija. Nijedan posetilac ne nailazi na ove linkove klikom — problem je ograničen na strukturirane podatke koje Google čita, ne na korisničko iskustvo. Prioritet snižen sa "Visok" na "Srednji".
**OWNER ACTION (ažurirano)**: (a) Očistiti cache plugin (ako postoji — WP Rocket/LiteSpeed/W3TC i sl.) ili ponovo sačuvati glavni meni (Appearance → Menus → Save Menu) da se regeneriše schema; (b) Za `/green-peel/` i `/nega-tela/` (koji nisu pronađeni ni u meniju ni u JSON-LD — pravi napušteni URL-ovi bez ijedne poznate reference) odlučiti da li se usluge i dalje nude i, ako da, ili vratiti sadržaj ili trajno redirektovati ka najbližem zameniku.

### #4 — Kanibalizacija brend upita "sensi skin" (15+ konkurentnih URL-ova)
`gsc_cannibalization` pokazuje da se za upit "sensi skin" (6.907 impresija/90 dana) takmiče: `/`, `/nega-lica/`, `/kontakt/`, `/sensi-skin/`, `/shop-2/`, `/cenovnik/`, `/product/soft-gel-za-umivanje/`, `/cenovnik-kozmetickih-tretmana-novi-sad/`, `/epilacija/` i još 6+ URL-ova. Delimično je ovo prirodno za brend upit (home page dominira sa CTR 20%), ali podela signala kroz 15+ stranica slabi ukupnu snagu brenda u SERP-u.
**Fix povezan sa #1**: Kada se 404 URL-ovi preusmere (#1), broj konkurenata za ovaj upit pada sa ~15 na ~10-11 — direktna posledica popravke #1.

### #5 — Kanibalizacija "hydrafacial novi sad" i "hydrafacial tretman" kroz 3 URL varijante
Trenutni kanonski `/hydrafacial-tretmani-lica-novi-sad/` deli SERP prostor sa `/hydrafacial-tretman-lica/` (404 — vidi #1) i `/hydrafacial-tretmani-lica/` (ispravno redirektovan). Nakon popravke #1, ostaje samo jedan aktivan URL za ovaj klaster — čist ishod.

### #6 — 2 blog posta koje Google odbija da indeksira uprkos crawl-u
`/pojava-osetljivosti-koze-tokom-zimskih-dana/` — Google je crawlovao stranicu (2026-02-04) i **odlučio da je ne indeksira**. Ovo NIJE tehnički problem (nema noindex taga, nema robots blokade) — ovo je signal da Google ocenjuje sadržaj kao nedovoljno vredan/dupliran u odnosu na drugi sadržaj na sajtu (verovatno preklapanje sa "posledice-starenja-na-kozi" ili "prva-pomoc-kozi-u-hladnim-danima" — slične teme o zimskoj nezi kože).
**FLAG ZA VLASNIKA (odluka o sadržaju, ne akcija SEO agenta)**: Proceniti da li ovaj post treba proširiti/diferencirati od sličnih zimskih postova, ili ga spojiti/preusmeriti ka jačoj stranici o istoj temi.

### #7 — 2 sitemap stranice još uvek "Discovered — nije indeksirano" bez jasnog tehničkog uzroka
`/strucni-saveti-za-negu-koze/` (magazin sekcija — poznat kanibalizacijski rizik iz prethodnog audita, 2026-06-09 odluka je bila da se repozicionira kao "Sensi Skin u medijima") i `/moj-nalog-sensi-skin-studio/` (WooCommerce "moj nalog" — utility stranica bez SEO vrednosti).
**Preporuka**: `/moj-nalog-sensi-skin-studio/` bi trebalo **isključiti iz sitemap-a i staviti noindex** (WooCommerce account stranice nemaju šta da traže u organskom indeksu — ovo je samo trošenje crawl budžeta). `/strucni-saveti-za-negu-koze/` treba prvo dobiti diferenciran sadržaj (repozicioniranje iz odluke 2026-06-09) pre traženja indeksiranja — inače rizikuje da bude proglašen duplikatom `/saveti-za-negu-koze/`.

### #8 — CTR ispod očekivanog na više dobro rangiranih stranica (potencijal ~700+ dodatnih klikova/90 dana)
`gsc_ctr_opportunities` pokazuje najveće gepove: `/perutanje-koze/` (199 potencijalnih dodatnih klikova), `/kontakt/` (126 — ali ovo je duplikat URL, videti #1), `/sensi-skin/` (110 — isto duplikat), `/shop-2/` (85 — 404, videti #3), `/nega-lica/` (69), `/stetnost-solarijuma/` (63). Realan, adresibilan potencijal nakon isključivanja duplikata: **/perutanje-koze/, /nega-lica/, /stetnost-solarijuma/** — sve tri su čiste, indeksirane, legitimne stranice čiji title/meta zaslužuju rewrite.
**Napomena**: `/perutanje-koze/` dodatno pokazuje pad klikova kroz 3 uzastopna 30-dnevna perioda (40→32→19, pad od 52.5%) po `gsc_content_decay` — kombinacija CTR problema i opadanja treba prioritetnu pažnju.

### #9 — robots.txt ne deklariše Sitemap direktivu
`migration_robots_audit` potvrđuje: robots.txt postoji (200, 158 bajtova), blokira samo `/wp-admin/` i `/search` (ispravno), ali **ne sadrži `Sitemap:` liniju**. Google ovo ne treba (sitemap je već ručno registrovan u GSC-u), ali Bing i drugi crawleri (uključujući AI botove koji poštuju robots.txt konvencije) se oslanjaju na ovu deklaraciju za samostalno otkrivanje.
**OWNER ACTION (niska hitnost)**: Dodati `Sitemap: https://sensiskinstudio.com/sitemap_index.xml` u robots.txt.

### #10 — Opšti pad saobraćaja na ključnim stranicama (delom posledica #1–#5)
`gsc_traffic_drops` pokazuje: početna strana -147 klikova (-12.3% impresija), `/nega-lica/` -43 klika ("demand_decline" — realan pad interesovanja ili gubitak ranga), `/mesojet-tretmani/` -32 klika (CTR kolaps). Deo ovog pada je direktna posledica curenja saobraćaja kroz mrtve/dupli URL-ove (#1, #4, #5) — očekuje se delimičan oporavak nakon popravke redirekcija.

---

## 4. Šta je već urađeno ovom sesijom (direktne akcije)

- **Sitemap status proveren preko `gsc_list_sitemaps` i `migration_sitemap_validate`**: `sitemap_index.xml` je registrovan, zdrav (health: green), 55/55 URL-ova vraća 200, 0 grešaka/upozorenja u GSC-u, poslednji put preuzet 2026-07-04. **NIJE bilo potrebno ponovo predati sitemap** — trenutna registracija je ispravna i ažurna. (Uslov iz brifinga za korišćenje `gsc_submit_sitemap` — "ako je sitemap zastareo/nepotpun/dual-sitemap problem i dalje živ u GSC-u" — nije ispunjen: problem je fajl na serveru koji GSC ne koristi, ne loša GSC registracija.)
- Pun crawl svih 48 sitemap URL-ova + 13 van-sitemap "duh" URL-ova preko GSC URL Inspection API-ja (63 poziva ukupno, bez problema sa kvotom).
- Uživo verifikovano (WebFetch) da su `/cenovnik-usluga-2/`, `/sensi-skin/`, `/hydrafacial-tretman-lica/` trenutno 404 na produkciji — ovo NIJE samo GSC keširan podatak, potvrđeno je da su stvarno mrtvi upravo sada.
- Uživo verifikovano da stari `/sitemap.xml` (2018, 21 URL) i dalje postoji na serveru.
- Pokrenuti `gsc_cannibalization`, `gsc_traffic_drops`, `gsc_ctr_opportunities`, `gsc_content_decay`, `gsc_quick_wins`, `migration_robots_audit` za sistematsku dijagnostiku van jednog već poznatog slučaja kanibalizacije.

**Nijedna promena nije napravljena na sajtu ili u GSC podešavanjima osim čitanja podataka** (nije bilo potrebe za `gsc_submit_sitemap` ovom sesijom).

---

## 5. Čeka odobrenje vlasnika (OWNER ACTIONS — sa konkretnim predlogom akcije)

| # | Problem | Predložena akcija | Prioritet |
|---|---|---|---|
| 1 | `/cenovnik-usluga-2/` 404 | 301 → `/cenovnik-kozmetickih-tretmana-novi-sad/` | **Kritično — 48h** |
| 2 | `/hydrafacial-tretman-lica/` 404 | 301 → `/hydrafacial-tretmani-lica-novi-sad/` | **Kritično — 48h** |
| 3 | `/sensi-skin/` 404 | 301 → `/kozmetoloski-centar-sensi-skin/` | **Kritično — 48h** |
| 4 | Stari `/sitemap.xml` (2018) i dalje živ | Obrisati fajl ili 301/410 ka `/sitemap_index.xml` | Visok — ova nedelja |
| 5 | `/shop-2/` 404 — samo u zastareloj JSON-LD schema, ne u pravom meniju (ispravka 2026-07-06) | Očistiti cache plugin ili re-save glavni meni (Appearance → Menus) da se schema regeneriše | Srednji — ova nedelja |
| 6 | `/tekstovi-iz-casopisa/` 404 — isto, samo u zastareloj JSON-LD schema (ispravka 2026-07-06) | Ista akcija kao stavka 5 — jedna popravka rešava oba | Srednji — ova nedelja |
| 7 | `/green-peel/`, `/nega-tela/` 404 | Odlučiti: vratiti sadržaj ili trajno redirektovati ka najbližoj zameni | Srednji — ovaj mesec |
| 8 | `/pojava-osetljivosti-koze-tokom-zimskih-dana/` — Google odbija indeksiranje | Sadržajna revizija: proširiti/diferencirati od sličnih zimskih postova ili spojiti sa jačim postom | Srednji (odluka o sadržaju, ne SEO agent akcija) |
| 9 | `/strucni-saveti-za-negu-koze/` — nije indeksirano | Sačekati repozicioniranje sadržaja (odluka od 2026-06-09) pre traženja indeksiranja | Srednji |
| 10 | `/moj-nalog-sensi-skin-studio/` — nije indeksirano | Preporuka: isključiti iz sitemap-a + noindex (WooCommerce account stranica, nulta SEO vrednost) | Nizak |
| 11 | robots.txt bez Sitemap direktive | Dodati `Sitemap: https://sensiskinstudio.com/sitemap_index.xml` | Nizak |
| 12 | CTR rewrite: `/perutanje-koze/`, `/nega-lica/`, `/stetnost-solarijuma/` | Title/meta rewrite (SEO agent može isporučiti u sledećoj sesiji) | Srednji — quick win |

---

## 6. Prioritizovana lista za ručno "Request Indexing" (GSC UI, vlasnik izvršava)

Redosled po očekivanom uticaju:

1. **`/faktori-rasta-u-borbi-protiv-starenja-koze/`** — Discovered, nije još crawlovan. Realan, evergreen sadržaj o faktorima rasta protiv starenja kože (potvrđeno postojanje u Blog Crawl Correction 2026-06-11). Nema tehničku prepreku — samo čeka crawl red. **Zatražiti indeksiranje odmah.**
2. **`/strucni-saveti-za-negu-koze/`** — SAMO nakon što se sadržaj repozicionira (transkripcija PDF-ova, jasna diferencijacija od `/saveti-za-negu-koze/`) po odluci od 2026-06-09. Ako se zatraži indeksiranje pre toga, rizik je da Google odmah proglasi duplikat.
3. **`/pojava-osetljivosti-koze-tokom-zimskih-dana/`** — NE tražiti indeksiranje dok se sadržaj ne proširi/diferencira (Google ga je već pregledao i odbio).
4. **`/moj-nalog-sensi-skin-studio/`** — NE tražiti indeksiranje. Preporuka je suprotna akcija (noindex + izbaciti iz sitemap-a).

Nakon što se izvrše 301 redirekcije iz Odeljka 5 (stavke 1–3), preporučuje se da vlasnik u GSC UI ručno pokrene "Validate Fix" na URL Inspection alatu za `/cenovnik-usluga-2/`, `/hydrafacial-tretman-lica/` i `/sensi-skin/` kako bi Google brže prepoznao nove redirekcije.

---

## 7. GSC API kvota

Nije dostignuta. Ukupno izvršeno ~63 URL Inspection poziva (48 sitemap + 13 van-sitemap + 2 dodatna) tokom ove sesije, bez ijedne greške kvote. Standardni dnevni limit (obično ~2.000) ostaje uveliko neiskorišćen — nema potrebe za follow-up sesijom radi dovršavanja inspekcije.

---

## 8. Napomena o memorijskom kontekstu

Ovaj audit potvrđuje da je "GA4 tracking gap" iz prethodnog izveštaja (2026-06-24, GA4/GSC odnos 0.226) van dosega ovog zadatka (fokus je isključivo GSC indeksiranje) — proverite GA4 audit posebno ako je potrebno.

Poznata URL slug neusklađenost iz MEMORY.md (2026-06-24 audit) je sada **potpuno razjašnjena**:
- `/kontakt/` → potvrđeno: 301 redirekcija ka `/kontakt-sensi-skin-novi-sad/` (živi, ispravan slug je potonji)
- `/sensi-skin/` → potvrđeno: **404**, treba redirekciju ka `/kozmetoloski-centar-sensi-skin/` (nije redirekcija kao što je bio slučaj sa /kontakt/)
- `/hydrafacial-tretman-lica/` → potvrđeno: **404**, treba redirekciju ka `/hydrafacial-tretmani-lica-novi-sad/`
