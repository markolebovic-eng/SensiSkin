# SOURCE: https://docs.perplexity.ai/guides/bots

## Documentation Index
Fetch the complete documentation index at: /llms.txt
Use this file to discover all available pages before exploring further.
Skip to main content

For AI agents: see the complete llms.txt documentation index.

Perplexity home page

Docs
Cookbook
API Reference

- Get Started
- Get Started

Search...

Navigation
Resources
Perplexity Crawlers

Search

⌘K

- Community
- Blog
- Changelog

### Getting Started

- Overview

- Quickstart

- Pricing

- Perplexity MCP Server

- Perplexity CLI

### Gateway API

- Quickstart

- Models

- Routing & Reliability

### Agent API

- Quickstart

- Building agents

- Models & Configuration

- Tools

- Features

- OpenAI Compatibility

- Migrate from Sonar

- Prompt Guide

### Search API

- Quickstart

- Best Practices

- Agent SDKs

- Filters

### Embeddings API

- Quickstart

- Best Practices

- Standard Embeddings

- Contextualized Embeddings

### Perplexity SDK

- Quickstart

- Guides

### Admin & Management

- Signing In

- API Groups & Billing

- API Key Management

- Computer Analytics API

- Rate Limits & Usage Tiers

- AWS Marketplace

### Resources

- Integrations

- API Roadmap

- Privacy & Security

- Frequently Asked Questions

- System Status

- Changelog

- Get in Touch

- Perplexity Crawlers

### Legacy API

- Sonar API

## On this page

- WAF Configuration
- Cloudflare WAF
- AWS WAF
- IP Address Sources
- Best Practices

Resources

# Perplexity Crawlers
Copy pageCopy page

We strive to improve our service every day by delivering the best search experience possible. To achieve this, we collect data using web crawlers (“robots”) and user agents that gather and index information from the internet, operating either automatically or in response to user requests. Webmasters can use the following robots.txt tags to manage how their sites and content interact with Perplexity. Each setting works independently, and it may take up to 24 hours for our systems to reflect changes.

Copy pageCopy page

User AgentDescription
 | PerplexityBot | PerplexityBot is designed to surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models. To ensure your site appears in search results, we recommend allowing PerplexityBot in your site’s robots.txt file and permitting requests from our published IP ranges listed below.Full user-agent string: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)Published IP addresses: https://www.perplexity.com/perplexitybot.json
 | Perplexity‑User | Perplexity-User supports user actions within Perplexity. When users ask Perplexity a question, it might visit a web page to help provide an accurate answer and include a link to the page in its response. Perplexity-User controls which sites these user requests can access. It is not used for web crawling or to collect content for training AI foundation models.Full user-agent string: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)Published IP addresses: https://www.perplexity.com/perplexity-user.jsonSince a user requested the fetch, this fetcher generally ignores robots.txt rules.

## ​

WAF Configuration

If you’re using a Web Application Firewall (WAF) to protect your site, you may need to explicitly whitelist Perplexity’s bots to ensure they can access your content. Below are configuration guidelines for popular WAF providers.

### ​

Cloudflare WAF

To configure Cloudflare WAF to allow Perplexity bots:

1

Navigate to WAF settings
In your Cloudflare dashboard, go to Security → WAF.

2

Create a new rule
Click on Custom rules and create a new rule to allow Perplexity bots.

3

Configure rule conditions
Set up a rule that combines both User-Agent and IP address conditions:

- Field: User Agent

- Operator: Contains

- Value: PerplexityBot OR Perplexity-User

AND

- Field: IP Source Address

- Operator: Is in

- Value: Use the IP ranges from the official endpoints listed below

4

Set rule action
Set the action to Allow to ensure these requests bypass other security rules.

### ​

AWS WAF

For AWS WAF configuration, create IP sets and string match conditions:

1

Create IP sets
In the AWS WAF console, create IP sets for both PerplexityBot and Perplexity-User using the IP addresses from the official endpoints listed below.

2

Create string match conditions
Create string match conditions for the User-Agent headers:

- PerplexityBot

- Perplexity-User

3

Create allow rules
Create rules that combine the IP sets with the corresponding User-Agent strings, and set the action to Allow.

4

Associate with Web ACL
Associate these rules with your Web ACL and ensure they have higher priority than blocking rules.

### ​

IP Address Sources

Always use the most current IP ranges from the official JSON endpoints. These addresses are updated regularly and should be the source of truth for your WAF configurations.

- PerplexityBot IP addresses: https://www.perplexity.com/perplexitybot.json

- Perplexity-User IP addresses: https://www.perplexity.com/perplexity-user.json

Set up automated processes to periodically fetch and update your WAF rules with the latest IP ranges from these endpoints to ensure continuous access for Perplexity bots.

### ​

Best Practices

When configuring WAF rules for Perplexity bots, combine both User-Agent string matching and IP address verification for enhanced security while ensuring legitimate bot traffic can access your content.

Changes to WAF configurations may take some time to propagate. Monitor your logs to ensure the rules are working as expected and that legitimate Perplexity bot traffic is being allowed through.

Was this page helpful?
YesNo

Get in Touch
Previous

Sonar API
Next

⌘I

xdiscordwebsite
Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions
What is the Agent API?Which Agent API model should I use?How do I create an API key?