# Casa Montana — video walkthrough (2026-07-17)

## Nekretnina
- **Naziv**: Casa Montana
- **Lokacija**: Kopaonik, Srbija
- **Tip**: Luksuzna brvnara, prizemlje + 2 sprata
- **Booking.com**: https://www.booking.com/hotel/rs/casa-montana.sr.html
- **Airbnb**: https://www.airbnb.rs/rooms/830956234236950016
- **Namena videa**: Deo budućeg namenskog sajta za Casa Montana brend — omogućava kupcu da "obiđe" kuću pre fizičke posete

## Raspored
| Sprat | Prostorije |
|---|---|
| Prizemlje | Garaža, sauna, nedovršen mali apartman |
| Prvi sprat | Mali WC, dnevna soba + terasa, kuhinja, trpezarija, kupatilo |
| Drugi sprat | Master bedroom + terasa, guest bedroom |

## Izbori ovog pokretanja
- **Izvor fotografija**: Airbnb (15 fotografija, direktan fetch) + Booking.com (44 fotografija, preko Apify aktera `voyager~booking-scraper`) — spojeno u jedan pool, kuriran na 12 kadrova
- **Kurirano**: sve prepoznatljive prostorije iz rasporeda (12 od 12) — kuća je manja pa je svaka prostorija dobila svoj klip, umesto standardne kuracije na 6-10
- **Nedostaje**: garaža (unutra) i nedovršen apartman — nisu se pojavili ni na Airbnb ni na Booking galeriji (logično, nisu deo gostujućeg prostora); potrebne dodatne fotografije od vlasnika ako se žele uključiti
- **Model**: Kling 3.0 Turbo, 720p, 3s po klipu, 16:9 (budžetska varijanta — vlasnik odobrio zbog ograničenih kredita)
- **Spajanje**: Higgsfield `explainer_video` (nativno, besplatno) — bez ffmpeg zavisnosti
- **Zvuk**: nema (nem video, po standardnom pravilu)
- **9:16 verzija**: NIJE napravljena (preflight pokazao 176-288 kredita samo za reframe — nesrazmerno skupo za ovaj budžet; video ide na sajt, ne na društvene mreže, pa 16:9 pokriva primarnu namenu)

## Trošak (stvarno potrošeno, ne procena)
- Higgsfield krediti pre: 271 → posle: 217 → **potrošeno 54 kredita** (12 × 4.5, tačno po preflight proceni)
- Apify scrape Booking.com: ~$0.005 (sub-cent, jedna nekretnina)
- Airbnb fetch: besplatno (direktan, bez Apify-ja)

## Fajlovi
- `final/walkthrough-16x9.mp4` — finalni spojeni video (12 klipova × 3s = ~36s, 1280×720, 9.3MB)
- `shot-list.md` — redosled kadrova sa izvorom i pokretom kamere
