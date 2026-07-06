# Predlog izmena Title/Meta — WordPress Yoast audit
**Sensi Skin Kozmetološki Centar — sensiskinstudio.com**
**Datum: 2026-07-06 | Izvor: podaci povučeni preko WordPress REST API (Yoast `yoast_head_json`) od strane orkestratora, 51 stavka (18 stranica + 33 posta) — ovaj dokument analizira 18 stranica + prioritetne blog postove**

---

## 0. Rezime — najvažniji nalaz pre svega ostalog

**Sistemski obrazac otkriven**: od 12 stranica koje IMAJU odobren unos u Master Keyword Table (2026-06-09), **6 stranica ima naslov koji suštinski odgovara odobrenoj verziji, ali meta opis je odsečen tačno na istom mestu — nedostaje poslednja rečenica sa pozivom na akciju i brojem telefona** ("Zakazite: 065/333-8-338."). Ovo nije 6 odvojenih problema — ovo je jedan te isti tehnički propust ponovljen 6 puta, verovatno iz istog uvoza/copy-paste koraka gde je meta opis odsečen pre CTA rečenice.

**Zaključak za vlasnika**: ovo je najveći "quick win" u čitavom auditu — 6 stranica se popravlja doslovnim dodavanjem već odobrene rečenice na kraj postojećeg meta opisa, bez ikakve nove odluke.

**Brojke (odgovor na tri pitanja iz zadatka)**:
- **6 stranica** — naslov već odgovara odobrenom (samo formatske razlike u crtici), meta samo treba vratiti odsečenu CTA rečenicu → GRUPA A
- **5 stranica** — naslov i/ili meta suštinski odudaraju od odobrene Master Table verzije, nikad nisu ispravno implementirani → GRUPA B (treba samo popiti/nalepiti već odobren tekst, ne nova SEO odluka)
- **2 stranice nisu uopšte u Master tabeli** (Cenovnik, Stručni saveti za negu kože) → GRUPA C, potrebna nova SEO odluka
- **2 utility stranice** (cart-2, checkout-2) → preporuka noindex, ista logika kao /moj-nalog/
- **Prioritetne 3 stranice iz GSC audita** (/perutanje-koze/, /nega-lica/, /stetnost-solarijuma/) obrađene posebno u Odeljku 2, jer imaju potvrđen CTR/content-decay problem

---

## 1. Metodologija cross-referenciranja

Za svaku od 14 stranica sa "pravim" sadržajem, uporedio sam:
1. Trenutni živi Yoast naslov/opis (dat u zadatku)
2. Odobrenu verziju iz MASTER KEYWORD TABLE (2026-06-09), ako postoji (redovi 1–14 u MEMORY.md)
3. Alternativni predlog iz SEO audita od 2026-06-24, ako postoji za istu stranicu (samo /nega-lica/, /kontakt/, /sensi-skin/, /epilacija/, /perutanje-koze/ imaju takav alternativni predlog)

---

## 2. PRIORITET — 3 stranice sa potvrđenim CTR/content-decay problemom (GSC audit 2026-07-06)

Iz `/outputs/sensiskin/seo/gsc-indexing-audit-2026-07-06.md`, odeljak #8: `gsc_ctr_opportunities` pokazuje realan, adresibilan potencijal na tri čiste, indeksirane stranice: **/perutanje-koze/** (199 potencijalnih dodatnih klikova/90 dana), **/nega-lica/** (69), **/stetnost-solarijuma/** (63). /perutanje-koze/ dodatno pokazuje `content_decay` — pad klikova 40→32→19 kroz tri uzastopna 30-dnevna perioda (-52.5%).

### 2.1 /perutanje-koze/ — VEĆ ODOBRENA KOPIJA ČEKA IMPLEMENTACIJU
Nije bila u pasted "page" podacima (ovo je blog post, ne stranica), ali odobrena kopija postoji od 2026-06-24 audita (Master Table red 14):

| | Trenutno (opšta napomena iz zadatka) | ODOBRENO (2026-06-24, red 14) |
|---|---|---|
| Naslov | 33 karaktera | **Perutanje kože — uzroci i tretmani \| Sensi Skin** (51c) |
| Meta | 102 karaktera | **Perutanje kože — uzroci, simptomi i kada potražiti pomoć stručnjaka. Saznajte šta radi Sensi Skin kad kućna nega više ne pomaže.** (150c) |

**Nemam tačan trenutni tekst** (samo dužinu) da potvrdim da li je odobrena verzija implementirana — 33/102 karaktera se NE poklapa sa odobrenih 51/150, što znači **odobrena kopija sigurno još nije live**. Ovo je najveći pojedinačni quick win u celom auditu: kopija je gotova od pre dve nedelje, spremna za copy-paste, i direktno adresira i CTR problem i content decay.
**Prioritet: KRITIČNO.**

### 2.2 /nega-lica/ — obrađeno detaljno u Grupi B (odeljak 3.2) — dve konkurentske odobrene verzije postoje, potrebna odluka vlasnika koju da implementiramo.

### 2.3 /stetnost-solarijuma/ — NEMA odobrenog keyword-a niti kopije
Nije u Master Table. Nemam tačan trenutni tekst (samo generalna napomena da postoji CTR gep od 63 klika). Ovo je genuinski nova SEO odluka, ne implementacija postojećeg.

**PREDLOG (novi, čeka odobrenje vlasnika, ne postojeća odluka)**:
- FOCUS KEYWORD: "šteta od solarijuma" (informativna namera — ovo je edukativni blog post, ne servisna stranica)
- SEO TITLE: „Šteta od solarijuma za kožu — šta treba da znate" (47c)
- META: „Šteta od solarijuma za kožu — uticaj UV zračenja na starenje kože i rizik od pigmentacije. Saznajte kada je izlaganje bezbedno." (135c)
- Napomena: ne mogu potvrditi koliziju sa postojećim keyword-ima bez uvida u trenutni tekst posta — preporučujem da se pre implementacije potvrdi da naslov posta već ne sadrži frazu koja bi kolidirala sa /perutanje-koze/ ili drugim postovima o zaštiti kože.
- **Prioritet: Visok** (potvrđen CTR gep), ali zahteva da vlasnik prvo potvrdi trenutni živi tekst pre finalne implementacije.

---

## 3. GRUPA A — naslov OK, meta odsečena (nedostaje CTA) — 6 stranica

Za ovih 6 stranica, JEDINA potrebna izmena je vraćanje odsečene CTA rečenice na kraj postojećeg meta opisa. Naslov ne treba dirati (razlike su samo crtica "-" vs em-crtica "—", što je kozmetičko i ne utiče na SEO).

| Stranica | Trenutna meta (živa) | Nedostaje na kraju | Kompletna odobrena meta (Master Table) |
|---|---|---|---|
| /dermalux/ | „...za akne, bore i obnovu kože." (111c) | „ Zakazite: 065/333-8-338." | „LED terapija za kožu lica Dermalux Tri-Wave — plava, crvena i infracrvena svetlost za akne, bore i obnovu kože. Zakazite: 065/333-8-338." (144c) |
| /mesojet-rf/ | „...za vidljivo zategnutiju kožu." (109c) | „ Zakazite: 065/333-8-338." | „Mesojet RF Novi Sad tretman kombinuje radiofrekvenciju i bezigalnu mezoterapiju za vidljivo zategnutiju kožu. Zakazite: 065/333-8-338." (141c) |
| / (početna) | „...Aura Reality 3D dijagnostika." (124c) | „ Zakazite: 065/333-8-338." | „Kozmetički centar Novi Sad — Sensi Skin, 20+ godina iskustva. HydraFacial, laserska epilacija, Aura Reality 3D dijagnostika. Zakazite: 065/333-8-338." (150c) |
| /aura-reality-3d-dijagnostika-koze/ | „...Jedina u regionu." (106c) | „ Zakazite u Sensi Skin: 065/333-8-338." | „Aura Reality dijagnostika kože — 3D analiza koja otkriva tačno stanje kože pre tretmana. Jedina u regionu. Zakazite u Sensi Skin: 065/333-8-338." (152c) |
| /mesojet-tretmani/ | „...pore i hidrataciju kože." (114c) | „ Zakazite: 065/333-8-338." | „Mesojet tretman bez igala — mlaz koji unosi aktivne supstance bez bola. Efikasan za bore, pore i hidrataciju kože. Zakazite: 065/333-8-338." (148c) |
| /kozmetoloski-centar-sensi-skin/ (O nama) | „...tretmane prilagođene vašoj koži." (117c) | „ Zakazite: 065/333-8-338." | „Kozmetički studio Novi Sad — Sensi Skin, 20+ godina iskustva. Nataša Burka i tim za tretmane prilagođene vašoj koži. Zakazite: 065/333-8-338." (145c) |

**Zašto je ovo prioritet**: nula rizika (kopija je već odobrena od pre mesec dana), efekat direktan na CTR (svih 6 opisa trenutno se prekidaju bez poziva na akciju, što u SERP-u izgleda nedovršeno), a vreme implementacije je ~2 minuta po stranici.

**Prioritet: Visok (implementacija ove nedelje).**

---

## 4. GRUPA B — naslov i/ili meta suštinski odudaraju od odobrene verzije — 5 stranica

Ovde ne treba nova SEO odluka — kopija je već odobrena, samo nikad nije ispravno postavljena u WordPress (ili je postavljena pa prepisana starijom verzijom).

### 4.1 /kontakt-sensi-skin-novi-sad/
| | Trenutno (živo) | ODOBRENO (Master Table red 10 = 2026-06-24 audit, identično) |
|---|---|---|
| Naslov | Kontakt - Sensi Skin (20c) | **Sensi Skin Novi Sad — kontakt i zakazivanje** (49c) |
| Meta | Kontakt Sensi Skin Novi Sad - zakažite tretman telefonom 065/333-8-338 ili nas posetite na Braće Popović 3, sprat 2. (116c) | **Sensi Skin Novi Sad — zakazite tretman telefonom 065/333-8-338 ili posetite nas na Braće Popović 3, sprat 2. Radno vreme i mapa u nastavku.** (152c) |

Naslov je potpuno drugačiji od odobrenog (fokus keyword "Sensi Skin Novi Sad kontakt" nije prisutan u trenutnom naslovu). GSC audit takođe pokazuje CTR gep od 126 dodatnih klikova na varijanti /kontakt/ (deo istog problema — videti napomenu o duplikatu u GSC auditu, odeljak #8). **Prioritet: Visok** — dve nezavisne odluke (06-09 i 06-24) se slažu oko iste kopije, nema konflikta, samo implementacija.

### 4.2 /nega-lica/ — KONFLIKT dve odobrene verzije, potrebna odluka vlasnika koju implementirati
| | Trenutno (živo) | Master Table red 3 (2026-06-09) | Alternativa (2026-06-24 audit) |
|---|---|---|---|
| Naslov | Nega lica - Sensi Skin (22c) | Nega lica tretmani — Sensi Skin kozmetički studio (53c) | Nega lica tretmani — Sensi Skin kozmetički studio (50c) |
| Meta | „...HydraFacial, mesojet, LED terapija." (113c) | „Nega lica tretmani u Sensi Skin — individualizovan pristup za svaki tip kože: HydraFacial, mesojet, LED terapija. Zakazite: 065/333-8-338." (148c) | „Nega lica tretmani u Sensi Skin — higijenski tretmani, HydraFacial i mesojet prilagođeni Vašem tipu kože. Zakazite konsultaciju: 065/333-8-338." (152c) |

Naslov je identičan u obe odobrene verzije (implementirati odmah, nema konflikta). **Meta ima suptilnu razliku u pozicioniranju**: 06-09 verzija naglašava "individualizovan pristup" (diferencijator protiv paketskih tretmana konkurencije), 06-24 verzija naglašava "higijenski tretmani" (praktičniji, manje diferencirajući ugao). S obzirom da je /nega-lica/ jedna od tri prioritetne CTR/demand-decline stranice iz 2026-07-06 audita, **preporučujem 06-24 verziju kao primarnu za implementaciju** jer je novija i pisana specifično sa CTR ciljem u vidu, ali ovo je poziciona odluka koju vlasnik treba da potvrdi pre implementacije — obe verzije su brend-glasovno ispravne.
**Prioritet: Visok** (naslov odmah implementirati; meta čeka odluku vlasnika o verziji).

### 4.3 /saveti-za-negu-koze/ (blog hub)
| | Trenutno (živo) | ODOBRENO (Master Table red 12) |
|---|---|---|
| Naslov | Saveti za negu kože - Sensi Skin (32c) | **Stručni saveti za negu kože — Sensi Skin, Novi Sad** (50c) |
| Meta | „...uz stručne savete." (129c) | **Saveti za negu kože koje zaista funkcionišu — čitajte blog Sensi Skin studija i naučite kako da brinete o koži uz stručne savete. Zakazite odmah.** (145c) |

Naslov ne sadrži odobreni fokus keyword. Meta je gotovo identična odobrenoj, samo nedostaje poslednja rečenica "Zakazite odmah." — isti obrazac odsecanja kao Grupa A, samo na stranici čiji naslov TAKOĐE nije implementiran, pa je svrstana ovde a ne u Grupu A.
**Prioritet: Srednji-Visok** (ova stranica je i hub za blog, veći dugoročni SEO uticaj).

### 4.4 /kozmeticki-proizvodi-sensi-skin-studio/
| | Trenutno (živo) | ODOBRENO (Master Table red 11) |
|---|---|---|
| Naslov | Kozmetički proizvodi - Sensi Skin (33c) | **Dermokozmetika Novi Sad — proizvodi Sensi Skin Studio** (53c) |
| Meta | „...Odabrano od strane stručnjaka." (115c) | **Dermokozmetika Novi Sad dostupna u Sensi Skin studiju — profesionalni proizvodi za negu kože odabrani od strane stručnjaka. Posetite nas ili zakazite.** (150c) |

Odobreni fokus keyword "dermokozmetika Novi Sad" (namerno biran nad generičkim "kozmetički proizvodi" — videti obrazloženje u MEMORY.md od 2026-06-08: cilja informisane kupce spremne za kupovinu/upit) **potpuno nedostaje** u trenutnom, live naslovu i meta opisu. Ovo je najčistiji primer stranice gde odobrena strateška odluka jednostavno nije nikad implementirana.
**Prioritet: Visok.**

### 4.5 /epilacija/
| | Trenutno (živo) | ODOBRENO (Master Table red 2) |
|---|---|---|
| Naslov | Laserska epilacija Novi Sad - Sensi Skin (40c) | Laserska epilacija Novi Sad — Sensi Skin studio (51c) |
| Meta | Trajna Laserska epilacija u Novom Sadu. Bezbedna metoda za sve tipove kože i dlake. Bez bola, bez uraslih dlaka. Sensi Skin (123c) | **Laserska epilacija Novi Sad — profesionalna oprema, tretmani po tipu kože, dugotrajni rezultati. Sensi Skin. Zakazite: 065/333-8-338.** (141c) |

Naslov sadrži fokus keyword ali nedostaje "studio" i CTA nije prisutan nigde u meta opisu — ovo NIJE isti obrazac odsecanja kao Grupa A (tekst je potpuno drugačije formulisan, ne samo skraćen), što znači da je ovo starija verzija kopije koja nikad nije zamenjena odobrenom. Nema poziva na akciju niti telefona u trenutnoj meta.
**Prioritet: Visok** (nedostatak CTA + telefona je direktan CTR gubitak na transakcionoj stranici).

---

## 5. GRUPA C — stranice BEZ odobrenog unosa u Master tabeli — potrebna nova odluka

### 5.1 /cenovnik-kozmetickih-tretmana-novi-sad/
Ova stranica nikad nije dobila zvaničnu keyword/title/meta odluku u Master Table, uprkos tome što je **ciljna stranica za 301 redirekciju najveće istorijske 404 greške na sajtu** (/cenovnik-usluga-2/, 560 klikova/90 dana po GSC auditu 2026-07-06) — ovo je jedna od najvažnijih stranica na sajtu i zaslužuje formalnu odluku, ne samo da ostane bez nje.

Trenutno: Naslov "Cenovnik Tretmana i Usluga — Sensi Skin Studio" (46c) | Meta "Cenovnik tretmana i usluga Sensi Skin kozmetološkog centra u Novom Sadu. HydraFacial, epilacija, nega lica, Ballancer Pro i više." (128c)

Naslov i meta su solidni i brend-glasovno ispravni, ali koriste reč "kozmetološkog" umesto odobrenog "kozmetički" (odluka od 2026-06-09: viši search volume za "kozmetički"). Meta pominje Ballancer Pro iako ta usluga po MEMORY.md nema svoju stranicu (samo H2 na početnoj) — ovo je prihvatljivo JER se ovde radi o cenovniku gde se pominju svi tretmani, ne o zasebnoj promociji stranice koja ne postoji.

**PREDLOG (novi, čeka odobrenje)**:
- FOCUS KEYWORD: "cenovnik tretmana Novi Sad"
- SEO TITLE: „Cenovnik tretmana i usluga Novi Sad — Sensi Skin" (48c)
- META: „Cenovnik tretmana i usluga Sensi Skin kozmetičkog centra u Novom Sadu. HydraFacial, epilacija, nega lica i više. Zakazite: 065/333-8-338." (150c)
- Razlika od trenutnog: "kozmetološkog" → "kozmetičkog" (usklađeno sa odlukom od 2026-06-09), dodata CTA rečenica sa telefonom (trenutno nedostaje na transakcionoj stranici koja direktno prima saobraćaj sa redirekcije).
- **Prioritet: Visok** — ovo popunjava rupu u Master tabeli za stranicu koja prima najveći redirect saobraćaj na sajtu.

### 5.2 /strucni-saveti-za-negu-koze/ — BLOKIRANO, ne raditi kopiju sada
Trenutno: Naslov "Stručni saveti za negu kože — Sensi Skin Studio" (47c) | Meta „...blog Sensi Skin studija i naučite kako da brinete o koži uz stručne savete." (137c)

Po odluci od 2026-06-09 (Confirmed strategic decisions), ova stranica ("magazin" sekcija) treba da bude **repozicionirana kao "Sensi Skin u medijima / Iz štampe"** kako bi se rešio kanibalizacijski rizik sa /saveti-za-negu-koze/ (koje imaju gotovo identičan trenutni naslov i temu). GSC audit 2026-07-06 takođe potvrđuje da ova stranica NIJE indeksirana ("Discovered — nije indeksirano") i da NE treba tražiti indeksiranje pre nego što se sadržaj diferencira.

**Preporuka**: NE pisati novu title/meta kopiju sada — bilo koja optimizacija pre repozicioniranja sadržaja bi se bacila kad se stranica preradi. Prvo: sadržajna odluka (transkripcija PDF-ova, jasno razdvajanje od bloga), ZATIM nova SEO kopija.
**Prioritet: Nizak (blokirano sadržajnom odlukom, ne SEO odlukom).**

---

## 6. Utility stranice — cart-2, checkout-2

**Preporuka: NOINDEX + isključiti iz sitemap-a**, ista logika kao za `/moj-nalog-sensi-skin-studio/` iz GSC audita od 2026-07-06 (stavka #10 u toj tabeli).

Razlozi:
1. Obe stranice su WooCommerce funkcionalne stranice bez ijedne rečenice originalnog sadržaja — nemaju šta da traže u organskom indeksu.
2. `checkout-2` posebno: WooCommerce checkout stranice često nose URL parametre vezane za korisničku sesiju/porudžbinu — indeksiranje takve stranice je i privatnosni rizik, ne samo SEO trošenje crawl budžeta.
3. Nijedna od njih nema meta opis — Yoast trenutno ne generiše čak ni fallback tekst, što znači da već sada, ako se slučajno indeksiraju, Google prikazuje automatski generisan/prazan snippet.
4. Ulaganje u title/meta kopiju za ove stranice ne donosi merljivu SEO vrednost — nijedan korisnik ne kuca "cart Sensi Skin" u Google.

**Akcija (vlasnik/WordPress)**: Yoast → Cart/Checkout stranica → SEO tab → Advanced → "Allow search engines to show this Page in search results?" → **No**. Zatim proveriti da li su ove dve stranice već isključene iz `page-sitemap.xml` (WooCommerce ih obično automatski isključuje, ali vredi potvrditi).
**Prioritet: Nizak** (nema aktivnog gubitka, samo higijena — uraditi kad se stigne).

---

## 7. Draft stranica — politika privatnosti

`/polotika-pritavnosti-sensi-skin-studio/` (ID 3) je u **draft** statusu, nije objavljena, nije u Master Table, nije indeksirana. Naslov (38c) i meta (135c) su solidni i brend-glasovno ispravni ako se ikad objavi.
**Preporuka**: ne raditi ništa na ovoj stranici dok se ne donese odluka o objavljivanju. Ako se objavi, trenutna kopija je već dovoljno dobra — ne treba prepravku.
**Prioritet: Nije primenjivo (van fokusa dok je draft).**

---

## 8. Nedostatak alt teksta na slikama — zaseban, manje-hitan ali stvaran problem

Nemam pristup imenima/sadržaju slika iz ovih podataka, pa ne mogu predložiti tačan alt tekst — ali evo prioritetne liste po broju slika BEZ alt teksta (najveći problem prvi):

| Rang | Stranica | Slike bez alt teksta |
|---|---|---|
| 1 | / (početna) | **14** (od 5 image widget-a) |
| 2 | /kozmetoloski-centar-sensi-skin/ (O nama) | **11** (od 8 image widget-a) |
| 3 | /hydrafacial-tretmani-lica-novi-sad/ | **9** (od 3 image widget-a) |
| 3 | /aura-reality-3d-dijagnostika-koze/ | **9** (od 3 image widget-a) |
| 5 | /dermalux/ | 7 (od 3) |
| 5 | /mesojet-rf/ | 7 (od 3) |
| 7 | /epilacija/ | 6 (od 1) |
| 7 | /nega-lica/ | 6 (od 1) |
| 7 | /mesojet-tretmani/ | 6 (od 1) |
| 10 | /strucni-saveti-za-negu-koze/ | 5 (od 3) |
| 11 | /cenovnik-kozmetickih-tretmana-novi-sad/ | 4 (od 0 image widget-a — verovatno slike direktno u sadržaju) |
| 12 | /kontakt-sensi-skin-novi-sad/ | 3 (od 0 image widget-a) |

**Zašto je ovo bitno ali ne hitno**: alt tekst je faktor pristupačnosti i sekundaran ranking signal za Google Images, ne primarni ranking faktor za tekstualnu pretragu. Ali na stranicama sa 9-14 slika bez alt teksta (početna, O nama, HydraFacial, Aura Reality), ovo predstavlja realan propušten prostor za dodatne, dugorepe keyword prilike (npr. alt="HydraFacial tretman lica u Sensi Skin studiju Novi Sad" na relevantnoj slici).
**Sledeći korak**: potreban je uvid u stvarne fajlove/kontekst slika da bi se napisao smislen alt tekst — predlažem da vlasnik ili copywriter agent dostavi listu slika po stranici (screenshot ili URL), pa SEO agent napravi tabelu alt-tekstova u sledećoj sesiji.
**Prioritet: Srednji** (visok potencijalni uticaj na 4 najveće stranice, ali zahteva dodatni input pre nego što se može izvršiti).

---

## 9. Kompletna prioritizovana tabela (za odobrenje vlasnika)

| # | URL | Trenutni title/desc (skraćeno) | Predloženi title/desc | Razlog | Prioritet |
|---|---|---|---|---|---|
| 1 | /perutanje-koze/ | 33c / 102c | Već odobreno 06-24 (51c/150c) — videti 2.1 | Implementacija postojeće odluke, CTR+decay potvrđen | **Kritično** |
| 2 | /dermalux/ | meta odsečena na 111c | Dodati „ Zakazite: 065/333-8-338." → 144c | Grupa A — restauracija odobrene kopije | Visok |
| 3 | /mesojet-rf/ | meta odsečena na 109c | Dodati „ Zakazite: 065/333-8-338." → 141c | Grupa A | Visok |
| 4 | / (početna) | meta odsečena na 124c | Dodati „ Zakazite: 065/333-8-338." → 150c | Grupa A | Visok |
| 5 | /aura-reality-3d-dijagnostika-koze/ | meta odsečena na 106c | Dodati „ Zakazite u Sensi Skin: 065/333-8-338." → 152c | Grupa A | Visok |
| 6 | /mesojet-tretmani/ | meta odsečena na 114c | Dodati „ Zakazite: 065/333-8-338." → 148c | Grupa A | Visok |
| 7 | /kozmetoloski-centar-sensi-skin/ | meta odsečena na 117c | Dodati „ Zakazite: 065/333-8-338." → 145c | Grupa A | Visok |
| 8 | /kontakt-sensi-skin-novi-sad/ | 20c / 116c | 49c / 152c (videti 4.1) | Naslov nikad implementiran | Visok |
| 9 | /nega-lica/ | 22c / 113c | 50-53c / 148-152c — DVE verzije, treba odluka vlasnika (videti 4.2) | CTR prioritet + konflikt verzija | Visok |
| 10 | /saveti-za-negu-koze/ | 32c / 129c | 50c / 145c (videti 4.3) | Naslov nikad implementiran, meta odsečena | Srednji-Visok |
| 11 | /kozmeticki-proizvodi-sensi-skin-studio/ | 33c / 115c | 53c / 150c (videti 4.4) | Fokus keyword potpuno odsutan | Visok |
| 12 | /epilacija/ | 40c / 123c | 51c / 141c (videti 4.5) | Meta bez CTA/telefona | Visok |
| 13 | /cenovnik-kozmetickih-tretmana-novi-sad/ | 46c / 128c | 48c / 150c (videti 5.1, NOVO) | Nema formalnu odluku, prima najveći redirect saobraćaj | Visok |
| 14 | /stetnost-solarijuma/ | nepoznato tačno | Predlog u 2.3 (NOVO, čeka verifikaciju živog teksta) | CTR gep 63 klika | Visok |
| 15 | cart-2, checkout-2 | bez meta | Noindex + isključiti iz sitemapa | Utility stranice, nula SEO vrednosti | Nizak |
| 16 | /strucni-saveti-za-negu-koze/ | 47c / 137c | Ne dirati — čeka repozicioniranje sadržaja | Blokirano sadržajnom odlukom od 06-09 | Nizak |
| 17 | /polotika-pritavnosti.../  | draft | Ne dirati | Nije objavljena | N/A |
| 18 | Alt tekst (12 stranica) | 4-14 slika bez alt teksta po stranici | Čeka listu slika/konteksta | Sekundaran ranking faktor, realan propušten prostor | Srednji |

---

## 10. Napomena o metodologiji dužine karaktera

Zadatak je ispravno primetio da svaka od 51 stavke tehnički "pada van" strogog 50-60/150-160 opsega. Ovaj izveštaj namerno NE tretira svaki takav slučaj kao problem — samo tamo gde: (a) postoji odobrena, duža verzija koja nikad nije implementirana, ili (b) trenutna kopija je generička/slaba i postoji realan prostor za poboljšanje bez povrede brend glasa (bez superlativa, bez pretpostavki o ceni, tačan format telefona 065/333-8-338 za sajt/blog kontekst). Stranice čija trenutna meta ima 128-137 karaktera (npr. Cenovnik, Stručni saveti) NISU tretirane kao hitne samo zbog dužine — dužina sama po sebi nije ranking faktor (potvrđeno u MEMORY.md, odluka od 2026-06-09).

---

*Sve izmene u ovom dokumentu čekaju odobrenje vlasnika pre primene preko WordPress API-ja. Nijedna izmena nije napravljena na sajtu tokom ove analize (SEO agent nije imao API/Bash pristup ovom sesijom).*
