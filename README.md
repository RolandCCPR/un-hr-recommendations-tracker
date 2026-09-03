# Assessment of recommendations — United States, UPR cycle 3

A small Python project that stores every recommendation the United States
received in the **3rd UPR cycle** (A/HRC/46/15, 36th session), its **source**,
and a **level-of-implementation grade**, and produces a first-pass assessment
of implementation ahead of the 4th-cycle review, using the UN and stakeholder
reports submitted for that cycle.

Storage is one local SQLite file (`recommendations.db`). The `recommendations`
package has no third-party runtime dependencies; the helper scripts use
`python-docx`.

## Grade scale

Adapted from the Human Rights Committee A–E follow-up assessment
(CCPR/C/108/2, https://ccprcentre.org/follow-up-and-assessment). The Committee
grades a State's *reply*; here the letters grade the *level of implementation*
on the strength of third-party reporting.

| Grade | Meaning here |
|---|---|
| `A` | Largely implemented / action largely satisfactory |
| `B` | Partially implemented / steps taken, further action needed |
| `C` | Not implemented / no relevant action taken |
| `D` | No information available on implementation |
| `E` | Contrary measures taken, or recommendation rejected |

## Data & evidence

| File | What it is |
|---|---|
| `UPR36_United_States_of_America_Thematic_List_of_Recommendations.docx` | OHCHR thematic list — the 347 cycle-3 recommendations, source of the import |
| `US UPR recommendations cycle 3 only.xlsx` | UHRI export of the same recommendations (alternative import source) |
| `evidence/A_HRC_WG.6_50_USA_2-EN.pdf` + `compilation_USA_2.txt` | OHCHR **Compilation of UN information**, 28 Aug 2025 |
| `evidence/A_HRC_WG.6_50_USA_3-EN.pdf` + `stakeholders_USA_3.txt` | OHCHR **Summary of stakeholders' submissions** (155 submissions), 1 Sep 2025 |

The US national report (A/HRC/WG.6/50/USA/1) was not available when the
assessment was run.

## Outputs

Generated into `output/`:

- `US_cycle3_implementation_report.md` — narrative report grouped by theme.
  Each block heading gives the collapsed recommendation ranges and a short
  action phrase, e.g. `### Recommendations 26.178-26.211 (Federal moratorium on
  / abolition of the death penalty)`, followed by the grade, an **Evidence:**
  list quoting each source (document, paragraph, UN body / organisation,
  verbatim quote) and a reasoned **Assessment:** line
- `us_cycle3_implementation_assessment.csv` — one row per recommendation:
  `action_summary`, `grade`, `rationale`, `sources`, `evidence_quotes`
- `UPR36_US_Thematic_List_of_Recommendations_ASSESSED.docx` — the OHCHR thematic
  list with column 4 ("Assessment/comments on level of implementation") filled
  in (grade, assessment, evidence quotes)

**Headline (first pass, for expert review):** of 347 recommendations —
**0 A**, **7 B**, **218 C**, **0 D**, **122 E**. Inaction plus 2025
retrogression (federal death penalty reinstated, Paris/HRC withdrawal, ICC
sanctions, asylum access removed, DEI and Tribal self-determination executive
orders revoked) dominate.

## Requirements

Python 3.10+ (uses the standard library; `sqlite3` is bundled). Helper scripts:
`pip install python-docx`.

## Reproduce

```bash
python -m venv .venv && .venv\Scripts\activate
pip install -e ".[dev]" python-docx

# 1. build + populate the database
python -m recommendations.cli import "UPR36_United_States_of_America_Thematic_List_of_Recommendations.docx"

# 2. run the assessment (idempotent)
python -m scripts.apply_assessment

# 3. regenerate the deliverables
python -m scripts.fill_thematic_list
python -m scripts.make_report

python -m recommendations.cli stats
```

## CLI

```bash
python -m recommendations.cli import <file.docx|file.xlsx>
python -m recommendations.cli list --grade E --theme "Death penalty"
python -m recommendations.cli list --position noted
python -m recommendations.cli grade 42 B --rationale "..." --sources "A/HRC/WG.6/50/USA/2 para. 53"
python -m recommendations.cli stats
python -m recommendations.cli grades
```

## Layout

```
recommendations/
  db.py             connection + schema
  models.py         Recommendation dataclass, Grade + Position enums
  repository.py     add / add_many / get / list / set_grade / count_by_grade
  thematic_list.py  OHCHR thematic-list .docx parser  (stdlib only)
  uhri.py           UHRI .xlsx export parser          (stdlib only)
  cli.py            import / list / grade / stats / grades
scripts/
  apply_assessment.py    cluster-based A–E grading against the evidence
  fill_thematic_list.py  write grades back into the OHCHR .docx (needs python-docx)
  make_report.py         build output/US_cycle3_implementation_report.md
tests/
  test_repository.py
  test_thematic_list.py
evidence/   downloaded UN PDFs + extracted text
output/     generated deliverables
```

## Caveat

`scripts/apply_assessment.py` grades by **thematic cluster** with keyword
overrides — appropriate for a set where most recommendations are near-duplicate
asks, but it is a **structured first pass for expert review**, not an
authoritative verdict. The rationale and citations for each recommendation are
stored so every grade can be checked against the source paragraphs.
