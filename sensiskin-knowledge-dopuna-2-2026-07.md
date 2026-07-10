Ovo je DODATAK uz sensiskin-agency-knowledge_1.md i sensiskin-knowledge-dopuna-2026-07.md — čita se zajedno sa njima, ne zamenjuje ih. Period: 2026-07-05 (commit a59ce95) → 2026-07-06 (danas)

Izvori: git istorija (4 commita: a59ce95, 33c7bae, 6457793, d0820d3), klijentski MEMORY.md, agent-memorije, fajl-sistem. Rad je tekao paralelno na dve mašine: MacBook Air (infrastruktura, research agent, prvi WP edit sa Mac-a) i Windows (SEO auditi, MCP proširenja, 6-post batch optimizacija).

---

## 1. INFRASTRUKTURA NA MACBOOK-U (sve novo u ovom periodu)

Bio: MacBook bez Node.js, bez Firecrawl-a, bez GitHub auth-a, bez WP pristupa → sada: kompletan radni čvor, sve verifikovano.

- **Node.js 26.4.0** instaliran preko Homebrew-a (mašina pre toga nije imala nikakav Node runtime)
- **firecrawl-cli v1.19.24** globalno + **31 firecrawl skill** u `~/.claude/skills/` (mašinski nivo, važi za sve klijente). Instalacija: `npx -y firecrawl-cli@latest init --all`
- **FIRECRAWL_API_KEY** persistiran u `~/.zshenv` (VAN repo-a — repo je public; CLI NE upisuje ključ na disk, radi čisto preko env varijable). `.env` i `.firecrawl/` su u `.gitignore`
- **Izmerena potrošnja kredita** (ne procena): global-only research run = 17 kredita (5× search po 2 + 7× scrape po 1), izmereno `firecrawl --status` pre (1.014) / posle (997). Zvanični cenovnik potvrđen scrape-om docs-a: scrape/map = 1 kredit/strana, search = 2 kredita/10 rezultata. Detalji: `.claude/agent-memory/research/firecrawl-credit-baseline.md`
- **GitHub auth**: gh CLI v2.96.0 + `gh auth login` kao `markolebovic-eng` (HTTPS, credential helper `gh auth git-credential`), git identitet postavljen na "Marko Lebović <marko.lebovic@gmail.com>". Napomena: prethodna 2 lokalna commita prepisana rebase-om radi ispravke autora (ce08695→a59ce95, f9e6242→33c7bae)
- **WordPress pristup sa Mac-a**: `.env` u root-u repo-a (WP_SITE_URL/WP_USERNAME/WP_APP_PASSWORD, gitignore verifikovan), REST auth test `/wp-json/wp/v2/users/me` vraća "Sensi Skin", rola administrator. Mac specifičnosti naspram Windows-a: bez `--ssl-no-revoke` flag-a, `python3` umesto `python`
- ⚠️ OTVORENO: firecrawl CLI NIJE instaliran na Windows mašini — research run 2 (Windows, 2026-07-06) ga nije našao ("command not found") i pao je na WebSearch fallback. Za Windows treba ponoviti instalaciju (Node + `firecrawl init --all`, ključ u System Environment Variables)

## 2. NOVI AGENT: RESEARCH (.claude/agents/research.md)

Bio: ne postoji → sada: aktivan, 143 linije, 2 odrađena runa.

- Namena: nedeljno/na-zahtev istraživanje blog tema — 10 tema sa obrazloženjem, klijent bira 2-3
- Arhitektura: **CLI+Bash odlučeno umesto MCP-a** (vlasnikova odluka 2026-07-05; workflow skillovi pokrivaju planiranu funkciju, MCP-ovih 11 alata ne). Frontmatter: `tools: Read, Write, Glob, Grep, Bash, WebSearch` + 4 google-seo-mcp alata dodata NAKNADNO u Windows sesiji (`gsc_search_analytics`, `gsc_content_decay`, `ga4_content_decay`, `ga4_query`) — commit 6457793
- Ugrađena pravila (4 odobrene iteracije): NE delegira glavni zadatak firecrawl workflow skillovima (deep-research eksplicitno odbija top-N liste); konkurenti grupisani po kategoriji usluge (epilacija vs kozmetološki centar) i poređenje praznina se radi UNUTAR kategorije; WebSearch predlaže URL-ove konkurenata ali ih označava "[PREDLOŽENO - NEVERIFIKOVANO]" i PRESKAČE za scrape do vlasnikove potvrde; kredit disciplina 10-20 po runu sa --status pre/posle
- **Run 1 (2026-07-05, Mac)**: 10 tema, 17 kredita → `outputs/sensiskin/research/topics-2026-07-05.md`. Kreiran `.agents/clients/sensiskin/competitors.md` (9 konkurenata, SVI URL-ovi neverifikovani; VIVA Beauty bez jasnog kandidata — dva slična salona)
- **Run 2 (2026-07-06, Windows)**: 9 opštih/evergreen tema kroz širi filter relevantnosti, WebSearch umesto CLI-ja (0 kredita) → `outputs/sensiskin/research/topics-2026-07-06-opste-teme.md`. Isključene 2 kandidat-teme zbog preklapanja sa živim sadržajem sajta
- ⚠️ OTVORENO: vlasnik još nije potvrdio nijedan URL u competitors.md — lokalni tok (scrape konkurenata) do tada ostaje prazan

## 3. SEO AUDITI (Windows sesije, 2026-07-06, commit 6457793)

- **Pun GSC indexing audit** → `outputs/sensiskin/seo/gsc-indexing-audit-2026-07-06.md` (217 linija): 48 sitemap URL-ova pojedinačno inspektovano — 44 indeksirano (91,7%), 4 ne. KRITIČNO: 3 legacy URL-a sa velikim istorijskim saobraćajem potvrđena kao živi 404 — `/cenovnik-usluga-2/` (560 klikova/90d, kolaps 551→1), `/hydrafacial-tretman-lica/` (215), `/sensi-skin/` (115) — **ispravljeni redirekcijama u istoj sesiji** (per handoff dokument). Stari sitemap.xml iz 2018 (21 mrtav URL) i dalje živ na serveru
- **Korekcija istog dana**: audit je pogrešno tvrdio da su `/shop-2/` i `/tekstovi-iz-casopisa/` linkovani iz žive navigacije — direktan curl sirovog HTML-a dokazao da su meniji čisti, mrtvi slugovi postoje samo u zastarelom JSON-LD SiteNavigationElement bloku (tema Blocksy). Izveštaj ispravljen in-place, prioritet spušten Visok→Srednji. LEKCIJA (upisana u seo agent-memory): tvrdnje o internim linkovima verifikovati sirovim HTML-om, ne WebFetch-om
- **Cross-ref audit 51 live title/meta parova** vs Master Keyword tabela → `outputs/sensiskin/seo/wp-title-meta-proposals-2026-07-06.md` (234 linije): SISTEMSKI BUG — 6 stranica ima meta opis isečen na identičnom mestu (nedostaje CTA rečenica sa telefonom) = jedan copy-paste bug, najveći quick-win; 5 stranica nikad nije dobilo odobreni copy (najgore: `/kozmeticki-proizvodi-sensi-skin-studio/` — focus keyword "dermokozmetika Novi Sad" potpuno odsutan); nove keyword propozicije za `/cenovnik-kozmetickih-tretmana-novi-sad/` i `/stetnost-solarijuma/`
- ⚠️ OTVORENO (vlasnikova odluka): `/nega-lica/` ima DVA neidentična odobrena meta opisa (06-09 Master tabela vs 06-24 audit) — preporučena 06-24 verzija, ali odluka nije doneta

## 4. WORDPRESS-EDIT SKILL + LIVE OPTIMIZACIJA (7 postova gotovo)

Bio: nikakav write pristup sajtu iz Claude Code-a → sada: skill + 7/33 postova kompletno optimizovano.

- **Novi skill `.claude/skills/wordpress-edit/`** (SKILL.md 563 linije + `references/elementor-safe-edit-template.py` 176 linija) — JEDINI skill sa write pristupom živom sajtu. Sadrži: pun Yoast checklist (SEO + Readability tab, prepisan sa vlasnikovih screenshotova), Elementor dvostruki-upis logiku (`content` + `_elementor_data`), site standard "podnaslovi bold, nikad italik", zabranu em-dash i AI fraza u title/meta, pravilo "nikad ne diraj slug", srpsku nominativ-zamku za keyphrase, backup-pre-upisa proceduru
- **6 postova (Windows)**: 2047 leto, 1899 Dermalux (Elementor — dupli upis + 2x2 grid slika), 1884 posledice starenja (vlasnik zadržao stari title/meta), 1877 prva pomoć zimi, 1819 laserska epilacija, 1754 sinergija. Svi verifikovani live; na svakom nađena bar jedna polomljena slika/link koji su PRETHODILI izmenama — uklonjeni
- **Post 1740 `/uticaj-kiseonika-na-kozu/` (Mac, 2026-07-06, prvi edit sa ove mašine)**: keyphrase zadržan "oksigenacija kože" (GSC pozicija 9 za "oksigenacija"), novi title 50c + meta 143c, gustina keyphrase 0→3, 2 interna linka (`/mesojet-tretmani/`, `/kontakt-sensi-skin-novi-sad/` — NE `/kontakt/` koji je 301) + 1 odlazni (sr.wikipedia Borov efekat), svih 11 `<em>` italika uklonjeno, polomljen CTA spojen sa standardnim formatom telefona, FAQPage schema (4 pitanja) dodata i validirana live. Čist Gutenberg — bez Elementor keša
- **Handoff dokument** `outputs/sensiskin/seo/wordpress-edit-handoff-macbook-2026-07-06.md` (123 linije) — uputstvo za nastavak rada sa Mac-a: setup, prompt šablon, lista već odrađenog
- **Request-indexing tracker** `outputs/sensiskin/seo/request-indexing-tracker.md` (NOVO 2026-07-06, ⚠️ NECOMMIT-OVANO): živa lista URL-ova koji čekaju ručni Request Indexing u GSC. Pravilo: svaki live upis ODMAH dodaje URL u tabelu. Trenutno stanje: 6 Windows postova = zatraženo (vlasnik potvrdio); post 1740 = čeka vlasnikov klik
- Pomoćni skriptovi (novi, commit-ovani): `scripts/wp_seo_audit.py` (84 linije, poređenje live Yoast parova) i `scripts/generate_topics_docx.py` (136 linija, generiše klijentski docx predlog tema)

## 5. MCP PROŠIRENJA AGENATA (Windows, commit 6457793)

- **analytics agent**: bio `tools: Read, Write, Glob, Bash, WebSearch` → sada +20 google-seo-mcp alata (gsc_search_analytics, ga4_query, ga4_conversion_funnel, cross_* dijagnostika, reload_credentials...)
- **seo agent**: +3 alata (gsc_list_sitemaps, gsc_submit_sitemap, migration_sitemap_validate) — sada 37 MCP alata
- **research agent**: +4 alata (videti sekciju 2)
- Napomena o arhitekturi: ovo znači da research agent sada ima hibrid — Firecrawl preko CLI+Bash (vlasnikova odluka), a GSC/GA4 podatke preko MCP-a

## 6. NOVE AGENT-MEMORIJE (institucionalno znanje agenata)

- **seo** (novo, 4 fajla): metodologija blog topic research-a za srpske beauty klijente (redosled: .rs portali → konkurentski blogovi → regionalni lag); metodologija GSC audita (ukrštanje 3 izvora URL-ova — sitemap-only propušta legacy 404 sa saobraćajem); potvrđeni srpski trendovi mid-2026 (skin longevity, LED terapija, analiza kože — spremni za copywriter brief; eksosomi — revizit za ~3 meseca)
- **orchestrator** (novo, 2 fajla): trend-lag routing — international→Srbija kašnjenje 3-6 meseci kao "get there first" prozor; topic research je single-domain SEO zadatak, ne paralelizovati agente
- **research** (novo, 3 fajla): competitors pending verification; kredit baseline (17 kredita/run)
- copywriter i claude-code-architect memorije: bez promena u ovom periodu

## 7. CONTENT DELIVERABLES COMMIT-OVANI U PERIODU (autorstvo delom pre 4. jula)

- `outputs/sensiskin/blog/formated/analiza-koze-2026-07-gbp.md` + `-newsltr.md` — GBP i newsletter adaptacije bloga o analizi kože (napisano 2. jula, commit-ovano 5. jula, commit 33c7bae)
- `outputs/sensiskin/seo/trending-topics-2026-07.md` (351 linija, datiran 2026-07-02) — SEO agent trend izveštaj, 3 rangirane teme
- `outputs/sensiskin/blog/predlog-tema-za-blog-2026-07-06.docx` — klijentski Word dokument predloga tema (generisan skriptom)
- `outputs/sensiskin/social/ig-skin-layers-2026-07-02.png` + `-base.png` — IG grafike (slojevi kože)

## 8. NECOMMIT-OVAN RAD (stanje na dan 2026-07-06 uveče)

- `.agents/clients/sensiskin/memory/MEMORY.md` — modifikovan: unosi o Mac WP setup-u, post 1740, tracker procesu, vlasnikovoj potvrdi indeksiranja, i ispravka "drugi Mac"→Windows mašina (vlasnik ima tačno 2 mašine: ovaj MacBook Air i Windows — raniji zapisi pogrešno pominjali drugi Mac)
- `outputs/sensiskin/seo/request-indexing-tracker.md` — nov, untracked
- `.firecrawl/` keš (gitignored, ne commit-uje se): pored install-check i docs scrape-ova, sadrži i 2 scrape-a konkurentskih sajtova od 5. jula (poliklinikanovakov.com, sredime.rs direktorijum) — test run za merenje potrošnje kredita, NIJE deliverable

## 9. OTVORENA PITANJA / PREOSTALI POSAO (eksplicitno neodlučeno ili nezavršeno)

1. competitors.md — vlasnik da potvrdi/ispravi 8 predloženih URL-ova; VIVA Beauty bez kandidata (ručna provera)
2. `/nega-lica/` — izbor između dva odobrena meta opisa (06-09 vs 06-24)
3. 18 stranica sajta — predlozi napisani, NIJEDAN primenjen preko API-ja
4. ~25 blog postova preostalo za optimizaciju (7/33 gotovo: 2047, 1899, 1884, 1877, 1819, 1754, 1740)
5. Post 1740 — čeka vlasnikov Request Indexing klik u GSC
6. Stari sitemap.xml (2018) — brisanje traži cPanel/File Manager pristup (van domašaja Claude Code-a)
7. Flagship novi blog post — planiran kao novi referentni šablon (zameniće /leto-i-promene-na-kozi/), nije započet
8. Firecrawl CLI na Windows mašini — nije instaliran (research fallback na WebSearch)
9. Slika u telu posta 1740 — Yoast alt-check ne može da prođe bez slike od vlasnika
10. Alt-text praznine na stranicama (homepage 14, O nama 11, HydraFacial 9...) — rangirano, nije pisano

## 10. BEZ PROMENA U OVOM PERIODU

- `.agents/clients/sensiskin/product-marketing.md` i `brand-voice-script.md` (poslednja izmena 2. jul)
- `.claude/settings.json` (2. jul); `.mcp.json` ne postoji u repou (MCP konfiguracija je na user nivou, van repo-a)
- Ostali skillovi u `.claude/skills/` (brand-voice-extractor, format-adapter, stop-slop)
- Agent definicije: orchestrator, copywriter, cro, email, paid-ads, social, strategy, claude-code-architect
- `.agents/agency/` (AGENCY.md, active-client.md = sensiskin)
