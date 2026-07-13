# Request Indexing — tracker

Živa lista URL-ova koji su izmenjeni (WordPress optimizacija) i čekaju ručni
"Request Indexing" u Google Search Console (GSC → URL Inspection → nalepi URL
→ Request Indexing). Nema API-ja za ovo — mora ručno, jedan po jedan.

**Pravilo za sve buduće sesije**: svaki put kad wordpress-edit skill upiše
izmenu na živu stranicu, URL se ODMAH dodaje u tabelu "Čeka indeksiranje"
ispod (uz datum i tip izmene). Kad vlasnik klikne Request Indexing, red se
prebacuje u "Zatraženo".

## Čeka indeksiranje

| Datum izmene | URL | Tip izmene |
|---|---|---|
| 2026-07-06 | https://sensiskinstudio.com/uticaj-kiseonika-na-kozu/ | sadržaj + title/meta + FAQ schema (svež crawl posebno vredi — menjan i sadržaj, ne samo meta) |

## Zatraženo (istorija)

| Datum zahteva | URL | Napomena |
|---|---|---|
| pre 2026-07-06 (Windows sesije) | https://sensiskinstudio.com/leto-i-promene-na-kozi/ | potvrdio vlasnik 2026-07-06 |
| pre 2026-07-06 (Windows sesije) | https://sensiskinstudio.com/dermalux-led-terapija-kao-resenje-problema/ | potvrdio vlasnik 2026-07-06 |
| pre 2026-07-06 (Windows sesije) | https://sensiskinstudio.com/posledice-starenja-na-kozi/ | potvrdio vlasnik 2026-07-06 |
| pre 2026-07-06 (Windows sesije) | https://sensiskinstudio.com/prva-pomoc-kozi-u-hladnim-danima/ | potvrdio vlasnik 2026-07-06 |
| pre 2026-07-06 (Windows sesije) | https://sensiskinstudio.com/sve-istine-o-laserskoj-epilaciji/ | potvrdio vlasnik 2026-07-06 |
| pre 2026-07-06 (Windows sesije) | https://sensiskinstudio.com/sinergija-estetskih-procedura-i-tretmana-lica/ | potvrdio vlasnik 2026-07-06 |
| 2026-07-13 | https://sensiskinstudio.com/hydrafacial-mesecna-rutina/ | Nov post, objavljen javno 2026-07-13. Vlasnik zatražio Request Indexing isti dan — GSC URL Inspection potvrđuje "Submitted and indexed", crawl 17:08 UTC (~2 min posle objave, veoma brzo). GA4 pageviews/bounce prati se pod pagePath `/hydrafacial-mesecna-rutina/` — 0 sesija u trenutku prve provere (isti dan kao objava, očekivano, nema još organskog saobraćaja).
