# SOURCE: https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google
# LAST-UPDATED: 2025-12-10

- 
 
 
 
 
 
 
 
 Home
 
 
 
 
 
 
 
 
- 
 
 
 

 
 
 
 
 
 
 
 Search Central
 
 
 
 
 
 
 
 
- 
 
 
 

 
 
 
 
 
 
 
 Documentation
 
 
 
 
 
 
 

 
 
 
 
 
 
 

 
 

 
 
 
 Send feedback
 
 

 
 
 
 
 

 
 
 
 
 

 
 
 
 

# Share your product data with Google

 
 
 To increase eligibility for
 richer appearances and on more surfaces across Google
 that can bring more relevant traffic to your site, share your ecommerce product data with
 Google. To take advantage of these benefits, Google recommends that you do the following:
 

 
 
- 
 Include structured data in your site's product pages.
 Learn more about the benefits of
 adding structured data to your web pages.
 
 
- 
 Tell Google directly which products you want to show on Google
 by uploading a feed to
 Google Merchant Center.
 Google Merchant Center is a Google service that has a deeper understanding of commerce data.
 Learn more about the benefits of Google Merchant Center.
 
 

 

## 
 Add product structured data to web pages
 

 
 Where feasible, add structured data to your product pages. While structured data isn't
 required to appear in Google Search results, it can help Google understand your page better
 and display it as a rich result. For example:
 

 
 
- 
 Structured data increases eligibility for
 Product rich results.
 
 
- 
 Structured data can improve the accuracy of Google's understanding of content such as price,
 discount, and shipping costs on a page (this can also help the accuracy of Google Merchant
 Center verification of product feeds against your site).
 
 

 
 Ready to start implementing? Check out
 Include structured data relevant to ecommerce
 for more information.
 

 
 Google may at times use other approaches to extract data from pages. If you want to explicitly
 tell Google not to use content on a page to form a snippet, add a
 data-nosnippet attribute
 to that HTML element.
 

 

## 
 Upload data to Google Merchant Center
 

 
 While uploading product data to Google Merchant Center isn't mandatory to appear in Google
 search results, it can enhance Google's understanding of your products. Participation in Google
 Merchant Center is mandatory for some Google surfaces, such as listings in the
 Google Shopping tab.
 

 What is Product Data? Product data describes various attributes of
 products, such as its title, description, color, pricing, and availability.
 
 For smaller sites that are updated less frequently, you can use an
 automated feed to build your product data
 from crawled web content (structured data can help improve the accuracy of data extraction).
 This approach can also be useful to get started with less effort.
 

 
 For larger sites or sites with frequently changing content, periodically
 upload new data feed files
 to Google Merchant Center (or for immediate updates use the
 Content API).
 This gives you greater control over your data in Google. Benefits of uploading feed files include:
 

 
 
- 
 Increase confidence Google knows all of your products.
 Web crawling is not guaranteed to find all products on your site.
 
 
- 
 Gain greater control over the timing of updates.
 Google does not guarantee how long it takes before changes on your site will be processed through crawling. Feeds
 can be used for weekly, daily, or even hourly updates, at your time of choice. The Content
 API allows immediate content updates, which is particularly useful for stock level updates.
 
 
- 
 Share data that's not present on your website.
 You may decide some information is not appropriate to include on your web site, such as
 physical store level inventory data. Feeds and the Content API let you share this data with
 Google without it being present on your website.
 
 

 
 Learn more about how to
 Sign up for Google Merchant Center.
 

 

## How Google uses structured data and Google Merchant Center data

 
 The following are examples of how Google uses structured data embedded in web pages and Google Merchant Center data
 for different experiences. Note that experiences may vary by country, device, and other
 factors.
 

 
 
 ExperienceStructured DataGoogle Merchant Center

 
 | Product rich results in Google Search
 | Google Search uses Product structured data to display product rich results.
 | Google Search may use Google Merchant Center data to display product rich results.
 

 
 | Google Images results with product annotations
 | Google Images uses Product structured data to display product annotations on images.
 | Google Images uses images listed in Google Merchant Center.
 

 
 | Google Shopping tab
 | Adding structured data can help Google Merchant Center in some cases (for example, during data verification).
 | Participation in Google Merchant Center is required to appear in the Google Shopping tab.
 

 
 | Google Lens image search results
 | Google Lens uses image structured data properties where available.
 | Google Images uses images listed in Google Merchant Center.
 

 
 

 

## 
 Resolving update delay issues
 

 
 When Google combines data from your website and Google Merchant Center feeds, it can lead to
 data inconsistency issues due to lag. For example, if a product sells out, your website would
 typically immediately mark it as unavailable for purchase, but Google Merchant
 Center may not be updated until some time later, especially if you're using feeds.
 

 
 To avoid this potential conflict in pricing and stock availability data (a common cause of
 synchronization issues), tell Google Merchant Center
 to automatically update its copy of your product data
 based on the website contents, when such a discrepancy is noticed.
 

 
 To learn more about how Googlebot and Google Merchant Center work together, see
 How to get your products into Search
 from the Search Central Lightning talk series.
 

 
 
 
 

 
 
 
 

 
 
 

 
 
 
 
 
 
 
 
 

 
 
 
 Send feedback