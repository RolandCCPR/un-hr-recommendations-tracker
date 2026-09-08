"""Build the static-site data layer.

Sources:
  * the four per-country UPR assessment databases (United States, Denmark,
    Namibia, Paraguay);
  * site/data/hrc_all.json - the Human Rights Committee's follow-up gradings for
    every country (~114), produced by scripts/hrc_extract.py from the Special
    Rapporteur's reports (sessions 109-145).

Emits:
  site/public/data/countries.json     - every country + per-mechanism summary
  site/public/data/<A3>.json          - full detail for each assessed country
  site/public/data/meta.json          - scale, methodology, generated date
  site/public/assets/iso-numeric-a3.json - numeric id -> alpha-3 (for the map)
  site/assessments.db                 - consolidated SQLite (the "database")

Run:  python site/build.py     (from the project root)
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

from recommendations.models import Grade  # noqa: E402
from recommendations.repository import RecommendationRepository  # noqa: E402
from scripts.countries import get  # noqa: E402

PUBLIC = HERE / "public"
DATA = PUBLIC / "data"
ASSETS = PUBLIC / "assets"
HRC_ALL = HERE / "data" / "hrc_all.json"

SLUG_A3 = {"united-states": "USA", "denmark": "DNK", "namibia": "NAM",
           "paraguay": "PRY"}

# Grade -> points on a 1-5 ordinal scale (E=1 .. A=5).
GRADE_SCORE = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}
GRADE_MEANING = {g.value: g.committee_meaning for g in Grade if g.value != "not_assessed"}
GRADE_LABEL = {g.value: g.label for g in Grade if g.value != "not_assessed"}

HRC_CAVEAT = (
    "The Human Rights Committee's follow-up procedure grades only the two to "
    "four “priority” recommendations it selected from this country's "
    "Concluding Observations (CoBs). The other CoBs are not graded."
)


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
    return round(sum(GRADE_SCORE[g] * n for g, n in dist.items()) / tot, 2) if tot else None


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
    return {"meta": meta, "themes": themes_out}


# --------------------------------------------------------------------------- HRC
def _grade_summary(hg: dict) -> str:
    return " · ".join(f"{p} {''.join(gg)}" for p, gg in
                           sorted(hg.items(), key=lambda kv: int(kv[0])))


def hrc_detail(rec: dict):
    dist = collections.Counter(rec["grade_dist"])
    paras = []
    for p in rec["paragraphs"]:
        hg = rec["header_grades"].get(p["num"], [])
        limbs = [{"limb": lb["label"], "grade": lb["grade"],
                  "meaning": GRADE_MEANING[lb["grade"]], "eval": lb["eval"]}
                 for lb in p["limbs"]]
        paras.append({
            "para": p["num"], "title": p["title"],
            "recommendation": p["recommendation"],
            "header_grades": hg, "limbs": limbs,
        })
    meta = {
        "mechanism": "hrc",
        "co_symbol": rec["co_symbol"],
        "co_session": rec.get("co_session"),
        "co_date": rec.get("co_date"),
        "fco_symbol": rec.get("fco_symbol"),
        "assessment_symbol": rec["assessment_symbol"],
        "assessment_session": rec.get("assessment_session"),
        "assessment_date": rec.get("assessment_date"),
        "year": rec.get("assessment_year"),
        "followup_paras": rec.get("followup_paras") or sorted(rec["header_grades"], key=int),
        "titles_editorial": rec.get("titles_editorial", False),
        "caveat": HRC_CAVEAT,
        "n": rec["n_grades"],
        "grade_dist": {g: dist.get(g, 0) for g in "ABCDE"},
        "score": rec["score"],
    }
    hist = [{"year": h.get("year"), "session": h["session"],
             "co_symbol": h["co_symbol"],
             "grades": _grade_summary(h["header_grades"])}
            for h in rec.get("history", []) if h.get("header_grades")]
    return {"meta": meta, "paragraphs": paras, "history": hist}


# ------------------------------------------------------------------------- write
def main():
    DATA.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    iso = json.loads((HERE / "data" / "iso3166.json").read_text(encoding="utf-8"))
    num_a3 = {str(int(r["country-code"])): r["alpha-3"] for r in iso}
    a3_num = {r["alpha-3"]: int(r["country-code"]) for r in iso}
    a3_region = {r["alpha-3"]: r["region"] for r in iso}
    a3_name = {r["alpha-3"]: r["name"] for r in iso}
    (ASSETS / "iso-numeric-a3.json").write_text(
        json.dumps(num_a3, ensure_ascii=False), encoding="utf-8")

    hrc_all = json.loads(HRC_ALL.read_text(encoding="utf-8"))
    upr = {a3: upr_detail(slug) for slug, a3 in SLUG_A3.items()}

    codes = sorted(set(hrc_all) | set(SLUG_A3.values()))
    details, summaries = {}, {}
    for a3 in codes:
        u = upr.get(a3)
        h = hrc_detail(hrc_all[a3]) if a3 in hrc_all else None
        us = u["meta"]["score"] if u else None
        hs = h["meta"]["score"] if h else None
        vals = [x for x in (us, hs) if x is not None]
        combined = round(sum(vals) / len(vals), 2) if vals else None

        details[a3] = {
            "a3": a3, "name": a3_name.get(a3, a3), "num": a3_num.get(a3),
            "upr": u, "hrc": h, "combined_score": combined,
        }
        (DATA / f"{a3}.json").write_text(
            json.dumps(details[a3], ensure_ascii=False, indent=1), encoding="utf-8")
        summaries[a3] = {
            "upr": ({"score": us, "grade_dist": u["meta"]["grade_dist"],
                     "n": u["meta"]["n"], "label": u["meta"]["cycle"]} if u else None),
            "hrc": ({"score": hs, "grade_dist": h["meta"]["grade_dist"],
                     "n": h["meta"]["n"], "label": h["meta"]["co_symbol"],
                     "year": h["meta"]["year"]} if h else None),
            "combined": combined,
        }

    countries = []
    for r in iso:
        a3 = r["alpha-3"]
        s = summaries.get(a3)
        countries.append({
            "a3": a3, "name": r["name"], "num": int(r["country-code"]),
            "region": r["region"], "assessed": bool(s),
            "upr": s["upr"] if s else None,
            "hrc": s["hrc"] if s else None,
            "combined": s["combined"] if s else None,
        })
    (DATA / "countries.json").write_text(
        json.dumps(countries, ensure_ascii=False), encoding="utf-8")

    meta = {
        "generated": _dt.date.today().isoformat(),
        "n_assessed": len(details),
        "n_hrc": len(hrc_all),
        "n_upr": len(upr),
        "upr_countries": [details[a]["name"] for a in sorted(SLUG_A3.values())],
        "hrc_year_range": [min(h["assessment_year"] for h in hrc_all.values()),
                           max(h["assessment_year"] for h in hrc_all.values())],
        "hrc_session_range": [min(h["assessment_session"] for h in hrc_all.values()),
                              max(h["assessment_session"] for h in hrc_all.values())],
        "hrc_caveat": HRC_CAVEAT,
        "mechanisms": {
            "upr": {
                "name": "Universal Periodic Review",
                "what": "A peer review of every UN member State's whole human "
                        "rights record, every ~4.5 years, by the other States. "
                        "This site assesses how four countries implemented the "
                        "recommendations they received in the 3rd cycle, judged "
                        "against the UN and civil-society reports prepared for "
                        "their 4th-cycle review.",
            },
            "hrc": {
                "name": "Human Rights Committee follow-up",
                "what": "The ICCPR treaty body selects two to four priority "
                        "recommendations from each country's Concluding "
                        "Observations. About three years later the State reports "
                        "back, NGOs may comment, and the Committee's Special "
                        "Rapporteur grades each one A–E (the scale has been used "
                        "in this tabular form since 2013). The map carries every "
                        "country whose most recent follow-up evaluation falls "
                        f"between the Committee's "
                        f"{min(h['assessment_session'] for h in hrc_all.values())}th "
                        f"({min(h['assessment_year'] for h in hrc_all.values())}) "
                        "and "
                        f"{max(h['assessment_session'] for h in hrc_all.values())}th "
                        f"({max(h['assessment_year'] for h in hrc_all.values())}) "
                        f"sessions — {len(hrc_all)} countries, every grade taken "
                        "verbatim from the Rapporteur's report. Countries with no "
                        "colour have not completed the procedure in that window.",
            },
        },
        "scale": [
            {"grade": g, "label": GRADE_LABEL[g], "score": GRADE_SCORE[g],
             "meaning": GRADE_MEANING[g]} for g in "ABCDE"
        ],
        "methodology": (
            "Each A–E grade is worth points (E=1, D=2, C=3, B=4, A=5); a "
            "country's score for a mechanism is the average of those points "
            "across its graded items, between 1 and 5, and the map shades red "
            "(1) to green (5). The “All (combined)” view averages a "
            "country's UPR and Human Rights Committee scores where both exist. "
            "The Human Rights Committee gradings are the Committee's own, taken "
            "verbatim from the Special Rapporteur's follow-up reports; topic "
            "titles for evaluations before 2019 are added by us for navigation "
            "because the documents of that period did not include them. The UPR "
            "gradings (four countries) are a first-pass assessment for expert "
            "review, built with AI from the UN compilation and stakeholder "
            "reports: a concrete on-point measure adopted in the review period "
            "scores B, a completed measure meeting the core ask scores A, only "
            "pre-existing framework or no action scores C, a new contrary "
            "measure or explicit rejection scores E, and no information scores D."
        ),
    }
    (DATA / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")

    build_sqlite(details)

    print(f"countries.json : {len(countries)} rows, {len(details)} assessed "
          f"({len(upr)} with UPR, {len(hrc_all)} with HR Committee)")
    for a3 in sorted(SLUG_A3.values()):
        s = summaries[a3]
        u = s["upr"]["score"] if s["upr"] else None
        print(f"  {a3}: UPR {u}/5   HRC {s['hrc']['score']}/5   combined {s['combined']}/5")
    print(f"data written to {DATA.relative_to(ROOT)}")


def build_sqlite(details):
    db = HERE / "assessments.db"
    if db.exists():
        db.unlink()
    con = sqlite3.connect(db)
    con.executescript("""
    CREATE TABLE country (a3 TEXT PRIMARY KEY, name TEXT, num INTEGER,
        has_upr INTEGER, has_hrc INTEGER, combined_score REAL);
    CREATE TABLE assessment (
        id INTEGER PRIMARY KEY, country_a3 TEXT, mechanism TEXT,
        scope TEXT, source_symbol TEXT, review TEXT, year INTEGER,
        n INTEGER, score REAL, a INTEGER, b INTEGER, c INTEGER, d INTEGER, e INTEGER);
    CREATE TABLE upr_recommendation (
        id INTEGER PRIMARY KEY, country_a3 TEXT, paragraph TEXT,
        recommending_state TEXT, position TEXT, theme TEXT, action_summary TEXT,
        grade TEXT, rationale TEXT, evidence TEXT, text TEXT);
    CREATE TABLE hrc_limb (
        id INTEGER PRIMARY KEY, country_a3 TEXT, co_symbol TEXT, co_paragraph TEXT,
        paragraph_title TEXT, limb TEXT, grade TEXT, committee_evaluation TEXT,
        recommendation TEXT, assessment_symbol TEXT, assessment_year INTEGER);
    """)
    for a3, d in details.items():
        con.execute("INSERT INTO country VALUES (?,?,?,?,?,?)",
                    (a3, d["name"], d["num"], int(bool(d["upr"])),
                     int(bool(d["hrc"])), d["combined_score"]))
        if d["upr"]:
            um = d["upr"]["meta"]
            g = um["grade_dist"]
            con.execute(
                "INSERT INTO assessment (country_a3,mechanism,scope,source_symbol,"
                "review,year,n,score,a,b,c,d,e) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (a3, "upr", um["cycle"], um["co_symbol"], um["review"], None,
                 um["n"], um["score"], g["A"], g["B"], g["C"], g["D"], g["E"]))
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
        if d["hrc"]:
            hm = d["hrc"]["meta"]
            g = hm["grade_dist"]
            con.execute(
                "INSERT INTO assessment (country_a3,mechanism,scope,source_symbol,"
                "review,year,n,score,a,b,c,d,e) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (a3, "hrc", hm["co_symbol"], hm["assessment_symbol"],
                 hm["assessment_date"], hm["year"], hm["n"], hm["score"],
                 g["A"], g["B"], g["C"], g["D"], g["E"]))
            for p in d["hrc"]["paragraphs"]:
                for lb in p["limbs"]:
                    con.execute(
                        "INSERT INTO hrc_limb (country_a3,co_symbol,co_paragraph,"
                        "paragraph_title,limb,grade,committee_evaluation,"
                        "recommendation,assessment_symbol,assessment_year) "
                        "VALUES (?,?,?,?,?,?,?,?,?,?)",
                        (a3, hm["co_symbol"], p["para"], p["title"], lb["limb"],
                         lb["grade"], lb["eval"], p["recommendation"],
                         hm["assessment_symbol"], hm["year"]))
    con.commit()
    con.close()
    print(f"assessments.db : {db.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
