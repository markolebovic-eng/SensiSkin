---
name: pisanje-izvestaja
description: Use when the user asks for a client-facing progress/analytics report — SEO, marketing, or general campaign progress — as an HTML page and/or a PDF document. Also use when the user mentions "izveštaj", "napravi mi izveštaj", "PDF izveštaj", "revizija napretka", "progress report", or asks to update/regenerate an existing report of this kind. Covers: what content rules to follow, how to pull the brand's real color palette, the HTML report design system, and the specific PDF-generation pipeline (Paged.js + puppeteer-core) that avoids Chromium's native print-engine bugs. This skill is a living document — update it whenever a new report session teaches a new lesson or the owner corrects something.
metadata:
  version: 1.0.0
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
3. Extract the client's real brand palette (§2) if this is a new client or the brand
   has changed since the last report.
4. Copy [references/report-template.html](references/report-template.html), swap in
   the palette, content, and numbers. Keep every heading wrapped in `.unit` with its
   content (§4b). Keep content wins-only (§1.3); recommendations go to the owner in
   chat.
5. `grep -n "—"` the finished HTML — must return nothing (§1.2).
6. Generate the PDF via [references/build-pdf-report.js](references/build-pdf-report.js)
   (§4), not the plain Chrome CLI.
7. Verify page-by-page via puppeteer screenshots (§4e) before telling the owner it's
   ready — check page 1 (cover alignment), a chart/table page, and the last page
   (footer position, full width, flush bottom).
8. Open the result for the owner with `dangerouslyDisableSandbox: true` (§5).
9. If the owner corrects anything — content rule, color, pagination behavior — **add
   the correction to this file** before closing the session, so the next report
   starts from the fixed state instead of repeating the same round-trip.
