import urllib.request, urllib.error, time, sys, json, ssl

UAS = {
 "OAI-SearchBot":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot",
 "GPTBot":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot",
 "ChatGPT-User":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot",
 "PerplexityBot":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)",
 "Perplexity-User":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)",
 "Claude-SearchBot":"Mozilla/5.0 (compatible; Claude-SearchBot/1.0; +http://www.anthropic.com/bot.html)",
 "Claude-User":"Mozilla/5.0 (compatible; Claude-User/1.0; +http://www.anthropic.com/bot.html)",
 "ClaudeBot":"Mozilla/5.0 (compatible; ClaudeBot/1.0; +http://www.anthropic.com/bot.html)",
 "Googlebot":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Google-Extended":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Bingbot":"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
 "Amazonbot":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 (compatible; Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)",
 "Amzn-SearchBot":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-SearchBot/0.1)",
 "Applebot":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)",
 "Applebot-Extended":"Mozilla/5.0 (Applebot-Extended/0.1; +http://www.apple.com/go/applebot)",
 "meta-externalagent":"meta-externalagent/1.1 (+https://developers.facebook.com/docs/sharing/webmasters/crawler)",
 "Bytespider":"Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; Bytespider; spider-feedback@bytedance.com)",
 "Chrome-baseline":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

def probe(url, ua):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept":"text/html,application/xhtml+xml,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, dict(r.headers), r.read()[:4000]
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()[:4000]
    except Exception as e:
        return None, {}, str(e).encode()

if __name__ == "__main__":
    url = sys.argv[1]; delay = float(sys.argv[2]) if len(sys.argv)>2 else 7.0
    only = sys.argv[3].split(",") if len(sys.argv)>3 else list(UAS)
    out={}
    for name in only:
        code, hdrs, body = probe(url, UAS[name])
        out[name]={"code":code,"server":hdrs.get("server"),"cf_ray":hdrs.get("cf-ray"),
                   "x_served_by":hdrs.get("x-served-by"),"via":hdrs.get("via"),
                   "x_sucuri":hdrs.get("x-sucuri-id"),"x_cache":hdrs.get("x-cache"),
                   "retry_after":hdrs.get("retry-after"),"len":len(body)}
        print(f"{name:<20} {str(code):<5} server={hdrs.get('server')} cf-ray={hdrs.get('cf-ray')}")
        time.sleep(delay)
    json.dump(out, open(f"probe_{abs(hash(url))%10000}.json","w"), indent=1)
