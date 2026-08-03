# Engine Differences — Why GEO Is Not Just SEO

Every row is documented by the engine itself and absent from Google's documentation. This file is the evidence base for `objection-handling.md`.

## Access & control divergence

| Behaviour | Google | ChatGPT | Perplexity | Claude | Apple | Amazon |
|---|---|---|---|---|---|---|
| Separate training vs search bot | No (for AI Search features) | **Yes** — GPTBot / OAI-SearchBot | **Yes** — PerplexityBot is search-only | **Yes** — ClaudeBot / Claude-SearchBot | **Yes** — Applebot / Applebot-Extended | **Yes** — Amzn-SearchBot never trains |
| Citation-critical token | `Googlebot` | `OAI-SearchBot` | `PerplexityBot` | `Claude-SearchBot`, `Claude-User` | `Applebot` | `Amzn-SearchBot` |
| User-fetcher ignores robots.txt | n/a | **Yes** (`ChatGPT-User`) | **Yes** (`Perplexity-User`) | No | n/a | **Yes** (`Amzn-User`) |
| `Crawl-delay` honoured | **No** | Not stated | Not stated | **Yes** | Not stated | **No** |
| Published IP JSON endpoints | rDNS instead | **Yes** ×4 | **Yes** ×2 | IP list published | Not published | **Yes** ×2 |
| Official WAF guidance | **None** | Recommends IP allowlist | **Yes — Cloudflare + AWS, step by step** | None | None | None |
| robots.txt read per host | Per host | Per host | Per host | **Per host, stated explicitly** | Per host | **Per host, stated explicitly** |
| robots.txt cache window | Not stated | Not stated | ~24h to reflect | Not stated | Not stated | **Up to 30 days** |
| Propagation after change | Days–months (recrawl) | **~24h** | **~24h** | Not stated | Not stated | Up to 30 days |
| Structured data as AI control | No | No | No | No | **Yes — `isAccessibleForFree: false`** | No |
| Meta tag as training opt-out | `Google-Extended` token | robots.txt only | n/a | robots.txt only | `Applebot-Extended` token | **`noarchive` meta** |
| Snippet controls limit AI output | **Yes** — nosnippet, max-snippet, data-nosnippet | Not stated | Not stated | Not stated | **Yes** — nosnippet | Supports noindex/noarchive |
| Console-level AI eligibility switch | **Yes** — GSC generative AI features inclusion | No | No | No | No | No |
| Cryptographic bot auth | **Web Bot Auth (experimental)**, `Google-Agent` | No | No | No | No | No |

## Index divergence

| Engine | Retrieval index |
|---|---|
| Google AI Overviews, AI Mode | Google index (RAG over core Search) |
| ChatGPT Search | Bing-derived + OpenAI's own crawl |
| Copilot | Bing |
| Perplexity | Own index + third-party |
| Claude | Own search infrastructure (`Claude-SearchBot`) |
| Apple | Applebot |
| Amazon | Amzn-SearchBot |

**Consequence:** being indexed by Google does not make a client retrievable anywhere else. Bing Webmaster Tools verification and IndexNow become GEO deliverables, not SEO afterthoughts, because Bing's index feeds two of the largest AI assistants.

## The deliverables each divergence justifies

| Divergence | Billable deliverable | Google will never mention it because |
|---|---|---|
| Training/search bot split | `A2` policy decision, per bot | Google has no equivalent split for AI Search |
| Wrong-bot problem | `A1` multi-crawler robots.txt audit | Google only documents its own tokens |
| WAF blocking | `A3`/`A4` edge audit + IP allowlists | Google publishes no WAF guidance |
| User-fetchers ignoring robots | `A3` edge rules for genuine exclusion | Googlebot always respects robots.txt |
| `Crawl-delay` | `A8` per-engine rate tuning | Google ignores the directive |
| `isAccessibleForFree` | `D5` per-engine grounding control | Google uses the property for a different purpose |
| `noarchive` | `E8` Amazon training opt-out | Google deprecated it |
| Per-host robots.txt + 30-day cache | `A11` subdomain coverage, remediation SLAs | Google recrawls on its own schedule |
| Separate indexes | `B6` IndexNow, `G7` Bing Webmaster baseline | Google does not index for Bing |
| GSC AI inclusion switch | `A5` eligibility check | Google *does* document this — and almost nobody reads it |
| Web Bot Auth | `A10` CDN readiness | Only Google is testing it, and only experimentally |

## What is genuinely the same everywhere

State this plainly to clients — it is why the SEO layer is in scope, and saying it builds trust:

- Content must be crawlable and server-rendered to be retrievable.
- Quality, originality and first-hand experience drive selection on every engine.
- Clear structure and descriptive headings help every parser.
- Entity coherence — consistent naming, `sameAs`, accurate third-party profiles — helps everywhere.
- Freshness signals matter everywhere.
- Blocked bot = no citation, everywhere, without exception.
