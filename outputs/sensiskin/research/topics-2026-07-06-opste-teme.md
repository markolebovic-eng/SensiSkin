# SensiSkin — Predlog opštih tema za blog (dopunsko pokretanje, širi filter relevantnosti)

**Datum**: 2026-07-06
**Agent**: research
**Tip pokretanja**: Dopunski batch — širi filter relevantnosti ("relevantno ciljanoj publici", ne "da li prodajemo ovu uslugu")
**Kredit disciplina**: Firecrawl CLI ("firecrawl search"/"firecrawl scrape" komanda) NIJE bio dostupan u ovoj sesiji (`command not found` u Bash-u; jedini dostupan ekvivalent bio je `npx firecrawl-mcp`, koji pokreće MCP server, ne CLI koji vraća rezultate direktno u Bash). Umesto toga, globalno istraživanje urađeno je isključivo preko **WebSearch alata** (9 upita, 0 firecrawl kredita potrošeno). Ovo je odstupanje od standardnog toka — vidi napomenu ispod.

---

## Napomena o ovom pokretanju (VAŽNO)

1. **Firecrawl CLI nedostupan.** Pokušaj `firecrawl --status` i `firecrawl search/scrape` vratio je "command not found". Provera `npx firecrawl-mcp` je instalirala MCP server bez API ključa (keyless/rate-limited mod), ali to je MCP server namenjen za trajnu konekciju, ne ad-hoc CLI poziv iz Bash-a — nije korišćen u ovom pokretanju iz razloga vremenske i tehničke izvodivosti. **Sledeće pokretanje treba proveriti da li je firecrawl CLI ponovo dostupan** pre nego što se pokuša lokalni tok (map/scrape konkurenata).
2. **Lokalni tok (Korak 1) je ovog puta izostao u potpunosti** — ne samo zbog neverifikovanih URL-ova (kao 2026-07-05), nego i zbog nedostupnosti alata za scrape. Kada firecrawl bude dostupan i URL-ovi u `competitors.md` budu potvrđeni, treba uraditi pravi scrape konkurentskih blogova pre sledeće runde.
3. **Filter relevantnosti u ovom pokretanju je NAMERNO širi** od standardnog toka: teme se ne filtriraju kroz "da li SensiSkin prodaje ovaj tretman", nego kroz "da li je tema relevantna ciljanoj publici SensiSkin-a (žene/muškarci zainteresovani za negu kože i lepotu), bez obzira na konkretnu uslugu". Ovo je eksplicitan zahtev za ovo pokretanje, ne trajna promena standardnog toka.
4. **Otkriven rizik preklapanja sa POSTOJEĆIM (živim) blog sadržajem sajta** — jedan WebSearch rezultat (upit o kozmetologu vs. dermatologu) vratio je stranicu sa samog sensiskinstudio.com ("Dermatolog ili estetičar – kome i kada se obratiti?"). Ovo potvrđuje da sajt već ima post na tu temu — **tema NIJE predložena** u listi ispod zbog direktnog preklapanja. Dodatno, iz MEMORY.md (Blog Crawl Correction, 2026-06-11) poznato je da sajt već ima žive postove o: serumu, hemijskim pilinzima, melazmi, rozacei, vrstama akni, menopauzi, predelu oko očiju, štetnosti solarijuma, **tipovima kože**, dnevnoj rutini, alopeciji. Teme koje bi direktno duplirale ove (npr. "kako prepoznati svoj tip kože") su **isključene** iz liste ispod iz istog razloga.

---

## 9 predloženih tema (opšte/evergreen, širi filter)

### 1. Pravilan redosled nanošenja proizvoda za negu kože (jutarnja i večernja rutina)
- **Keyword**: redosled nanošenja proizvoda za negu kože
- **Izvor**: Globalni trend + lokalno interesovanje
- **Obrazloženje**: Ovo je opšteznana, evergreen tema koju traži svako ko koristi više od jednog proizvoda za negu — nezavisno od toga da li je ikada bio na profesionalnom tretmanu. Srpski portali (xenia.rs, dnevno.rs, idjtv.nova.rs, zenskimagazin.rs, wanted.mondo.rs) redovno objavljuju varijacije ove teme jer generiše konstantan pretraživački interes ("koja krema ide prva"). Tema NIJE vezana ni za jednu specifičnu SensiSkin uslugu — relevantna je svakome ko uopšte koristi kozmetiku. **Oprez**: postojeći live blog post sajta o "dnevnoj rutini" (pomenut u MEMORY.md, Blog Crawl Correction 2026-06-11) možda već delimično pokriva ovo — pre pisanja proveriti tačan sadržaj tog posta da se izbegne dupliranje; ako taj post pokriva SAMO korake rutine (čišćenje/tonik/krema) bez fokusa na redosled prema teksturi/molekulskoj težini proizvoda, ovaj ugao je dovoljno različit.

### 2. Skincare mitovi razotkriveni — šta je tačno, a šta ne
- **Keyword**: mitovi o nezi kože
- **Izvor**: Globalni trend
- **Obrazloženje**: Dermatološki izvori (Harvard Health, US Dermatology Partners, DermGroup) u 2026. aktivno obaraju rasprostranjene mitove: "masna koža ne treba kremu", "vruća voda otvara pore", "viši SPF je uvek bolji", "prekomerna eksfolijacija je dobra". Ovo je klasična, širokoprivlačna edukativna tema koja ne zahteva da čitalac ikada poseti kozmetološki centar — cilj je edukacija šire publike, ne prodaja tretmana, pa prolazi širi filter relevantnosti ovog pokretanja. Format (mit → objašnjenje → tačna praksa) prirodno generiše deljenje na društvenim mrežama.

### 3. San, stres i koža — nevidljivi uzročnici lošeg stanja kože
- **Keyword**: uticaj stresa na kožu
- **Izvor**: Globalni trend + lokalni izvor
- **Obrazloženje**: Srpski portali (krugzdravlja.rs — psihodermatologija, lepotaizdravlje.rs — inflammaging) i međunarodni dermatolozi sve više pišu o kortizolu, hroničnom stresu i nedostatku sna kao direktnim uzročnicima upale, razgradnje kolagena i pojačane osetljivosti kože. Ovo je lifestyle tema koja ne pominje nijedan tretman — relevantna je svakome ko ima kožu, ne samo klijentima kozmetoloških centara, što je tačno filter koji ovo pokretanje traži.

### 4. Ishrana i koža — šta antiinflamatorna ishrana zaista menja
- **Keyword**: uticaj ishrane na kožu
- **Izvor**: Globalni trend + lokalni izvor
- **Obrazloženje**: minutzamene.com i drkozarevcosmedics.com (2026) povezuju ishranu bogatu antioksidansima, omega-3 masnim kiselinama i smanjenim unosom šećera/ultraprerađene hrane sa vidljivim poboljšanjem stanja kože, posebno kod akni kod odraslih. Ovo je opšta, nutritivno-lifestyle tema bez ijedne reference na profesionalni tretman — čisto edukativna i široko relevantna, van tipičnog "prodajnog" filtera.

### 5. Skin cycling 2026 — zašto se koncept promenio i kako da ga prilagodite svojoj koži
- **Keyword**: skin cycling rutina
- **Izvor**: Globalni trend (jasno strujanje u medijima 2026)
- **Obrazloženje**: Prema Vine Vera, ISDIN i Beauty Independent (2026), "skin cycling" trend (TikTok koncept iz ranijih godina) se u 2026. promenio ka personalizovanom, manje agresivnom pristupu (naizmenično korišćenje aktivnih sastojaka i "recovery" noći prilagođenih tipu kože). Tema je opšte poznata iz medija (masovno pokrivena na Instagramu/TikToku), ne zahteva prethodno poznavanje SensiSkin usluga — čitalac je može primeniti isključivo kućnom rutinom. Razlikuje se od već predloženih tema iz 2026-07-05 (personalizacija tretmana, retinol/vitamin C formule) jer se fokusira na redosled/raspored kućne rutine kroz nedelju, ne na profesionalne tretmane ili sastojke same po sebi.

### 6. Kako čitati deklaraciju (INCI listu) kozmetičkog proizvoda
- **Keyword**: kako čitati deklaraciju kozmetike
- **Izvor**: Globalni/regionalni trend (EU regulativa + rastuće potrošačko interesovanje)
- **Obrazloženje**: INCI standard i EU Uredba 1223/2009 regulišu redosled navođenja sastojaka (opadajući po masenom udelu), a potrošači sve više traže vodiče kako da sami protumače etiketu pre kupovine (izvori: meavia-mh.hr, slowliving.hr). Ova tema je čisto potrošačko-edukativna — pomaže bilo kome ko kupuje bilo koji kozmetički proizvod, u bilo kojoj prodavnici, ne samo klijentima SensiSkin-a. Indirektno gradi autoritet brenda kao stručnog izvora bez ijednog pominjanja konkretnog tretmana.

### 7. Sezonska promena rutine nege kože — šta menjate leti, a šta zimi
- **Keyword**: sezonska nega kože leto zima
- **Izvor**: Globalni/regionalni trend
- **Obrazloženje**: buro247.rs i lepotaizdravlje.rs (2026) opisuju kako se rutina mora prilagoditi promeni klime (lakše teksture i blaža eksfolijacija leti, fokus na barijeru i hidrataciju zimi). Ovo je evergreen, sezonski recikliran topik koji privlači širu publiku van postojećih klijenata — svako menja svoju rutinu sezonski, bez obzira da li koristi profesionalne tretmane. Distinktivno od postojeće live teme "perutanje kože" (koja je specifičan simptom/problem) — ovde je ugao preventivno-rutinski, celogodišnji pregled navika.

### 8. Da li kolagen suplementi zaista deluju na kožu
- **Keyword**: kolagen suplementi efekat na kožu
- **Izvor**: Globalni trend (aktuelna potrošačka tema, veliki broj novih studija 2026)
- **Obrazloženje**: Prema pregledu 113 kliničkih ispitivanja (izvor: zdravlje.kurir.rs, 2026), oralni kolagen suplementi pokazuju umerene, ali nekonzistentne dokaze poboljšanja hidratacije i elastičnosti kože, uz efekat vidljiv tek posle 8-12 nedelja redovne upotrebe. Ovo je masovno pretraživana potrošačka tema (suplementi se prodaju u apotekama i online, van konteksta kozmetoloških usluga) — čitalac ne mora nikada čuti za SensiSkin da bi mu ova tema bila korisna. Namerno se ne povezuje direktno sa Mesojet RF (koji stimuliše prirodni kolagen) da bi tema ostala objektivna/edukativna, a ne prodajna — eventualna veza sa uslugom može se pomenuti u zaključku teksta, ne kao glavni ugao.

### 9. Prirodna vs. sintetička kozmetika — da li "prirodno" znači bezbednije
- **Keyword**: prirodna kozmetika bezbednost mit
- **Izvor**: Globalni trend (dugotrajna, ali stalno aktuelna potrošačka debata)
- **Obrazloženje**: Ovo je jedna od najčešćih zabluda u industriji nege kože — pretpostavka da je "prirodan" sastojak automatski bezbedniji ili delotvorniji od sintetičkog, dok dermatološka struka konstantno naglašava da je bezbednost pitanje koncentracije i formulacije, ne porekla sastojka. Tema je masovno relevantna svakom potrošaču kozmetike (ne samo klijentima SensiSkin-a) i ne zahteva prethodno poznavanje bilo kog konkretnog tretmana ili brenda — čisto potrošačko-edukativna, razlikuje se od teme #6 (koja uči KAKO čitati listu) fokusom na ČESTU ZABLUDU o poreklu sastojka.

---

## Napomene / odstupanja od standardnog toka

1. **Firecrawl CLI nije bio dostupan** u ovoj sesiji — sve globalno istraživanje urađeno je preko WebSearch alata (9 upita), 0 firecrawl kredita potrošeno. Kredit bilans firecrawl naloga ostaje isti kao na kraju prethodnog pokretanja (2026-07-05: 997 kredita) — nije proveravan ovog puta jer CLI nije bio dostupan.
2. **Lokalni tok (konkurencija) potpuno izostao** — ni zbog neverifikovanih URL-ova (isti razlog kao 2026-07-05), ni zbog nedostupnosti alata za scrape. Ne postoji "konkurentska praznina" analiza za ovaj set tema — obrazloženja se oslanjaju isključivo na globalnu/regionalnu medijsku pokrivenost i evergreen relevantnost.
3. **Filter relevantnosti u ovom pokretanju namerno širi** od standardnog — teme NISU filtrirane kroz "da li SensiSkin prodaje ovu uslugu", nego kroz "da li je relevantno ciljanoj publici SensiSkin-a". Ovo je eksplicitan zahtev za ovo dopunsko pokretanje, ne promena stalnog toka — sledeće redovno (nedeljno) pokretanje treba da se vrati na standardni filter osim ako se ne zatraži drugačije.
4. **Jedna tema isključena zbog direktnog preklapanja sa živim sadržajem sajta**: "kozmetolog vs. dermatolog — kome se obratiti" — WebSearch je otkrio da sensiskinstudio.com već ima objavljen post tačno na tu temu.
5. **Jedna tema isključena zbog preklapanja sa poznatim postojećim postom iz MEMORY.md**: "kako prepoznati svoj tip kože" — sajt već ima live post "tipovi kože" (pomenut u Blog Crawl Correction, 2026-06-11).
6. Nijedna od 9 tema ne duplira teme iz `topics-2026-07-05.md` (videti Rerun Inputs ispod za punu listu prethodno predloženih tema) niti tri postojeća DRAFT fajla u `/outputs/sensiskin/blog/` (skin-longevity, led-terapija, analiza-koze).

---

## Rerun Inputs (za buduće ponavljanje)

**Alat korišćen ovog puta**: WebSearch (firecrawl CLI nedostupan — proveriti dostupnost pre sledećeg pokretanja).

**Konkurenti korišćeni (lokalni tok)**: Nijedan — lokalni tok izostao ovog puta (videti napomene 1-2 iznad).

**WebSearch upiti korišćeni (9)**:
1. "redosled nanošenja proizvoda za negu kože 2026 vodič"
2. "skincare myths debunked 2026 dermatologist"
3. "kako prepoznati svoj tip kože suva masna mešovita test" (rezultat isključen iz liste — direktan konflikt sa postojećim postom)
4. "uticaj sna stresa ishrane na kožu 2026 dermatolog"
5. "skin cycling trend 2026"
6. "kako čitati deklaraciju sastojaka kozmetičkih proizvoda vodič"
7. "znaci da je vreme da posetite kozmetologa ili dermatologa umesto kućne nege" (rezultat isključen iz liste — otkriveno direktno preklapanje sa sensiskinstudio.com postom)
8. "sezonska promena rutine nege kože leto zima navike"
9. "kolagen suplementi ishrana efekat na kožu 2026 dokazi"

**Teme već predložene u prethodnim pokretanjima (ne ponavljati)**:
- Iz 2026-07-05 (10 tema, sve vezane za konkretne SensiSkin usluge): nega pre/posle tretmana, Mesojet RF kolagen stimulacija (tretman, ne suplement), HydraFacial mesečna rutina, laserska epilacija za muškarce, LED terapija kod kuće vs. Dermalux, AI analiza kože vs. Aura Reality, retinol/vitamin C 2.0, zaštita kožne barijere/perutanje kože, personalizovana nega kože (tretmani), Aura Reality u medijima.
- Iz 2026-07-02 (SEO agent, 3 test drafta): skin longevity tretmani, LED terapija svetlom za kožu (mehanizam), analiza kože pre tretmana (mehanizam).
- Iz postojećeg live sadržaja sajta (MEMORY.md, Blog Crawl Correction 2026-06-11): serum, hemijski pilinzi, melazma, rozacea, vrste akni, menopauza, predeo oko očiju, štetnost solarijuma, tipovi kože, dnevna rutina, alopecija, kozmetolog vs. dermatolog.

**Kredit potrošnja ovog runa**: 0 firecrawl kredita (CLI nedostupan, WebSearch korišćen umesto toga — WebSearch nije deo firecrawl kredit sistema).
