# URL Inventory — Google Search Central + Crawling Infrastructure

Harvested 2026-08-03. Method: parsed the full left-nav from the static HTML of `/search/docs` (166 links) plus the
separate `/crawling/docs` tree (22 pages, enumerated from the nav of `/crawling/docs/crawlers-fetchers/overview-google-crawlers`,
since `/crawling/docs` itself returns a noindex stub with no nav).

**Cross-check status:** `developers.google.com/sitemap.xml` resolves to a 40-part sitemap index. Fetching the nested parts
was rate-limited/timed out repeatedly (HTTP 500 at concurrency>4, timeouts at concurrency<=4). Recorded as
`skipped: rate-limited by developers.google.com` — see `04-open-questions.md` for the re-run plan. Nav-derived count (178)
falls inside the expected 180-220 band, and every structured-data feature page listed in `/search/docs/appearance/structured-data/search-gallery`
was present in the nav parse, so the parse is believed complete.

**All 178 URLs scraped successfully (0 failures).** Each row's `Updated` is the literal `Last updated <date> UTC` footer value.

> **Staleness caveat that matters:** 115 of 178 pages carry `2025-12-10` — a site-wide bulk republish, not 115 genuine content
> updates. Treat `2025-12-10` as 'unknown true age', not 'fresh'. The dates that carry real signal are the ones that differ from it.

| # | Nav section | URL | Title | Updated | Chars | Status |
|---|---|---|---|---|---|---|
| 1 | Appearance / Structured data | /search/docs/appearance/structured-data/article | Learn About Article Schema Markup | 2025-12-10 | 14807 | done |
| 2 | Appearance / Structured data | /search/docs/appearance/structured-data/book | Book Schema for Google Search | 2025-12-10 | 40810 | done |
| 3 | Appearance / Structured data | /search/docs/appearance/structured-data/breadcrumb | How To Add Breadcrumb (BreadcrumbList) Markup | 2025-12-10 | 22678 | done |
| 4 | Appearance / Structured data | /search/docs/appearance/structured-data/carousel | Carousel (ItemList) Structured Data | 2025-12-10 | 29911 | done |
| 5 | Appearance / Structured data | /search/docs/appearance/structured-data/carousels-beta | Carousels (Beta) Structured Data | 2026-01-21 | 34326 | done |
| 6 | Appearance / Structured data | /search/docs/appearance/structured-data/course | Use Schema for Course List | 2025-12-10 | 11603 | done |
| 7 | Appearance / Structured data | /search/docs/appearance/structured-data/dataset | Dataset Structured Data | 2025-12-10 | 9223 | done |
| 8 | Appearance / Structured data | /search/docs/appearance/structured-data/discussion-forum | Discussion Forum (DiscussionForumPosting, SocialMediaPosting | 2026-03-24 | 8488 | done |
| 9 | Appearance / Structured data | /search/docs/appearance/structured-data/education-qa | Education Q&A Structured Data | 2026-01-06 | 15236 | done |
| 10 | Appearance / Structured data | /search/docs/appearance/structured-data/employer-rating | Employer Rating (EmployerAggregateRating) Structured Data | 2025-12-10 | 8931 | done |
| 11 | Appearance / Structured data | /search/docs/appearance/structured-data/event | Learn About Google Event Schema Markup | 2025-12-10 | 36698 | done |
| 12 | Appearance / Structured data | /search/docs/appearance/structured-data/factcheck | Fact Check (ClaimReview) Markup for Search | 2025-12-10 | 18649 | done |
| 13 | Appearance / Structured data | /search/docs/appearance/structured-data/generate-structured-data-with-javascript | Generate Structured Data with JavaScript | 2025-12-10 | 5492 | done |
| 14 | Appearance / Structured data | /search/docs/appearance/structured-data/image-license-metadata | Google Images SEO: Image Metadata | 2025-12-10 | 32490 | done |
| 15 | Appearance / Structured data | /search/docs/appearance/structured-data/intro-structured-data | Intro to How Structured Data Markup Works | 2025-12-10 | 11224 | done |
| 16 | Appearance / Structured data | /search/docs/appearance/structured-data/job-posting | Learn About Job Posting Schema Markup | 2025-12-18 | 47892 | done |
| 17 | Appearance / Structured data | /search/docs/appearance/structured-data/local-business | Local Business (LocalBusiness) Structured Data | 2025-12-10 | 8486 | done |
| 18 | Appearance / Structured data | /search/docs/appearance/structured-data/loyalty-program | Loyalty Program Structured Data (MemberProgram) | 2025-12-10 | 11947 | done |
| 19 | Appearance / Structured data | /search/docs/appearance/structured-data/math-solvers | Math Solver (MathSolver) Structured Data | 2025-12-18 | 18509 | done |
| 20 | Appearance / Structured data | /search/docs/appearance/structured-data/merchant-listing | How To Add Merchant Listing Structured Data | 2026-07-07 | 86666 | done |
| 21 | Appearance / Structured data | /search/docs/appearance/structured-data/movie | Mark Up Movies with Structured Data | 2025-12-10 | 11120 | done |
| 22 | Appearance / Structured data | /search/docs/appearance/structured-data/organization | Organization Schema Markup | 2026-04-15 | 19466 | done |
| 23 | Appearance / Structured data | /search/docs/appearance/structured-data/paywalled-content | Subscription and Paywalled Content Markup | 2025-12-10 | 9992 | done |
| 24 | Appearance / Structured data | /search/docs/appearance/structured-data/product | Intro to Product Structured Data on Google | 2025-12-10 | 5256 | done |
| 25 | Appearance / Structured data | /search/docs/appearance/structured-data/product-snippet | How To Add Product Snippet Structured Data | 2025-12-10 | 42993 | done |
| 26 | Appearance / Structured data | /search/docs/appearance/structured-data/product-variants | Product Variant Structured Data (ProductGroup, Product) | 2026-05-20 | 44388 | done |
| 27 | Appearance / Structured data | /search/docs/appearance/structured-data/profile-page | Profile Page (ProfilePage) Schema Markup | 2025-12-10 | 4535 | done |
| 28 | Appearance / Structured data | /search/docs/appearance/structured-data/qapage | Schema for Q&A Pages (QAPage) | 2026-06-15 | 7031 | done |
| 29 | Appearance / Structured data | /search/docs/appearance/structured-data/recipe | Recipe Schema Markup | 2025-12-10 | 26827 | done |
| 30 | Appearance / Structured data | /search/docs/appearance/structured-data/return-policy | Merchant Return Policy Structured Data (MerchantReturnPolicy | 2025-12-10 | 21006 | done |
| 31 | Appearance / Structured data | /search/docs/appearance/structured-data/review-snippet | Review Snippet (Review, AggregateRating) Structured Data | 2026-07-24 | 44241 | done |
| 32 | Appearance / Structured data | /search/docs/appearance/structured-data/sd-policies | General Structured Data Guidelines | 2026-07-10 | 10471 | done |
| 33 | Appearance / Structured data | /search/docs/appearance/structured-data/search-gallery | Structured Data Markup that Google Search Supports | 2026-06-15 | 6291 | done |
| 34 | Appearance / Structured data | /search/docs/appearance/structured-data/shipping-policy | Merchant Shipping Policy Structured Data (ShippingService) | 2026-01-07 | 30528 | done |
| 35 | Appearance / Structured data | /search/docs/appearance/structured-data/software-app | Software App (SoftwareApplication) Schema | 2025-12-10 | 3106 | done |
| 36 | Appearance / Structured data | /search/docs/appearance/structured-data/speakable | Speakable (BETA) Schema Markup | 2025-12-10 | 7712 | done |
| 37 | Appearance / Structured data | /search/docs/appearance/structured-data/vacation-rental | Vacation Rental Schema Markup | 2025-12-10 | 23828 | done |
| 38 | Appearance / Structured data | /search/docs/appearance/structured-data/video | Video (VideoObject, Clip, BroadcastEvent) Schema Markup | 2026-02-13 | 7605 | done |
| 39 | Appearance / Structured data | /search/docs/specialty/ecommerce/include-structured-data-relevant-to-ecommerce | Structured Data for Ecommerce Sites | 2025-12-10 | 3565 | done |
| 40 | Crawling and indexing | /search/docs/crawling-indexing | Google Crawling and Indexing | 2025-12-10 | 3022 | done |
| 41 | Crawling and indexing | /search/docs/crawling-indexing/301-redirects | Redirects and Google Search | 2026-04-14 | 11046 | done |
| 42 | Crawling and indexing | /search/docs/crawling-indexing/amp | About AMP on Google Search | 2026-07-01 | 3335 | done |
| 43 | Crawling and indexing | /search/docs/crawling-indexing/amp/enhance-amp | Enhance AMP Content in Google Search | 2026-07-01 | 4352 | done |
| 44 | Crawling and indexing | /search/docs/crawling-indexing/amp/remove-amp | How To Remove your AMP Pages From Search | 2026-07-01 | 4911 | done |
| 45 | Crawling and indexing | /search/docs/crawling-indexing/amp/validate-amp | Validate your AMP Pages | 2026-07-01 | 2197 | done |
| 46 | Crawling and indexing | /search/docs/crawling-indexing/ask-google-to-recrawl | Ask Google to Recrawl Your Website | 2025-12-10 | 1842 | done |
| 47 | Crawling and indexing | /search/docs/crawling-indexing/block-indexing | Block Search Indexing with noindex | 2025-12-10 | 4364 | done |
| 48 | Crawling and indexing | /search/docs/crawling-indexing/canonicalization | What is URL Canonicalization | 2026-07-10 | 3619 | done |
| 49 | Crawling and indexing | /search/docs/crawling-indexing/canonicalization-troubleshooting | Fix Canonicalization Issues | 2026-07-10 | 4584 | done |
| 50 | Crawling and indexing | /search/docs/crawling-indexing/consolidate-duplicate-urls | How to Specify a Canonical with rel="canonical" and Other Me | 2026-07-10 | 14276 | done |
| 51 | Crawling and indexing | /search/docs/crawling-indexing/control-what-you-share | Control the Content You Share on Search | 2025-12-10 | 3592 | done |
| 52 | Crawling and indexing | /search/docs/crawling-indexing/googlebot | What Is Googlebot | 2026-02-03 | 3868 | done |
| 53 | Crawling and indexing | /search/docs/crawling-indexing/indexable-file-types | File Types Indexable by Google | 2026-02-03 | 2522 | done |
| 54 | Crawling and indexing | /search/docs/crawling-indexing/javascript/dynamic-rendering | Dynamic Rendering as a workaround | 2025-12-10 | 3236 | done |
| 55 | Crawling and indexing | /search/docs/crawling-indexing/javascript/fix-search-javascript | Fix Search-Related JavaScript Problems | 2025-12-18 | 8670 | done |
| 56 | Crawling and indexing | /search/docs/crawling-indexing/javascript/javascript-seo-basics | Understand JavaScript SEO Basics | 2026-03-04 | 14080 | done |
| 57 | Crawling and indexing | /search/docs/crawling-indexing/javascript/lazy-loading | Fix Lazy-Loaded Website Content | 2025-12-10 | 3516 | done |
| 58 | Crawling and indexing | /search/docs/crawling-indexing/keep-redacted-information-out | Keep Redacted Information out of Google | 2025-12-10 | 6064 | done |
| 59 | Crawling and indexing | /search/docs/crawling-indexing/links-crawlable | SEO Link Best Practices for Google | 2025-12-10 | 8249 | done |
| 60 | Crawling and indexing | /search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing | Mobile-first Indexing Best Practices | 2025-12-10 | 20668 | done |
| 61 | Crawling and indexing | /search/docs/crawling-indexing/pause-online-business | Temporarily Pause Or Disable Website | 2025-12-10 | 9525 | done |
| 62 | Crawling and indexing | /search/docs/crawling-indexing/prevent-images-on-your-page | Remove your own site's images from Google Search | 2025-12-10 | 4738 | done |
| 63 | Crawling and indexing | /search/docs/crawling-indexing/qualify-outbound-links | Qualify Outbound Links for SEO | 2025-12-10 | 3059 | done |
| 64 | Crawling and indexing | /search/docs/crawling-indexing/remove-information | Remove Your Site Info from Google | 2025-12-10 | 2409 | done |
| 65 | Crawling and indexing | /search/docs/crawling-indexing/robots-meta-tag | Robots Meta Tags Specifications | 2026-03-24 | 18928 | done |
| 66 | Crawling and indexing | /search/docs/crawling-indexing/robots/intro | Robots.txt Introduction and Guide | 2025-12-10 | 5781 | done |
| 67 | Crawling and indexing | /search/docs/crawling-indexing/site-move-no-url-changes | Changing Your Web Hosting and SEO | 2025-12-10 | 6287 | done |
| 68 | Crawling and indexing | /search/docs/crawling-indexing/site-move-with-url-changes | Site Moves and Migrations | 2026-06-17 | 22038 | done |
| 69 | Crawling and indexing | /search/docs/crawling-indexing/sitemaps/build-sitemap | Build and Submit a Sitemap | 2026-07-08 | 12653 | done |
| 70 | Crawling and indexing | /search/docs/crawling-indexing/sitemaps/combine-sitemap-extensions | How to Combine Sitemap Extensions | 2025-12-10 | 4377 | done |
| 71 | Crawling and indexing | /search/docs/crawling-indexing/sitemaps/image-sitemaps | Image Sitemaps | 2025-12-10 | 3139 | done |
| 72 | Crawling and indexing | /search/docs/crawling-indexing/sitemaps/large-sitemaps | Manage Your Sitemaps With Sitemap Index Files | 2025-12-10 | 3230 | done |
| 73 | Crawling and indexing | /search/docs/crawling-indexing/sitemaps/news-sitemap | Create a News Sitemap | 2025-12-10 | 5272 | done |
| 74 | Crawling and indexing | /search/docs/crawling-indexing/sitemaps/overview | What Is a Sitemap | 2025-12-10 | 3465 | done |
| 75 | Crawling and indexing | /search/docs/crawling-indexing/sitemaps/video-sitemaps | Video Sitemaps and Examples | 2026-05-20 | 20083 | done |
| 76 | Crawling and indexing | /search/docs/crawling-indexing/special-tags | Meta Tags and Attributes that Google Supports | 2025-12-10 | 8387 | done |
| 77 | Crawling and indexing | /search/docs/crawling-indexing/troubleshoot-crawling-errors | Troubleshoot Google Search Crawling Errors | 2025-12-18 | 16245 | done |
| 78 | Crawling and indexing | /search/docs/crawling-indexing/url-structure | URL Structure Best Practices for Google Search | 2025-12-10 | 10264 | done |
| 79 | Crawling and indexing | /search/docs/crawling-indexing/valid-page-metadata | Valid Page Metadata for Google Search | 2025-12-10 | 1706 | done |
| 80 | Crawling and indexing | /search/docs/crawling-indexing/website-testing | A/B Testing Best Practices for Search | 2025-12-10 | 5974 | done |
| 81 | Crawling infrastructure (separate tree) | /crawling/docs/about-crawling | Things to Know about Google's Web Crawling | 2026-03-03 | 6579 | done |
| 82 | Crawling infrastructure (separate tree) | /crawling/docs/changelog | Google's Crawling Documentation Changelog | 2026-07-22 | 8024 | done |
| 83 | Crawling infrastructure (separate tree) | /crawling/docs/crawl-budget | Crawl Budget Management | 2026-07-22 | 9080 | done |
| 84 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/apis-user-agent | APIs-Google User Agent | 2025-11-21 | 3334 | done |
| 85 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/feedfetcher | Google Feedfetcher | 2026-02-11 | 4400 | done |
| 86 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/google-common-crawlers | Google's common crawlers | 2026-07-14 | 10442 | done |
| 87 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/google-special-case-crawlers | Google Special-Case Crawlers | 2026-02-11 | 7293 | done |
| 88 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/google-user-triggered-fetchers | Google User-Triggered Fetchers | 2026-07-16 | 5959 | done |
| 89 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/overview-google-crawlers | Google Crawler (User Agent) Overview | 2026-06-12 | 7201 | done |
| 90 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/read-aloud-user-agent | Google Read Aloud User Agent | 2025-12-02 | 2261 | done |
| 91 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/reduce-crawl-rate | Reduce Google Crawl Rate | 2025-12-18 | 3750 | done |
| 92 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/verify-google-requests | Verify Requests from Google Crawlers and Fetchers | 2026-03-20 | 4445 | done |
| 93 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/verifying-googlebot | Verify Requests from Google Crawlers and Fetchers | 2026-03-20 | 4445 | done |
| 94 | Crawling infrastructure (separate tree) | /crawling/docs/crawlers-fetchers/web-bot-auth | Google's Guide to Authenticating Requests with Web Bot Auth  | 2026-05-04 | 5452 | done |
| 95 | Crawling infrastructure (separate tree) | /crawling/docs/faceted-navigation | Managing crawling of faceted navigation URLs | 2025-12-18 | 6012 | done |
| 96 | Crawling infrastructure (separate tree) | /crawling/docs/myths-about-crawling | Myths and facts about crawling | 2025-12-18 | 6112 | done |
| 97 | Crawling infrastructure (separate tree) | /crawling/docs/robots-txt/create-robots-txt | Create and Submit a robots.txt File | 2025-11-21 | 9678 | done |
| 98 | Crawling infrastructure (separate tree) | /crawling/docs/robots-txt/robots-txt-spec | How Google Interprets the robots.txt Specification | 2026-07-08 | 19316 | done |
| 99 | Crawling infrastructure (separate tree) | /crawling/docs/robots-txt/submit-updated-robots-txt | Updating Your Robots.txt File | 2025-11-21 | 3023 | done |
| 100 | Crawling infrastructure (separate tree) | /crawling/docs/robots-txt/useful-robots-txt-rules | Useful robots.txt Rules | 2026-06-12 | 4171 | done |
| 101 | Crawling infrastructure (separate tree) | /crawling/docs/troubleshooting/dns-network-errors | Debug Network and DNS Errors for Google's Crawlers | 2025-12-18 | 3670 | done |
| 102 | Crawling infrastructure (separate tree) | /crawling/docs/troubleshooting/http-status-codes | How HTTP Status Codes Affect Google's Crawlers | 2026-02-04 | 6578 | done |
| 103 | Monitoring and debugging | /search/docs/monitor-debug/analyze-social-video-content | Analyze Social and Video Content in Search Console | 2026-07-29 | 9304 | done |
| 104 | Monitoring and debugging | /search/docs/monitor-debug/bubble-chart-analysis | How to Create a Search Console Bubble Chart | 2025-12-10 | 8935 | done |
| 105 | Monitoring and debugging | /search/docs/monitor-debug/debugging-search-traffic-drops | Debug Google Search Traffic Drops | 2025-12-10 | 11770 | done |
| 106 | Monitoring and debugging | /search/docs/monitor-debug/google-analytics-search-console | Using Search Console and Google Analytics Data for SEO | 2026-01-07 | 16720 | done |
| 107 | Monitoring and debugging | /search/docs/monitor-debug/prevent-abuse | Prevent User-Generated Spam on Your Site | 2025-12-10 | 4192 | done |
| 108 | Monitoring and debugging | /search/docs/monitor-debug/search-console-start | How To Use Search Console | 2025-12-10 | 5348 | done |
| 109 | Monitoring and debugging | /search/docs/monitor-debug/search-operators | Debugging with Google Search Operators | 2025-12-10 | 1824 | done |
| 110 | Monitoring and debugging | /search/docs/monitor-debug/search-operators/all-search-site | How To Use the Site Search Operator | 2025-12-10 | 2881 | done |
| 111 | Monitoring and debugging | /search/docs/monitor-debug/search-operators/image-search | Google Images Search Operators | 2025-12-10 | 1676 | done |
| 112 | Monitoring and debugging | /search/docs/monitor-debug/security | Prevent Abuse on Your Site | 2025-12-10 | 1311 | done |
| 113 | Monitoring and debugging | /search/docs/monitor-debug/security/malware | Malware and Unwanted Software Overview | 2025-12-10 | 11972 | done |
| 114 | Monitoring and debugging | /search/docs/monitor-debug/security/prevent-malware | How To Prevent Malware Infection | 2025-12-10 | 5518 | done |
| 115 | Monitoring and debugging | /search/docs/monitor-debug/security/safe-browsing-repeat-offenders | Google Safe Browsing Repeat Offenders Policy | 2025-12-10 | 1178 | done |
| 116 | Monitoring and debugging | /search/docs/monitor-debug/security/social-engineering | Social Engineering (Phishing and Deceptive Sites) | 2025-12-10 | 8570 | done |
| 117 | Monitoring and debugging | /search/docs/monitor-debug/trends-start | Get started with Google Trends | 2025-12-10 | 11370 | done |
| 118 | Other | /search/blog | Search and SEO Blog | 2026-07-16 | 2450 | done |
| 119 | Other | /search/docs | Documentation to Improve SEO | 2025-02-04 | 4634 | done |
| 120 | Other | /search/updates | Latest Google Search Documentation Updates | 2026-07-29 | 120548 | done |
| 121 | Ranking and appearance | /search/docs/appearance | Google Search Appearance | 2026-06-15 | 2258 | done |
| 122 | Ranking and appearance | /search/docs/appearance/ad-network-and-translation | Ad Networks & Translation Search Features | 2025-12-10 | 5608 | done |
| 123 | Ranking and appearance | /search/docs/appearance/ai-features | AI Features and Your Website | 2025-12-10 | 6648 | done |
| 124 | Ranking and appearance | /search/docs/appearance/avoid-intrusive-interstitials | Interstitials and dialogs | 2025-12-10 | 4075 | done |
| 125 | Ranking and appearance | /search/docs/appearance/core-updates | Google Search's Core Updates | 2025-12-10 | 6165 | done |
| 126 | Ranking and appearance | /search/docs/appearance/core-web-vitals | Understanding Core Web Vitals and Google search results | 2025-12-10 | 1988 | done |
| 127 | Ranking and appearance | /search/docs/appearance/enable-web-stories | Enable Web Stories on Google | 2026-07-01 | 4063 | done |
| 128 | Ranking and appearance | /search/docs/appearance/enriched-search-results | Enriched and Interactive Search Results | 2025-12-10 | 4278 | done |
| 129 | Ranking and appearance | /search/docs/appearance/establish-business-details | Add Business Details to Google | 2025-12-10 | 4345 | done |
| 130 | Ranking and appearance | /search/docs/appearance/favicon-in-search | Define Website Favicon for Search Results | 2026-02-04 | 4267 | done |
| 131 | Ranking and appearance | /search/docs/appearance/featured-snippets | Featured Snippets and Your Website | 2025-12-10 | 2938 | done |
| 132 | Ranking and appearance | /search/docs/appearance/flexible-sampling | Flexible Sampling Guidelines | 2025-12-10 | 5115 | done |
| 133 | Ranking and appearance | /search/docs/appearance/google-discover | Get on Discover | 2026-03-09 | 6523 | done |
| 134 | Ranking and appearance | /search/docs/appearance/google-images | Image SEO Best Practices | 2026-03-02 | 12759 | done |
| 135 | Ranking and appearance | /search/docs/appearance/package-tracking | Package Tracking on Google | 2026-07-14 | 3056 | done |
| 136 | Ranking and appearance | /search/docs/appearance/page-experience | Understanding Google Page Experience | 2025-12-10 | 4276 | done |
| 137 | Ranking and appearance | /search/docs/appearance/preferred-sources | Guide to Preferred Sources in Google Search for Web Publishe | 2026-05-27 | 2976 | done |
| 138 | Ranking and appearance | /search/docs/appearance/publication-dates | Add a Byline Date to Google Search Results | 2025-12-10 | 3988 | done |
| 139 | Ranking and appearance | /search/docs/appearance/ranking-systems-guide | A Guide to Google Search Ranking Systems | 2025-12-10 | 11685 | done |
| 140 | Ranking and appearance | /search/docs/appearance/reviews-system | Google Search's Reviews System | 2025-12-10 | 2692 | done |
| 141 | Ranking and appearance | /search/docs/appearance/site-names | Site Names in Google Search | 2025-12-10 | 13328 | done |
| 142 | Ranking and appearance | /search/docs/appearance/sitelinks | Learn About What Sitelinks Are | 2025-12-10 | 1626 | done |
| 143 | Ranking and appearance | /search/docs/appearance/snippet | How to Write Meta Descriptions | 2026-04-20 | 8224 | done |
| 144 | Ranking and appearance | /search/docs/appearance/spam-updates | Google Search Spam Updates | 2025-12-10 | 1515 | done |
| 145 | Ranking and appearance | /search/docs/appearance/title-link | Influencing Title Links in Google Search | 2025-12-10 | 11390 | done |
| 146 | Ranking and appearance | /search/docs/appearance/top-places-list | Top Places List Optimization | 2025-12-10 | 1463 | done |
| 147 | Ranking and appearance | /search/docs/appearance/translated-results | Translated Google Search Results | 2025-12-10 | 2963 | done |
| 148 | Ranking and appearance | /search/docs/appearance/video | Video SEO Best Practices | 2025-12-18 | 20176 | done |
| 149 | Ranking and appearance | /search/docs/appearance/visual-elements-gallery | Visual Elements Gallery of Google Search | 2026-02-04 | 8523 | done |
| 150 | Ranking and appearance | /search/docs/appearance/web-stories-content-policy | Google Web Story Content Policies | 2025-12-10 | 2808 | done |
| 151 | Ranking and appearance | /search/docs/appearance/web-stories-creation-best-practices | Best Practices for Creating Web Stories | 2026-06-09 | 9253 | done |
| 152 | SEO fundamentals | /search/docs/fundamentals/ai-optimization-guide | Google's Guide to Optimizing for Generative AI Features on G | 2026-07-10 | 17442 | done |
| 153 | SEO fundamentals | /search/docs/fundamentals/creating-helpful-content | Creating Helpful, Reliable, People-First Content | 2025-12-10 | 11946 | done |
| 154 | SEO fundamentals | /search/docs/fundamentals/do-i-need-seo | Do You Need an SEO? Tips for Hiring an SEO | 2026-06-05 | 7774 | done |
| 155 | SEO fundamentals | /search/docs/fundamentals/get-on-google | How to Get Information on Google | 2025-12-10 | 6245 | done |
| 156 | SEO fundamentals | /search/docs/fundamentals/get-started | Technical SEO Techniques and Strategies | 2025-12-18 | 11566 | done |
| 157 | SEO fundamentals | /search/docs/fundamentals/get-started-developers | SEO Guide for Web Developers | 2025-12-10 | 1696 | done |
| 158 | SEO fundamentals | /search/docs/fundamentals/how-search-works | In-Depth Guide to How Google Search Works | 2025-12-18 | 7180 | done |
| 159 | SEO fundamentals | /search/docs/fundamentals/seo-starter-guide | SEO Starter Guide: The Basics | 2025-12-10 | 24596 | done |
| 160 | SEO fundamentals | /search/docs/fundamentals/third-party-seo | Google Search's Guidance on Third-Party SEO Tools & Advice | 2026-06-05 | 2971 | done |
| 161 | SEO fundamentals | /search/docs/fundamentals/using-gen-ai-content | Google Search's Guidance on Generative AI Content on Your We | 2025-12-10 | 2607 | done |
| 162 | Search Essentials | /search/docs/essentials | Google Search Essentials (formerly Webmaster Guidelines) | 2025-12-10 | 3120 | done |
| 163 | Search Essentials | /search/docs/essentials/spam-policies | Spam Policies for Google Web Search | 2026-05-15 | 22574 | done |
| 164 | Search Essentials | /search/docs/essentials/technical | Google Search Technical Requirements | 2025-12-18 | 2507 | done |
| 165 | Site-specific | /search/docs/specialty/ecommerce | SEO Best Practices for Ecommerce Sites | 2025-12-10 | 2676 | done |
| 166 | Site-specific | /search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites | Ecommerce URL Structure Best Practices | 2025-12-10 | 7462 | done |
| 167 | Site-specific | /search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure | Ecommerce Website Navigation Structure | 2025-12-10 | 3391 | done |
| 168 | Site-specific | /search/docs/specialty/ecommerce/how-to-launch-an-ecommerce-website | How To Launch an Ecommerce Site on Google | 2025-12-10 | 5988 | done |
| 169 | Site-specific | /search/docs/specialty/ecommerce/pagination-and-incremental-page-loading | Pagination Best Practices for Google | 2025-12-10 | 7073 | done |
| 170 | Site-specific | /search/docs/specialty/ecommerce/share-your-product-data-with-google | Share Your Product Data With Google | 2025-12-10 | 5881 | done |
| 171 | Site-specific | /search/docs/specialty/ecommerce/where-ecommerce-data-can-appear-on-google | Ecommerce Product Data and Content on Google | 2025-12-10 | 4285 | done |
| 172 | Site-specific | /search/docs/specialty/ecommerce/write-high-quality-reviews | How To Write Reviews | 2025-12-10 | 3205 | done |
| 173 | Site-specific | /search/docs/specialty/explicit/guidelines | SEO Guidelines for Explicit Content | 2025-12-10 | 9872 | done |
| 174 | Site-specific | /search/docs/specialty/explicit/troubleshooting | My Site is Incorrectly Flagged as Explicit in Google Search | 2025-12-10 | 5863 | done |
| 175 | Site-specific | /search/docs/specialty/international | Overview of International and Multilingual Site Topics | 2025-12-10 | 1305 | done |
| 176 | Site-specific | /search/docs/specialty/international/locale-adaptive-pages | How Google Crawls Locale-Adaptive Pages | 2025-12-10 | 1908 | done |
| 177 | Site-specific | /search/docs/specialty/international/localized-versions | Localized Versions of your Pages | 2025-12-22 | 16979 | done |
| 178 | Site-specific | /search/docs/specialty/international/managing-multi-regional-sites | Managing Multi-Regional and Multilingual Sites | 2025-12-10 | 10165 | done |