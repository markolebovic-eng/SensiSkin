# SensiSkin WordPress SEO/GEO — vodič za nastavak rada (MacBook)

Ovaj dokument je za kolegu koji nastavlja SEO/GEO optimizaciju sensiskinstudio.com
preko Claude Code-a, na MacBook-u. Sve tehničke instrukcije (Yoast pravila, Elementor
logika, FAQ standard) već su zapisane u projektu — ovde je samo kako da se poveže i
šta je već urađeno.

---

## 1. Setup (jednokratno, na početku)

### Korak 1 — Povuci repo
```bash
git pull
```
(pretpostavka: repo je već klonirán ranije preko `git clone`; ako nije, prvo klonirati)

### Korak 2 — Napravi `.env` fajl sa WordPress kredencijalima
U root folderu projekta (isti nivo gde je `.gitignore`), napravi fajl `.env`
(ne postoji u git-u — namerno, jer sadrži lozinku):

```
WP_SITE_URL=https://sensiskinstudio.com
WP_USERNAME=natasa
WP_APP_PASSWORD="xxxx xxxx xxxx xxxx"
```

**Važno**: WordPress Application Password ima razmake u sebi (format "xxxx xxxx xxxx xxxx")
— **mora biti pod navodnicima** u `.env` fajlu, inače se lozinka pogrešno učitava.

(Zatraži tačnu lozinku od [ime/kontakt] — nije ovde navedena namerno, radi bezbednosti.)

### Korak 3 — Reload Claude Code
`Cmd+Shift+P` → "Developer: Reload Window" (da učita `.env` i sve skillove/agente iz repoa)

### Korak 4 — Testiraj konekciju
U Claude Code chatu, pošalji:

> Koristi wordpress-edit skill i proveri konekciju sa WordPress-om (test /wp-json/wp/v2/users/me)

Ako vrati "Ulogovan kao Sensi Skin, rola administrator" — sve radi.

**Napomena za Mac (razlika od Windows-a)**: Claude Code NE treba da koristi `--ssl-no-revoke`
flag na curl komandama (to je bio Windows-specifičan fix) — na Mac-u će curl raditi
normalno bez njega. Isto tako, Python komanda na Mac-u je često `python3`, ne `python` —
Claude Code će ovo sam prepoznati i prilagoditi, ali ako naiđe na grešku "command not found",
to je razlog.

---

## 2. Kako da tražiš rad (prompt koji koristiš svaki put)

Najjednostavniji prompt, kad god želiš da se radi SEO/GEO optimizacija na sajtu:

> **"Koristi wordpress-edit skill i optimizuj post [ID ili naziv] — analitika, title/meta/keyphrase, FAQ schema, sve po standardnom protokolu."**

Ili, ako samo nastavljaš tamo gde je stalo:

> **"Nastavi WordPress SEO optimizaciju — proveri MEMORY.md šta je urađeno pa idi na sledeći post."**

Ne treba ništa dodatno da objašnjavaš — ceo protokol (Elementor detekcija, Yoast
checklist, FAQ pravila, "nikad ne diraj slug", stil podnaslova, provera pokvarenih
slika/linkova) je već zapisan u `.claude/skills/wordpress-edit/SKILL.md` i Claude
Code ga čita automatski kad pozoveš skill.

**Uvek na kraju** dobićeš listu linkova za "Request Indexing" u Google Search Console —
to je jedini ručni korak koji ti ostaje (nema API-ja za to, mora se kliknuti ručno).

Takođe: kad god Claude Code traži da klikneš **"Elementor → Tools → Clear Files and Data"**
— to je normalan deo procesa (samo za postove koji koriste Elementor), ne znači da je
nešto pošlo po zlu.

---

## 3. Šta je već urađeno (da se NE ponavlja)

### Kompletno optimizovano (title, meta, keyphrase, FAQ schema, linkovi, provera slika) — 5 blog postova:

| ID | Post | URL |
|---|---|---|
| 2047 | Leto i promene na koži | `/leto-i-promene-na-kozi/` |
| 1899 | Dermalux LED terapija | `/dermalux-led-terapija-kao-resenje-problema/` |
| 1884 | Posledice starenja na koži | `/posledice-starenja-na-kozi/` |
| 1877 | Prva pomoć koži zimi | `/prva-pomoc-kozi-u-hladnim-danima/` |
| 1819 | Sve istine o laserskoj epilaciji | `/sve-istine-o-laserskoj-epilaciji/` |
| 1754 | Sinergija estetskih procedura | `/sinergija-estetskih-procedura-i-tretmana-lica/` |

Za svaki od ovih: keyphrase je zasnovan na stvarnim GSC podacima (šta ljudi zaista
pretražuju), title/meta usklađeni, FAQ schema dodata (ili potvrđeno da već postoji),
pokvarene slike/linkovi uklonjeni, interni+odlazni linkovi dodati, podnaslovi
usklađeni na bold stil.

### Posebno urađeno (van blog optimizacije):
- **Pun GSC indexing audit** sajta (48 stranica proverene, 3 kritične 404 stranice
  pronađene i ispravljene preko redirekcija — vidi `/outputs/sensiskin/seo/gsc-indexing-audit-2026-07-06.md`)
- **Cross-referenca svih 51 postojećih title/meta parova** naspram odobrene Master
  Keyword tabele iz juna — vidi `/outputs/sensiskin/seo/wp-title-meta-proposals-2026-07-06.md`
  (identifikovan sistemski bug: 6 stranica je imalo isečen meta opis na istom mestu — ispravljeno)

### NIJE urađeno — preostaje (ne treba ponavljati istraživanje, samo nastaviti):
- **~26 preostalih blog postova** (od ukupno 33) — puna lista svih postova sa ID-jevima
  je dostupna ako zatražiš od Claude Code-a "prikaži mi listu svih blog postova"
- **18 stranica sajta** (ne blog postovi) — analiza title/meta je urađena (vidi fajl
  gore), ali PRIMENA (upis preko API-ja) još nije izvršena ni za jednu
- Stari `sitemap.xml` (2018, mrtvi linkovi) — i dalje treba obrisati sa servera
  preko cPanel/File Manager (van domašaja Claude Code-a, treba hosting pristup)
- Novi "flagship" blog post — planiran kao potpuno nov, pažljivo sređen post koji
  će postati referentni primer za sve ostale (trenutno je to `/leto-i-promene-na-kozi/`)

**Gde proveriti tačno stanje u svakom trenutku**: `.agents/clients/sensiskin/memory/MEMORY.md`
— svaka sesija upisuje šta je urađeno na kraju, uključujući datum. To je najpouzdaniji
izvor "šta je već gotovo" — pitaj Claude Code da ga pročita ako nisi siguran/na.

---

## 4. Ako nešto ne radi

- **"No task found" / auth greška**: proveri da li je `.env` ispravno formatiran
  (navodnici oko lozinke sa razmacima)
- **Izmena se ne vidi na sajtu, iako Claude kaže da je upisano**: verovatno treba
  Elementor cache clear (Tools → Clear Files and Data) — Claude će to tražiti od tebe
- **Yoast i dalje pokazuje crveno posle izmene**: osveži WP admin stranicu (Ctrl/Cmd+Shift+R)
  — Yoast panel se ponekad ne osvežava automatski
