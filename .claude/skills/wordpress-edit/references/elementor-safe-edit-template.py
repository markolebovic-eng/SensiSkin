"""
Elementor-safe WordPress content edit template.

This is a REFERENCE TEMPLATE, not a runnable script — it has no argparse/CLI,
no credential loading. Copy the relevant function(s) inline into an ad-hoc
python snippet during a wordpress-edit session, adapting the exact `old`/`new`
strings and paths to the page you're actually editing. Do not run this file
as-is.

Why this exists: every content edit on this site must consider that the page
might be rendered by Elementor (`_elementor_edit_mode == "builder"`), in which
case the visible frontend comes from a JSON blob in `_elementor_data`, NOT from
the WordPress core `content` field alone. Editing only `content` produces a
change you can see in wp-admin / the Gutenberg editor but NOT on the live site
— this exact mistake happened in the session that produced this skill. This
template exists so it doesn't happen again.

Requires: WP_SITE_URL, WP_USERNAME, WP_APP_PASSWORD loaded into the environment
(`set -a; source .env; set +a` in bash) before the curl calls. Never print
these values. All curl calls need --ssl-no-revoke on this machine's Git Bash.
"""

import json
import os
import subprocess

SCRATCH = os.environ.get("SCRATCH", ".")  # set this to the actual scratchpad path


# ---------------------------------------------------------------------------
# Step 1 — fetch current state (do this from bash with curl, not from here;
# this function just documents the shape of what you get back)
# ---------------------------------------------------------------------------
def expected_fetch_fields():
    """
    curl -s --ssl-no-revoke -u "$WP_USERNAME:$WP_APP_PASSWORD" \
      "${WP_SITE_URL%/}/wp-json/wp/v2/posts/{ID}?context=edit&_fields=id,slug,status,title,content,meta,yoast_head_json" \
      -o "$SCRATCH/post-{ID}-current.json"
    """
    return ["id", "slug", "status", "title", "content", "meta", "yoast_head_json"]


# ---------------------------------------------------------------------------
# Step 2 — check Elementor status. ALWAYS do this before deciding how to write.
# ---------------------------------------------------------------------------
def check_elementor(fetched_json_path: str) -> tuple[bool, dict | None]:
    with open(fetched_json_path, encoding="utf-8") as f:
        data = json.load(f)
    meta = data.get("meta", {})
    edit_mode = meta.get("_elementor_edit_mode")
    is_elementor = edit_mode == "builder"
    elements = None
    if is_elementor and meta.get("_elementor_data"):
        elements = json.loads(meta["_elementor_data"])
    return is_elementor, elements


# ---------------------------------------------------------------------------
# Step 3 — ALWAYS back up the pre-edit state to a local file before writing
# anything. Do this for both content and _elementor_data (if present).
# ---------------------------------------------------------------------------
def backup_current_state(fetched_json_path: str, backup_dir: str, post_id: str):
    with open(fetched_json_path, encoding="utf-8") as f:
        data = json.load(f)

    content_raw = data["content"].get("raw", data["content"].get("rendered", ""))
    with open(f"{backup_dir}/post-{post_id}-content-backup.html", "w", encoding="utf-8") as f:
        f.write(content_raw)

    elementor_raw = data.get("meta", {}).get("_elementor_data")
    if elementor_raw:
        with open(f"{backup_dir}/post-{post_id}-elementor-backup.json", "w", encoding="utf-8") as f:
            f.write(elementor_raw)

    print(f"Backed up post {post_id}: content + elementor_data (if present)")


# ---------------------------------------------------------------------------
# Step 4 — find the exact text node inside _elementor_data. DO NOT assume the
# path (elements[0]["elements"][0]["settings"]["editor"]) is the same on every
# page — walk and search for a known substring first to confirm the real path,
# especially on pages with multiple widgets/columns/sections.
# ---------------------------------------------------------------------------
def find_text_nodes_containing(elements, needle: str, path: str = "root"):
    """Recursively search for any string value containing `needle`.
    Prints the path and a repr preview — use this BEFORE assuming a fixed
    path like elements[0]['elements'][0]['settings']['editor'].
    """
    matches = []

    def walk(node, p):
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, str) and needle.lower() in v.lower():
                    matches.append((f"{p}.{k}", v))
                walk(v, f"{p}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{p}[{i}]")

    walk(elements, path)
    return matches


# ---------------------------------------------------------------------------
# Step 5 — apply an EXACT, single-occurrence string replacement. Never do a
# broad regex rewrite across the whole blob. count=1 (via .replace(a,b,1)) so
# you can never accidentally clobber more than the one spot you verified.
# ---------------------------------------------------------------------------
def apply_single_replacement(text: str, old: str, new: str) -> str:
    assert old in text, f"Expected text not found — did the page change since you fetched it?\n{old!r}"
    new_text = text.replace(old, new, 1)
    assert new_text != text
    return new_text


# ---------------------------------------------------------------------------
# Step 6 — verify structural integrity of re-serialized JSON before writing.
# Compare key counts, not raw string length (ensure_ascii=False legitimately
# produces a shorter string than WordPress's original \uXXXX-escaped version
# — that is NOT data loss, but confirm it isn't real data loss too).
# ---------------------------------------------------------------------------
def count_keys(node) -> int:
    n = 0
    if isinstance(node, dict):
        n += len(node)
        for v in node.values():
            n += count_keys(v)
    elif isinstance(node, list):
        for v in node:
            n += count_keys(v)
    return n


def verify_no_structural_loss(old_raw: str, new_raw: str):
    old_data = json.loads(old_raw)
    new_data = json.loads(new_raw)
    old_count, new_count = count_keys(old_data), count_keys(new_data)
    assert old_count == new_count, f"Key count mismatch: {old_count} -> {new_count} — investigate before writing!"
    assert len(old_data) == len(new_data), "Top-level element count changed — investigate!"


# ---------------------------------------------------------------------------
# Step 7 — build the PATCH payload. Write BOTH content and _elementor_data if
# Elementor is active — writing only one leaves wp-admin and the frontend out
# of sync with each other.
# ---------------------------------------------------------------------------
def build_payload(new_content_html: str, new_elementor_elements: list | None,
                   extra_meta: dict | None = None) -> dict:
    meta = dict(extra_meta or {})
    if new_elementor_elements is not None:
        meta["_elementor_data"] = json.dumps(new_elementor_elements, ensure_ascii=False)
    return {"content": new_content_html, "meta": meta}


"""
Step 8 — apply via curl (run from bash, not python):

  python -c "import json; json.dump(payload, open('$SCRATCH/payload.json','w',encoding='utf-8'), ensure_ascii=False)"

  curl -s --ssl-no-revoke -u "$WP_USERNAME:$WP_APP_PASSWORD" \
    -X POST -H "Content-Type: application/json" \
    --data-binary "@$SCRATCH/payload.json" \
    "${WP_SITE_URL%/}/wp-json/wp/v2/posts/{ID}?context=edit" \
    -o "$SCRATCH/response.json" -w "HTTP: %{http_code}\n"

Step 9 — remind the owner to clear Elementor's cache:
  Elementor -> Tools -> General -> "Clear Files and Data"
  (a page-cache plugin or CDN may need a separate cache clear too)

Step 10 — verify against the LIVE frontend, not just the API echo response:

  curl -s --ssl-no-revoke -L "https://sensiskinstudio.com/{slug}/" -o "$SCRATCH/verify.html"
  grep -o "<title>.*</title>" "$SCRATCH/verify.html"
  grep -c "expected-new-text-fragment" "$SCRATCH/verify.html"
"""
