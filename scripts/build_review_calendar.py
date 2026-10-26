"""Build the "When is my country next?" dataset (UPR + Human Rights Committee).

Inputs (all in site/data):
  upr_cycle4_calendar_source.txt  UPR 4th-cycle calendar (OHCHR), countries per session
  hrc_calendar_raw.json           dates read from the HRC concluding observations
  hrc_sessions_raw.txt            HRC session lists (reviews, LOIPR adoptions), 2016-2026
  hrc_parties_excel.json          States with an HRC dialogue 2006-2025 (CCPR Centre sheet)
Output:
  site/data/review_calendar.json  one record per country
  site/data/review_calendar_check.csv  flat table for review

Rules (as agreed with the CCPR Centre):
  UPR  cycle 5 starts Nov 2027; sessions Nov, Jan, Apr; same order as cycle 4
       (US, Ukraine -> original slot 50th / 42nd; Myanmar -> date not set).
       Adoption: Nov review -> March next year; Jan -> June; Apr/May -> September.
       Cycle-5 deadlines: stakeholders Apr/Jul/Oct, national report Aug/Oct/Jan
       (for Nov/Jan/Apr sessions); cycle 4 uses the calendar's actual months.
  HRC  next review = LOIPR adoption + 2 years when a LOIPR was adopted after the
       last review; else the year stated in the last concluding observations;
       else last review + 8 years ("tentative"). Month = session month of the
       last review (Mar / Jun / Oct); summer session counted as June.
       LOIPR = review - 2 years, State replies = review - 1 year.
       NGO deadline for the LOIPR = LOIPR month - 2; for the review = month - 1.
       Follow-up due = exact date stated in the concluding observations.
"""

from __future__ import annotations

import csv
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "site/data"
TODAY = date.today()
WINDOW_START = date(2016, 1, 1)


def norm(s: str) -> str:
    s = s.replace("’", "'")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^a-z ]", " ", s)
    return " ".join(s.split())


# ---------------------------------------------------------------- names -> a3
def name_map() -> dict[str, str]:
    cs = json.loads((ROOT / "site/public/data/countries.json").read_text(encoding="utf-8"))
    m: dict[str, str] = {}
    for c in cs:
        m[norm(c["name"])] = c["a3"]
        if "," in c["name"]:
            m[norm(c["name"].split(",", 1)[0])] = c["a3"]
    m.update({
        "czech republic": "CZE", "republic of korea": "KOR", "korea dpr": "PRK",
        "democratic people s republic of korea": "PRK", "republic of moldova": "MDA",
        "united republic of tanzania": "TZA", "state of palestine": "PSE",
        "palestine": "PSE", "cabo verde": "CPV", "cape verde": "CPV", "viet nam": "VNM",
        "vietnam": "VNM", "north macedonia": "MKD", "turkiye": "TUR", "turkey": "TUR",
        "cote d ivoire": "CIV", "lao people s democratic republic": "LAO", "laos": "LAO",
        "iran islamic republic of": "IRN", "iran": "IRN", "russian federation": "RUS",
        "russia": "RUS", "syria": "SYR", "syrian arab republic": "SYR",
        "united kingdom of great britain and northern ireland": "GBR",
        "united states of america": "USA", "congo": "COG", "congo republic of the": "COG",
        "democratic republic of the congo": "COD", "east timor": "TLS",
        "timor leste": "TLS", "swaziland": "SWZ", "eswatini": "SWZ", "gambia the": "GMB",
        "gambia": "GMB", "bahamas the": "BHS", "bahamas": "BHS", "netherlands": "NLD",
        "kyrgyzstan": "KGZ", "bolivia": "BOL", "venezuela": "VEN", "holy see": "VAT",
        "micronesia": "FSM", "sao tome and principe": "STP", "myanmar": "MMR",
        "china hong kong": "CHN-HKG", "china macau": "CHN-MAC",
    })
    return m


NAMES = name_map()


def a3_of(name: str) -> str | None:
    n = norm(name)
    if name.strip().startswith("China (Hong Kong)"):
        return "CHN-HKG"
    if name.strip().startswith("China (Macau)"):
        return "CHN-MAC"
    return NAMES.get(n)


# ----------------------------------------------------------------------- UPR
# session no. -> (start, end, stakeholders' deadline month, national report deadline month)
C4 = {
    41: ("2022-11-07", "2022-11-18", "2022-03", "2022-08"),
    42: ("2023-01-23", "2023-02-03", "2022-07", "2022-10"),
    43: ("2023-05-01", "2023-05-12", "2022-10", "2023-02"),
    44: ("2023-11-06", "2023-11-17", "2023-04", "2023-08"),
    45: ("2024-01-22", "2024-02-02", "2023-07", "2023-10"),
    46: ("2024-04-29", "2024-05-10", "2023-10", "2024-01"),
    47: ("2024-11-04", "2024-11-15", "2024-04", "2024-08"),
    48: ("2025-01-20", "2025-01-31", "2024-07", "2024-10"),
    49: ("2025-04-28", "2025-05-09", "2024-10", "2025-01"),
    50: ("2025-11-03", "2025-11-14", "2025-04", "2025-08"),
    51: ("2026-01-19", "2026-01-30", "2025-07", "2025-10"),
    52: ("2026-05-04", "2026-05-15", "2025-10", "2026-01"),
    53: ("2026-11-02", "2026-11-13", "2026-04", "2026-08"),
    54: ("2027-01-01", "2027-02-28", "2026-07", "2026-10"),  # dates "Jan - Feb 2027"
}
# cycle-5 sessions in order (index 1..14): Nov 2027, Jan 2028, Apr 2028, Nov 2028, ...
# sessions cycle Nov(y) -> Jan(y+1) -> Apr(y+1) -> Nov(y+1)
C5_MONTHS = []
for i in range(14):
    k, r = divmod(i, 3)
    C5_MONTHS.append([(2027 + k, 11), (2028 + k, 1), (2028 + k, 4)][r])


def ym(y: int, m: int) -> str:
    return f"{y:04d}-{m:02d}"


def shift(y: int, m: int, delta: int) -> tuple[int, int]:
    t = y * 12 + (m - 1) + delta
    return t // 12, t % 12 + 1


def upr_adoption(y: int, m: int) -> str:
    if m >= 10:
        return ym(y + 1, 3)
    if m <= 2:
        return ym(y, 6)
    return ym(y, 9)


def c5_deadlines(y: int, m: int) -> tuple[str, str]:
    """(stakeholders, national report) months for a cycle-5 session in (y, m)."""
    if m == 11:
        return ym(y, 4), ym(y, 8)
    if m == 1:
        return ym(y - 1, 7), ym(y - 1, 10)
    return ym(y - 1, 10), ym(y, 1)


def parse_upr_calendar() -> dict:
    raw = (DATA / "upr_cycle4_calendar_source.txt").read_text(encoding="utf-8-sig")
    raw = raw.replace("\x07", "").replace("\x02", "")  # Word table-cell marks
    lines = [l.strip() for l in re.split(r"[\r\n]+", raw) if l.strip()]
    sessions: dict[int, list[tuple[str, int | None]]] = {}
    cur = None
    for l in lines:
        mm = re.match(r"(\d{2})(?:st|nd|rd|th) session", l)
        if mm:
            cur = int(mm.group(1))
            continue
        if cur and l.count(",") >= 8 and "deadline" not in l.lower():
            out = []
            for part in [p.strip() for p in re.split(r",\s*(?![^()]*\))", l)]:
                p = part.replace("*", "")
                orig = None
                mo = re.search(r"\(postponed from (\d+)", p)
                if mo:
                    orig = int(mo.group(1))
                p = re.sub(r"\s*\(postponed.*?\)", "", p).strip()
                if p:
                    out.append((p, orig, "(postponed)" in part))
            sessions[cur] = out
    return sessions


def build_upr() -> dict[str, dict]:
    sessions = parse_upr_calendar()
    res: dict[str, dict] = {}
    unmatched = []
    for no, lst in sessions.items():
        for name, orig, postponed_unspecified in lst:
            a3 = a3_of(name)
            if not a3:
                unmatched.append(name)
                continue
            start, end, sh, nr = C4[no]
            s = date.fromisoformat(start)
            c4 = {
                "session": no, "start": start, "end": end, "exam": ym(s.year, s.month),
                "adoption": upr_adoption(s.year, s.month),
                "stakeholders_deadline": sh, "national_report_deadline": nr,
                "status": "past" if date.fromisoformat(end) < TODAY else "upcoming",
            }
            slot = orig if orig else no
            if no == 54 and not orig and a3 == "MMR":
                c4.update(status="date_not_set", exam=None, adoption=None,
                          stakeholders_deadline=None, national_report_deadline=None,
                          session=None, start=None, end=None)
                c5 = {"status": "date_not_set"}
            else:
                i = slot - 41
                cy, cm = C5_MONTHS[i]
                shd, nrd = c5_deadlines(cy, cm)
                c5 = {"session_index": i + 1, "exam": ym(cy, cm), "adoption": upr_adoption(cy, cm),
                      "stakeholders_deadline": shd, "national_report_deadline": nrd,
                      "status": "predicted"}
            if orig:
                c4["postponed_from_session"] = orig
            res[a3] = {"name": name, "cycle4": c4, "cycle5": c5}
    res["_unmatched"] = unmatched  # type: ignore[assignment]
    return res


# ----------------------------------------------------------------------- HRC
def session_month(d: date) -> int:
    """Map a date to the session month used on the site: 3, 6 or 10."""
    if d.month in (2, 3, 4):
        return 3
    if d.month in (5, 6, 7):
        return 6
    return 10


def parse_sessions() -> tuple[dict, dict]:
    """-> (loipr events {a3: [date]}, pending reviews {a3: (start, end)} for the current session)."""
    MON = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
    loipr: dict[str, list[date]] = {}
    pending: dict[str, tuple[date, date]] = {}
    for line in (DATA / "hrc_sessions_raw.txt").read_text(encoding="utf-8").splitlines():
        mm = re.match(r"(\d{3}) (\d\d) (\w{3}) (\d{4}) (\d\d) (\w{3}) (\d{4}) (.*)", line)
        if not mm:
            continue
        n, d1, m1, y1, d2, m2, y2, rest = mm.groups()
        start = date(int(y1), MON[m1], int(d1))
        end = date(int(y2), MON[m2], int(d2))
        lo = re.search(r"LISTS OF ISSUES PRIOR TO REPORTING (.*?)(?= NON REPORTING| LISTS OF ISSUES| STATES PARTIES|$)", rest)
        if lo:
            for nm in lo.group(1).split(", "):
                a3 = a3_of(nm.strip())
                if a3:
                    loipr.setdefault(a3, []).append(start)
        spr = re.search(r"STATES PARTIES REPORTS (.*?)(?= NON REPORTING| LISTS OF ISSUES|$)", rest)
        if spr and start <= TODAY <= end:
            for nm in spr.group(1).split(", "):
                a3 = a3_of(nm.strip())
                if a3:
                    pending[a3] = (start, end)
    return loipr, pending


def parse_future_list() -> set[str]:
    """States on the Committee's undated 'Future Sessions' entry (scheduled, no date set)."""
    out: set[str] = set()
    for line in (DATA / "hrc_sessions_raw.txt").read_text(encoding="utf-8").splitlines():
        m = re.match(r'Future Sessions \(no date[^)]*\) (.*)', line)
        if m:
            for nm in m.group(1).split(", "):
                a3 = a3_of(nm.strip())
                if a3:
                    out.add(a3)
    return out


def month_name(m: int) -> str:
    return ["", "January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"][m]


def build_hrc() -> dict[str, dict]:
    raw = json.loads((DATA / "hrc_calendar_raw.json").read_text(encoding="utf-8"))
    loipr, pending = parse_sessions()
    future_list = parse_future_list()
    excel = json.loads((DATA / "hrc_parties_excel.json").read_text(encoding="utf-8"))
    parties = set(raw) - {"HKG", "MAC"}  # Hong Kong / Macau appear as CHN-HKG / CHN-MAC
    for r in excel:
        if r["name"].startswith("China ("):
            continue
        a3 = a3_of(r["name"])
        if a3:
            parties.add(a3)
    res: dict[str, dict] = {}
    flags: list[str] = []
    for a3 in sorted(parties):
        docs = [d for d in raw.get(a3, []) if d.get("adopted") and d.get("dialogue")]
        reviews = []
        for d in docs:
            dd = [date.fromisoformat(x) for x in d["dialogue"]]
            if min(dd) < WINDOW_START:
                continue
            reviews.append({
                "symbol": d["symbol"], "dialogue": d["dialogue"],
                "follow_up_due": d.get("follow_up_due"),
                "no_state_report": "absence" in (d.get("title") or "").lower(),
                "status": "past",
            })
        # reviews taking place now (session 146): treated as already held
        if a3 in pending:
            s, e = pending[a3]
            reviews.append({"symbol": None, "dialogue": [s.isoformat(), e.isoformat()],
                            "follow_up_due": date(e.year + 3, e.month, e.day).isoformat(),
                            "follow_up_tentative": True, "no_state_report": False,
                            "status": "held_now"})
        reviews.sort(key=lambda r: r["dialogue"][0])
        rec: dict = {"reviews": reviews}
        if not reviews:
            rec["status"] = "no_dialogue_10y"
        # last review (incl. earlier than window, for deriving the next one)
        last = None
        if reviews:
            last = reviews[-1]
            L = date.fromisoformat(last["dialogue"][0])
            Lend = date.fromisoformat(last["dialogue"][-1])
        else:
            older = sorted(docs, key=lambda d: d["adopted"])
            L = Lend = date.fromisoformat(older[-1]["dialogue"][0]) if older else None
        co = None
        if reviews and last["symbol"]:
            co = next((d for d in docs if d["symbol"] == last["symbol"]), None)
        elif not reviews and docs:  # last dialogue is older than the window
            co = max(docs, key=lambda d: d["adopted"])
        ev = sorted(x for x in loipr.get(a3, []) if L is None or x > Lend)
        nxt = None
        exact_due = None
        if ev:  # reality takes over: an adopted LOIPR anchors everything
            e = ev[-1]
            nxt = (e.year + 2, session_month(e), "loipr_adopted+2y", e)
        elif co and co.get("next_dialogue_year"):
            nxt = (co["next_dialogue_year"], session_month(L), "stated_in_concluding_observations", None)
        elif co and co.get("next_report_due"):
            rd = date.fromisoformat(co["next_report_due"])
            nxt = (rd.year + 1, session_month(rd), "stated_report_due+1y", None)
            exact_due = co["next_report_due"]
        elif co and co.get("next_report_year"):
            nxt = (co["next_report_year"] + 1, session_month(L), "stated_report_due+1y", None)
            exact_due = str(co["next_report_year"])
        elif L:
            nxt = (L.year + 8, session_month(L), "last_dialogue+8y_tentative", None)
        if nxt:
            Y, M, basis, e = nxt
            if co and co.get("next_dialogue_year") and co["next_dialogue_year"] != Y and basis == "loipr_adopted+2y":
                flags.append(f"{a3}: LOIPR rule gives {Y}, concluding observations state {co['next_dialogue_year']}")
            ly, lm = shift(Y, M, -24)
            ry, rm = shift(Y, M, -12)
            ngo_l = shift(ly, lm, -2)
            ngo_r = shift(Y, M, -1)
            rec["next"] = {
                "dialogue": ym(Y, M),
                "basis": basis,
                "tentative": True,
                "loipr_adoption": ym(e.year, session_month(e)) if e else ym(ly, lm),
                "loipr_source": "adopted" if e else ("stated_year" if basis == "stated_in_concluding_observations" else "calculated"),
                "state_report_due": exact_due or ym(ry, rm),
                "state_report_source": "stated" if exact_due else ("stated_year" if basis == "stated_in_concluding_observations" else "calculated"),
                "ngo_loipr_deadline": ym(*ngo_l),
                "ngo_dialogue_deadline": ym(*ngo_r),
            }
            if date(Y, M, 28) < TODAY:
                rec["next"]["overdue"] = True
            if a3 in future_list:
                rec["next"]["on_future_list"] = True
            if any(r["no_state_report"] for r in reviews[-1:]):
                rec["next"]["note"] = "last dialogue took place without a State report"
        res[a3] = rec
    res["_flags"] = flags  # type: ignore[assignment]
    return res


# ---------------------------------------------------------------------- main
def main() -> None:
    upr = build_upr()
    hrc = build_hrc()
    unmatched = upr.pop("_unmatched")
    flags = hrc.pop("_flags")
    cs = {c["a3"]: c for c in json.loads((ROOT / "site/public/data/countries.json").read_text(encoding="utf-8"))}
    ids = set(upr) | set(hrc) | {"PSE", "VAT"}
    out = []
    for a3 in sorted(ids):
        if a3 in ("CHN-HKG", "CHN-MAC"):
            name = "China (Hong Kong)" if a3 == "CHN-HKG" else "China (Macau)"
        elif a3 == "VAT":
            name = "Holy See"
        elif a3 == "PSE":
            name = "State of Palestine"
        else:
            name = upr.get(a3, {}).get("name") or (cs.get(a3) or {}).get("name") or a3
        out.append({"a3": a3, "name": name,
                    "upr": ({k: v for k, v in upr[a3].items() if k != "name"} if a3 in upr else None),
                    "hrc": hrc.get(a3)})
    (DATA / "review_calendar.json").write_text(
        json.dumps({"generated": TODAY.isoformat(), "countries": out}, ensure_ascii=False, indent=1),
        encoding="utf-8")
    with open(DATA / "review_calendar_check.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["a3", "country", "UPR cycle4 exam", "UPR cycle4 adoption", "UPR cycle5 exam",
                    "UPR cycle5 adoption", "HRCttee last dialogue", "HRCttee follow-up due",
                    "HRCttee next dialogue", "basis", "LOIPR (tentative unless adopted)", "State report due", "NGO deadline LOIPR",
                    "NGO deadline dialogue", "note"])
        for c in out:
            u, h = c["upr"], c["hrc"]
            last = h["reviews"][-1] if h and h["reviews"] else None
            n = (h or {}).get("next") or {}
            w.writerow([c["a3"], c["name"],
                        (u or {}).get("cycle4", {}).get("exam") if u else "",
                        (u or {}).get("cycle4", {}).get("adoption") if u else "",
                        (u or {}).get("cycle5", {}).get("exam") if u else "",
                        (u or {}).get("cycle5", {}).get("adoption") if u else "",
                        last["dialogue"][0] if last else ((h or {}).get("status") or ""),
                        last.get("follow_up_due") if last else "",
                        n.get("dialogue", ""), n.get("basis", ""), n.get("loipr_adoption", ""),
                        n.get("state_report_due", ""), n.get("ngo_loipr_deadline", ""),
                        n.get("ngo_dialogue_deadline", ""),
                        ("overdue; " if n.get("overdue") else "") + (n.get("note") or "")])
    print(f"{len(out)} countries; UPR {sum(1 for c in out if c['upr'])}; HRC {sum(1 for c in out if c['hrc'])}")
    print("UPR names not matched:", unmatched)
    print("flags:", *flags, sep="\n  ")


if __name__ == "__main__":
    main()
