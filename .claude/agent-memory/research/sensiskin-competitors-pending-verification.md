---
name: sensiskin-competitors-pending-verification
description: SensiSkin competitors.md was created 2026-07-05 with all-unverified WebSearch-proposed URLs; owner confirmation still pending as of that date
metadata:
  type: project
---

On 2026-07-05, `.agents/clients/sensiskin/competitors.md` did not exist, so it was created
during the first research agent run with the default competitor list (5 in "laserska
epilacija": Vita Elos, Divine Beauty, Studio LiliuM, K2 Derma, Dr. Jelena Glavinić Clinic;
4 in "kozmetološki centar": Soze Beauty, Ceca Skincare, Madam In, VIVA Beauty).

Every competitor got a WebSearch-proposed URL, marked "[PREDLOŽENO - NEVERIFIKOVANO]" in the
file. Two are flagged as needing extra owner attention:
- **Divine Beauty** (https://divinebeauty.rs/) — owner-named competitor, never verified in
  MEMORY.md, but WebSearch found a clear single candidate site.
- **VIVA Beauty** — WebSearch found TWO distinct, similarly-named salons (VIVA Beauty Centar,
  Somborska 17, social-only presence; VIVA LAM, vivalam.com, different address) and could not
  confidently pick one — left as "URL nije pronađen, potrebna ručna provera."

**Why this matters:** Per the research agent's own rules ([[research agent definition]]),
newly-proposed/unverified URLs must be skipped for map/scrape until the owner confirms them.
This means the 2026-07-05 run's "local/regional" competitor flow was entirely empty — all 10
proposed blog topics came from global trend research + MEMORY.md history only, not from
fresh competitor content.

**How to apply:** Before the next research run, check whether the owner has edited
competitors.md to confirm/correct URLs (especially Divine Beauty and VIVA Beauty). If still
unconfirmed, the local competitor flow will again be empty — flag this to the user rather
than silently proceeding as if competitor data was fresh.
