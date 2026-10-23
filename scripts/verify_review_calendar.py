"""Consistency checks on the "When is my country next?" data, for every country.

    python scripts/verify_review_calendar.py <cache_dir>

Each check compares the extracted/derived values with independent evidence
(the session lists, the text of the concluding observations, the UPR calendar)
and prints every violation, so nothing relies on spot checks.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hrc_calendar_extract as ex  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "site/data"
cache = Path(sys.argv[1])

raw = json.loads((DATA / "hrc_calendar_raw.json").read_text(encoding="utf-8"))
cal = {c["a3"]: c for c in json.loads((DATA / "review_calendar.json").read_text(encoding="utf-8"))["countries"]}
manifest = {co["symbol"]: co for m in json.loads((cache / "manifest.json").read_text(encoding="utf-8")) for co in m["cos"]}

# session date ranges from the session list
MON = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
sessions = []
for line in (DATA / "hrc_sessions_raw.txt").read_text(encoding="utf-8").splitlines():
    mm = re.match(r"(\d{3}) (\d\d) (\w{3}) (\d{4}) (\d\d) (\w{3}) (\d{4})", line)
    if mm:
        n, d1, m1, y1, d2, m2, y2 = mm.groups()
        sessions.append((date(int(y1), MON[m1], int(d1)), date(int(y2), MON[m2], int(d2))))

problems: list[str] = []
checked = Counter()


def bad(a3: str, msg: str) -> None:
    problems.append(f"{a3}: {msg}")


def d(s: str) -> date:
    return date.fromisoformat(s)


for a3, c in sorted(cal.items()):
    h = c["hrc"]
    if not h:
        continue
    for r in h["reviews"]:
        checked["dialogues"] += 1
        dl = [d(x) for x in r["dialogue"]]
        if r["symbol"]:  # past dialogue read from a concluding-observations document
            if not any(s <= dl[0] <= e for s, e in sessions if s.year >= 2016):
                bad(a3, f"dialogue {r['dialogue'][0]} is not inside any HRCttee session ({r['symbol']})")
            rawrec = next((x for x in raw[a3] if x["symbol"] == r["symbol"]), None)
            if rawrec is None:
                bad(a3, f"{r['symbol']} not in raw data")
                continue
            ad = d(rawrec["adopted"])
            if not (0 <= (ad - dl[-1]).days <= 40):
                bad(a3, f"adoption {ad} is {(ad - dl[-1]).days} days after the dialogue ({r['symbol']})")
            fu = r.get("follow_up_due")
            if fu:
                gap = (d(fu) - ad).days
                if not (330 <= gap <= 1200):
                    bad(a3, f"follow-up due {fu} is {gap} days after adoption ({r['symbol']})")
            # re-read the document text with a different method and compare the stated years
            co = manifest.get(r["symbol"])
            if co and co.get("file"):
                text = re.sub(r"\s+", " ", ex.norm(ex.read_text(cache / co["file"])))
                tail = text[-2600:]
                years = {int(y) for y in re.findall(r"\b(20[2-4]\d)\b", tail)}
                for key in ("next_dialogue_year", "loipr_year", "next_report_year"):
                    v = rawrec.get(key)
                    if v:
                        checked[key] += 1
                        if v not in years:
                            bad(a3, f"{key}={v} does not appear in the closing paragraphs of {r['symbol']}")
                if rawrec.get("follow_up_due") and rawrec["follow_up_due"][:4] not in tail:
                    bad(a3, f"follow-up date {rawrec['follow_up_due']} not in closing text")
                if rawrec.get("next_report_due"):
                    checked["next_report_due"] += 1
                    dd = d(rawrec["next_report_due"])
                    if not (0 <= (dd - ad).days / 365.25 <= 9):
                        bad(a3, f"report due {dd} is {(dd - ad).days / 365.25:.1f} years after adoption")
                if rawrec.get("next_dialogue_year") and rawrec.get("loipr_year"):
                    if rawrec["next_dialogue_year"] - rawrec["loipr_year"] != 2:
                        bad(a3, f"stated LOIPR {rawrec['loipr_year']} and dialogue {rawrec['next_dialogue_year']} are not 2 years apart")
                if rawrec.get("next_dialogue_year") and not (1 <= rawrec["next_dialogue_year"] - dl[0].year <= 9):
                    bad(a3, f"stated next dialogue {rawrec['next_dialogue_year']} vs last {dl[0].year}")
    n = h.get("next")
    if n:
        checked["next"] += 1
        Y, M = map(int, n["dialogue"].split("-"))
        if M not in (3, 6, 10):
            bad(a3, f"next dialogue month {M} is not 3/6/10")
        ly, lm = map(int, n["loipr_adoption"].split("-"))
        if (Y - ly) * 12 + (M - lm) != 24:
            bad(a3, f"LOIPR {n['loipr_adoption']} is not 24 months before {n['review']}")
        if n["basis"] != "stated_report_due+1y":
            ry, rm = map(int, n["state_report_due"].split("-")[:2])
            if (Y - ry) * 12 + (M - rm) != 12:
                bad(a3, "State report due is not 12 months before the dialogue")
        else:
            dy = int(n["state_report_due"][:4])
            if Y != dy + 1:
                bad(a3, f"dialogue {Y} is not the stated report year {dy} + 1")
        if h["reviews"]:
            last = d(h["reviews"][-1]["dialogue"][0])
            if (Y, M) <= (last.year, last.month):
                bad(a3, f"next dialogue {n['review']} is not after the last one {last}")
    elif h["reviews"] or h.get("status") != "no_dialogue_10y":
        bad(a3, "has dialogues but no next dialogue")

# UPR: every State exactly once in cycle 4, cycle-5 slots 1..14, 13-14 States a session
per_session = Counter()
for a3, c in cal.items():
    u = c["upr"]
    if not u:
        continue
    checked["upr"] += 1
    c4, c5 = u["cycle4"], u["cycle5"]
    if c4.get("session"):
        per_session[c4["session"]] += 1
        s = d(c4["start"])
        exp = {11: 3, 1: 6, 4: 9, 5: 9}[s.month]
        if int(c4["adoption"][5:]) != exp:
            bad(a3, f"UPR adoption month {c4['adoption']} for session starting {c4['start']}")
    if c5.get("status") == "predicted" and not 1 <= c5["session_index"] <= 14:
        bad(a3, "UPR cycle-5 slot out of range")
for n, k in sorted(per_session.items()):
    if not 12 <= k <= 15:
        problems.append(f"UPR session {n} has {k} States")
if len([c for c in cal.values() if c["upr"]]) != 193:
    problems.append("UPR does not cover 193 States")

print("checked:", dict(checked))
print("session sizes:", dict(sorted(per_session.items())))
print(f"{len(problems)} problems")
for p in problems:
    print(" ", p)
