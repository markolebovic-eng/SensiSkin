---
name: wordpress-edit
description: When the user wants to run SEO/GEO optimization directly on the live SensiSkin WordPress site (sensiskinstudio.com) via the REST API — reading or changing title tags, meta descriptions, focus keyphrases, page/post body content, FAQ schema, or creating new blog posts. Also use when the user mentions "wordpress edit," "izmeni na sajtu," "primeni na WordPress," "novi blog post," "ubaci FAQ semu," "izmeni title/meta na sajtu," or references a specific page/post ID/URL to edit live. This skill is the only one in this project authorized to write to the live WordPress site — seo-audit and schema skills analyze and recommend, this skill executes. Requires WP_SITE_URL, WP_USERNAME, WP_APP_PASSWORD in the project's local `.env` file (never committed, never printed).
metadata:
  version: 1.0.0
---

# WordPress Edit (SensiSkin live-site SEO/GEO execution)

You are executing SEO/GEO changes directly on the live sensiskinstudio.com WordPress
site via the REST API using Application Password (Basic Auth) credentials. This is
the **only** skill in this project with write access to the live site. Every other
SEO skill (seo-audit, schema, ai-seo) produces recommendations on paper — this one
applies them, carefully, with the owner's explicit sign-off.

This playbook was written after a real session doing exactly this work on
`/leto-i-promene-na-kozi/` (post 2047) — every rule below exists because something
broke, looked wrong, or needed a decision in that session. Read it end to end
before touching a live page; skipping steps here means redoing them live.

**Division of labor**: the `seo` agent does not have Bash access (deliberately —
its tool list is MCP/read-focused) and therefore cannot run the `curl` commands
in this skill itself. The `seo` agent's job when this skill is invoked is the
*analysis and proposal* half — cross-referencing MEMORY.md, picking keyphrases,
drafting FAQ content, deciding what needs to change and why. The main
orchestrator (or whoever has Bash in the current conversation) is the one who
actually authenticates, fetches, patches, and verifies against the live site per
Sections 1C–1F below. If you are the `seo` agent reading this: produce the
proposal, then hand the concrete before/after values back to the orchestrator to
execute — don't attempt the curl steps yourself.

---

## 0. Non-negotiable rules (read before doing anything else)

1. **NEVER change a URL/slug.** Ever. Not even to "improve" it. A slug change on an
   already-indexed page requires a 301 redirect plan, a GSC re-validation cycle,
   and risks the page's existing rankings — that is a separate, much bigger
   decision the owner must make explicitly and separately from routine SEO/GEO
   work. If a keyphrase would benefit from being in the slug, note it as a
   flagged, deferred item — do not act on it.
2. **Always propose before applying.** For every page: show the owner the current
   value and the proposed new value (title, meta description, keyphrase, body
   copy, FAQ content) in a clear before/after format, and wait for explicit
   approval — even if a previous page in the same session was already approved.
   Do not assume blanket approval carries across pages unless the owner says so
   explicitly ("uradi sve", "primeni sve odobreno", etc.).
3. **Never print WP_APP_PASSWORD (or any credential) anywhere** — not in command
   text shown to the user, not in files, not in commit messages. Load it into a
   shell variable via `source .env` and reference `$WP_APP_PASSWORD` in curl's
   `-u` flag; never echo it.
4. **Never edit files inside the git repo to store credentials or site data
   pulled from the API.** All working files (fetched JSON, backups, generated
   payloads) go in the scratchpad temp directory, not the project folder.
5. **Always back up before overwriting.** Before any content or `_elementor_data`
   write, save the current live value to a local scratch file first. If
   something breaks, you need the exact prior state to restore it.

---

## 1. Standard workflow order

### Step A — Run the `analytics` agent first, not last

Before proposing any title/meta/keyphrase change, get the `analytics` agent (or
call the relevant `mcp__google-seo-mcp__ga4_*` / `gsc_*` tools directly if you're
the orchestrator) to answer:

- What are people actually searching to find this page or similar pages
  (`gsc_search_analytics` with `dimensions: ["query"]`, filtered/grepped to the
  page's URL via `dimensions: ["query","page"]`)?
- Is this page under-performing on CTR for its current ranking position
  (`gsc_ctr_opportunities`)?
- Is there content decay (`gsc_content_decay`, `ga4_content_decay`) suggesting
  the page needs a refresh, not just a meta tag tweak?
- What does GA4 say about actual on-page engagement for this URL
  (`ga4_query` with `pagePath` dimension)?

**Do not skip this and go straight to "the title looks short, let me lengthen
it."** The whole point of doing this live, on a real site, instead of writing a
generic proposal doc, is that you have real search-intent data available —
use it. A keyphrase choice that isn't grounded in what GSC shows people actually
type is a guess, not SEO.

### Step B — Cross-reference MEMORY.md before inventing anything

`.agents/clients/sensiskin/memory/MEMORY.md` contains a **Master Keyword Table**
with previously-approved focus keyword + title + meta description assignments
for many pages, plus a full history of past SEO/GEO audits, known cannibalization
risks, and content decisions (e.g. which topics are already covered by which
blog post — check before assigning a keyphrase that collides with an existing
post). If a page already has an approved assignment in that table:
- Check whether the LIVE title/description actually matches the approved
  version (fetch via `yoast_head_json`, compare byte-for-byte, not "looks
  similar").
- If it doesn't match, that's priority #1 — implement what was already decided,
  don't re-litigate the keyword choice.
- If it does match but is truncated (a very real, previously-found bug — 6
  pages had their approved meta description cut off mid-sentence from a
  copy-paste error), fix the truncation, don't invent new copy.

Only propose a genuinely NEW keyphrase/title/description for pages that have no
prior Master Table entry, and always check the new choice against:
- Every other assigned keyword in the Master Table (no duplicate targeting)
- Every existing blog post topic (no content cannibalization — e.g. don't reuse
  "letovanje" as a keyphrase root if another post already targets
  "tretmani...pre i posle letovanja")

### Step C — Authenticate and pull current state

```bash
set -a
source .env
set +a

curl -s --ssl-no-revoke -u "$WP_USERNAME:$WP_APP_PASSWORD" \
  -H "Accept: application/json" \
  "${WP_SITE_URL%/}/wp-json/wp/v2/users/me?context=edit"
```

Confirm `roles` includes `administrator` (or at minimum `edit_posts`/`edit_pages`)
before doing anything else. If this fails, stop — do not attempt writes with
broken auth.

`--ssl-no-revoke` is required on this Windows/Git-Bash setup — plain `curl`
fails with a schannel revocation-check error otherwise (unrelated to WordPress).

For any page/post, pull the full editable record:

```bash
curl -s --ssl-no-revoke -u "$WP_USERNAME:$WP_APP_PASSWORD" \
  "${WP_SITE_URL%/}/wp-json/wp/v2/pages/{ID}?context=edit&_fields=id,slug,status,title,content,meta,yoast_head_json" \
  -o scratch/page-{ID}.json
```

Yoast SEO exposes the **computed, final** title/description via
`yoast_head_json.title` / `.description` — this is what Google will actually use,
more reliable than reading the raw `_yoast_wpseo_title` meta field alone for
verification (though you write to the raw `_yoast_wpseo_*` meta fields, you
verify against `yoast_head_json` after).

### Step D — CRITICAL: check for Elementor before writing anything

```python
meta = data["meta"]
edit_mode = meta.get("_elementor_edit_mode")  # 'builder' means Elementor renders this page
elementor_data = meta.get("_elementor_data")  # JSON string, present if Elementor is active
```

**If `_elementor_edit_mode == "builder"`, the WordPress core `content` field is
NOT what gets displayed.** Elementor stores its own copy of the page in the
`_elementor_data` JSON meta field (a nested array of `elements` → `settings`, often
including a "text-editor" widget whose `settings.editor` field contains the SAME
Gutenberg-block HTML as `content` — a duplicate copy Elementor renders instead).

This means: **any body-text edit (keyphrase insertion, subheading changes, FAQ
block, internal/outbound links, alt text) must be applied to BOTH**:
1. The WP core `content` field (so `content.raw`/`content.rendered` stays in
   sync — some things, like Yoast's own analysis in wp-admin, may read this), **and**
2. The matching text inside the parsed `_elementor_data` JSON (this is what
   actually renders on the frontend for Elementor-managed pages)

To edit inside `_elementor_data` safely:
```python
import json
elements = json.loads(meta["_elementor_data"])  # parse
# walk the structure to find the widget with the target text — for a simple
# single "text-editor" widget page, it's typically elements[0]["elements"][0]["settings"]["editor"]
# but CONFIRM the exact path per page by searching for a known substring first,
# don't assume the path is identical on every page.
old_text = elements[0]["elements"][0]["settings"]["editor"]
new_text = old_text.replace(exact_old_string, exact_new_string, 1)  # exact string match, count=1
elements[0]["elements"][0]["settings"]["editor"] = new_text
new_elementor_raw = json.dumps(elements, ensure_ascii=False)  # ensure_ascii=False keeps it human-readable, WP accepts it fine — it's just a different valid JSON encoding than what Yoast/Elementor originally wrote (raw UTF-8 chars instead of \uXXXX escapes), confirm no data loss by comparing key counts before/after, not just string length
```

Never do a blind full-content regex rewrite across the whole `_elementor_data`
blob — locate the exact widget/field first, replace one exact substring with
`.replace(old, new, 1)` (count=1, so you never accidentally replace more than
one occurrence), and verify the JSON still parses and has the same structural
key count before writing it back.

PATCH via:
```bash
curl -s --ssl-no-revoke -u "$WP_USERNAME:$WP_APP_PASSWORD" \
  -X POST -H "Content-Type: application/json" \
  --data-binary @payload.json \
  "${WP_SITE_URL%/}/wp-json/wp/v2/posts/{ID}?context=edit"
```
where `payload.json` contains `{"content": "...", "meta": {"_elementor_data": "..."}}`
built via Python's `json.dump(..., ensure_ascii=False)` to a file (avoids shell
quoting/escaping issues with Serbian diacritics entirely — never try to inline
JSON with Cyrillic/Latin diacritics directly in a `-d` flag).

### Step E — Clear Elementor's render cache after every write

Elementor caches its compiled CSS/HTML and does **not** regenerate it just
because the underlying data changed via the API (only saving through the visual
editor normally triggers that). After every write to an Elementor-managed page,
ask the owner to click **Elementor → Tools → General → "Clear Files and Data"**
(labelled "Clear Files and Data" / "Regenerate CSS & Data" depending on version).
If a separate page-cache plugin (WP Rocket, LiteSpeed, etc.) or CDN is active,
its cache may also need clearing — check if the frontend still shows stale
content after the Elementor cache clear before assuming the write failed.

### Step F — Verify against the LIVE frontend, not just the API response

The API PATCH response echoing back your new values only proves the database
was updated — it does NOT prove the frontend shows it (see Step E). Always do a
final check with a raw `curl` fetch of the actual public URL and grep for the
expected text/tags:

```bash
curl -s --ssl-no-revoke -L "https://sensiskinstudio.com/{slug}/" -o scratch/verify.html
grep -o "<title>.*</title>" scratch/verify.html
grep -c "expected-new-text-fragment" scratch/verify.html
```

Do this after every meaningful change, not just once at the end of a batch.

### Step G — Always end with a "request indexing" link list for the owner

There is no real bulk API for "request indexing" on ordinary pages — the URL
Inspection API is read-only, and the Indexing API
(`mcp__google-seo-mcp__google_indexing_publish`) is officially restricted to
`JobPosting`/`BroadcastEvent` content; using it for regular pages risks losing
API access and should not be done here (a standing decision from an earlier
session — see MEMORY.md GSC indexing audit entries). So the owner must click
"Request Indexing" manually in the GSC UI for each changed URL.

**Every time you finish optimizing one page, or a batch of several pages,**
close out with a plain list of the exact live URLs touched, ready to paste into
GSC's URL Inspection tool one at a time:

```
Zatraži indeksiranje za sledeće stranice (GSC → URL Inspection → nalepi URL → Request Indexing):
1. https://sensiskinstudio.com/{slug-1}/
2. https://sensiskinstudio.com/{slug-2}/
...
```

Do this even for a single-page session — don't skip it just because it's only
one URL. If a page's edit included a genuine content/structure change (not just
a meta tag tweak), mention that in the list too, since content changes benefit
more from a fresh crawl than a pure metadata change does.

---

## 2. What to check and fix, in priority order

### Writing style rule: no em dashes, no AI-sounding phrasing

When writing or editing **title tags, meta descriptions, and focus
keyphrases**, avoid the em dash ("—") entirely — use a comma, colon, period,
or a regular hyphen ("-") instead, matching how the existing human-written
copy on this site is punctuated. Also avoid generic AI-sounding phrasing
(stock transitions, hollow intensifiers, corporate-brochure tone) — the goal
is copy that reads like a person wrote it, per the site's established brand
voice (`.agents/clients/sensiskin/product-marketing.md`,
`.agents/clients/sensiskin/brand-voice-script.md`) and every naming/tone rule
already logged in MEMORY.md (no superlatives, no overclaiming, fair-balance
phrasing). Run the `stop-slop` skill's checklist mentally (or invoke it) on
any title/meta/keyphrase text you draft before proposing it — this applies
even to short strings, not just full body copy.

This is the full checklist, transcribed directly from the actual Yoast panel
(both the "SEO" and "Čitljivost"/Readability tabs) after the owner shared
screenshots of exactly what it flags. Go through **every item below** for
every page/post this skill touches — don't wait to be told which ones failed.
Use `yoast_head_json` and raw content/regex checks to verify each one
programmatically before declaring a page done; you do not have visual access
to the live Yoast panel, so these checks are your only ground truth — be
rigorous about them rather than eyeballing "looks about right."

### SEO tab

- **Odlazne veze (outbound links)** — at least one. Red/critical if zero.
- **Interne veze (internal links)** — at least one. Red/critical if zero. (A
  real session shipped a fully-optimized post with zero links of either kind
  and it wasn't caught until the owner asked afterward — grep for `<a\s+href="`
  before ever declaring a post done; a zero count is not optional to fix.)
- **Ključna fraza u uvodu (keyphrase in intro)** — must appear, literally, in
  the **first** `<p>` tag of the content — not "early in the post," not
  "the paragraph that feels like the real intro." Count paragraph blocks and
  confirm which one is genuinely first before inserting; a real session
  mistake put the phrase in paragraph 2 while paragraph 1 (a rhetorical-
  question opener) had nothing, and Yoast didn't count it.
- **Gustina ključnih fraza (keyphrase density)** — appears **3+ times** in body
  text for a typical post length (Yoast scales the minimum with word count —
  longer text needs more repetitions; treat 3 as the floor, not the target).
  Must be the literal phrase. **Serbian-specific pitfall**: insert the
  keyphrase in its exact nominative form (matching `_yoast_wpseo_focuskw`), not
  a grammatically natural declined case. "uveli smo Dermalux LED lampu"
  (accusative) does NOT literal-match keyphrase "dermalux led lampa"
  (nominative) even though it reads naturally. Restructure the sentence to keep
  the phrase in nominative (e.g. as an appositive/named label: "uveli smo
  tretman Dermalux LED lampa") rather than accept a fluent sentence that
  silently fails the check.
- **Ključna fraza u SEO naslovu (keyphrase in SEO title)** — this is stricter
  than "the keyphrase appears somewhere in the title": Yoast wants **every
  word** of the keyphrase present, ideally as an **exact contiguous match**,
  and flags it if the words are scattered or only partially present (e.g.
  keyphrase "unapređena nega lica" needs all of "unapređena," "nega," and
  "lica" in the title, together). It also specifically recommends putting the
  keyphrase **at the very start of the title** for the best score, not buried
  mid-title or at the end.
- **Ključni izraz u meta opisu (keyphrase in meta description)** — the full
  phrase, not just one word from it, must appear in the description text.
- **Ključna fraza u podnaslovima (keyphrase in subheadings)** — needs an actual
  `<h2>`/`<h3>` tag, not a bold paragraph. See the visual-consistency caveat
  below — don't break the post's established heading style just for this one
  checkmark.
- **Ključna fraza u ALT atributima slika (keyphrase in image ALT text)** —
  at least the most relevant image(s) should have alt text containing the
  keyphrase or a close natural variant. First confirm the image itself
  actually loads (`curl -o /dev/null -w "%{http_code}"` on the `src`) — this
  site has had genuinely broken image references (empty `<figure></figure>`
  with no `<img>` inside, `<img>` tags pointing to 404 files) that predate your
  edits; if found, confirm it was already broken (check your pre-edit backup),
  then remove the broken image block entirely rather than adding alt text to a
  dead image.
- **Dužina meta opisa (meta description length)** — Yoast flags **both**
  directions: too long (roughly over ~156 characters, gets truncated in
  search results) **and too short** (under ~120 characters — flagged as a
  wasted opportunity, "imate 156 karaktera na raspolaganju, koristite ih").
  The real target range is **~120–156 characters**, not just "under 156."
- **Dužina ključne fraze (keyphrase length)** — the keyphrase itself shouldn't
  be a single generic word (too short/broad) nor an unnaturally long string
  (too specific/no one searches the whole thing). A 2-4 word phrase grounded
  in real search language (per Section 1 Step A) is the right zone.
- **Prethodno korišćena ključna fraza (previously used keyphrase)** — the exact
  keyphrase must be **unique across the entire site** — Yoast checks this
  automatically and flags reuse. This reinforces (at the plugin-mechanics
  level) the cannibalization cross-check already required in Section 1 Step B
  against the Master Keyword Table and existing post topics — a duplicate
  keyphrase fails both Yoast's own check AND the site's content strategy.
- **Jedan naslov (single H1)** — the page must have exactly one `<h1>`. Be
  careful here if you ever do add a real heading block for the subheading
  check above — confirm you're adding an `<h2>` (or `<h3>`), never accidentally
  introducing a second `<h1>`.
- **Ključni izraz u podlošku (keyphrase in the slug)** — Yoast checks whether
  more than half the keyphrase's words appear in the URL slug. **This is
  informational only for existing pages — never change an existing slug to
  satisfy it (rule 0.1 overrides this Yoast check, always).** For **brand-new**
  posts (Section 4), choose the slug with the keyphrase in mind from the start
  so this passes naturally without ever needing a later change.
- **Konkurentne veze (competing links)** — Yoast flags it if any link's anchor
  text elsewhere on the page uses this page's own keyphrase (or a synonym) to
  point to a *different* page — that dilutes/competes for the ranking signal
  this page is trying to own. When adding the required internal links (above),
  use anchor text describing the destination page's own topic, not this page's
  keyphrase, e.g. link the word "Akne" or "vrste akni" to the acne post, don't
  link the phrase "dermalux led lampa" itself out to another page.
- **Dužina teksta (word count)** — needs a substantive minimum (roughly 300+
  words as a floor; Yoast rates longer/more thorough content as "odličan
  posao" — 700+ words scored well in a real session). Very short posts/pages
  will get flagged here independent of everything else.
- **Širina SEO naslova (SEO title width)** — this is a **pixel-width** check,
  not purely a character count — some characters are wider than others, so a
  title could be flagged even under 60 characters if it uses wide letters, or
  pass slightly over 60 if narrow. Treat the 50–60 character guideline as an
  approximation; if Yoast's own width meter is visible, trust it over a raw
  `len()` count.

### Readability tab (separate from the SEO tab — check both)

- **Distribucija podnaslova (subheading distribution)** — flagged if a fairly
  long post uses **no subheadings at all** structurally (independent of
  whether they contain the keyphrase — this is about reading structure, not
  SEO targeting). If a post is long and has zero subheadings of any kind,
  recommend adding several, distributed through the text, matching whatever
  heading style convention that post already uses (see the visual-consistency
  note above).
- **Dužina rečenica (sentence length)** — Yoast flags it if more than ~25% of
  sentences exceed 20 words. If flagged, shorten the longest/most complex
  sentences rather than doing a wholesale rewrite.
- **Dužina paragrafa (paragraph length)** — flags any single paragraph that's
  too long (a wall of text). Break up dense paragraphs if flagged.

### Visual-consistency caveat (applies to the subheading checks above)

Converting a bold pseudo-heading (`<p><strong>...</strong></p>`) to a real
`<h2>`/`<h3>` satisfies the "keyphrase in subheading" and "subheading
distribution" checks, but a real heading tag typically inherits the theme's
default heading font-size/weight — which will look visually inconsistent if
every OTHER subheading on that same post (or across the blog generally) is
styled as a bold paragraph instead. **If every other subheading on the site's
blog is a bold paragraph, do NOT convert just one page's heading to a real
`<h2>` for the sake of the Yoast checkmark** — visual consistency with the
site's established pattern wins over one checklist item. Flag the tradeoff to
the owner if genuinely unsure; don't silently pick the "more correct" SEO
option if it breaks the page's look.

### Site-wide subheading style standard: bold, never italic

The owner has set an explicit, site-wide pseudo-heading standard: subheadings
must be **plain bold** — `<p><strong>Tekst</strong></p>` — matching
`/leto-i-promene-na-kozi/` as the reference page. **Never leave (or introduce)
italic in a subheading**, whether as pure `<p><em>Tekst</em></p>` (found on the
Dermalux post) or the mixed `<p><em><strong>Tekst</strong></em></p>` /
`<p><strong><em>Tekst</em></strong></p>` forms (found on the
"posledice-starenja-na-kozi" post — note real posts have used both orderings,
so check for both when searching). This is a real, recurring inconsistency
across older posts — **check every post's subheadings for stray `<em>` tags as
a standard part of every optimization pass**, even when the post's other
SEO/GEO work is otherwise unrelated to headings, and convert them to plain
bold. Use a regex substitution rather than literal string matching, since
exact whitespace (including `\xa0` non-breaking spaces) inside these tags
varies unpredictably between posts:
```python
import re
text = re.sub(r'<p><em><strong>(.*?)</strong></em></p>', r'<p><strong>\1</strong></p>', text)
text = re.sub(r'<p><strong><em>(.*?)</em></strong></p>', r'<p><strong>\1</strong></p>', text)
text = re.sub(r'<p><em>(.*?)</em></p>', r'<p><strong>\1</strong></p>', text)
```
Run all three substitutions (order doesn't matter, each targets a distinct
pattern) and verify the "before" count matches converted count before writing
back. Apply this to both `content` and `_elementor_data` if Elementor is
active (Step D) — a fix applied only to `content` will not appear on the live
Elementor-rendered frontend, same as any other body-text edit.

### Verifying rendered output: search broadly, not by a fixed tag guess

When verifying a live change by fetching the frontend HTML and grepping for an
expected tag, **don't assume the exact attribute/class wrapping the text** —
real WordPress output includes classes like `<p class="wp-block-paragraph">`
that a naive `<p><strong>...` grep will miss even though the fix is correctly
live. If a verification grep comes back empty, before concluding the fix
failed: search for the plain text fragment alone (no surrounding tag
assumptions) and print the actual surrounding context to see the real markup,
rather than iterating on slightly different tag-guess patterns. Also be aware
that the same text may appear multiple times in the raw HTML for unrelated
reasons (once in the real rendered body, once inside a JSON-LD `articleBody`
string as escaped plain text, possibly once more inside an FAQ schema
question/answer) — match on the version wrapped in real HTML tags, not the
JSON-LD copy, when checking for a specific tag/style.

---

## 3. FAQ schema (GEO/AI-search optimization) — add to every page worked on

Per standing instruction: every page/post touched by this skill should get a
**FAQPage JSON-LD schema block** added, even though Google retired the visual
FAQ rich-result dropdown (May 2026) — the schema still has real citation value
for AI answer engines (ChatGPT, Perplexity, Google AI Overviews), which is the
whole point of doing this ("GEO"/AEO, not classic SERP rich results).

Rules for the FAQ content itself:
- **3-5 questions**, grounded strictly in claims **already made in the existing
  article body** — do not invent new facts, statistics, or claims that aren't
  already substantiated in the page's own text. This is the same fair-balance /
  no-overclaiming rule that governs all SensiSkin copy (see
  `.agents/clients/sensiskin/product-marketing.md` and the brand voice rules in
  MEMORY.md) — a fabricated FAQ answer is a factual-accuracy risk, not just a
  style one.
- Check first whether the page already has a `FAQPage` type via
  `mcp__google-seo-mcp__schema_extract_url` — don't duplicate.
- Implementation: append a `core/html` Gutenberg block containing a single
  `<script type="application/ld+json">` tag with the FAQPage schema, to the end
  of the content (both the `content` field and, if Elementor is active, inside
  `_elementor_data` per Step D). This is invisible/non-visual — it does not add
  a visible FAQ section to the page unless the owner separately asks for
  visible on-page FAQ text too (that's a content-visibility decision, different
  from just adding the schema — ask if unclear which they want).
- Verify with `mcp__google-seo-mcp__schema_validate_url` after clearing cache —
  confirm `FAQPage` appears in `types` and `successes` includes something like
  "FAQPage declares N questions", with no new `issues`.

---

## 4. Creating new blog posts (not just editing existing ones)

**Reference-page status (pending change)**: `/leto-i-promene-na-kozi/` is
currently the main reference example for structure/style (bold subheadings,
etc.) across this skill. The owner has said that the **next brand-new blog
post** created will be fully, deliberately set up as a new template, and will
then likely replace `/leto-i-promene-na-kozi/` as the go-to reference example
for all other pages. When that happens, update the references throughout this
skill file accordingly (the opening summary and Section 2's "Site-wide
subheading style standard" both currently cite `/leto-i-promene-na-kozi/` by
name) — don't assume it stays the canonical example indefinitely.

When asked to write and publish an entirely new blog post (not just edit an
existing one):
1. Do the analytics-first + MEMORY.md cross-reference from Section 1 to pick a
   keyphrase with zero collision against the Master Keyword Table or any
   existing post topic.
2. Draft body copy following the established brand voice rules already logged
   in MEMORY.md (fair-balance on home care vs. professional treatment, no
   superlatives/overclaiming, exact CTA phone format, Nataša Burka's authentic
   voice per `.agents/clients/sensiskin/brand-voice-script.md`) — this is
   normally the `copywriter` agent's job; hand off to it for the actual prose,
   then use this skill only for the technical publish step.
3. Create via `POST /wp-json/wp/v2/posts` with `status: "draft"` initially —
   **never publish directly to `status: "publish"` without the owner reviewing
   the draft first.** Set title, content (as clean Gutenberg block HTML,
   matching the site's existing bold-paragraph pseudo-heading convention unless
   told otherwise), and the `_yoast_wpseo_*` meta fields, plus a FAQ block per
   Section 3, all in the same draft-creation call.
4. Report the draft edit URL (`{WP_SITE_URL}/wp-admin/post.php?post={new_id}&action=edit`)
   back to the owner for review before ever setting status to `publish`.
5. A brand-new post has no Elementor data by default (Gutenberg content only)
   unless the owner explicitly enables Elementor for it — don't assume Step D
   applies until you've confirmed `_elementor_edit_mode` is actually set.

---

## 5. Known pitfalls from real sessions (avoid repeating these)

- **`.env` values with spaces** (WordPress Application Passwords are
  space-separated, e.g. `abcd TjkR efgh ijkl`) must be quoted in `.env`
  (`WP_APP_PASSWORD="abcd TjkR efgh ijkl"`) or `source .env` silently
  mis-parses them and later curl calls fail auth with no useful error beyond a
  stray "command not found" on the trailing word. If auth fails right after a
  fresh `.env` edit, check quoting first.
- **Windows/Git-Bash `curl` SSL errors** (`schannel: next
  InitializeSecurityContext failed: CRYPT_E_NO_REVOCATION_CHECK`) — always pass
  `--ssl-no-revoke`.
- **`/tmp` doesn't reliably resolve** in this Git-Bash-on-Windows setup for
  Python's `open()` — use the actual scratchpad Windows path
  (`C:/Users/.../scratchpad/...` or the `$SCRATCH` var if already exported)
  instead of `/tmp/...` for any file you write in bash and then read in Python
  or vice versa.
- **Python `print()` of Serbian diacritics crashes on Windows console**
  (`UnicodeEncodeError: 'charmap' codec can't encode character`) unless you set
  `PYTHONIOENCODING=utf-8` in the environment before running the script.
- **`json.dumps(..., ensure_ascii=False)` produces a shorter string** than the
  original WordPress-provided JSON (which uses `\uXXXX` escapes) — this is
  expected and harmless (just a different valid encoding of the same data),
  but verify with a key-count comparison, not a raw length comparison, before
  trusting a re-serialized JSON blob is intact.
- **`.env` files are blocked from the `Read` tool** by permission settings in
  this environment (a safety feature, not a bug) — load credentials via `source
  .env` in Bash instead, and never attempt to work around the Read block.
- **GSC's "internal links" / stale JSON-LD `SiteNavigationElement` data can lag
  behind the actual live page** — if an audit or GSC report claims a link
  exists on a page, verify with a direct raw `curl` fetch of that page's HTML
  (not `WebFetch`, which converts to markdown and loses exact tag structure)
  before proposing a content-edit fix. A stale theme-generated schema block can
  look exactly like a real dead link in aggregated reports when it isn't one.

---

## 6. Reference template

[references/elementor-safe-edit-template.py](references/elementor-safe-edit-template.py)
contains the full fetch → check-Elementor → backup → find-exact-text →
replace → verify-integrity → build-payload sequence as reusable functions with
inline curl command comments for the steps that must run in bash. Not a
runnable CLI script — copy the relevant function(s) inline per edit, adapting
the exact `old`/`new` strings to the page in hand. Use this instead of
reconstructing the pattern from scratch each session.

## 7. Related skills / agents

- **analytics** agent — run first, always, per Section 1 Step A.
- **seo-audit** skill — for the broader, non-live-editing audit (site-wide
  indexing/visibility review). This skill (`wordpress-edit`) is the execution
  arm once specific pages/posts are identified as needing changes.
- **schema** skill — general schema.org reference; this skill's Section 3 is
  the project-specific FAQPage implementation procedure.
- **copywriter** agent — for drafting new body copy / new blog posts in brand
  voice; this skill handles the technical publish step, not prose authorship.
