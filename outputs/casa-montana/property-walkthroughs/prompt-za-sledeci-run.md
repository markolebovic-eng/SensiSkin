# Prompt za sledeći walkthrough run (pripremljeno 2026-07-18)

Kontekst: prvi video (2026-07-17) imao je probleme — neki klipovi izgledali kao
statična slika sa zoom animacijom, bez tranzicija između klipova, mešan kvalitet
fotografija. Vlasnik sutra slika sopstvene fotografije (više njih, uključujući
garažu i nedovršeni apartman) i ubacuje ih u
`.agents/clients/casa-montana/photos/local/`.

Kopiraj prompt ispod, popuni redosled soba, i pošalji:

---

Napravi profesionalan cinematic walkthrough video za Casa Montana od mojih novih
fotografija. Radi direktno u glavnoj sesiji, po property-walkthrough protokolu,
ali sa strožim pravilima ispod — ona imaju prednost nad default tokom agenta.

ULAZ:
- Fotografije: .agents/clients/casa-montana/photos/local/ (moje, ima ih dosta)
- Redosled soba (putanja šetnje kroz kuću — video TAČNO ovim redom):
  [OVDE UPIŠI REDOSLED, npr: 1. prilaz kući, 2. ulaz, 3. dnevna soba, ...]

FAZA 1 — KONTROLA KVALITETA FOTOGRAFIJA (obavezna, pre svega ostalog):
- Pregledaj (Read) svaku fotografiju i oceni: oštrinu/fokus, ekspoziciju,
  kompoziciju, iskrivljene vertikale
- ODBACI sve mutne, loše fokusirane, pre/podeksponirane — kvalitet finalnog
  videa određuje najslabija fotografija, bolje manje odličnih nego sve osrednje
- Za svaku prostoriju iz mog redosleda izaberi TAČNO JEDNU najbolju; ako se
  dvoumiš između dve, prikaži mi obe da ja presudim
- Prikaži mi finalnu shot-listu (fotografija → prostorija → pozicija) i ČEKAJ
  moju potvrdu pre bilo kakvog generisanja

FAZA 2 — KONTINUITET ŠETNJE (ključna razlika u odnosu na prošli video):
Video mora da izgleda kao NEPREKIDNA šetnja, ne slajdšou klipova:
- Svi unutrašnji klipovi: pokret NAPRED sa paralaksom (steadicam/walking
  forward) — kamera se FIZIČKI kreće kroz prostor. NIKAD čist zoom-in: ako
  klip izgleda kao statična slika sa zoom efektom, to je automatski FAIL i
  regeneriše se
- Pravac kretanja teče iz klipa u klip: klip se završava kretanjem KA
  vratima/prelazu, sledeći počinje kretanjem OD ulaza — kao da ista kamera
  nastavlja hod
- TRANZICIJE: koristi start_image + end_image tehniku — end_image klipa =
  fotografija SLEDEĆE prostorije, prompt tipa "camera walks forward through
  the doorway into the next room, continuous walking motion". Proveri kroz
  models_explore koji modeli podržavaju start+end image (Kling 3.0 std DA,
  Turbo NE). PRVO napravi JEDAN test-par (dve susedne sobe) i pokaži mi
  rezultat pre nego što tako radiš ceo video
- Ako end_image tranzicije ne izgledaju dobro na testu: fallback je ffmpeg
  (brew install ffmpeg) i spajanje sa kratkim crossfade-om (xfade, 0.4-0.5s)
  umesto tvrdih rezova — takođe mi pokaži test pre celog posla

FAZA 3 — KONZISTENTNOST (apsolutni zahtev, "isti kvalitet svakog trenutka"):
- JEDAN isti model za SVE klipove, ISTA rezolucija, ISTO trajanje po klipu,
  ISTI stil prompta — bez ikakvog menjanja usred posla
- Prompt uvek opisuje samo KAMERU i SVETLO, nikad sadržaj sobe
- Jedan spor pokret po klipu, bez kombinovanih pokreta

FAZA 4 — BUDŽET I ODOBRENJE:
- Pre generisanja: balance + get_cost preflight za izabrani model i ukupan
  broj klipova (uključujući tranzicione ako ih ima) — prikaži mi tačan ukupan
  trošak i ČEKAJ odobrenje
- Iz prošlog runa: kling3_0 std (3s, sound off) je koštao isto kao Turbo
  (4.5 kr/klip) a podržava end_image — proveri da li i dalje važi, i predloži
  i 1080p varijantu sa cenom ako je izvodljiva

FAZA 5 — QA SVAKOG KLIPA PRE SPAJANJA:
- Kad se svi klipovi završe, pregledaj svaki: zoom-umesto-kretanja, topljenje
  nameštaja, krivljenje vrata/ivica = regeneriši taj klip sa blažim/drugačijim
  pokretom (jednom; ako opet ne valja, javi mi umesto da guraš dalje)
- NE spajaj dok svi klipovi ne prođu proveru

FAZA 6 — SPAJANJE I ISPORUKA:
- Spoji tačno po mom redosledu, sa tranzicijama po planu iz Faze 2
- Snimi u outputs/casa-montana/property-walkthroughs/{današnji datum}/final/
  + ažuriraj PROPERTY.md, shot-list.md i MEMORY.md
- Video je nem, bez muzike

---

## Saveti za slikanje (pre pokretanja prompta)

1. Slikaj svaku sobu SA ULAZA, gledajući unutra — kadar koji vodi pogled kroz
   prostor (vrata sledeće sobe, hodnik, prozor u dubini) daje modelu geometriju
   za "hodanje"; frontalni kadar ravnog zida = zoom efekat, garantovano
2. Horizontalno (landscape), u visini očiju — ista visina kroz celu kuću
3. Ista podešavanja svetla kroz celu sesiju (jedno doba dana, ista svetla
   upaljena u svim sobama)
4. Pazi na prozore — jak dnevni kontrast "pregori" prozor u belo; mekše
   spoljno svetlo (jutro/kasno popodne) ili ugao koji ne gleda direktno u prozor
5. Po 2-3 kadra svake sobe iz različitih uglova — kuracija bira najbolji, a
   kadar "kroz vrata ka sledećoj sobi" dobro dođe za tranzicije
6. Uslikaj i garažu i nedovršeni apartman — jedino što prošli video nije imao
