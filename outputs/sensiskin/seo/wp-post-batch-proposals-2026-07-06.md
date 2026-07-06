# WordPress SEO/GEO predlozi — pojedinačna obrada po postu
**Datum:** 2026-07-06
**Status:** Radi se post po post, po odluci vlasnika (promena plana usred sesije). Ovaj fajl trenutno sadrži SAMO Post 1899. Postovi 1884, 1877, 1819, 1754 slede kao posebni zahtevi nakon što vlasnik pregleda i odobri ovaj.
**Napomena:** Ovo su predlozi za odobrenje — orchestrator izvršava promene na live sajtu tek posle eksplicitnog "da" vlasnika, po `wordpress-edit` skill protokolu (Elementor aktivan na ovom postu — mora se patch-ovati i `content` i `_elementor_data`).

---

## POST 1899 — /dermalux-led-terapija-kao-resenje-problema/

### 1. Trenutno stanje
- **Focus keyphrase:** dermalux LED terapija
- **Title (49 char):** "Dermalux LED terapija - za koga i koliko tretmana"
- **Meta (122 char):** "DERMALUX LED terapija kao rešenje za problematičnu, aknoznu i reaktivnu kožu — kako svetlost leči i koliko tretmana treba."
- **Elementor:** AKTIVAN — svaka izmena mora ići u `content` I `_elementor_data` (Korak D iz skill-a)
- **Body:** ~7312 karaktera

### 2. Realni GSC podaci (90 dana, 2026-04-08 do 2026-07-06)
| Upit | Impresije | Klikovi | Pozicija |
|------|-----------|---------|----------|
| dermalux led lampa cena | 15 | 0 | 8.9 |
| dermalux lampa | 16 | 1 | 6.3 |
| dermalux led lampa | 6 | 0 | 7.7 |
| dermalux led | 6 | 0 | 7.7 |
| fototerapija lica | 6 | 0 | 53.2 |
| dermalux rosacea | 1 | 0 | 11 |
| led terapija | 2 | 0 | 10 |

**Zaključak iz podataka:** ljudi zaista kucaju "dermalux lampa" / "dermalux led lampa" (kolokvijalno, uređaj-framing) — ne "LED terapija" kao stručni termin. Postoji jasan cena-intent upit ("dermalux led lampa cena", 15 impresija, solidna pozicija 8.9) koji trenutni naslov/meta uopšte ne adresira. "fototerapija lica" je alternativna terminologija sa jako lošom pozicijom (53.2) — vredna hvatanja, ali sekundarno, ne kao glavni keyphrase (nema dovoljno impresija da opravda promenu fokusa).

### 3. Predlog

**FOCUS KEYPHRASE (novo): "dermalux led lampa"**

Razlog: ovo je fraza koju realni pretraživači zaista kucaju (16+6 impresija kombinovano na varijante), prirodnija je od stručnog "LED terapija" i direktno je iz GSC podataka, ne pretpostavka.

**SEO TITLE:**
"Dermalux LED lampa: za koga je i koliko tretmana treba" (54 karaktera — keyphrase na početku)

**META DESCRIPTION:**
"Dermalux LED lampa pomaže kod problematične, aknozne i reaktivne kože. Saznajte za koga je namenjena i koliko tretmana je potrebno." (132 karaktera — keyphrase u prvoj rečenici, bez em-crtice po brend pravilu, bez superlativa)

**YOAST CHECKLIST:**
- ✓ Keyword u naslovu (pozicija: početak)
- ✓ Keyword u prvoj rečenici meta opisa
- ✓ Meta dužina: 132 char (120–156 opseg: ✓)
- ✓ Title dužina: 54 char (50–60 opseg: ✓)
- ⚠ Keyword u telu teksta 3+ puta doslovno, keyword u bar jednom H2 — NIJE PROVERENO ovu sesiju (nemam pristup telu posta), orchestrator mora proveriti pre implementacije i po potrebi dodati 1-2 pojavljivanja "dermalux led lampa" u telo (npr. u prvom pasusu ili podnaslovu) da zadrži Yoast zeleno svetlo — trenutni H1/podnaslovi verovatno koriste stariji "LED terapija" oblik.

**KEYWORD COLLISION CHECK:** Servisna stranica `/dermalux/` (Master Keyword Table, red 8) ima dodeljen keyphrase "LED terapija za kožu lica" — transakciona/opšta namera. Novi blog keyphrase "dermalux led lampa" je uređaj-specifičan, informativan, kolokvijalan — različita fraza, različita namera. Nema doslovnog preklapanja fraze. ✓ nema kolizije, ALI oba dele koren "LED terapija/Dermalux" — preporuka ispod (odeljak 4) eksplicitno razdvaja uloge.

### 4. Rešenje kanibalizacije (blog post 1899 vs. servisna stranica /dermalux/)

Iako fraze ne kolidiraju doslovno, obe stranice dele isti brend/temu (Dermalux LED). Razdvajanje uloga:
- **Blog post 1899** = informativna uloga: "šta je Dermalux LED lampa, za koga je namenjena, koliko tretmana je potrebno, kako se koristi kod problematične/aknozne/reaktivne kože" — odgovara na pitanja pre rezervacije.
- **Servisna stranica /dermalux/** = transakciona uloga: "LED terapija za kožu lica" kod Sensi Skin, rezervacija, protokol studija.

Preporuka: zadržati ovu podelu kakva već postoji (blog = edukacija, servisna stranica = booking), samo uskladiti blog keyphrase sa stvarnim jezikom pretrage ("dermalux led lampa" umesto "dermalux LED terapija"). Nije potrebna promena na servisnoj stranici.

### 5. FAQ draft (za FAQPage schema, GEO/AI-search vrednost)

Pošto nemam pristup punom telu posta ove sesije, ispod su Q&A parovi izvedeni ISKLJUČIVO iz onoga što trenutni title/meta već tvrde (a što bi telo posta trebalo da potkrepljuje, jer title/meta se generišu iz njega). **Orchestrator mora proveriti svaki odgovor protiv stvarnog teksta tela pre implementacije — ništa ispod nije potvrđeno van title/meta.**

1. **Za koga je namenjena Dermalux LED lampa?**
   Predlog odgovora (izvedeno iz meta opisa): "Dermalux LED terapija je namenjena osobama sa problematičnom, aknoznom i reaktivnom kožom." — ⚠ VERIFIKOVATI: proveriti da li telo navodi i druge tipove kože/stanja (npr. rozaceu — vidi tačku 3 ispod).

2. **Koliko tretmana je potrebno za vidljive rezultate?**
   Trenutni title eksplicitno obećava odgovor na ovo pitanje ("...i koliko tretmana"), pa je vrlo verovatno da telo sadrži konkretan broj ili raspon. ⚠ VERIFIKOVATI: uneti tačan broj/raspon tretmana iz tela — NE izmišljati broj u ovoj fazi, nemam ga.

3. **Da li Dermalux LED lampa pomaže kod rozacee?**
   Osnov: realan GSC upit "dermalux rosacea" (1 impresija) postoji, a meta pominje "reaktivnu kožu" što može, ali ne mora, pokrivati rozaceu eksplicitno. ⚠ VERIFIKOVATI: dodati ovo FAQ pitanje SAMO ako telo posta eksplicitno pominje rozaceu/rosaceu — ako ne pominje, izbaciti pitanje umesto da se izmišlja tvrdnja o efikasnosti kod specifične dijagnoze.

4. **Kako svetlost leči kožu (mehanizam)?**
   Osnov: meta opis eksplicitno kaže "kako svetlost leči". ⚠ VERIFIKOVATI: preuzeti tačnu formulaciju mehanizma (verovatno fotobiomodulacija / talasne dužine, po postojećem brend rečniku iz product-marketing.md — "633 nm", "fotobiomodulacija" su termini koje sajt već koristi za slične teme) direktno iz tela, ne generalizovati.

**NAPOMENA O CENI (tačka 6 iz brief-a):** Realan upit "dermalux led lampa cena" ima 15 impresija i solidnu poziciju (8.9) — jasan signal potražnje za cenom. Trenutni title/meta NE pominju cenu, i **nemam potvrdu da telo posta uopšte navodi cenu** (opis govori samo o "kako svetlost leči i koliko tretmana treba", ne o ceni). Zato:
- **NE predlažem dodavanje cene u title/meta** — to bi bilo izmišljanje podatka koji možda ne postoji u telu.
- Broj tretmana ("koliko tretmana") JESTE bezbedno signalizirati u title-u, jer je to već deo postojećeg naslova/meta i pretpostavlja se da telo to pokriva (novi title iznad to i radi: "za koga je i koliko tretmana treba").
- **FLAG ZA VLASNIKA (sadržajna praznina):** ako telo posta zaista ne sadrži nikakvu informaciju o ceni ili o tome šta određuje cenu/broj tretmana, ovo je realna prilika koja se propušta — 15 impresija na pozicijama blizu prve strane je konkretan trag potražnje. Preporuka: dodati kratak pasus u telo (ne u meta) tipa "od čega zavisi broj i cena tretmana" (opšti faktori: stanje kože, broj sesija, individualna procena na konsultaciji — bez navođenja konkretnog dinarskog iznosa ako se cena inače ne objavljuje javno na sajtu, po dosadašnjoj praksi CTA formule "Zakazite konsultaciju"). Ovo je odluka za vlasnika i copywritera, ne nešto što ja sada pišem bez uvida u telo.

---

## Sledeći koraci
1. Vlasnik pregleda predlog za Post 1899 iznad.
2. Po odobrenju: orchestrator izvršava (title/meta u Yoast meta poljima + `_elementor_data`, FAQ JSON-LD schema blok, cache clear, verifikacija na živom sajtu, zahtev za indeksiranje u GSC).
3. Nakon odobrenja/implementacije Post 1899, nastaviti sa Post 1884, zatim 1877, 1819, 1754 — svaki kao poseban zahtev.
