---
name: pisanje-izvestaja
description: Use when the user asks for a client-facing progress/analytics report — SEO, marketing, or general campaign progress — as an HTML page and/or a PDF document. Also use when the user mentions "izveštaj", "napravi mi izveštaj", "PDF izveštaj", "revizija napretka", "progress report", or asks to update/regenerate an existing report of this kind. Covers: what content rules to follow, how to pull the brand's real color palette, the HTML report design system, and the specific PDF-generation pipeline (Paged.js + puppeteer-core) that avoids Chromium's native print-engine bugs. This skill is a living document — update it whenever a new report session teaches a new lesson or the owner corrects something.
metadata:
  version: 1.1.0
---

# Pisanje izveštaja (client report writing)

This skill was written after the first full SensiSkin "izveštaj o napretku" (progress
report) session (2026-08-02), which went through several rounds of owner corrections on
content, color, and PDF pagination. Every rule below exists because something was wrong
and got corrected — read it end to end before starting a new report, and **add to it**
whenever a future session teaches something new. Do not silently work around a problem
this file already documents; fix the root cause and update this file if the fix changes.

---

## 1. Content rules (apply to every client report, not just SensiSkin)

These are standing rules from direct owner correction — do not re-litigate them on the
next report, just follow them:

1. **Compare like-for-like periods only.** Never compare a 6-month block against a
   1-month block. If the ask is "pre vs posle X", break it into **month vs month**
   (maj vs jun vs jul vs avgust, etc.), not two unevenly-sized aggregate windows.
   Uneven-period comparisons are misleading and the owner will reject them.
2. **No em dash (—) anywhere in the document.** This is the same site-wide copy rule
   that governs blog posts (see `.agents/clients/{slug}/product-marketing.md`
   "Izbegavati" list) but it applies to the **whole report**, not just body copy —
   titles, table cells, alt text, everything. Grep the final HTML for `—` before
   calling a report done: `grep -n "—" <file>`. Use a comma, period, or new sentence
   instead.
3. **The client-facing document contains only wins/improvements.** Anything that
   still needs fixing, any gap, any recommendation — does **not** go in the polished
   deliverable. Report it directly to the owner in the conversation instead. The
   report itself should read as a clean, positive artifact; the punch-list is a
   conversational side-channel, not a report section.
4. **Lead with raw growth, framed as "more than before."** The headline stat should
   be about actual traffic/visits/impressions going up, with one or two standout
   keyword/metric wins as supporting proof (e.g. a keyword jumping to page 1) —
   not a wall of caveats before the reader reaches anything positive.
5. **Translate every section heading to Serbian.** Never leave "Executive Summary"
   (use **"Rezime"**), or any other English label, in a client-facing document —
   even if the rest of the draft is already in Serbian, section headers are easy
   to miss when assembling from a template.
6. **Correct agency attribution: "Marconi Agency"**, not "AI Marketing Agency" (an
   earlier, wrong placeholder name that leaked into a first draft from the internal
   project's own `AGENCY.md` framing — that internal name is not the client-facing
   brand name). The footer must explicitly say **we** (Marconi Agency) created the
   report and its PDF — see template footer text below.
7. **If GA4/GSC data has a real gap** (e.g. tracking wasn't live for part of the
   requested period), stop and say so plainly before building anything — do not
   quietly extrapolate or invent a "before" number. Ask the owner how they want to
   handle the gap (see the AskUserQuestion pattern used in the original session:
   options were "use what's available + explain the gap", "drop that section
   entirely", or "wait for more data").
8. **Write for the brand owner, not for another marketer.** Direct feedback on the
   first real August 2026 report (WhatsApp, 2026-08-04, verbatim): *"Ima malo za
   mene previše informacija koje ne razumem... Bitno je da razumem brojeve i
   procente i to je ok."* and, about the itemized per-page technical work: *"baš
   stručno to mi nije neophodno ali kontam nekome će biti značajno ko se u to
   razume."* What she actually wants to walk away with, in her own words: *"da
   vidim šta je sve povećano i šta je urađeno — tipa blog postovi, koje ključne
   reči su forsirane... jer to mi daje smernice za sadržaj na Instagramu."*
   Concretely, this flips the default balance of the report:
   - **Keep, prominent**: growth numbers/percentages (plain, large, chart-backed),
     which blog posts were published, which keyword themes were pushed.
   - **Cut or reduce to one line**: itemized technical SEO work — Yoast checks,
     schema markup, meta-tag edits, per-page technical audits. A single summary
     sentence ("optimizovali smo naslove i opise na 51 stranici") is enough; do
     not list it page-by-page like a dev changelog. The `.month-block` checklist
     format itself is fine and liked ("Super mi je što je taksativno navedeno šta
     je urađeno svaki mesec") — it's the *content* of the bullets that needs to
     shift from technical-task language to plain-outcome language.
9. **Every newest published blog post gets its own dedicated subsection with its
   own analytics** (page views/sessions, and clicks/impressions once it has GSC
   history), not just a one-line mention buried in a month's checklist. This was
   an explicit owner ask ("moramo da ubacimo novi blog u izveštaj i kakva je
   njegova analitika") — check GA4 landing-page data and GSC per-URL data for
   each post published since the last report before writing this section.
10. **Keyword-to-content-ideas bridge section is opt-in, per client — not a
    default.** SensiSkin's owner explicitly uses the report's keyword data as
    her Instagram content-planning input and asked for this bridge; that is a
    SensiSkin-specific fact, not a universal one. Only add a "content ideas"
    section when a client has explicitly said they want their SEO/marketing
    report tied to their own content planning (Instagram or otherwise) — ask if
    unclear, don't assume every client runs their own social content off this
    report. For SensiSkin specifically: yes, always include it, translate the
    top keyword wins into a short plain-language list of content suggestions
    (e.g. "ljudi traže '[fraza]' → ideja za Reel/objavu o tome").
11. **"Top pretrage ovog meseca" is a compact mini-table WITH position numbers,
    not a numberless list.** Correction to an earlier version of this rule: the
    owner does want to see positions here, specifically because several are
    strong ("jako dobrim pozicijama") and that's part of what she's proud of/
    wants to see. Keep it compact and separate from the full multi-column
    pre/posle/pomak comparison table (§4b still applies for the detailed
    version) — just **phrase + current position**, 5-8 rows, nothing else. This
    is a lighter-weight companion to the full table, not a replacement for it,
    and not a plain unnumbered list either.
12. **Mark "hot" phrases (new or jumped significantly) with a visual badge next
    to the position number**, not instead of it. Combine with §1.11: the mini-
    table shows phrase, position, and a small marker (flame icon / `.badge.new`)
    on rows that are new or moved up a lot, so what's worth a post *this month*
    is visible at a glance without losing the actual number she wants to see.
13. **Every new blog post section also shows WHICH PLATFORM its readers came from.**
    Explicit owner ask (2026-08-04): *"izvadi podatke sa kojim platformi dolaze ljudi
    na nove blogove"*. Pull GA4 `landingPage` filtered to the post slug, broken down by
    `sessionSourceMedium` (more useful than `sessionDefaultChannelGroup` here, because
    it separates Instagram from Facebook, which the channel group lumps into "Organic
    Social"). Render as horizontal bars (`.src-list` / `.src-row` / `.src-fill`), not a
    table. This matters to her specifically because it proves her own Instagram work is
    what drives readers to new content: in the August 2026 report, 78% and 68% of the
    two new posts' readers came from Instagram. Note that `l.instagram.com / referral`,
    `instagram.com / referral` and `m.facebook.com / referral` are separate rows in GA4
    and must be summed per platform before charting.
14. **Cap every month-checklist bullet at one short, non-technical sentence.**
    (`<li>` items inside `.month-block .checklist`, §3). If a task needs more
    than one sentence to describe, that's a signal it's a technical detail that
    belongs cut per §1.8, not a longer bullet. Write outcomes, not tasks — "Novi
    tekst objavljen o X" rather than "Optimizovan title/meta/keyphrase/FAQ na Y
    prema Yoast checklisti".

---

## 2. Getting the brand's real color palette

Never guess a client's brand colors or reuse a previous client's palette. Pull the
real one, in this order (most to least authoritative):

1. **WordPress Global Styles API** (if the site is WordPress): `GET
   {site}/wp-json/wp/v2/global-styles/themes/{active-theme-stylesheet}` — find the
   active theme slug first via `GET /wp-json/wp/v2/themes?status=active&_fields=stylesheet,name`.
   The response's `settings.color.palette.theme` array is the theme customizer's own
   declared palette (authoritative, structured, labeled `palette-color-1..8`).
2. **Compiled customizer CSS** (cross-check / fallback): for Blocksy-based sites this
   is `{site}/wp-content/uploads/blocksy/css/global.css` — scrape it (`firecrawl scrape
   <url> -f rawHtml`) and grep for `--theme-palette-color-N:#hex` and
   `--theme-button-background-initial-color` / `-hover-color` (this is where CTA/button
   colors live — they're often NOT part of the Global Styles palette API above, since
   button colors are a separate Blocksy customizer section).
3. **Elementor kit** (only if the site actually uses Elementor global colors): `GET
   /wp-json/wp/v2/elementor_library?_fields=id,title,type,status` to find kit post(s),
   then fetch each with `?context=edit&_fields=id,title,meta` and inspect
   `meta._elementor_page_settings` for color entries. In the SensiSkin case both kit
   posts were empty (`_elementor_data: ""`, `_elementor_page_settings: null`) — the
   site's real palette lived entirely in Blocksy's theme customizer, not Elementor.
   Don't assume Elementor globals exist just because Elementor is installed.
4. Distinguish **WordPress default block-editor palette colors** (pale-pink,
   vivid-red, luminous-vivid-orange, etc. — these are stock defaults present on
   almost every WP site, not brand colors) from the **theme's own palette** — grep
   output will contain both; only the `--theme-palette-color-N` / theme-specific
   variables are real signal.

Once you have candidate hex codes, identify their *role* by grep'ing the surrounding
CSS for context (`grep -oE '.{60}#hexcode.{20}' file.css`) — e.g. which color is
`--theme-button-background-initial-color` (→ primary CTA color) vs a generic palette
slot (→ likely a secondary/background accent).

If the owner asks for a color that **isn't** in the real extracted palette (e.g. "a
darker green variant" when the real palette has no green), say so explicitly, propose
the closest sensible substitute, and let them correct you rather than silently
inventing a color and presenting it as if it came from the brand.

---

## 3. HTML report design system

Base every new report on the working template at
[references/report-template.html](references/report-template.html) — it has the full
CSS system already wired up correctly (see Section 4 for why it's structured this
way). Key structural classes:

- `.cover` — full-bleed title page (only page 1 should look like this).
- `.hero-stat` — the one big highlighted stat block for the Executive-Summary-now-called-Rezime section.
- `.kpi-grid` / `.kpi` — 4-across small stat tiles.
- `.chart-card` — wraps a bar chart (see Section 3a) plus its title.
- `.month-block` / `.checklist` — the "what we did" chronological cards.
- `table` / `.badge` — data tables with colored pill badges for status (`.badge.up`,
  `.badge.new`, `.badge.stable`).
- `.alert-box` (`.success` / `.gold` variants) — pull-quote / callout boxes.
- `.unit` — **critical wrapper class**, see Section 4. Every heading must be grouped
  with the content that must stay with it (its intro paragraph, its chart, its table)
  inside a `.unit` div.
- `.footer` — stays `display:none` in the stylesheet; the *visible* footer copy is
  injected only onto the true last page by the finishing script (Section 4d) — do not
  try to make this visible via CSS alone.
- `.phrase-table` (`tr.hot` modifier) — the §1.11/§1.12 "Top pretrage ovog meseca"
  component: a compact two-column mini-table, phrase + current position, no other
  columns. Add `.hot` to the `<tr>` for a phrase that's new or jumped significantly
  this month — the row gets bold text, the brand-accent color, and a small flame
  marker next to its position. Lighter-weight than the full multi-column pre/posle/
  pomak comparison table, but **keeps the real position number** — the owner wants
  to see her strong positions, not just an unnumbered phrase list.

- `.src-list` / `.src-row` / `.src-track` / `.src-fill` — horizontal "where did the
  visitors come from" bars (§1.13). One row per platform: label, proportional track,
  value on the right. Widths are percentages of the largest row, not of the total, so
  the top platform always fills the track. Use `.src-fill.gold` for the smaller rows so
  the dominant channel reads first.

### 3a. Charts

Simple div-based bar charts (see `.bars`, `.bar-col`, `.bar-shape`, `.bar-val`,
`.bar-lbl` in the template) are enough for a monthly-trend report — no charting
library needed. Load the `dataviz` skill before building any chart to sanity-check
form/color choices even for these simple bars (one hue per metric, direct value
labels, thin bars, rounded top corners, baseline-anchored).

---

## 4. PDF generation pipeline (read this before generating any PDF)

**Do not use `chrome --headless --print-to-pdf` directly for a multi-page report with
grouped/unbreakable content blocks.** Chromium's native print engine has a real bug:
combining `break-after: avoid` on a heading with `break-inside: avoid` on the very next
sibling — especially when that sibling is a CSS grid/flex container (`.kpi-grid`,
`.cover`) — silently inserts a spurious fully-blank page. This cost an entire debugging
round in the original session before the cause was found. The fix that actually works:

### 4a. Use Paged.js instead of Chromium's native pagination

Add `<script src="https://unpkg.com/pagedjs/dist/paged.polyfill.js"></script>` before
`</body>`. This is a real CSS Paged Media implementation done in JS — it lays the whole
document out into fixed-size `.pagedjs_page` divs *before* any printing happens, so the
final print/PDF step just reproduces an already-correct layout instead of relying on
Chromium's own (buggy) native fragmentation logic. This one change fixed the blank-page
bug, heading-orphan problem, and table-splitting problem simultaneously.

```css
@page {
  size: A4;
  margin: 16mm 14mm 20mm 14mm;
}
@page :first {
  margin: 0;   /* lets a full-bleed cover page touch all four edges — natively supported */
}
```

**`@page :last` is NOT supported by Paged.js** (only `:first`/`:left`/`:right`/`:blank`
are implemented) — a rule scoped to `:last` silently never fires. Do not rely on it.
See 4d for how "only on the last page" is actually achieved.

### 4b. Group every heading with its content in a `.unit` wrapper

```css
.kpi, .hero-stat, .chart-card, .month-block, .alert-box, table, tr, .unit {
  break-inside: avoid;
}
```

Wrap `<h2>`/`<h3>` + the paragraph/chart/table that must stay with it in a single
`<div class="unit">...</div>`. This is what actually solves "heading stranded at the
bottom of a page" and "chart on one page, its caption text on the next" — **not** a
`break-after: avoid` on the heading tag itself (that's the combination that triggers the
Chromium blank-page bug in 4a; the `.unit` wrapper achieves the same "keep together"
goal safely under Paged.js). Do this for every section: Rezime+hero-stat, each chart
+ its intro/outro paragraph, each table + its intro paragraph, Zaključak + its closing
alert-box.

Adding `table { break-inside: avoid; }` is safe and necessary under Paged.js — under
native Chromium printing this same rule was one of the blank-page triggers; under
Paged.js it correctly keeps an entire table (even 10+ rows) on one page instead of
splitting rows across a page boundary.

### 4c. Match horizontal padding across the whole document

The cover (`.cover`) and the main content wrapper (`.container`) must use the **same**
left/right padding value. If they don't, cover text and body text will start at visibly
different left margins, and the report will look misaligned on page 1 specifically.
Also: give `.container` generous padding (around 55-60px, not a tight 40px) — loose
paragraphs that aren't inside a card/box will otherwise visually stretch edge-to-edge
compared to boxed elements (`.chart-card`, `.alert-box`, `.kpi`), which reads as
inconsistent/uncentered even though nothing is technically broken.

### 4d. The last-page-only, true-bottom footer (the hard part)

A footer that must appear **only on the physically last page**, spanning the **full**
page width, sitting exactly at the bottom edge, cannot be done with CSS alone (no
`:last` support, and the native `@bottom-center` margin box is only about a third of
the page width — a full sentence wrapped into that narrow box overflows the margin
box's height and gets silently clipped off-canvas, which is a second real bug
encountered in the original session: the footer text was present in the DOM but
invisible because it overflowed its container).

The actual working solution: **generate the PDF via puppeteer-core, not the plain
Chrome CLI**, so you can script a post-render finishing step:

1. Load the HTML in a real (puppeteer-controlled) browser, `waitUntil: 'networkidle0'`.
2. `await page.waitForSelector('.pagedjs_pages')` then an extra ~1.5s settle delay —
   Paged.js needs a moment after that selector appears to finish internal layout.
3. In `page.evaluate()`: grab `document.querySelectorAll('.pagedjs_page')`, take the
   **last** one, create a new `<div class="final-footer-bar">` with the real `.footer`
   element's `innerHTML`, and append it **directly into that last `.pagedjs_page`
   element** (not into its `.pagedjs_margin-bottom-center` margin box) with:
   ```js
   if (getComputedStyle(last).position === 'static') last.style.position = 'relative';
   bar.style.position = 'absolute';
   bar.style.left = '0'; bar.style.right = '0'; bar.style.bottom = '0'; bar.style.width = '100%';
   ```
   This makes it span the true full page width and sit flush with the true bottom
   edge, appearing on that one page only.
4. Then `await page.pdf({ path, printBackground: true, preferCSSPageSize: true,
   margin: {top:0,bottom:0,left:0,right:0} })` — zero extra margin here because
   Paged.js has already baked the `@page` margins into its own layout; adding
   Puppeteer's own default margin on top would double them up.

The full working script is at
[references/build-pdf-report.js](references/build-pdf-report.js) — copy and adapt the
file paths, don't rewrite it from scratch.

### 4e. Verifying pagination before calling it done

**Never assume a PDF is correct just because Chrome generated one without an error.**
Verify visually, page by page, using the same puppeteer session:

```js
const pages = await page.$$('.pagedjs_page');
for (let i = 0; i < pages.length; i++) {
  const box = await pages[i].boundingBox();
  await page.screenshot({ path: `page-${i+1}.png`, clip: box });
}
```
Then actually look at a handful of the resulting images (first page, a middle page with
a chart/table, and the last page with the footer) before telling the owner it's fixed.
A `chrome --headless --screenshot` of the **exported PDF file itself** does not
reliably work in this environment (headless Chrome's built-in PDF viewer plugin does
not render inside a headless screenshot — you get a tiny near-blank image back). Always
verify against the **live HTML DOM** (post-Paged.js, pre-export) — puppeteer's
`page.pdf()` captures that same DOM state faithfully, so verifying the DOM screenshot is
equivalent to verifying the PDF.

---

## 5. Environment / tooling pitfalls (Windows + Git Bash + sandboxed Bash tool)

- **GUI apps and file writes may need `dangerouslyDisableSandbox: true`.** The default
  sandboxed Bash tool can run in an isolated filesystem view — a PDF written from a
  sandboxed shell and a `chrome.exe` launched from that same sandboxed shell can each
  work "successfully" while the user's real, visible desktop Chrome still reports
  `ERR_FILE_NOT_FOUND` / "file couldn't be accessed" for the same path. If the user
  says a file you just wrote or an app you just launched doesn't work on their end even
  though your own commands reported success, re-run the write/launch with
  `dangerouslyDisableSandbox: true` before debugging anything else.
- **GA4 via MCP fails with an SSL handshake error while GSC keeps working.** Symptom:
  `get_capabilities` reports `ga4.ok: false` with
  `503 ... Ssl handshake failed (TSI_PROTOCOL_FAILURE) ... CERTIFICATE_VERIFY_FAILED:
  unable to get local issuer certificate`, and every `ga4_*` tool errors out, while all
  `gsc_*` tools are fine. **Root cause (diagnosed 2026-08-04): AVG Antivirus's
  "Web/Mail Shield" intercepts TLS and re-signs it with its own root CA.** That root is
  installed in the Windows certificate store, so Python's `ssl` module (and therefore
  GSC, which goes over REST) trusts it, but the **GA4 Data API client uses gRPC, whose
  BoringSSL reads its own bundled `roots.pem` and never consults the Windows store** so
  it rejects the intercepted certificate. `reload_credentials` does nothing for this;
  it is not an auth problem at all.
  Confirm it in one command before assuming anything else:
  ```bash
  python -c "import ssl,socket; ctx=ssl.create_default_context(); s=ctx.wrap_socket(socket.socket(), server_hostname='analyticsdata.googleapis.com'); s.connect(('analyticsdata.googleapis.com',443)); print(s.getpeercert()['issuer'])"
  ```
  If the issuer is an antivirus rather than a real Google CA, this is the bug. The fix
  (already applied on this machine, `~/.claude.json` → `mcpServers.google-seo-mcp.env`)
  is to append the AV root to the bundles gRPC and requests actually read:
  `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` → grpc's `roots.pem` + AV root, and
  `SSL_CERT_FILE` / `REQUESTS_CA_BUNDLE` → certifi's `cacert.pem` + AV root, both
  written to `C:\Users\Marko\.local\certs\`. **The env change only takes effect after
  the MCP server restarts**, so to finish the current session run GA4 queries directly
  through the MCP's own venv python
  (`C:\Users\Marko\pipx\venvs\google-seo-mcp\Scripts\python.exe`) with those same env
  vars exported, using `BetaAnalyticsDataClient` / `AnalyticsAdminServiceClient`. If the
  AV is ever reinstalled its root cert changes and the bundles must be rebuilt.
  SensiSkin GA4 property is `properties/532419831` ("Kozmetološki Centar").
- **JS string literals with Windows paths need double backslashes.** `'C:\Program
  Files\...'` inside a single-quoted JS string silently drops every backslash before a
  non-special character (`\P`, `\G`, `\C`, etc. all just become the letter), corrupting
  the path into something like `C:Program FilesGoogleChromeApplicationchrome.exe`. Always
  write `'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'`. Prefer the
  **Write tool** over Bash heredocs for generating `.js` scripts — heredoc quoting
  through Git Bash is an extra layer that has silently mangled escaped backslashes in
  this project before; Write puts the exact bytes you intend into the file.
  Puppeteer's own error message (`Browser was not found at the configured
  executablePath (C:Program Files...)`, note the missing backslashes) is the tell-tale
  sign this has happened again.
- **A PDF open in a Chrome tab locks the file on Windows.** Regenerating to the exact
  same path fails with "Device or resource busy" / "process cannot access the file."
  During active iteration, write to a new suffixed filename each round (`-v2`, `-v3`,
  ...) rather than fighting the lock, and only rename to the clean canonical filename
  once the owner confirms they've closed the old tab.
- **puppeteer-core, not puppeteer**, and point it at the real installed Chrome via
  `executablePath` — no need to download a second bundled Chromium. Install into the
  session's scratchpad directory, not the client project folder:
  `npm install --prefix <scratchpad-dir> puppeteer-core --no-save`.
- Loading Paged.js from `unpkg.com` requires outbound network access from the
  browser process — confirmed working in this environment (`curl` to unpkg.com
  returned a live redirect), but if a future environment has no internet access,
  download `paged.polyfill.js` once and reference it as a local `<script src="./paged.polyfill.js">`
  instead.

---

## 6. Checklist for a new report

1. Read this file end to end.
2. Confirm the reporting period(s) and pull real data (GA4/GSC/whatever source) —
   month by month, not uneven blocks. Stop and ask if there's a real data gap (§1.7).
3. Check for any blog post(s) published since the last report and pull their own
   analytics (GA4 landing-page data, GSC per-URL data) — each gets its own
   subsection (§1.9).
4. Extract the client's real brand palette (§2) if this is a new client or the brand
   has changed since the last report.
5. Copy [references/report-template.html](references/report-template.html), swap in
   the palette, content, and numbers. Keep every heading wrapped in `.unit` with its
   content (§4b). Keep content wins-only (§1.3); recommendations go to the owner in
   chat.
6. Write for the brand owner, not for a marketer (§1.8): growth numbers and blog/
   keyword content prominent, technical SEO work reduced to one summary line per
   item. Add the keyword-to-content-ideas bridge for her Instagram planning (§1.10).
7. `grep -n "—"` the finished HTML — must return nothing (§1.2).
8. Generate the PDF via [references/build-pdf-report.js](references/build-pdf-report.js)
   (§4), not the plain Chrome CLI.
9. Verify page-by-page via puppeteer screenshots (§4e) before telling the owner it's
   ready — check page 1 (cover alignment), a chart/table page, and the last page
   (footer position, full width, flush bottom).
10. Open the result for the owner with `dangerouslyDisableSandbox: true` (§5).
11. If the owner corrects anything — content rule, color, pagination behavior — **add
    the correction to this file** before closing the session, so the next report
    starts from the fixed state instead of repeating the same round-trip.
