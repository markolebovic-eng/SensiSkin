# SOURCE: https://developers.google.com/search/docs/appearance/structured-data/software-app
# LAST-UPDATED: 2025-12-10

- 
 
 
 
 
 
 
 
 Home
 
 
 
 
 
 
 
 
- 
 
 
 

 
 
 
 
 
 
 
 Search Central
 
 
 
 
 
 
 
 
- 
 
 
 

 
 
 
 
 
 
 
 Documentation
 
 
 
 
 
 
 

 
 
 
 
 
 
 

 
 

 
 
 
 Send feedback
 
 

 
 
 
 
 

 
 
 
 
 

 
 
 
 

# Software app (SoftwareApplication) structured data

 
 Mark up software application information in the body of a web page to better display your app
 details in Google Search results.

 
 
 Note: The actual appearance in search results might be different. You can
 preview most features with the
 Rich Results Test.
 
 
 
 

## 
 How to add structured data
 

 Structured data is a standardized format for providing information about a page and classifying the page
 content. If you're new to structured data, you can learn more about
 how structured data works.
 

 
 Here's an overview of how to build, test, and release structured data.

 
 
- Add the required properties. Based on the
 format you're using, learn where to insert structured data on the page.
 
 Using a CMS? It may be easier to use a plugin that's integrated into your CMS.
 
 Using JavaScript? Learn how to
 generate structured data with JavaScript.
 
 
- Follow the guidelines.
 
- Validate your code using the
 Rich Results Test
 and fix any critical errors. Consider also fixing any non-critical issues that may be flagged
 in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results). 
 
- Deploy a few pages that include your structured data and use the URL Inspection tool to test how Google sees the page. Be sure that your page is
 accessible to Google and not blocked by a robots.txt file, the noindex tag, or
 login requirements. If the page looks okay, you can
 ask Google to recrawl your URLs.
 Note: Allow time for re-crawling and re-indexing. Remember that it
 may take several days after publishing a page for Google to find and crawl it.
 
 
- To keep Google informed of future changes, we recommend that you
 submit a sitemap. You can automate this with the
 Search Console Sitemap API.
 

 
 

## Examples

 
 
 JSON-LD
 Here's an example of a software app in JSON-LD:

 <html>
 <head>
 <title>Angry Birds</title>
 <script type="application/ld+json">
 {
 "@context": "https://schema.org",
 "@type": "SoftwareApplication",
 "name": "Angry Birds",
 "operatingSystem": "ANDROID",
 "applicationCategory": "GameApplication",
 "aggregateRating": {
 "@type": "AggregateRating",
 "ratingValue": 4.6,
 "ratingCount": 8864
 },
 "offers": {
 "@type": "Offer",
 "price": 1.00,
 "priceCurrency": "USD"
 }
 }
 </script>
 </head>
 <body>
 </body>
</html>
 
 
<html>
 <head>
 <title>Angry Birds</title>
 <script type="application/ld+json">
 {
 "@context": "https://schema.org",
 "@type": "SoftwareApplication",
 "name": "Angry Birds",
 "operatingSystem": "ANDROID",
 "applicationCategory": "GameApplication",
 "aggregateRating": {
 "@type": "AggregateRating",
 "ratingValue": 4.6,
 "ratingCount": 8864
 },
 "offers": {
 "@type": "Offer",
 "price": 1.00,
 "priceCurrency": "USD"
 }
 }
 </script>
 </head>
 <body>
 </body>
</html>