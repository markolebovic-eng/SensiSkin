# vikendica_reel_v3 — eksterijer showcase reel (edit decisions)

Datum: 2026-07-21
Fajl: `vikendica_reel_v3.mp4` — 1080×1920 (9:16), 30fps, H.264 high, **Rec.709-tagovano**, faststart, **nemo**, 20.0s, 36.6MB.
Supersedes: `casa-montana-eksterijer-9x16-2026-07-20.mp4` (v1 — loši dissolve prelazi, prekompresovano, HDR neispravan).
Izvor: `~/Desktop/Casa Montana/Snimci - Claude/` (11 iPhone klipova, 4K HLG HDR, uspravno). `1.MOV` = bivši prilazni klip; klip sa znakom (4901) uklonjen od strane vlasnika.
Alat: static ffmpeg (Martin Riedl, arm64) sa `zscale`+`tonemap` — lokalno, bez Higgsfield/bez AI generisanja.

## Redosled + cut lista (clip → sekunda)
| # | Klip | Skala | Uloga | Start–Kraj |
|---|---|---|---|---|
| 1 | 1 (prilaz) | WIDE | HOOK — hladno otvaranje, push-in; crop gornjeg 9:16 prozora da se tabla auta skloni | 0.0–3.0 |
| 2 | IMG_4899 | WIDE | reveal payoff — cela fasada | 3.0–6.5 |
| 3 | IMG_4917 | DETAIL | zanat — balvani/krov | 6.5–8.5 |
| 4 | IMG_4933 | MEDIUM | ulaz | 8.5–11.0 |
| 5 | IMG_4915 | WIDE | okolina — potok + senica | 11.0–13.5 |
| 6 | IMG_4926 | MEDIUM | potok → kuća (match cut sa #5, isti pravac pana) | 13.5–16.5 |
| 7 | IMG_4936 | WIDE | CLOSER — kuća u šumi, aspiraciono, loop ka hook-u | 16.5–20.0 |

Izbačeni: 4906 (redundantno sa 4926), 4921/4924/4928 (zaklonjeni granjem), 4901 (uklonio vlasnik).

## Obrada (po fazama v3 brief-a)
- **Prelazi:** SAMO hard rezovi. Bez crossfade/dissolve. Bez fade-in na početku (hladan hook). Fade-out u crno 0.5s na kraju (19.5–20.0).
- **Format:** izvor je već uspravan 9:16 (2160×3840 posle rotacije) → čist downscale na 1080×1920 (lanczos), bez blur bar-ova. Hook dodatno kropovan (crop=1800:3200:180:0) da se tabla auta gurne van kadra.
- **HDR→SDR (Faza 5):** pravi tonemap `zscale(tin=arib-std-b67/bt2020→linear, npl=100) → tonemap=hable:desat=0 → zscale(bt709 tv) → yuv420p`, + blagi grade `eq=contrast=1.03:saturation=1.05`. Boja **validirana na 3 test-kadra** (fasada/potok/prilaz) pre punog rendera — nebo ne pregoreva, lišće zadržava zasićenost, senke čiste.
- **Enkod (Faza 6):** x264 preset slow, profile high, yuv420p, CRF 19 + maxrate 16M/bufsize 24M (bez 12M cap-a koji je u v1 pravio kašasto lišće), 30fps, Rec.709 tagovi, faststart. 36.6MB (<50MB target).
- **Tekst overlay:** isključen (Faza 7 — nije traženo).

## Reprodukcija
`scratchpad/cm-video/build_v3.sh` (tonemap isečci → `v3seg/`) + `final_v3.sh` (concat hard-cut + fade-out + enkod). Static ffmpeg: `scratchpad/ffbin/ffmpeg`.

## Napomene
- Nemo namerno — muzika se dodaje kasnije; cut lista gore je za sinhronizaciju rezova na bit.
- Za sledeći put (sync na bit): izaberi track prvo, pa se trajanja kadrova podese da rezovi padnu na dobovanje.
- Enterijer folder još nije dostavljen.
