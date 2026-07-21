# Casa Montana — Eksterijer cinematic reel (edit decisions)

Datum: 2026-07-20
Fajl: `casa-montana-eksterijer-9x16-2026-07-20.mp4`
Format: 1080×1920 (9:16), 30fps, H.264, silent, ~22.5s, ~32MB — za Instagram/TikTok.
Izvor: `~/Desktop/Casa Montana/Snimci - Claude/` (12 iPhone klipova, 4K HLG HDR, uspravno).
Alat: ffmpeg lokalno (bez Higgsfield / bez AI generisanja) — čista montaža.

## Redosled (walkthrough logika: dolazak → kuća → okolina → brend)

| # | Izvorni klip | Beat | In/len |
|---|---|---|---|
| 1 | IMG_4896 | Dolazak — kuća se pomalja kroz šumu (iz auta) | 6.0s / 3.2s |
| 2 | IMG_4899 | Hero — puna fasada brvnare | 1.8s / 3.6s |
| 3 | IMG_4936 | Kuća ugnežđena u šumi (viši rakurs) | 2.0s / 3.2s |
| 4 | IMG_4917 | Detalj zanata — krov/balvani (donji rakurs) | 1.5s / 3.2s |
| 5 | IMG_4915 | Planinski potok + senica | 3.2s / 3.2s |
| 6 | IMG_4926 | Pan sa potoka na kuću | 3.8s / 3.4s |
| 7 | IMG_4933 | Ulaz — topla svetlost | 1.2s / 3.0s |
| 8 | IMG_4901 | CASA MONTANA rezbareni znak (brend potpis) | 1.6s / 3.2s |

Izbačeni: IMG_4921, IMG_4924, IMG_4928 (redundantni/zaklonjeni granjem), IMG_4906 (dupli "znak" beat).

## Obrada
- **HDR→SDR:** izvor je 10-bit HLG/BT.2020; ovaj ffmpeg build nema `zscale`/`libplacebo`,
  pa je korišćen direktan dekod + blagi grade (vizuelno provereno — bez ispranosti).
- **Grade:** `eq=contrast=1.08:saturation=1.12:gamma=0.975` + `unsharp=3:3:0.4` (blaga oštrina posle 4K→1080 skaliranja). Konzistentno na svim klipovima.
- **Prelazi:** crossfade (dissolve) 0.5s između svih beat-ova.
- **Krajevi:** fade-in 0.5s (iz crne), fade-out 0.6s (u crnu).
- **Bitrate:** crf 22 + maxrate 12M (kontrola veličine na gustom lišću šume).

## Reprodukcija
Build skripta: scratchpad `cm-video/build.sh` (normalizovani isečci u `cm-video/seg/`, pa xfade lanac).

## Napomene / moguća doterivanja
- Enterijer folder još nije dostavljen — ovo je samo eksterijer.
- Ako se traži duže "disanje" kadrova, produžiti in/len po beat-u (trenutno snappy ~2.5-3.5s po klipu).
- Ako se traži čist rez umesto dissolve-a — trivijalna izmena u build skripti.
