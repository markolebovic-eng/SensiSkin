# Output Templates — Brand Voice Extractor

Two mandatory output files. Fill every {PLACEHOLDER} — never leave one 
empty or with a generic value. If a placeholder can't be filled from the 
analysis, note why.

---

## Template A — brand-voice-script.md (Full Document)

**Location:** `.agents/clients/{CLIENT_SLUG}/brand-voice-script.md`  
**Length target:** 1500–2500 words  
**Purpose:** Primary reference for revisions and debugging. Not read on 
every task — consulted when output "doesn't sound right."

```markdown
# Brand Voice Script — {CLIENT_NAME}

Generated: {DATE}  
Posts analyzed: {POST_COUNT}  
Analysis period: {OLDEST_POST_DATE} to {NEWEST_POST_DATE}  
Source URLs:
{LIST_OF_ANALYZED_URLS_ONE_PER_LINE}

---

## 1. Reader Addressing

Dominant form: {ti / Vi / vi / no direct address / mi} — {PERCENTAGE}% of instances

Distribution:
- "ti" (familiar): {COUNT} instances across {POST_COUNT} posts
- "Vi" (formal): {COUNT} instances
- "vi" (plural): {COUNT} instances
- No direct address: {COUNT} instances
- "mi" (author + reader): {COUNT} instances

Representative opening examples:
- "{QUOTE_1}" — {SOURCE_POST_TITLE_OR_URL}
- "{QUOTE_2}" — {SOURCE_POST_TITLE_OR_URL}
- "{QUOTE_3}" — {SOURCE_POST_TITLE_OR_URL}

Notable pattern: {ONE_SENTENCE_ABOUT_ANY_SHIFTS_OR_EXCEPTIONS}

---

## 2. Post Openings

Most common opening type: {TYPE} — {COUNT} of {POST_COUNT} posts

Opening distribution:
- Direct question to reader: {COUNT} ({PERCENTAGE}%)
- Personal practice anecdote: {COUNT} ({PERCENTAGE}%)
- Client quote frame: {COUNT} ({PERCENTAGE}%)
- Myth debunking: {COUNT} ({PERCENTAGE}%)
- Statistic or research: {COUNT} ({PERCENTAGE}%)
- Direct problem entry: {COUNT} ({PERCENTAGE}%)
- Concept definition: {COUNT} ({PERCENTAGE}%)

Examples of dominant opening type:
- "{FULL_FIRST_SENTENCE_OF_POST_1}"
- "{FULL_FIRST_SENTENCE_OF_POST_2}"
- "{FULL_FIRST_SENTENCE_OF_POST_3}"

{ONE_SENTENCE_ABOUT_WHAT_THESE_EXAMPLES_HAVE_IN_COMMON}

---

## 3. Sentence Length and Rhythm

Average sentence length: {N} words  
Typical range: {MIN_TYPICAL}–{MAX_TYPICAL} words  
90th percentile (longest typical): {N} words  
Shortest emphasis sentences: {N}–{N} words

Rhythm pattern: {DESCRIPTION — e.g., "alternating medium-short-medium" 
or "consistently medium with occasional short punches"}

Short emphasis sentences (examples):
- "{SHORT_SENTENCE_1}" — {SOURCE}
- "{SHORT_SENTENCE_2}" — {SOURCE}

Punctuation habits: {DESCRIPTION — e.g., "frequent dashes for thought 
extension, rare colons, no ellipses in body text"}

---

## 4. Paragraphs

Average sentences per paragraph: {N}  
Average words per paragraph: {N}  
Maximum paragraph length observed: {N} sentences / {N} words  
Single-sentence paragraphs: {yes — describe when used / no}

Structural pattern: {DESCRIPTION — e.g., "short intro paragraph → 
medium explanatory blocks → single-sentence conclusion or CTA"}

---

## 5. Lexical Habits

### Signature words and phrases (recurring, non-generic)

{WORD_OR_PHRASE_1} — appears in {N}/{POST_COUNT} posts  
{WORD_OR_PHRASE_2} — appears in {N}/{POST_COUNT} posts  
{WORD_OR_PHRASE_3} — appears in {N}/{POST_COUNT} posts  
{WORD_OR_PHRASE_4} — appears in {N}/{POST_COUNT} posts  
{WORD_OR_PHRASE_5} — appears in {N}/{POST_COUNT} posts  
{WORD_OR_PHRASE_6} — appears in {N}/{POST_COUNT} posts  
{WORD_OR_PHRASE_7} — appears in {N}/{POST_COUNT} posts  
{WORD_OR_PHRASE_8} — appears in {N}/{POST_COUNT} posts

### Translation policy (English terms)

{DESCRIPTION — e.g., "Consistently translates: 'hidratantna krema' not 
'moisturizer', 'zaštita od sunca' not 'SPF'. Exception: retinol used 
directly (no Serbian equivalent in common use)."}

### Technical term handling

{DESCRIPTION — e.g., "Introduces technical terms with immediate lay 
translation in parentheses on first use, then uses the term freely. 
Never assumes reader knows terminology."}

### Words consistently absent

{ABSENT_WORD_1} — expected in this category, never appears  
{ABSENT_WORD_2} — expected in this category, never appears  
{ABSENT_WORD_3} — expected in this category, never appears

---

## 6. Emotional Register

Primary register: {REGISTER_NAME}  
Secondary register: {REGISTER_NAME}

Evidence for primary register:
- "{QUOTE_1}" — {SOURCE}
- "{QUOTE_2}" — {SOURCE}

Evidence for secondary register:
- "{QUOTE_1}" — {SOURCE}

Register NOT present: {REGISTER_NAME} — {ONE_SENTENCE_WHY_NOTABLE}

---

## 7. Authority — How It's Built

Main authority mechanisms (in order of frequency):

1. {MECHANISM_1 — e.g., "Client story pattern"}: {DESCRIPTION_AND_FORMULA}
   Example: "{QUOTE}" — {SOURCE}

2. {MECHANISM_2}: {DESCRIPTION}
   Example: "{QUOTE}" — {SOURCE}

3. {MECHANISM_3}: {DESCRIPTION}
   Example: "{QUOTE}" — {SOURCE}

Research citation approach: {DESCRIPTION — how formal, how frequent}

Limit acknowledgment: {yes with examples / no}

---

## 8. CTA and Calls to Action

Post ending distribution:
- Soft invitation: {COUNT} ({PERCENTAGE}%)
- Open reader question: {COUNT} ({PERCENTAGE}%)
- Direct CTA: {COUNT} ({PERCENTAGE}%)
- Reflective close (no action): {COUNT} ({PERCENTAGE}%)
- Educational close: {COUNT} ({PERCENTAGE}%)

CTA addressing form: {ti / Vi / mixed} — {NOTE_IF_CONSISTENT_WITH_POST}

Representative CTAs:
- "{CTA_QUOTE_1}" — {SOURCE}
- "{CTA_QUOTE_2}" — {SOURCE}

---

## 9. Forbidden List

Consistently absent across all {POST_COUNT} posts:

- {ABSENT_PATTERN_1}: {EVIDENCE — e.g., "0 instances found"}
- {ABSENT_PATTERN_2}: {EVIDENCE}
- {ABSENT_PATTERN_3}: {EVIDENCE}
- {ABSENT_PATTERN_4}: {EVIDENCE}
- {ABSENT_PATTERN_5}: {EVIDENCE}
- {ABSENT_PATTERN_6}: {EVIDENCE}
- {ABSENT_PATTERN_7}: {EVIDENCE}

---

## Concise Voice Profile

{4–6_SENTENCES_DESCRIBING_THIS_AUTHOR_AS_A_SPECIFIC_PERSON.
Must be concrete enough that it could describe only this author.
Must sound like it was written about a real person, not a brand archetype.
Example structure: Who they write like → how they build trust → 
what makes their rhythm distinctive → what they never do.}
```

---

## Template B — "Ton i glas" section for product-marketing.md

**Location:** Appended to `.agents/clients/{CLIENT_SLUG}/product-marketing.md`  
**Language:** Serbian (Latin script)  
**Length target:** 300–500 words maximum — this is read before every 
writing task, so conciseness is critical  
**Purpose:** Operational instruction for the copywriter agent

```markdown
## Ton i glas

**Adresiranje:** {ti / Vi / mi / bez direktnog obraćanja}, dominantno {PERCENTAGE}%

**Otvaranje posta:** Tipično {pitanjem / anegdotom iz prakse / citatom klijenta / ...}.
Primer: "{REPRESENTATIVE_OPENING_QUOTE_MAX_20_WORDS}"

**Rečenice:** Prosečno {N} reči. Smenjuj kratke ({SHORT_RANGE} reči) i srednje 
({MEDIUM_RANGE} reči). Izbegavaj duže od {MAX_WORDS} reči. Koristi kratke 
rečenice ({N_WORDS}) za naglasak — uvek u zasebnom pasusu.

**Pasusi:** {N} rečenice u proseku. {SINGLE_SENTENCE_NOTE — e.g., "Kratki 
jednoredni pasusi se koriste za naglasak i zaključak."}

**Karakteristične reči i fraze (koristi):**
- {PHRASE_1}
- {PHRASE_2}
- {PHRASE_3}
- {PHRASE_4}
- {PHRASE_5}

**Karakteristične konstrukcije:**
- "{CONSTRUCTION_1 — full example phrase}"
- "{CONSTRUCTION_2 — full example phrase}"

**Prevod vs. engleski:** {POLICY — e.g., "Uvek piši na srpskom: 'hidratantna 
krema' ne 'moisturizer', 'zaštita od sunca' ne 'SPF'. Izuzetak: {EXCEPTIONS_IF_ANY}."}

**Registar:** {PRIMARY_REGISTER}, sa elementima {SECONDARY_REGISTER}.
{1–2_SENTENCES_HOW_THIS_MANIFESTS_IN_PRACTICE.}

**Autoritet — kako se gradi:**
- {AUTHORITY_TECHNIQUE_1 — concrete, e.g., "Priče klijentkinja: 'Nedavno mi je 
  došla klijentkinja koja...' + dijagnoza + ishod"}
- {AUTHORITY_TECHNIQUE_2}
- {AUTHORITY_TECHNIQUE_3}

**CTA stil:** {TYPE}. Tipičan zaključak: "{REPRESENTATIVE_CTA_QUOTE}"

---

## Izbegavati

- {FORBIDDEN_PATTERN_1}
- {FORBIDDEN_PATTERN_2}
- {FORBIDDEN_PATTERN_3}
- {FORBIDDEN_PATTERN_4}
- {FORBIDDEN_PATTERN_5}
- {FORBIDDEN_PATTERN_6}
- {FORBIDDEN_PATTERN_7_IF_RELEVANT}
```

---

## Quality check before saving

Run these checks on Template B before writing the file:

1. **Word count under 500** — count "Ton i glas" + "Izbegavati" sections 
   combined. If over, cut the least specific lines first.

2. **No placeholder left empty** — every {PLACEHOLDER} must be filled 
   with a real value from the analysis.

3. **Forbidden list has minimum 5 items** — if fewer, return to dimension 9.

4. **Voice profile in Template A sounds like a specific person** — read 
   aloud. If it could describe any wellness brand, it fails. Rewrite.

5. **Quotes are actual quotes** — not paraphrases. Must have quotation 
   marks and source attribution in Template A.
