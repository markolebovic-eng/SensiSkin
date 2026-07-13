# HydraFacial mesečna rutina — status i rezime (2026-07-10, ažurirano 2026-07-13)

## WordPress
- Post ID: **2661**, status: **PUBLISH — javno objavljen** (2026-07-13)
- Live URL: https://sensiskinstudio.com/hydrafacial-mesecna-rutina/
- Slug: `hydrafacial-mesecna-rutina`
- Edit URL: https://sensiskinstudio.com/wp-admin/post.php?post=2661&action=edit
- Kategorija: Blog
- OTVORENO: zatražiti "Request Indexing" u GSC-u za ovaj URL (nije još urađeno)

## Title / Meta (nepromenjeno iz originalnog predloga — provereno i potvrđeno dobrim)
- Title (50 karaktera): "HydraFacial mesečna rutina, ne jednokratni tretman"
- Meta (148 karaktera): "HydraFacial mesečna rutina daje bolje rezultate od povremenih poseta jer prati ciklus obnove kože. Saznajte pravi interval. Zakažite: 065/333-8-338."
- Provereno: nema kanibalizacije sa "hydrafacial Novi Sad" (Master Table red 1, transakcioni intent vs. ovaj informativni intent).

## Šta je promenjeno u odnosu na originalni draft
- FAQ pitanje #1 preformulisano u "Koliko često treba raditi HydraFacial?" da direktno pogodi GSC search-suggest "koliko često raditi hydrafacial".

## Vizuelni redizajn (2026-07-10) — pokušano, pa u potpunosti VRAĆENO
Isprobano nekoliko varijanti (highlight box/pull-quote/tabela/razdelnici → uklonjeno; zatim samo CTA box plave pa sive boje → i to uklonjeno). Vlasnici se nijedna vizuelna izmena nije dopala.

**Finalno stanje (verifikovano bajt-za-bajt identično originalu):** sadržaj je vraćen tačno na stanje iz backupa, bez ijedne vizuelne izmene — plain paragrafi, bold pseudo-podnaslovi, bez okvira/boksova/boja na CTA-u. Status `private`, ništa nije objavljeno javno.

Backup fajl (`post-2661-BACKUP-pre-vizuelnog-redizajna-2026-07-10.json`) i dalje čuvan u ovom folderu za slučaj da ikad zatreba referenca ili poređenje.

## Poslednja izmena (2026-07-10, zadržana)
Rečenica "Pozovite nas na 065/333-8-338 i zakažite konsultaciju." izdvojena u zaseban pasus (ranije je bila deo prethodne rečenice). Broj telefona je klikabilan `tel:` link — na klik/tap poziva broj direktno, bez ikakvog vizuelnog boksa/okvira, plain tekst.

## Ručne izmene vlasnice + čišćenje (2026-07-13)
Nataša je ručno u WP editoru dodala 2 slike i prave centrirane H2/H3 naslove (umesto bold pseudo-podnaslova) — ovo ostaje, dopalo joj se. Usput su ušla i dva "box" elementa (pullquote oko uvodne rečenice, obojeni okvir sa crvenom bordom oko liste benefita) koja nisu htela — **uklonjeno**, sada je čist tekst + slike + centrirani naslovi.

**Takođe:** sticky flag uklonjen sa Dermalux posta (ID 1899) — više ne blokira HydraFacial (ili bilo koji noviji) post da bude prvi na `/saveti-za-negu-koze/` listingu po datumu.

## Finalna verzija (2026-07-13, kraj dana)
Otkriveno da je druga sesija (druga mašina, Fable 5) u međuvremenu uradila potpuno drugačiji "flagship estetski" prolaz (pullquote, obojena key-takeaways kutija, drop cap, VIDLJIVA FAQ sekcija u telu) i to komitovala u git zajedno sa backupom pre te izmene (`outputs/sensiskin/wp-backups/2661-2026-07-13-pre-aesthetic-pass.json`).

Finalna odluka: vraćeno na taj pre-estetski backup kao osnovu (već sadrži ispravke "Vaš/Vaše" velikim slovom i "zakažite tretman" umesto konsultacije, plus 2 slike koje je Nataša ranije dodala), a zatim primenjeno SAMO:
- 9 bold pseudo-podnaslova → prave centrirane `<h2>` (zadržano, dopalo se)
- Slike ostale sa blago zaobljenim ivicama (`border-radius:8px`) — nepromenjeno
- FAQ ostaje SAMO kao nevidljiva JSON-LD schema (5 pitanja) — NEMA vidljive "Najčešća pitanja" sekcije u telu teksta

Nema pullquote-a, nema obojenih box-ova, nema drop cap-a. Ovo je trenutno tačno finalno stanje live posta (private, kategorija Blog).

## Dijakritika (č/ć/š/đ/ž) — provera i odluka
Testirano preko Google Suggest: kucanje "koliko često raditi hydrafacial" (sa dijakritikom) vraća sugestiju "koliko cesto raditi hydrafacial" (bez dijakritike) — Google sam normalizuje i tretira obe forme kao ekvivalentne pri pretrazi/indeksiranju. Zaključak: sumnja da dijakritika "kvari" pretraživost je delimično tačna u smislu da ljudi realno kucaju bez kvačica, ali NIJE tehnički SEO problem jer Google to normalizuje automatski.
Odluka: title/meta/focus keyphrase i telo teksta ostaju sa ispravnom srpskom dijakritikom (pravilan pravopis, brend glas) — nije uneta veštački "pogrešno napisana" ASCII varijanta u vidljiv tekst jer bi to izgledalo kao greška čitaocu i narušilo brend ton. Ako želiš dodatnu sigurnost, alt tekst na slikama (kad ih dodaš) može biti u ASCII varijanti kao dopunski signal — nije neophodno.

## Fajlovi u ovom folderu
- `hydrafacial-mesecna-rutina-2026-07-DRAFT.md` — tekst bloga (draft verzija pre WP unosa)
- `hydrafacial-mesecna-rutina-faq-schema-2026-07-10.json` — FAQ schema (JSON-LD), 5 pitanja
- `hydrafacial-mesecna-rutina-article-schema-2026-07-10.json` — Article/BlogPosting schema (REFERENCA — SASWP plugin je automatski generiše na sajtu, ovo se ne lepi ručno)

## Otvoreno za odluku
1. **Podnaslovi:** trenutno bold-paragrafi (repliciraju stil postojećih blogova), ne prava H2/H3 → Yoast će markirati "ključna fraza u podnaslovima" kao problem. Javi ako želiš prave H2 blokove umesto vizuelne konzistentnosti.
2. **Slike:** NISU dodate — dodaješ ručno (uključujući alt tekst sa keyphrase-om).
3. GSC "Request Indexing" nije rađen jer je post privatan — radi se posle javne objave.
