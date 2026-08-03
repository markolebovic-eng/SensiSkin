import re
base="https://developers.google.com"
nav=[l.strip() for l in open("nav_links.txt",encoding="utf-8") if l.startswith("/")]
crawl="""/crawling/docs/about-crawling
/crawling/docs/changelog
/crawling/docs/crawl-budget
/crawling/docs/crawlers-fetchers/apis-user-agent
/crawling/docs/crawlers-fetchers/feedfetcher
/crawling/docs/crawlers-fetchers/google-common-crawlers
/crawling/docs/crawlers-fetchers/google-special-case-crawlers
/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers
/crawling/docs/crawlers-fetchers/overview-google-crawlers
/crawling/docs/crawlers-fetchers/read-aloud-user-agent
/crawling/docs/crawlers-fetchers/reduce-crawl-rate
/crawling/docs/crawlers-fetchers/verify-google-requests
/crawling/docs/crawlers-fetchers/verifying-googlebot
/crawling/docs/crawlers-fetchers/web-bot-auth
/crawling/docs/faceted-navigation
/crawling/docs/myths-about-crawling
/crawling/docs/robots-txt/create-robots-txt
/crawling/docs/robots-txt/robots-txt-spec
/crawling/docs/robots-txt/submit-updated-robots-txt
/crawling/docs/robots-txt/useful-robots-txt-rules
/crawling/docs/troubleshooting/dns-network-errors
/crawling/docs/troubleshooting/http-status-codes""".split("\n")
extra="""/search/docs/appearance/structured-data/search-gallery
/search/updates
/search/blog"""
allp=sorted(set([p for p in nav if "/docs" in p or p in ("/search/updates","/search/blog")] + crawl + extra.split("\n")))
open("urls.txt","w").write("\n".join(base+p for p in allp))
print(len(allp))
