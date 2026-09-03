---
name: reference-ccpr-grading-calibration
description: Where the CCPR A-E follow-up grading rules live and the corrected B/C threshold used for the UPR assessments
metadata: 
  node_type: memory
  type: reference
  originSessionId: d309f4c7-1abc-4acb-b889-03d4e5c6dc71
  modified: 2026-09-03T14:36:59.515Z
---

The A–E scale used across this project (US/Denmark/Namibia/Paraguay UPR cycle-3
implementation assessments) is the Human Rights Committee's follow-up scale
(CCPR/C/108/2). Two training docs in the repo hold the calibration:

- `training/CCPR_followup_grading_corpus_analysis.md` — mined all 143 CCPR
  follow-up reports (OHCHR TBSearch TreatyID=8, DocTypeID=117, cat 3), ~800
  graded sub-limbs. Distribution: A 4–6%, B ~44%, C ~43%, D 4–5%, E ~3%
  (E rising to ~9% in 2022–2026). Downloaded PDFs cached at
  `%LOCALAPPDATA%/Temp/claude/.../fu_all/`.
- `training/CCPR_followup_grading_calibration.md` — the working rules, plus a
  blind-test (18/24, all 6 misses one notch too strict) and the **corrected
  B/C threshold**: C is narrow (pre-existing/ongoing measures, "under study",
  years-stalled bill, off-point); B = any concrete on-point measure
  enacted/adopted/amended/launched/introduced *in the review period* even if
  not in force or partial; A = core ask essentially met.

That corrected rule was applied to the four `*/assess.py` files (2026-09-03):
Denmark 4 themes C→B, Namibia 15, Paraguay 12, **US unchanged** (its evidence is
inaction + 2025 regression, correctly C/E). Post-recal shares: Denmark B 68%,
Namibia B 61%, Paraguay B 59%, US C 63% / E 35%. Re-run with
`python -m countries.<slug>.assess` then `scripts.make_report` +
`scripts.fill_thematic_list`; US uses `scripts.apply_assessment`.
See [[user-ccpr-centre]].

## The `site/` deliverable (database + world map + website)

Built 2026-09-03. `python site/build.py` reads the four country DBs +
`site/data/hrc_followup.py` (hand-entered HRC follow-up grades: US CCPR/C/114/2,
DNK CCPR/C/125/2/Add.4, NAM CCPR/C/126/2/Add.4, PRY CCPR/C/140/2/Add.2) and
regenerates `site/assessments.db` (consolidated SQLite) + `site/public/data/*.json`.
`site/public/` is a dependency-free static site: `index.html` (d3 choropleth,
UPR/HRC toggle, vendored d3+topojson+world-110m), `country.html?c=USA` (per-country
detail, both mechanisms). Map score = A100/B70/C35/D15/E0 mean. Deploy: drag
`site/public/` to Netlify drop, or GitHub Pages from `/site/public`. Preview:
`cd site/public && python -m http.server`. Full how-to in `site/README.md`.
Add a country: assess it, add an HRC block, add one line to `SLUG_A3` in
`site/build.py`, rebuild.
