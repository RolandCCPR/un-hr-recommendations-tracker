"""Build the static-site data layer.

Reads the four per-country UPR assessment databases and the hand-curated Human
Rights Committee follow-up gradings, and emits:

  site/public/data/countries.json     - every country + per-mechanism summary
  site/public/data/<A3>.json          - full detail for each assessed country
  site/public/data/meta.json          - scale, methodology, generated date
  site/public/assets/iso-numeric-a3.json - numeric id -> alpha-3 (for the map)
  site/assessments.db                 - consolidated SQLite (the "database")

Run:  python -m site.build       (from the project root)
      python site/build.py
"""

from __future__ import annotations

import collections
import datetime as _dt
import json
import sqlite3
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE / "data"))

from recommendations.models import Grade  # noqa: E402
from recommendations.repository import RecommendationRepository  # noqa: E402
from scripts.countries import get  # noqa: E402
from hrc_followup import HRC  # noqa: E402

PUBLIC = HERE / "public"
DATA = PUBLIC / "data"
ASSETS = PUBLIC / "assets"

SLUG_A3 = {"united-states": "USA", "denmark": "DNK", "namibia": "NAM",
           "paraguay": "PRY"}

# Grade -> points on a 1-5 ordinal scale (E=1 .. A=5). The country/mechanism
# score is the mean of these points; it drives the choropleth colour.
GRADE_SCORE = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}
GRADE_MEANING = {g.value: g.committee_meaning for g in Grade if g.value != "not_assessed"}
GRADE_LABEL = {g.value: g.label for g in Grade if g.value != "not_assessed"}


def _para_key(p):
    if p and "." in p:
        try:
            return int(p.split(".")[1])
        except ValueError:
            return 0
    return 0


def _collapse_ranges(paras):
    paras = [p for p in paras if p and "." in p]
    if not paras:
        return ""
    pref = paras[0].split(".")[0]
    nums = sorted({int(p.split(".")[1]) for p in paras})
    parts, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if j == i:
            parts.append(f"{pref}.{nums[i]}")
        elif j == i + 1:
            parts.append(f"{pref}.{nums[i]}, {pref}.{nums[j]}")
        else:
            parts.append(f"{pref}.{nums[i]}-{pref}.{nums[j]}")
        i = j + 1
    return ", ".join(parts)


def _score(dist: dict[str, int]) -> float | None:
    tot = sum(dist.values())
    if not tot:
        return None
    return round(sum(GRADE_SCORE[g] * n for g, n in dist.items()) / tot, 2)


# --------------------------------------------------------------------------- UPR
def upr_detail(slug: str):
    cfg = get(slug)
    repo = RecommendationRepository(cfg["db"])
    recs = repo.list()
    total = len(recs)

    dist = collections.Counter()
    blocks: dict[tuple, list] = collections.defaultdict(list)
    for r in recs:
        dist[r.grade.value] += 1
        primary = (r.themes or "—").split(";")[0].strip()
        blocks[(primary, r.action_summary or "", r.grade.value,
                r.assessment_rationale or "", r.assessment_evidence or "")].append(r)

    theme_min: dict[str, int] = {}
    for (theme, *_), items in blocks.items():
        m = min(_para_key(r.paragraph) for r in items)
        theme_min[theme] = min(theme_min.get(theme, m), m)

    themes_out = []
    for theme in sorted(theme_min, key=lambda t: theme_min[t]):
        tb = sorted(
            [(k, v) for k, v in blocks.items() if k[0] == theme],
            key=lambda kv: (-len(kv[1]), min(_para_key(r.paragraph) for r in kv[1])),
        )
        blocks_out = []
        for (_t, summary, grade_v, rationale, evidence), items in tb:
            items.sort(key=lambda r: _para_key(r.paragraph))
            pos = collections.Counter(r.position.value for r in items)
            blocks_out.append({
                "paras": _collapse_ranges([r.paragraph for r in items]),
                "n": len(items),
                "summary": summary,
                "grade": grade_v,
                "meaning": GRADE_MEANING[grade_v],
                "rationale": rationale,
                "evidence": [ln.strip() for ln in evidence.splitlines() if ln.strip()],
                "position": ", ".join(f"{n} {p.replace('_', '-')}" for p, n in pos.items()),
                "recommendations": [
                    {"paragraph": r.paragraph, "by": r.recommending_state,
                     "position": r.position.value, "text": r.text}
                    for r in items
                ],
            })
        themes_out.append({"theme": theme, "blocks": blocks_out})
    repo.close()

    dist = {g: dist.get(g, 0) for g in "ABCDE"}
    meta = {
        "mechanism": "upr",
        "cycle": f"{cfg['cycle3_session']} session ({cfg['cycle3_review'][:4]})",
        "co_symbol": cfg["cycle3_symbol"],
        "review": cfg["cycle4_review"],
        "sources": cfg["sources"],
        "headline": cfg.get("headline", ""),
        "n": total,
        "grade_dist": dist,
        "score": _score(dist),
    }
    return meta, themes_out


# --------------------------------------------------------------------------- HRC
def hrc_detail(a3: str):
    h = HRC[a3]
    dist = collections.Counter()
    paras = []
    for p in h["paragraphs"]:
        limbs = []
        for lb in p["limbs"]:
            dist[lb["grade"]] += 1
            limbs.append({"limb": lb["limb"], "grade": lb["grade"],
                          "meaning": GRADE_MEANING[lb["grade"]], "eval": lb["eval"]})
        paras.append({"para": p["para"], "title": p["title"],
                      "recommendation": p["recommendation"], "limbs": limbs})
    dist = {g: dist.get(g, 0) for g in "ABCDE"}
    meta = {
        "mechanism": "hrc",
        "co_symbol": h["co_symbol"],
        "session": h["session"],
        "assessment_symbol": h["assessment_symbol"],
        "assessment_date": h["assessment_date"],
        "round": h["round"],
        "n": sum(dist.values()),
        "grade_dist": dist,
        "score": _score(dist),
    }
    return meta, paras


# ------------------------------------------------------------------------- write
def main():
    DATA.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    iso = json.loads((HERE / "data" / "iso3166.json").read_text(encoding="utf-8"))

    num_a3 = {}
    a3_name = {}
    for row in iso:
        a3 = row["alpha-3"]
        num = int(row["country-code"])
        num_a3[str(num)] = a3
        a3_name[a3] = row["name"]
    (ASSETS / "iso-numeric-a3.json").write_text(
        json.dumps(num_a3, ensure_ascii=False), encoding="utf-8")

    # per-country detail + summary rows
    summaries = {}
    details = {}
    for slug, a3 in SLUG_A3.items():
        um, ut = upr_detail(slug)
        hm, hp = hrc_detail(a3)
        name = get(slug)["name"]
        details[a3] = {"a3": a3, "name": name,
                       "num": next(k for k, v in num_a3.items() if v == a3),
                       "upr": {"meta": um, "themes": ut},
                       "hrc": {"meta": hm, "paragraphs": hp}}
        us, hs = um["score"], hm["score"]
        combined = (round((us + hs) / 2, 2) if us is not None and hs is not None
                    else (us if us is not None else hs))
        details[a3]["combined_score"] = combined
        summaries[a3] = {
            "upr": {"score": us, "grade_dist": um["grade_dist"],
                    "n": um["n"], "label": um["cycle"]},
            "hrc": {"score": hs, "grade_dist": hm["grade_dist"],
                    "n": hm["n"], "label": hm["session"]},
            "combined": combined,
        }
        (DATA / f"{a3}.json").write_text(
            json.dumps(details[a3], ensure_ascii=False, indent=1), encoding="utf-8")

    countries = []
    for row in iso:
        a3 = row["alpha-3"]
        s = summaries.get(a3)
        countries.append({
            "a3": a3, "name": row["name"], "num": int(row["country-code"]),
            "region": row["region"], "assessed": bool(s),
            "upr": s["upr"] if s else None,
            "hrc": s["hrc"] if s else None,
            "combined": s["combined"] if s else None,
        })
    (DATA / "countries.json").write_text(
        json.dumps(countries, ensure_ascii=False), encoding="utf-8")

    meta = {
        "generated": _dt.date.today().isoformat(),
        "assessed_countries": sorted(SLUG_A3.values()),
        "mechanisms": {
            "upr": {
                "name": "Universal Periodic Review",
                "what": "A peer review of every UN member State's whole human "
                        "rights record, every ~4.5 years, by the other States. "
                        "This site tracks how each country implemented the "
                        "recommendations it received in the 3rd cycle, judged "
                        "against the UN and civil-society reports prepared for "
                        "its 4th-cycle review.",
            },
            "hrc": {
                "name": "Human Rights Committee follow-up",
                "what": "The ICCPR treaty body selects ~3 priority "
                        "recommendations from each country's Concluding "
                        "Observations. About three years later the State "
                        "reports back, NGOs comment, and the Committee's Special "
                        "Rapporteur grades each one A–E. These are the "
                        "Committee's own gradings.",
            },
        },
        "scale": [
            {"grade": "A", "label": GRADE_LABEL["A"], "score": GRADE_SCORE["A"],
             "meaning": GRADE_MEANING["A"]},
            {"grade": "B", "label": GRADE_LABEL["B"], "score": GRADE_SCORE["B"],
             "meaning": GRADE_MEANING["B"]},
            {"grade": "C", "label": GRADE_LABEL["C"], "score": GRADE_SCORE["C"],
             "meaning": GRADE_MEANING["C"]},
            {"grade": "D", "label": GRADE_LABEL["D"], "score": GRADE_SCORE["D"],
             "meaning": GRADE_MEANING["D"]},
            {"grade": "E", "label": GRADE_LABEL["E"], "score": GRADE_SCORE["E"],
             "meaning": GRADE_MEANING["E"]},
        ],
        "methodology": "Recommendations are grouped by their OHCHR theme and "
                       "graded on the Human Rights Committee's A–E scale "
                       "(CCPR/C/108/2). A concrete, on-point measure adopted in "
                       "the review period scores B; a completed measure meeting "
                       "the core ask scores A; only pre-existing framework, "
                       "stalled bills or no action scores C; a new contrary "
                       "measure or explicit rejection scores E; no information "
                       "scores D. Each grade is worth points (E=1, D=2, C=3, "
                       "B=4, A=5) and a country's score for a mechanism is the "
                       "average of those points across all its graded items, "
                       "between 1 and 5. The UPR grading is a first-pass "
                       "assessment for expert review; the Human Rights Committee "
                       "gradings are the Committee's own.",
    }
    (DATA / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")

    build_sqlite(details, a3_name)

    print(f"countries.json : {len(countries)} countries "
          f"({len(summaries)} assessed)")
    for a3 in sorted(SLUG_A3.values()):
        u = summaries[a3]["upr"]
        hh = summaries[a3]["hrc"]
        print(f"  {a3}: UPR {u['score']:>4}/5 (n={u['n']:>3})   "
              f"HRC {hh['score']:>4}/5 (n={hh['n']:>2})   "
              f"combined {summaries[a3]['combined']:>4}/5")
    print(f"data written to {DATA.relative_to(ROOT)}")


def build_sqlite(details, a3_name):
    db = HERE / "assessments.db"
    if db.exists():
        db.unlink()
    con = sqlite3.connect(db)
    con.executescript("""
    CREATE TABLE country (a3 TEXT PRIMARY KEY, name TEXT, num INTEGER);
    CREATE TABLE assessment (
        id INTEGER PRIMARY KEY, country_a3 TEXT, mechanism TEXT,
        scope TEXT, source_symbol TEXT, review TEXT,
        n INTEGER, score REAL,
        a INTEGER, b INTEGER, c INTEGER, d INTEGER, e INTEGER
    );
    CREATE TABLE upr_recommendation (
        id INTEGER PRIMARY KEY, country_a3 TEXT, paragraph TEXT,
        recommending_state TEXT, position TEXT, theme TEXT,
        action_summary TEXT, grade TEXT, rationale TEXT, evidence TEXT,
        text TEXT
    );
    CREATE TABLE hrc_limb (
        id INTEGER PRIMARY KEY, country_a3 TEXT, co_paragraph TEXT,
        paragraph_title TEXT, limb TEXT, grade TEXT,
        committee_evaluation TEXT, recommendation TEXT
    );
    """)
    for a3, d in details.items():
        con.execute("INSERT INTO country VALUES (?,?,?)",
                    (a3, d["name"], int(d["num"])))
        um = d["upr"]["meta"]
        gd = um["grade_dist"]
        con.execute(
            "INSERT INTO assessment (country_a3,mechanism,scope,source_symbol,"
            "review,n,score,a,b,c,d,e) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (a3, "upr", um["cycle"], um["co_symbol"], um["review"], um["n"],
             um["score"], gd["A"], gd["B"], gd["C"], gd["D"], gd["E"]))
        for th in d["upr"]["themes"]:
            for bl in th["blocks"]:
                for r in bl["recommendations"]:
                    con.execute(
                        "INSERT INTO upr_recommendation (country_a3,paragraph,"
                        "recommending_state,position,theme,action_summary,grade,"
                        "rationale,evidence,text) VALUES (?,?,?,?,?,?,?,?,?,?)",
                        (a3, r["paragraph"], r["by"], r["position"], th["theme"],
                         bl["summary"], bl["grade"], bl["rationale"],
                         "\n".join(bl["evidence"]), r["text"]))
        hm = d["hrc"]["meta"]
        gd = hm["grade_dist"]
        con.execute(
            "INSERT INTO assessment (country_a3,mechanism,scope,source_symbol,"
            "review,n,score,a,b,c,d,e) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (a3, "hrc", hm["session"], hm["assessment_symbol"],
             hm["assessment_date"], hm["n"], hm["score"],
             gd["A"], gd["B"], gd["C"], gd["D"], gd["E"]))
        for p in d["hrc"]["paragraphs"]:
            for lb in p["limbs"]:
                con.execute(
                    "INSERT INTO hrc_limb (country_a3,co_paragraph,"
                    "paragraph_title,limb,grade,committee_evaluation,"
                    "recommendation) VALUES (?,?,?,?,?,?,?)",
                    (a3, p["para"], p["title"], lb["limb"], lb["grade"],
                     lb["eval"], p["recommendation"]))
    con.commit()
    con.close()
    print(f"assessments.db : {db.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
