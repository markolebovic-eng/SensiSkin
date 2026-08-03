# Objection Handling

The client, or their developer, reads Google's AI optimization guide and asks: **"Google says GEO isn't a thing. Why am I paying for it?"**

This is a good question asked in good faith. Answer it confidently and accurately. Never defensively, and never by attacking Google — the page is largely correct about the thing it describes.

---

## The short answer

> "Google is right about Google. Their AI features run on their search index, so SEO is the path — which is why your GEO engagement contains a complete SEO program rather than sitting next to one. What Google's page doesn't cover is every other engine, because it can't. ChatGPT, Perplexity, Claude, Copilot, Apple and Amazon each run their own crawlers with their own controls, and the settings that govern whether they can cite you are different on each one — and different from Google's. That's most of what we do that Google's guidance will never tell you."

---

## The long answer, in five moves

### 1. Concede what's true — immediately and without qualification

Google says its generative AI features are grounded in core Search ranking via retrieval-augmented generation. That means index health, content quality, E-E-A-T and technical fundamentals determine AI Overview visibility. **We agree.** It is exactly why the engagement includes the full technical and content SEO layer as scope, not as an upsell.

Conceding this first is what makes everything after it credible.

### 2. Correct what's being misread

Two specific misreadings come up constantly:

- **"Google says structured data is useless."** It does not. It says structured data "isn't required for generative AI search, and there's no special schema.org markup you need to add" — and then, in the same paragraph: *"However, it's a good idea to continue using it as part of your overall SEO strategy, as it helps with being eligible for rich results on Google Search."* Not required for one specific purpose ≠ not useful.
- **"Google says AI files are harmful."** It says the opposite: they "will neither harm nor help your site's visibility or rankings in Google Search, as Google Search ignores them," and "It's completely fine if you decide to create and maintain LLMS.txt files… for other services or systems that use these files."

### 3. Establish the scope limit — this is the whole argument

Google's documentation describes Google. It is silent on every other engine, and those engines behave differently in ways that are documented by *them*:

- **OpenAI runs two crawlers with independent controls.** `GPTBot` is training only; `OAI-SearchBot` governs ChatGPT search visibility. Nearly every robots.txt template on the internet blocks the wrong one. A client can refuse model training and keep full ChatGPT citation visibility — Google offers no equivalent split.
- **Perplexity publishes Cloudflare and AWS WAF configuration procedures**, because firewall rules block AI crawlers routinely and silently. Google has never published WAF guidance. A firewall rule is invisible in Search Console and produces exactly zero citations forever.
- **Anthropic honours `Crawl-delay`.** Google ignores it. Anthropic runs `Claude-SearchBot` for indexing — a bot absent from most published AI-bot lists.
- **Apple reads `isAccessibleForFree: false`** to decide whether your page can ground an AI answer. Structured data as a per-engine AI control.
- **Amazon treats `noarchive`** — a directive Google deprecated — as "do not use for model training."
- **`Perplexity-User`, `ChatGPT-User` and `Amzn-User` ignore robots.txt** by design, so robots.txt is not a complete access model.

None of this is discoverable by reading Google's documentation, because none of it is Google's to document.

### 4. Bring the independent evidence

Peer-reviewed research at KDD 2024 measured up to **40% visibility gains** in generative engine responses from adding citations, credible quotations, and statistics — validated on Perplexity at up to **37%**.

The same research found the effect **inverts by existing rank**: those tactics gave a rank-5 source **+115%** and a rank-1 source **−30%**. So we assign them by position rather than applying them everywhere — which is the opposite of standard GEO advice, and a reason to work with specialists rather than a checklist.

### 5. Close on Google's own page

Google's AI optimization guide states that **a site must be included in Search generative AI features in Search Console to be eligible for display in generative AI features on Google Search.**

That is a switch. A client who is off it has zero AI Overview visibility regardless of how good their content is. Checking it — and every equivalent gate on every other engine — is a GEO deliverable.

---

## Handling the harder follow-ups

**"So you're just doing SEO and calling it GEO."**
> "The SEO layer is in scope and we do it properly — Google's right that it's the foundation. On top of it: per-engine crawler access across eight operators, WAF and CDN allowlisting, IP-verified bot monitoring, per-engine snippet and grounding controls, entity work, and cross-engine citation measurement that doesn't exist in any SEO toolset. If you'd rather buy it as SEO, the technical work overlaps substantially and we're happy to scope it that way — you'd be giving up the non-Google engines."

**"Google says these are hacks that don't work."**
> "For Google, some are — chunking and llms.txt do nothing there, and Google says so plainly. We don't sell them as Google tactics. We implement them where they're plausibly useful on other engines, at near-zero cost and zero risk. What we don't do is the thing Google actually warns about: mass-generating pages per query variation. That's a spam policy violation, it would take your organic visibility down with it, and it's the one tactic we refuse."

**"Can you guarantee AI citations?"**
> "No, and anyone who does is selling something. Google states plainly that indexing and serving aren't guaranteed even when you meet every requirement. What we guarantee is scope: every engine can reach you, your content is structured and sourced to be citable, your entity is coherent, and you have measurement that shows movement. We baseline before we start so you can see what changes."

**"Our developer says our robots.txt is fine."**
> "It probably is. robots.txt is one of two access layers — the other is your CDN or firewall, and that one fails silently. We test a live request with each engine's actual user agent against your origin. It takes a few minutes and it's the single most common cause of zero AI visibility we find."

---

## Tone rules

- Concede Google's correct points first, fully, without hedging.
- Never argue that Google is lying. Argue that Google's scope is Google.
- Lead with documented per-engine facts, not with theory.
- Quote Google accurately, including the parts that support us — the structured-data sentence and the inclusion-setting sentence both do.
- Never say "studies show" without naming the study.
- Never hedge our own deliverables with confidence language. The evidence ledger is internal.
