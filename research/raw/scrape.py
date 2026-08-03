import urllib.request, concurrent.futures, re, os, json, time, html as H
os.makedirs("pages",exist_ok=True)
urls=[l.strip() for l in open("urls.txt",encoding="utf-8") if l.strip()]
def slug(u): return re.sub(r'[^a-z0-9]+','_',u.replace("https://developers.google.com/","").lower()).strip("_")
def clean(h):
    m=re.search(r'<div[^>]*class="devsite-article-body[^"]*"[^>]*>(.*?)</div>\s*</article>',h,re.S)
    body=m.group(1) if m else h
    body=re.sub(r'<(script|style|nav|noscript)[^>]*>.*?</\1>','',body,flags=re.S)
    body=re.sub(r'<h([1-6])[^>]*>','\n\n#'*1+r'',body)  # placeholder
    return body
def txt(h):
    b=h
    m=re.search(r'<article[^>]*>(.*?)</article>',h,re.S)
    if m: b=m.group(1)
    b=re.sub(r'<(script|style|nav|noscript|svg)[^>]*>.*?</\1>','',b,flags=re.S)
    for lvl in range(1,7):
        b=re.sub(r'<h%d[^>]*>(.*?)</h%d>'%(lvl,lvl),lambda m,l=lvl:"\n\n"+"#"*l+" "+m.group(1)+"\n",b,flags=re.S)
    b=re.sub(r'<li[^>]*>',"\n- ",b)
    b=re.sub(r'</(p|div|tr|table|pre|ul|ol)>',"\n",b)
    b=re.sub(r'<td[^>]*>'," | ",b)
    b=re.sub(r'<[^>]+>','',b)
    b=H.unescape(b)
    b=re.sub(r'\n{3,}','\n\n',b)
    b=re.sub(r'[ \t]{2,}',' ',b)
    return b.strip()
def get(u):
    p=f"pages/{slug(u)}.html"
    if os.path.exists(p) and os.path.getsize(p)>5000: 
        return u, open(p,encoding="utf-8",errors="replace").read()
    for a in range(4):
        try:
            r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"})
            d=urllib.request.urlopen(r,timeout=45).read().decode("utf-8","replace")
            open(p,"w",encoding="utf-8").write(d)
            return u,d
        except Exception as e:
            time.sleep(1.5+a*2); err=str(e)
    return u,None
recs=[]
with concurrent.futures.ThreadPoolExecutor(5) as ex:
    for u,d in ex.map(get,urls):
        if not d:
            recs.append({"url":u,"status":"FAILED"}); print("FAIL",u); continue
        t=re.search(r'<title>(.*?)</title>',d,re.S)
        upd=re.search(r'Last updated ([0-9]{4}-[0-9]{2}-[0-9]{2}) UTC',d)
        if not upd: upd=re.search(r'"dateModified"\s*:\s*"([0-9-]+)',d)
        body=txt(d)
        open(f"pages/{slug(u)}.md","w",encoding="utf-8").write(f"# SOURCE: {u}\n# LAST-UPDATED: {upd.group(1) if upd else 'UNKNOWN'}\n\n"+body)
        recs.append({"url":u,"title":H.unescape(t.group(1)).replace("&nbsp;"," ").strip() if t else "",
                     "updated":upd.group(1) if upd else "UNKNOWN","chars":len(body),"status":"done"})
json.dump(recs,open("scrape_index.json","w"),indent=1)
print("done:",sum(1 for r in recs if r["status"]=="done"),"failed:",sum(1 for r in recs if r["status"]=="FAILED"))
