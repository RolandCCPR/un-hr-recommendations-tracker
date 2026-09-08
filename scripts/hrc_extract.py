"""Extract the Human Rights Committee's follow-up gradings for every country
from the Special Rapporteur's reports (sessions 109-145, the A-E era).

Input : training/ccpr_followup/reports/*.txt   (pdftotext of the UN documents)
Output: site/data/hrc_all.json

Rules agreed with the user:
  * one record per country = its MOST RECENT follow-up evaluation
    (most recent report; within it, the LAST grading round);
  * earlier rounds/cycles kept as a light history list;
  * grades normalised: B1/B2 -> B, A1/A2 -> A, C1/C2 -> C (same D, E);
  * countries that only received a blanket [D] for non-cooperation
    (never filed a follow-up report) are EXCLUDED;
  * all wording is verbatim from the UN document.

    python scripts/hrc_extract.py
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "training" / "ccpr_followup" / "reports"
OUT = ROOT / "site" / "data" / "hrc_all.json"
ISO = json.loads((ROOT / "site" / "data" / "iso3166.json").read_text(encoding="utf-8"))
A3_NUM = {r["alpha-3"]: int(r["country-code"]) for r in ISO}
A3_NAME = {r["alpha-3"]: r["name"] for r in ISO}
SKIP_CODES = {"UNK"}  # Kosovo: not on the world map / no ISO code

CO_RE = re.compile(r"CCPR/C/([A-Z]{2,4})/CO/(\d+)")
GRADE = re.compile(r"\[([ABCDE])[12]?\]")
PTS = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}

# Editorial topic titles for pre-2019 evaluations where the UN document gave
# none. Short, neutral, in the Committee's own naming style. Flagged as
# editorial in the site methodology.
EDITORIAL_TITLES = {
    "ALB": {"9": "Investigation into the January 2011 demonstrations",
            "13": "Identification of persons needing international protection"},
    "BOL": {"14": "Racial violence in Pando and Sucre (2008)"},
    "CHL": {"7": "Counter-Terrorism Act", "15": "Access to abortion",
            "19": "Torture and ill-treatment"},
    "CYP": {"23": "Rights of Turkish Cypriots and minorities"},
    "DJI": {"12": "Freedom of expression, association and assembly"},
    "HRV": {"13": "Return of refugees and displaced persons",
            "23": "Freedom of expression and the press"},
    "HTI": {"7": "Impunity and the Duvalier case",
            "10": "Firearm deaths caused by law enforcement",
            "19": "Human rights defenders and journalists",
            "20": "Legislative and municipal elections"},
    "IDN": {"8": "Accountability for enforced disappearances (1997-1998)",
            "10": "Death penalty", "12": "Female genital mutilation",
            "25": "Blasphemy law"},
    "LKA": {"5": "Constitutional and institutional reform",
            "14": "Unlawful use of force and the right to life",
            "15": "Enforced disappearances and missing persons",
            "21": "Freedom of expression"},
    "LVA": {"15": "Conditions of detention",
            "19": "Racially motivated crime and hate speech",
            "20": "Minority-language education"},
    "MOZ": {"13": "Arbitrary arrest and detention",
            "14": "Conditions of detention and monitoring",
            "15": "Administration of justice"},
    "NPL": {"5": "Accountability for torture and enforced disappearance",
            "7": "National human rights commission",
            "10": "Excessive use of force"},
    "URY": {"7": "National human rights institution",
            "8": "Reform of the Code of Criminal Procedure",
            "19": "Racial discrimination"},
    "USA": {"5": "Accountability for unlawful killing, torture and enforced disappearance",
            "10": "Gun violence and Stand Your Ground laws",
            "21": "Guantanamo Bay",
            "22": "Surveillance and the right to privacy"},
    "YEM": {"7": "National human rights institution",
            "10": "Equality between men and women",
            "15": "Investigation of killings of civilians",
            "21": "Refugee and asylum procedures"},
    "ISL": {"7": "Gender pay gap and women in decision-making",
            "15": "Solitary confinement in pretrial detention"},
    "TGO": {"10": "Accountability for the 2005 human rights violations",
            "15": "Torture and impunity", "16": "Conditions of detention"},
    "TUR": {"10": "Discrimination based on sexual orientation and gender identity",
            "13": "So-called honour killings",
            "23": "Freedom of expression and the press"},
    "COL": {"39": "Threats and attacks against human rights defenders, "
                  "journalists and social leaders"},
}

# Grade summary lines the parser cannot recover (multi-round old reports where
# pdftotext mangled the layout). Verified by hand against the PDF; LAST round.
MANUAL_HEADER = {
    "BOL": {"12": ["C", "C", "C", "C"], "13": ["D", "B", "C", "B"], "14": ["B"]},
}


def _ws(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").replace("’", "'").replace("�", "-")).strip()


def _scrub(s: str, name: str = "") -> str:
    """Remove the page headers/footers pdftotext drops into the running text:
    'GE.25-11924', bare 'CCPR/C/120/2', page numbers glued to the doc symbol,
    and the country name repeated at page breaks."""
    s = s or ""
    s = re.sub(r"\bGE\.\d\d-\d{3,}(?:\s*\(E\))?(?:\s*\d{6,})?", " ", s)
    s = re.sub(r"\b\d{0,3}\s*CCPR/C/\d+/[0-9A-Za-z/.]+(?:\s*\(E\))?\s*\d{0,3}", " ", s)
    if name:
        for variant in {name, name.replace("United States of America", "United States")}:
            s = re.sub(r"\s+" + re.escape(variant) + r"\s+(?=[a-z(])", " ", s)
            s = re.sub(r"(?<=[a-z,])\s+" + re.escape(variant) + r"\s+", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip(" .")


def _sess(fn: str) -> int:
    m = re.match(r"(\d+)_", fn)
    return int(m.group(1)) if m else 0


def _year(s: str | None):
    m = re.search(r"(20\d\d)", s or "")
    return int(m.group(1)) if m else None


# ------------------------------------------------------------------ block split
def country_blocks(text: str):
    """Yield (code, co_symbol, block_text). One block per CCPR/C/XXX/CO/n, from
    the session heading / country name that precedes it to just before the next
    CO symbol."""
    cos = list(CO_RE.finditer(text))
    for i, cm in enumerate(cos):
        code = cm.group(1)
        # look back up to 700 chars for a "<N>th session (...)" heading
        pre = text[max(0, cm.start() - 700): cm.start()]
        hm = list(re.finditer(r"\d{2,3}(?:st|nd|rd|th) session \([^)]+\)", pre))
        bstart = (cm.start() - 700 + hm[-1].start()) if hm else max(0, text.rfind("\n\n", 0, cm.start()))
        bend = cos[i + 1].start() if i + 1 < len(cos) else len(text)
        yield code, cm.group(0), text[bstart:bend]


# --------------------------------------------------------------- header grades
def header_grades(block: str):
    """{'21': ['B'], '31': ['B','C','A'] ...}. If several rounds are shown,
    use the LAST 'Additional information required on paragraphs ...' line."""
    # every "Additional information required on paragraphs ..." fragment, in order;
    # take the LAST one that actually carries grades (most recent round)
    frags = re.split(r"Additional information required on paragraph[s]?", block)
    seg = ""
    for fr in frags[1:]:
        fr = fr.split("\n\n")[0].split("Paragraph ")[0]
        if "see ccpr/c/" in fr.lower():
            continue
        if GRADE.search(fr):
            seg = fr
    if "[" not in seg:
        m = re.search(r"Committee.s evaluation:?\s*(.+?)(?:\n\s*\n|\nParagraph |\Z)", block, re.S)
        if m:
            seg = m.group(1).split("Paragraph ")[0]
    if "see ccpr/c/" in seg.lower() or "[" not in seg:
        return {}
    res = {}
    for pm in re.finditer(r"(\d{1,3})\s*((?:\[[ABCDE][12]?\]\s*)+)", seg):
        res[pm.group(1)] = [g.upper() for g in GRADE.findall(pm.group(2))]
    return res


# ------------------------------------------------------------------- paragraphs
_REC_START = re.compile(
    r"\b(The State [Pp]art(?:y|ies) should|The Committee (?:recommends|reiterates|urges|encourages)"
    r"|In light of and bearing in mind|Recalling (?:the|its)|Bearing in mind|Noting)\b")


def parse_paragraphs(block: str, name: str = "", editorial: dict | None = None,
                     valid: set | None = None):
    editorial = editorial or {}
    out = []
    heads = list(re.finditer(
        r"(?m)^\s*Paragraph\s+(\d+)\b[:.]?[ \t]*\n?[ \t]*(.*)$", block))
    for i, h in enumerate(heads):
        num = h.group(1)
        if valid and num not in valid:          # drop stray "Paragraph 37" refs
            continue
        after = h.group(2).strip()
        seg = block[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(block)]
        # new-format reports put a short topic title on the header line;
        # old-format reports put the recommendation text there instead; and the
        # LAST paragraph of a block often has BOTH on one line.
        title, lead = "", ""
        sm = _REC_START.search(after)
        has_verb = re.search(r"\bshould\b|\bstate part(?:y|ies)\b|\bcommittee\b", after, re.I)
        if sm and sm.start() > 3:
            cand = _ws(after[:sm.start()]).rstrip(" .1234567890")
            if 4 <= len(cand) <= 120:
                title, lead = cand, after[sm.start():]
            else:
                lead = after
        elif after and not has_verb and 4 <= len(after) <= 160:
            # a bare noun-phrase topic title on its own line
            title = _ws(after).rstrip(" .1234567890")
        else:
            lead = after
        body = (lead + "\n" + seg) if lead else seg
        # recommendation = up to the state-reply / NGO / evaluation / first grade
        cut = re.search(
            r"\n\s*(?:Summary of (?:the information received|State party|the State)"
            r"|Non-governmental organizations?:|Information received from"
            r"|Follow-up question:|Committee.s evaluation)\b", body)
        rec = _scrub(body[: cut.start()] if cut else body[:1600], name)
        # evaluation = after the LAST "Committee's evaluation"; else after "Follow-up question:"
        ev = body
        mev = list(re.finditer(r"Committee.s evaluation\s*", body))
        if mev:
            ev = body[mev[-1].end():]
        elif "Follow-up question:" in body:
            ev = body.split("Follow-up question:", 1)[1]
        ev = re.split(r"\n\s*(?:Recommended action|Next periodic report)\b", ev)[0]
        limbs = parse_limbs(ev, name)
        if not title and num in editorial:
            title = editorial[num]
        out.append({"num": num, "title": title, "recommendation": rec, "limbs": limbs})
    return out


_LABEL = (r"\(\s*[a-z0-9]{1,4}\s*\)(?:\s*(?:\((?:i|ii|iii|iv|v|vi)\))?)?"
          r"(?:\s*(?:,|and|&|to|-|–)\s*\(\s*[a-z0-9]{1,4}\s*\)(?:\s*\((?:i|ii|iii|iv|v|vi)\))?)*")


def parse_limbs(ev: str, name: str = ""):
    ev = ev.strip()
    marks = list(re.finditer(
        r"\[([ABCDE])[12]?\]\s*(" + _LABEL + r")?\s*[:.]?\s*(?=[A-Z\"(])", ev))
    out = []
    for j, m in enumerate(marks):
        grade = m.group(1).upper()
        label = _ws(m.group(2) or "").strip(" :.-–,")
        raw = ev[m.end(): marks[j + 1].start() if j + 1 < len(marks) else len(ev)]
        # the scope of the grade ("(a), (b) and (c)") sometimes sits at the front
        # of the evaluation text instead of in the label slot. Pull it out — an
        # optional single "(x)" that begins the itemised comment stays in the text.
        if not label:
            _SCOPE = (r"\(\s*[a-z0-9]{1,3}\s*\)"
                      r"(?:[\s,]*(?:and\s+|&\s+|to\s+|[-–]\s*)?[\s,]*\(\s*[a-z0-9]{1,3}\s*\))+")
            lm = re.match(
                r"\s*(" + _SCOPE + r")\s+"
                r"(?=(?:\([a-z0-9]{1,3}\)\s+)?"
                r"(?:The|While|With|As|Recalling|Concerning|Regarding|Noting|It|In)\b)",
                raw)
            if lm:
                label = _ws(lm.group(1)).strip(" :.-–,")
                raw = raw[lm.end():]
                # the greedy scope may have swallowed the single "(x)" that
                # begins the itemised comment — push it back onto the text
                tail = re.match(r"^(.+\))\s+(\([a-z0-9]{1,3}\))$", label)
                if tail and re.match(r'[A-Z"]', raw):
                    label = tail.group(1).strip()
                    raw = tail.group(2) + " " + raw
        txt = _scrub(raw, name)
        if len(txt) < 20:
            continue
        out.append({"label": label, "grade": grade, "eval": txt})
    return out


# ------------------------------------------------------------------- CO context
def co_context(block: str, co: str):
    d = {}
    m = re.search(r"\((\d+)(?:st|nd|rd|th) session\)\s*:?[^\n]*?"
                  + re.escape(co) + r"\s*,?\s*([0-9]{1,2} \w+ 20\d\d)?", block, re.S)
    if m:
        d["co_session"] = int(m.group(1))
        if m.group(2):
            d["co_date"] = _ws(m.group(2))
    if "co_date" not in d:
        m2 = re.search(re.escape(co) + r"\s*,\s*([0-9]{1,2} \w+ 20\d\d)", block)
        if m2:
            d["co_date"] = _ws(m2.group(1))
    fm = re.search(r"(CCPR/C/[A-Z]{2,4}/FCO/\d+)\s*,?\s*([0-9]{1,2} \w+ 20\d\d)?", block)
    if fm:
        d["fco_symbol"] = fm.group(1)
        if fm.group(2):
            d["fco_date"] = _ws(fm.group(2))
    pm = re.search(r"Follow-up paragraph[s]?\s*:?\s*\n?\s*([0-9][0-9,\s()and]+)", block)
    if pm:
        d["followup_paras"] = re.findall(r"\d+", pm.group(1))
    return d


def is_noncoop_list(block: str) -> bool:
    return bool(re.search(r"evaluated with a \[D\] grade for failure to cooperate", block, re.I))


# -------------------------------------------------------------------------- run
def main():
    files = sorted(REPORTS.glob("*.txt"), key=lambda p: _sess(p.name))
    files = [f for f in files if 109 <= _sess(f.name) <= 145]

    seen = {}     # code -> best record so far
    hist = {}     # code -> [ {session, co_symbol, year, header_grades} ]

    for f in files:
        s = _sess(f.name)
        text = f.read_text(encoding="utf-8", errors="replace")
        am = re.search(r"[Aa]dopted by the Committee at its (\d+)(?:st|nd|rd|th) session\s*\(([^)]+)\)", text)
        adopt_s = int(am.group(1)) if am else s
        adopt_d = _ws(am.group(2)) if am else None
        symm = re.search(r"CCPR/C/\d+/[23](?:/Add\.\d+)?", text)
        report_sym = symm.group(0) if symm else f"CCPR/C/{s}/2"

        for code, co, block in country_blocks(text):
            if code in SKIP_CODES:
                continue
            if is_noncoop_list(block):
                continue
            hg = header_grades(block) or MANUAL_HEADER.get(code, {})
            ctx = co_context(block, co)
            valid = set(hg) | set(ctx.get("followup_paras") or [])
            paras = parse_paragraphs(block, A3_NAME.get(code, code),
                                     EDITORIAL_TITLES.get(code), valid or None)
            if not hg and not paras:
                continue
            hist.setdefault(code, []).append({
                "session": s, "co_symbol": co,
                "year": _year(ctx.get("co_date")), "header_grades": hg})
            if code in seen and s < seen[code]["_s"]:
                continue
            seen[code] = {
                "_s": s,
                "code": code,
                "name": A3_NAME.get(code, code),
                "num": A3_NUM.get(code),
                "co_symbol": co,
                "co_session": ctx.get("co_session"),
                "co_date": ctx.get("co_date"),
                "fco_symbol": ctx.get("fco_symbol"),
                "fco_date": ctx.get("fco_date"),
                "followup_paras": ctx.get("followup_paras") or sorted(hg, key=int),
                "assessment_symbol": report_sym,
                "assessment_session": adopt_s,
                "assessment_date": adopt_d,
                "assessment_year": _year(adopt_d) or (2011 + (s - 100) // 3),
                "header_grades": hg,
                "paragraphs": paras,
                "titles_editorial": code in EDITORIAL_TITLES,
                "source_file": f.name,
            }

    records = {}
    for code, r in seen.items():
        cur_s = r.pop("_s")
        past = [h for h in hist.get(code, [])
                if h["session"] != cur_s and h["header_grades"]]
        r["history"] = sorted(past, key=lambda h: -h["session"])
        # grades for the score: header line first, else limb grades
        gs = [g for gg in r["header_grades"].values() for g in gg]
        if not gs:
            gs = [lb["grade"] for p in r["paragraphs"] for lb in p["limbs"]]
        r["n_grades"] = len(gs)
        r["score"] = round(sum(PTS[g] for g in gs) / len(gs), 2) if gs else None
        c = Counter(gs)
        r["grade_dist"] = {g: c.get(g, 0) for g in "ABCDE"}
        records[code] = r

    OUT.write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")

    scored = [c for c, r in records.items() if r["score"] is not None]
    notitle = [c for c, r in records.items()
               if r["paragraphs"] and not any(p["title"] for p in r["paragraphs"])]
    nolimbs = [c for c, r in records.items() if not r["paragraphs"]]
    tot = sum(r["n_grades"] for r in records.values())
    print(f"{len(records)} countries -> {OUT.relative_to(ROOT)}")
    print(f"  scored               : {len(scored)}")
    print(f"  no paragraph text    : {len(nolimbs)}  {sorted(nolimbs)}")
    print(f"  no topic titles (old): {len(notitle)}")
    print(f"  total header grades  : {tot}")
    print(f"  displayable eval rows: {sum(len(p['limbs']) for r in records.values() for p in r['paragraphs'])}")


if __name__ == "__main__":
    main()
