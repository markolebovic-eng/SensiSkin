import json
import re
import sys

SCRATCH = sys.argv[1]

def load(name):
    with open(f"{SCRATCH}/{name}", encoding="utf-8") as f:
        return json.load(f)

def analyze(items, kind):
    rows = []
    for it in items:
        title_rendered = it["title"]["rendered"]
        yh = it.get("yoast_head_json") or {}
        yoast_title = yh.get("title", "")
        yoast_desc = yh.get("description", "")
        meta = it.get("meta") or {}
        elementor_data = meta.get("_elementor_data") or ""
        has_elementor = bool(elementor_data)

        # crude alt-text signal: count image widgets vs count of empty "alt" keys in the raw JSON string
        alt_empty_count = len(re.findall(r'"alt":\s*""', elementor_data)) if has_elementor else None
        img_widget_count = len(re.findall(r'"widgetType":\s*"image"', elementor_data)) if has_elementor else None

        problems = []
        if not yoast_title.strip():
            problems.append("NEMA title (Yoast)")
        elif not (50 <= len(yoast_title) <= 60):
            problems.append(f"title duzina {len(yoast_title)} (van 50-60)")

        if not yoast_desc.strip():
            problems.append("NEMA meta description")
        elif not (150 <= len(yoast_desc) <= 160):
            problems.append(f"desc duzina {len(yoast_desc)} (van 150-160)")

        if has_elementor and alt_empty_count:
            problems.append(f"{alt_empty_count} slika bez alt teksta (od {img_widget_count} image widget-a)")

        rows.append({
            "kind": kind,
            "id": it["id"],
            "slug": it["slug"],
            "status": it["status"],
            "link": it.get("link", ""),
            "title_rendered": title_rendered,
            "yoast_title": yoast_title,
            "yoast_title_len": len(yoast_title),
            "yoast_desc": yoast_desc,
            "yoast_desc_len": len(yoast_desc),
            "has_elementor": has_elementor,
            "problems": problems,
        })
    return rows

pages = analyze(load("wp-pages-full.json"), "page")
posts = analyze(load("wp-posts-full.json"), "post")
all_rows = pages + posts

def priority(row):
    p = row["problems"]
    if any("NEMA title" in x or "NEMA meta description" in x for x in p):
        return 0
    if p:
        return 1
    return 2

all_rows.sort(key=priority)

with open(f"{SCRATCH}/wp_seo_audit_result.json", "w", encoding="utf-8") as f:
    json.dump(all_rows, f, ensure_ascii=False, indent=2)

total = len(all_rows)
with_problems = [r for r in all_rows if r["problems"]]
missing_critical = [r for r in all_rows if any("NEMA" in x for x in r["problems"])]

print(f"UKUPNO stavki: {total} ({len(pages)} stranica + {len(posts)} postova)")
print(f"Sa bar 1 problemom: {len(with_problems)}")
print(f"Kriticno (nedostaje title ili description): {len(missing_critical)}")
print()
print("=== TOP prioritet (nedostaje title/description) ===")
for r in all_rows:
    if any("NEMA" in x for x in r["problems"]):
        print(f"[{r['kind']}] {r['slug']} (status={r['status']}) -> {r['problems']}")
