# Search Diagnostics — traffic drops, updates, manual actions

Method for answering "my traffic dropped" and "did an update hit me". Every fact here is
traced to the Google Search Central corpus harvested 2026-08; source path given per section.

The SKILL.md audit framework asks *is the site healthy*. This reference asks *what changed*.
Different question, different method — do not run an audit checklist at a traffic drop and
hope the cause falls out.

---

## Step 0 — rule out the data before the site

Check the Search Console **Data Anomalies** page first. A drop can be a change in Google's
data processing or a logging error, in which case nothing on the site changed at all.

Source: `/search/docs/monitor-debug/debugging-search-traffic-drops`

---

## Step 1 — read the shape of the curve

Open the Search Console Performance report and separate clicks from impressions. The pairing
tells you which family of causes to investigate.

| Pattern | What it points at |
|---|---|
| Clicks and impressions both drop | Ranking, indexing, or demand — continue to step 2 |
| Impressions flat, clicks drop | Title link and snippet are not earning the click, or a competitor gained a rich result. Not a ranking problem |
| Position drops but impressions hold | Small positional shift; often self-correcting |

Google's own guidance on the clicks-only case: "you might not be generating the best page
title and snippet that you could." Fix the title link and description before touching rankings.

Source: `/search/docs/monitor-debug/debugging-search-traffic-drops`

---

## Step 2 — the six documented causes

Google names six. Work them in this order — cheapest to rule out first.

1. **Technical issues.** Server availability, robots.txt fetch failures, 404s, a misplaced
   `noindex`. Check the **Crawl stats** report and the **Page indexing** report for a spike
   that lines up with the drop. Site-wide failures (site down) drop traffic sharply;
   page-level failures (a stray `noindex`) drop it slowly, because Google has to crawl the
   page to see the rule.
2. **Security issues.** Malware or phishing triggers user-facing warnings before the click.
   Check the **Security Issues** report.
3. **Spam issues.** Check the **Manual Actions** report. A manual action is issued after
   automated detection or human review of a spam-policy violation.
4. **Algorithmic update.** Check the ranking-updates list and the Search Status Dashboard.
   Google is explicit: "there might not be anything fundamentally wrong with your content."
5. **Seasonality and changing interests.** Filter the Performance report to one high-traffic
   query at a time, then check that query in Google Trends. If the whole web dropped for that
   query, the site did not.
6. **Site moves and migrations.** URL changes cause ranking fluctuation while Google recrawls
   and reindexes. A medium-sized site takes a few weeks; larger sites longer. If it is not
   recovering, see `site-moves.md`.

Source: `/search/docs/monitor-debug/debugging-search-traffic-drops`

---

## Step 3 — the four Performance-report filters that actually isolate the cause

Run all four. Each one eliminates a family of causes.

- **Date → Last 16 months.** Confirms whether the same drop happened last year. Seasonal drops
  reproduce on the same calendar dates. For more than 16 months, use the Search Analytics API
  or bulk data export.
- **Date → Compare.** "Last 3 months vs previous period" and "vs year over year". Then click
  through *every* tab — queries, pages, countries, devices, search appearances. The tab where
  the delta concentrates is the answer.
- **Search type filter.** Web, Image, Video, News. A drop confined to Images is not a web
  ranking problem.
- **Pages table, sorted by Clicks Difference.** Establishes blast radius: whole site, a page
  group, or one page. Site-wide → Page indexing report. Group → URL Inspection on a sample.

Source: `/search/docs/monitor-debug/debugging-search-traffic-drops`

---

## Core updates

**How they work.** Broad changes to ranking systems, several times a year, announced on the
ranking-updates list. "These changes are broad in nature, and don't target specific sites or
individual web pages." A page that moves down is not thereby "bad" — Google's own analogy is
a top-20 restaurant list being reassessed as new restaurants open.

**Timing discipline — this is where most analyses go wrong:**
1. Confirm on the **Search Status Dashboard** that the update finished rolling out. Note start
   and end dates.
2. Wait **at least a full week after completion** before analysing.
3. Compare *that* week against a week *before the update started rolling out*. Comparing
   mid-rollout to mid-rollout produces noise and a wrong conclusion.

**Then size the move:**
- Small drop (position 2 → 4): take no drastic action. Google explicitly recommends against
  changing content that is already performing well.
- Large drop (position 4 → 29): assess the site *as a whole*, not the individual pages, against
  the helpful-content self-assessment questions.

**What not to do.** Google names three anti-patterns: "quick fix" changes made because you
heard an element was bad for SEO; changes that are not sustainable for users; and deleting
content, which is a last resort. Google's own note on deletion: if you are considering deleting
entire sections, "that's likely a sign those sections were created for search engines first."

**Recovery timing.** Some changes take effect in days; site-level helpful-content
reassessment "could take several months." You do not have to wait for the next announced core
update — smaller unannounced core updates run continually. And there is no guarantee changes
produce noticeable impact.

Source: `/search/docs/appearance/core-updates`

---

## Spam policies and manual actions

The full list of violations (`/search/docs/essentials/spam-policies`), all of which can cause
lower ranking or removal:

Cloaking · Doorway abuse · Expired domain abuse · Hacked content · Hidden text and link abuse ·
Keyword stuffing · Link spam · Machine-generated traffic · Malicious practices · Misleading
functionality · Scaled content abuse · Scraping · Site reputation abuse · Sneaky redirects ·
Thin affiliation · User-generated spam

Plus demotion/removal grounds outside the spam list: legal removals, personal information
removals, policy circumvention, scam and fraud.

**Two facts worth stating to a client:**
- The spam policies **apply to all of Google Search, including generative AI responses**
  (documentation updated May 2026). A spam problem is not containable to one surface.
- A **structured-data manual action** removes rich-result eligibility only; it "doesn't affect
  how the page ranks in Google web search." Do not let a client treat an SD manual action as a
  ranking emergency. Source: `/search/docs/appearance/structured-data/sd-policies`

Before recommending anything at scale, read `../../geo/references/risk-register.md` — scaled
content abuse is the violation most likely to be triggered accidentally by our own work.

---

## Crawl-budget myths worth correcting during a diagnosis

From `/crawling/docs/myths-about-crawling`. Clients arrive with these; correcting them saves
wasted work.

- **Crawling is not a ranking factor.** "Improving your crawl rate won't necessarily lead to
  better positions." Crawling is necessary for inclusion, not a ranking signal.
- **`crawl-delay` in robots.txt is not processed by Google's crawlers.** Non-standard rule.
- **Compressing sitemaps does not increase crawl budget.** They still have to be fetched.
- **4xx pages (except 429) do not waste crawl budget.**
- **`nofollow` does not protect crawl budget** — another page anywhere on the web can link
  the same URL without it.
- **`noindex` costs crawl budget short-term** (Google must crawl the page to see the rule) but
  frees it long-term as URLs leave the index.
- **Alternate URLs and embedded resources do consume crawl budget** — hreflang alternates, AMP,
  CSS, JS, XHR fetches all count.
- **Freshness is not a signal in itself.** "Content is rated by quality, regardless of age.
  … there's no additional value in making pages artificially appear to be fresh by making
  trivial changes and updating the page date." Do not sell date-bumping as a tactic.
- **Proximity to the home page affects crawl frequency, not ranking.** Pages linked from the
  home page "may be seen as more important, and therefore crawled more often. However, this
  doesn't mean that these pages will be ranked more highly."
- **Site speed and 5xx/429 rates do move crawl capacity.** Consistent fast responses raise the
  crawl capacity limit; server errors and rate limiting lower it.

Crawl budget is only worth a work item for sites Google defines as in scope
(`/crawling/docs/crawl-budget`): 1M+ pages changing weekly, 10K+ pages changing daily, or a
large share of URLs sitting in "Discovered – currently not indexed". Google calls these "a
rough estimate … not exact thresholds". Note that crawl budget is per *hostname* —
`www.example.com` and `shop.example.com` have separate budgets.
