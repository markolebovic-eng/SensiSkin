---
name: brand-voice-extractor
description: >
  Analyze the client's existing written content (blog posts from their site, 
  or uploaded samples) and generate a precise brand voice script that the 
  copywriter agent uses to replicate the authentic authorial voice in all 
  future content. Run once for a new client before the first content task, 
  or as re-calibration after 3-6 months of active work. Trigger phrases: 
  "extract brand voice", "analyze how the client writes", "build voice 
  script", "before I start writing for the client", "calibrate brand voice".
metadata:
  version: 1.0.0
---

# Brand Voice Extractor

You systematically extract the authentic authorial voice from a client's 
existing texts and turn it into an operational script the copywriter agent 
uses for every future content task. The output of this skill is the 
difference between "well-written generic AI content" and "content that 
sounds like a specific person with years of experience."

This is not a task you run often — it runs once per new client and 
occasionally as re-calibration. So it can afford to be thorough.

---

## When to use this skill

- First content engagement with a client — before any blog, newsletter, or 
  social post gets written
- Re-calibration after 3-6 months of active work (the client's style evolves)
- When the user says existing output "doesn't sound like the client"
- When the client adds significant new content to their site that shifts 
  their tone (new service line, new audience segment)

**When NOT to use:**
- For tasks where brand-voice-script.md already exists and context hasn't changed
- For one-off ad-hoc tasks where long-term voice replication doesn't matter
- For clients with no existing written material (acquire samples first)

---

## Prerequisites

1. Active client slug in `.agents/agency/active-client.md`
2. `WebFetch` tool available to the agent (if not in the copywriter's 
   tools list, add it before running this skill)
3. Client has minimum 5 blog posts on site, OR user has provided samples 
   (Word, PDF, paste) — without these the skill cannot operate

---

## Phase 1 — Discovery (locate the source material)

Before fetching anything, determine where the texts live. Ask the user 
which scenario applies:

**Scenario A — User provides sitemap URL**
Direct path. Fetch sitemap.xml, parse it, filter URLs containing common 
Serbian blog markers: `/blog/`, `/blogovi/`, `/clanci/`, `/članci/`, 
`/saveti/`, `/edukacija/`, `/novosti/`, `/zurnal/`, `/journal/`

**Scenario B — User provides only the domain**
Try in this order:
1. `https://{domain}/sitemap.xml`
2. `https://{domain}/sitemap_index.xml`
3. Direct paths: `/blog`, `/blogovi`, `/clanci`, `/saveti`
4. WebSearch query: `site:{domain} blog`

If none of this returns a list of posts, **stop and ask the user** instead 
of guessing further.

**Scenario C — User has provided samples directly**
Skip Discovery and Sample selection — go straight to Phase 3.

**Sanity check after fetching:**
If WebFetch returns fewer than 200 words per page, the site is likely 
JavaScript-rendered (Wix, Squarespace, some Webflow templates). In that 
case, tell the user they need to manually paste samples instead of 
autofetching.

---

## Phase 2 — Sample selection

**Default:** 8-12 posts, balanced mix by length and type.

If the site has more than 12 posts, use this algorithm for a balanced mix:

1. **By length** — roughly one third short (<800 words), one third medium 
   (800-1500), one third long (>1500). Length reveals different registers — 
   short posts show how the author "breaks down" a topic, long ones show 
   how they build an argument.

2. **By type** — try to cover:
   - Educational post (explains a concept)
   - Experience / case study post (story from practice)
   - "Myth vs truth" / debunking post
   - Seasonal / topical post (autumn, summer, new treatment)
   - "Tips" / how-to post

   Type is often recognizable from the title — use heuristics, not strict rules.

3. **By date** — favor posts from the last 12-18 months. Posts older than 
   3 years may show an outdated brand voice. If the client doesn't have 
   enough recent material, take the newest available and note this in the output.

**If the user wants to pick the posts themselves** — skip the algorithm 
and use their list, but verify minimum 5 (below that, patterns aren't reliable).

**Before fetching:** Show the user the list of 8-12 URLs you plan to 
analyze and ask if it's OK to proceed. This saves tokens if the selection is bad.

---

## Phase 3 — Extraction (analyze across 9 dimensions)

Read all samples via WebFetch (or directly if provided). For each of the 
9 dimensions below, extract **concrete examples with quotes** — not 
generic descriptions. Quotes should be short (under 15 words), attributed 
to source posts.

### 1. Reader addressing

Identify which form dominates:
- "ti" (familiar, direct) — measure frequency
- "Vi" with capital V (formal, distanced)
- "vi" lowercase (plural, informal)
- No direct address (everything in third person / "oni koji...")
- "mi" — author includes themselves ("mi koje brinemo o koži")

Record percentage dominance and provide 2-3 representative opening 
examples where the addressing is visible.

### 2. Post openings

Classify the first paragraph of each post:
- Question directed at the reader
- Personal experience / practice anecdote
- Statistic or research
- Myth you're debunking
- Direct entry into the problem
- Concept definition
- Quoting a client ("Često me pitaju...")

Identify the **most common opening structure** — this is one of the 
strongest recognizable voice signals.

### 3. Sentence length and rhythm

Calculate average sentence length in words across all samples. Record:
- Average length (e.g., 14 words)
- Typical maximum length (90th percentile)
- Whether they use very short (5-7 word) sentences for emphasis
- Whether they alternate lengths or are metronomically uniform
- Whether they use sentence fragments, colons, dashes

This is technical but critical — AI generators have uniform rhythm that 
betrays artificial origin.

### 4. Paragraphs

- Average sentences per paragraph
- Average words per paragraph
- Whether they use single-sentence paragraphs for emphasis
- Maximum paragraph length (how dense does it get?)

Short paragraphs (1-2 sentences) signal a web-friendly tone. Longer (4-6) 
signal an essay or expert register.

### 5. Lexical habits

**Characteristically recurring words:**
List 10-15 words/phrases that appear often but are NOT generic for the topic. 
Example (hypothetical for a cosmetologist): "rituali nege", "klijentkinje", 
"tretman", "prirodno", "godinama radim sa".

**Words they avoid:**
Note what is MISSING despite being naturally expected:
- Do they use English terms (skincare, anti-aging) or translate everything?
- Do they use Latin medical terms or explain in plain language?
- Do they use superlatives ("najbolji", "savršen") or avoid them?

**Technical vocabulary:**
How do they treat technical terms? Introduce with explanation? Assume the 
reader knows? Translate to everyday language?

### 6. Emotional register

Place the voice in one or a combination of these registers:
- Warm and empathetic ("razumem koliko ovo zna da bude frustrirajuće")
- Expert and distanced (relies on data, less on emotion)
- Direct and no-nonsense ("istina je da...")
- Narrative and chatty (lots of anecdotes, dialogue)
- Educator (explains patiently, like a lecturer)
- Mentor (shares wisdom from experience)

The strongest brands usually have a primary + secondary register, not just one.

### 7. Authority — how it's built

How does the author demonstrate competence without bragging?
- References to years of experience (and how they're framed)
- Examples from practice ("Nedavno mi je došla klijentkinja sa...")
- Scientific sources and studies (how often, how cited)
- Acknowledging limits ("Ne postoji jedinstven odgovor", "Zavisi od...")
- Concrete results and numbers

Record the exact phrases used to construct authority — these are recognizable.

### 8. CTA and calls to action

How does the author invite the reader to the next step at the end of a post?
- Direct CTA ("Zakažite konsultaciju")
- Soft invitation ("Ako želite da razgovaramo...")
- Open question ("Imate iskustvo sa ovim? Pišite mi.")
- No CTA — post ends reflectively
- Educational close ("Nadam se da vam je ovo pomoglo da razumete...")

Percentage frequency of each type.

### 9. What they NEVER do (forbidden list)

This is perhaps the most important dimension. Identify what is 
**consistently absent**:
- Emojis? Yes/no
- ALL CAPS for emphasis (LIKE THIS)? Yes/no
- Bolding phrases mid-sentence?
- Product brand names?
- Concrete result promises ("Garantujem da ćete...")?
- Clickbait headlines ("Šokirana ćeš biti...")?
- Anything else systematically avoided

This list becomes the "Izbegavati" section in product-marketing.md.

---

## Phase 4 — Output (dual delivery)

The skill generates two files. Both are mandatory.

### A) Full script (detailed document)

Location: `.agents/clients/{slug}/brand-voice-script.md`

Format:
```markdown
# Brand Voice Script — {Client Name}

Generated: {date}
Posts analyzed: {count}
Analyzed URLs list: {list}

## 1. Reader addressing
{detailed analysis with examples and quotes}

## 2. Post openings
{...}

## 3. Sentence length and rhythm
{statistics + examples}

[... all 9 dimensions ...]

## Concise voice profile (1 paragraph)
{One tight 4-6 sentence paragraph that sounds like a description of a person.
Example: "Stručnjak koji piše kao iskusna mentorka. Prosečna rečenica 14 reči, 
mnoge u 'ti' formi. Otvara pitanjem ili anegdotom iz prakse. Empatičan ali 
bez preteranog kićenja..."}
```

Length ~1500-2500 words. This is the reference document for revisions and debugging.

### B) Operational summary (what the agent actually reads)

Location: append to existing `.agents/clients/{slug}/product-marketing.md` 
under a section called **"Ton i glas"**.

**IMPORTANT:** This summary is written in Serbian because it will guide 
Serbian content generation. The agent reads it as direct instruction for 
output language. Keep section headers in Serbian for consistency with the 
client's product-marketing.md structure.

Format (concise, ~300-500 words):

```markdown
## Ton i glas

**Adresiranje:** {ti/Vi/mi/neutralan}, dominantno {X%}

**Otvaranje posta:** Tipično {pitanjem/anegdotom/...}. 
Primer: "{quote}"

**Rečenice:** Prosečno {N} reči. Smenjuj kratke (5-7) i srednje (12-18). 
Izbegavaj duže od {N}.

**Pasusi:** {N} rečenica u proseku. Kratki pasusi za naglasak su OK.

**Karakteristične reči (koristi često):**
- {word 1}, {word 2}, {word 3}, ...

**Karakteristične konstrukcije (koristi):**
- "{phrase 1}"
- "{phrase 2}"

**Registar:** {primary}, sa elementima {secondary}.
Konkretno: {1-2 sentences how it manifests}.

**Autoritet — kako se gradi:**
{List of 3-4 concrete techniques with examples.}

**CTA stil:** {direct/soft/question}. Tipičan zaključak: 
"{typical completion}"

## Izbegavati

- {concrete item 1}
- {concrete item 2}
- Engleske izraze tipa "skincare" — uvek prevod
- Superlative tipa "najbolji"
- Emotikone
- ...
```

### Memory update

After generating both files, append to 
`.agents/clients/{slug}/memory/MEMORY.md`:

```markdown
## Brand voice
- Script generated: {date}
- Analyzed: {N} posts from period {date-from} to {date-to}
- Next re-calibration suggested: {date + 6 months}
- brand-voice-script.md is the primary source; product-marketing.md has the concise version
```

---

## Quality check before completion

Before telling the user it's done, verify:

1. **Summary in product-marketing.md is under 500 words.** If longer, the 
   agent won't use it efficiently. Shorten.
2. **Each dimension has a concrete example.** If something says "warm tone" 
   without a supporting quote, that's not analysis — that's guessing.
3. **Forbidden list has minimum 5 items.** If fewer, you haven't looked 
   carefully enough at what's MISSING in the samples.
4. **The concise voice profile sounds like a description of a specific 
   person** when read aloud. If it sounds generic ("professional and 
   warm") — go back and sharpen.

---

## What to hand over to the user at the end

Short chat report:
- "Analyzed {N} posts from {domain}"
- Concise voice profile (3-4 sentences, copy from brand-voice-script.md)
- 3-5 most distinctive voice characteristics
- Locations of generated files
- Proposed next step: "Spreman/na sam da napišem prvi blog/newsletter/GBP 
  post — samo navedi temu."

Don't brag about analysis depth. The user wants results, not an audit trail.

---

## What this skill does NOT do

- Doesn't write content — that's the copywriter agent's job with this script in hand
- Doesn't do competitive analysis — that's a different skill
- Doesn't recommend SEO keywords — that's the seo agent
- Doesn't judge whether the voice is "good" — records what IS, not what SHOULD BE

---

## Re-calibration (mode 2)

When the skill runs a second time for the same client:
1. Read existing brand-voice-script.md
2. Identify posts added AFTER the last analysis date
3. Analyze only new posts (5-8 is enough for diff)
4. Generate DIFF document: "What changed since last analysis"
5. Update product-marketing.md "Ton i glas" section only where there are real changes
6. Note the re-calibration date in MEMORY.md

Don't overwrite brand-voice-script.md — save the previous version as 
brand-voice-script-{date}.md for auditing.