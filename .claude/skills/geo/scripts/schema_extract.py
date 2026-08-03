#!/usr/bin/env python3
"""
JSON-LD extractor and structural validator.

Pulls every application/ld+json block from a page, parses it, expands @graph,
and reports the type inventory plus required-property gaps for the Google
feature types we implement most.

KNOWN LIMIT - read this before reporting "no schema found":
This script sees the raw HTML only. Many CMS plugins (Yoast, RankMath, AIOSEO)
and most JS frameworks inject JSON-LD client-side, where it is invisible here.
A clean "no schema" result from this tool is NOT a finding until confirmed with
a rendering tool (Rich Results Test, or a headless browser evaluating
document.querySelectorAll('script[type="application/ld+json"]')).
Use --strict to make the script refuse to report an empty result as a finding.

Usage:
    python schema_extract.py https://example.com/page
    python schema_extract.py --urls urls.txt --json out.json
"""
import argparse, json, re, sys, urllib.request, urllib.error

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"

# Required properties per Google's feature documentation. Recommended props are in
# references/structured-data-matrix.md - these are the ones that cost you eligibility.
REQUIRED = {
    "Article":       ["headline"],
    "NewsArticle":   ["headline"],
    "BlogPosting":   ["headline"],
    "Product":       ["name"],
    "Recipe":        ["name", "image"],
    "Event":         ["name", "startDate", "location"],
    "JobPosting":    ["title", "description", "hiringOrganization", "datePosted"],
    "LocalBusiness": ["name", "address"],
    "Organization":  ["name"],
    "FAQPage":       ["mainEntity"],
    "HowTo":         ["name", "step"],
    "BreadcrumbList":["itemListElement"],
    "VideoObject":   ["name", "description", "thumbnailUrl", "uploadDate"],
    "Person":        ["name"],
    "Review":        ["itemReviewed", "reviewRating", "author"],
    "SoftwareApplication": ["name"],
    "Course":        ["name", "description"],
}

# Types that carry per-engine AI meaning beyond Google rich results.
AI_RELEVANT_NOTES = {
    "isAccessibleForFree": "Apple honours isAccessibleForFree:false to exclude a page from AI grounding "
                           "while keeping it search-eligible (page-level only; hasPart not supported).",
    "sameAs": "Feeds entity resolution across every engine - the strongest off-site GEO signal in markup.",
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def extract(html):
    blocks, errors = [], []
    for m in re.finditer(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.S | re.I
    ):
        raw = m.group(1).strip()
        # strip CDATA wrappers and HTML comments some CMSes emit
        raw = re.sub(r'^\s*<!\[CDATA\[|\]\]>\s*$', '', raw).strip()
        raw = re.sub(r'^\s*<!--|-->\s*$', '', raw).strip()
        try:
            blocks.append(json.loads(raw))
        except json.JSONDecodeError as e:
            errors.append(f"invalid JSON at offset {m.start()}: {e}")
    return blocks, errors


def flatten(obj, out=None):
    """Expand @graph and arrays into a flat list of typed nodes."""
    out = out if out is not None else []
    if isinstance(obj, list):
        for o in obj:
            flatten(o, out)
    elif isinstance(obj, dict):
        if "@graph" in obj:
            flatten(obj["@graph"], out)
            rest = {k: v for k, v in obj.items() if k != "@graph"}
            if rest.get("@type"):
                out.append(rest)
        elif obj.get("@type"):
            out.append(obj)
    return out


def types_of(node):
    t = node.get("@type", [])
    return [t] if isinstance(t, str) else list(t)


def analyse(url, html):
    blocks, errors = extract(html)
    nodes = flatten(blocks)
    findings, inventory = [], {}

    for n in nodes:
        for t in types_of(n):
            inventory[t] = inventory.get(t, 0) + 1
            for prop in REQUIRED.get(t, []):
                if prop not in n:
                    findings.append(f"{t}: missing required property '{prop}'")

    notes = []
    blob = json.dumps(blocks)
    for prop, note in AI_RELEVANT_NOTES.items():
        if prop in blob:
            notes.append(f"{prop} present - {note}")

    return {
        "url": url,
        "blocks": len(blocks),
        "nodes": len(nodes),
        "types": inventory,
        "parse_errors": errors,
        "missing_required": findings,
        "ai_notes": notes,
        "js_injection_warning": len(blocks) == 0,
    }


def report(r):
    print(f"\n=== {r['url']}")
    if r["js_injection_warning"]:
        print("  NO JSON-LD IN RAW HTML.")
        print("  NOT YET A FINDING - confirm with a renderer before reporting. Schema may be JS-injected.")
        return
    print(f"  {r['blocks']} block(s), {r['nodes']} typed node(s)")
    print("  types: " + ", ".join(f"{k}({v})" for k, v in sorted(r["types"].items())))
    for e in r["parse_errors"]:
        print(f"  PARSE ERROR: {e}")
    for f in r["missing_required"]:
        print(f"  GAP: {f}")
    for n in r["ai_notes"]:
        print(f"  NOTE: {n}")
    if not r["parse_errors"] and not r["missing_required"]:
        print("  no required-property gaps detected")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url", nargs="?")
    ap.add_argument("--urls")
    ap.add_argument("--json")
    ap.add_argument("--strict", action="store_true",
                    help="exit 2 if any page has zero raw-HTML JSON-LD (forces manual render check)")
    a = ap.parse_args()

    targets = [a.url] if a.url else []
    if a.urls:
        targets += [l.strip() for l in open(a.urls, encoding="utf-8") if l.strip()]
    if not targets:
        ap.error("give a URL or --urls")

    out = []
    for u in targets:
        try:
            r = analyse(u, fetch(u))
        except Exception as e:
            r = {"url": u, "error": str(e), "js_injection_warning": False,
                 "blocks": 0, "nodes": 0, "types": {}, "parse_errors": [str(e)],
                 "missing_required": [], "ai_notes": []}
        out.append(r)
        report(r)

    if a.json:
        json.dump(out, open(a.json, "w"), indent=2)
        print(f"\nwrote {a.json}")

    if a.strict and any(r["js_injection_warning"] for r in out):
        sys.exit(2)
    sys.exit(1 if any(r["parse_errors"] or r["missing_required"] for r in out) else 0)


if __name__ == "__main__":
    main()
