import urllib.request, urllib.error, time, sys, json
from ua_probe import UAS

def classify(code, body, ctype):
    t = body.decode("utf-8","replace")[:3000]
    if code != 200:
        return f"HTTP_{code}"
    if "One moment, please" in t or "window.location.reload()" in t[:1200]:
        return "INTERSTITIAL"      # 200 status, JS challenge body - a FALSE PASS
    if "xml" in (ctype or "") or t.lstrip().startswith("<?xml"):
        return "OK_XML"
    if len(t) > 800:
        return "OK_CONTENT"
    return "THIN"

def probe(url, ua):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept":"text/html,application/xhtml+xml,application/xml,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return r.status, r.read(), r.headers.get("Content-Type"), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read(), e.headers.get("Content-Type"), dict(e.headers)
    except Exception as e:
        return None, str(e).encode(), None, {}

if __name__=="__main__":
    url=sys.argv[1]; gap=float(sys.argv[2]); warm=float(sys.argv[3]) if len(sys.argv)>3 else 0
    names=sys.argv[4].split(",") if len(sys.argv)>4 else list(UAS)
    if warm:
        print(f"(cooling down {warm}s before first request...)", flush=True)
        time.sleep(warm)
    res={}
    for n in names:
        code, body, ctype, hdrs = probe(url, UAS[n])
        v = classify(code, body, ctype)
        res[n]=v
        print(f"{n:<20} {str(code):<5} {v:<14} len={len(body):<7} server={hdrs.get('Server')}", flush=True)
        time.sleep(gap)
    json.dump(res, open("classified_"+str(abs(hash(url))%1000)+".json","w"), indent=1)
    print("\nSUMMARY:", json.dumps(res, indent=1))
