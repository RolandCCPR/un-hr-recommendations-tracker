"""Read the dates out of the Human Rights Committee's concluding observations.

Input: the cache directory written by `hrc_calendar_fetch.py` (raw .docx/.pdf,
plus `<name>.doc.txt` for the old .doc files, converted with Word).
Output: `site/data/hrc_calendar_raw.json` — for every country and every
concluding-observations document: the dialogue and adoption dates, the date the
follow-up information is due, the year of the next list of issues prior to
reporting (LOIPR), the year of the next dialogue, and (older documents) the date
the next periodic report is due.  Only what the text states is recorded.

    python scripts/hrc_calendar_extract.py <cache_dir>
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}
MONTH_RE = "|".join(MONTHS)
NUM_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}
DATE_RE = r"(\d{1,2})\s+(" + MONTH_RE + r")\s+(\d{4})"


def read_text(path: Path) -> str:
    if path.suffix == ".docx":
        import docx
        d = docx.Document(str(path))
        return "\n".join(p.text for p in d.paragraphs)
    if path.suffix == ".doc":
        t = Path(str(path) + ".txt")
        return t.read_text(encoding="utf-8-sig", errors="replace").replace("\r", "\n")
    if path.suffix == ".pdf":
        return subprocess.run(["pdftotext", "-nopgbrk", "-enc", "UTF-8", str(path), "-"],
                              capture_output=True, text=True, encoding="utf-8").stdout
    return ""


def norm(t: str) -> str:
    return re.sub(r"[ \t ]+", " ", t.replace("’", "'"))


def iso(d: int, m: str, y: int) -> str | None:
    try:
        return date(y, MONTHS[m], d).isoformat()
    except Exception:
        return None


def segment_dates(seg: str, default_year: int | None = None) -> list[str]:
    """'30 June and 1 July 2016' / '2 and 3 March 2026' -> ISO dates."""
    out = []
    pat = re.compile(r"((?:\d{1,2}(?:\s*(?:,|and|to|-|–)\s*)?)+)\s*(" + MONTH_RE + r")(?:\s+(\d{4}))?")
    for m in pat.finditer(seg):
        y = int(m.group(3)) if m.group(3) else default_year
        if y is None:
            continue
        for d in re.findall(r"\d{1,2}", m.group(1)):
            out.append(iso(int(d), m.group(2), y))
    return [d for d in out if d]


def parse(text: str) -> dict:
    t = norm(text)
    flat = re.sub(r"\s+", " ", t)
    rec: dict = {}
    m = re.search(r"Concluding observations on (?:the )?(.{5,140}?)(?:\*|\s1\.|\s*Human Rights)", flat)
    rec["title"] = m.group(1).strip() if m else None
    rec["english"] = "oncluding observations" in flat[:600]
    # "CO/n/Add.1" is either a real CO (Belize, Cabo Verde) or the State's reply on follow-up
    rec["followup_addendum"] = bool(re.search(r"Addendum|Information received from", flat[:900]))

    head = flat[: flat.find("Introduction") if "Introduction" in flat[:3000] else 1800]
    head = re.sub(r"\([^)]*\)", "", head)  # drop "(see CCPR/C/SR.1234 ...)" etc.
    sents = re.split(r"(?<=[a-z0-9])\.\s+(?=[A-Z])", head)
    dlg = next((x for x in sents if re.search(r"considered", x)), "")
    rec["dialogue"] = segment_dates(dlg)
    dy = int(rec["dialogue"][0][:4]) if rec["dialogue"] else None
    ad = next((x for x in sents if "adopted" in x), "")
    d = segment_dates(ad, dy) or (segment_dates(dlg) if "adopted" in dlg else [])
    rec["adopted"] = d[-1] if d else None
    if rec["adopted"] and dy and not (dy <= int(rec["adopted"][:4]) <= dy + 1):
        rec["adopted_suspect"] = rec["adopted"]
        rec["adopted"] = None
    m = re.search(r"Distr\.?:? ?\w+ (" + DATE_RE + ")", flat[:900])
    rec["doc_date"] = iso(int(m.group(2)), m.group(3), int(m.group(4))) if m else None

    m = re.search(r"by (" + DATE_RE + r"),? information on the implementation", flat)
    rec["follow_up_due"] = iso(int(m.group(2)), m.group(3), int(m.group(4))) if m else None
    m = re.search(r"within (\w+) years?,? information on the implementation", flat)
    rec["follow_up_within_years"] = NUM_WORDS.get(m.group(1).lower(), None) if m else None

    m = re.search(r"will receive,? in (\d{4}),? the Committee's list of issues prior", flat)
    rec["loipr_year"] = int(m.group(1)) if m else None
    m = re.search(r"next (?:interactive and )?constructive dialogue[^.]{0,120}?in (\d{4})", flat)
    rec["next_dialogue_year"] = int(m.group(1)) if m else None
    # the Committee's request, not the (historical) date the report was first due
    req = r"(?:requests|requested)[^.]{0,80}?submit (?:its |the )?(?:next |initial |[a-z]+ )?(?:periodic )?report[^.]{0,40}?by "
    m = re.search(req + r"(\d{4})\b(?! \w+ \d)", flat)
    rec["next_report_year"] = int(m.group(1)) if m else None
    m = re.search(req + "(" + DATE_RE + ")", flat)
    rec["next_report_due"] = iso(int(m.group(2)), m.group(3), int(m.group(4))) if m else None
    m = re.search(r"((?:In line with|In accordance with)[^.]{0,80}predictable review cycle.{0,700}|"
                  r"The State party is requested to submit its [^.]{0,200}\.[^.]{0,300}\.)", flat)
    rec["excerpt"] = m.group(1)[:800] if m else None
    return rec


def main() -> None:
    cache = Path(sys.argv[1])
    manifest = json.loads((cache / "manifest.json").read_text(encoding="utf-8"))
    out = {}
    for c in manifest:
        docs = []
        for co in c["cos"]:
            if not co.get("file"):
                docs.append({"symbol": co["symbol"], "n": co["n"], "error": "no file"})
                continue
            p = cache / co["file"]
            try:
                rec = parse(read_text(p))
            except Exception as e:  # keep going; flag
                rec = {"error": repr(e)}
            rec.update(symbol=co["symbol"], n=co["n"])
            if rec.get("followup_addendum"):
                continue  # not a concluding-observations document
            docs.append(rec)
        if docs:
            out[c["a3"]] = docs
    dest = ROOT / "site/data/hrc_calendar_raw.json"
    dest.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    n = sum(len(v) for v in out.values())
    print(f"{len(out)} countries, {n} documents -> {dest}")


if __name__ == "__main__":
    main()
