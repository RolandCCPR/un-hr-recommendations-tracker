"""Shared machinery for the per-country implementation assessment.

A country module (``countries/<slug>/assess.py``) defines its cluster and
keyword rules and calls :func:`run`. Rules are graded on the adapted Human
Rights Committee A-E scale and each carries verbatim quotes from that country's
4th-cycle documents (National report /1, OHCHR Compilation /2, Stakeholders'
Summary /3).
"""

from __future__ import annotations

import csv
import re

from recommendations.models import Grade
from recommendations.repository import RecommendationRepository

from scripts.countries import ROOT, get, out_dir

# A quote = (organisation/body as named, doc key "1"|"2"|"3", paragraph, text)
Quote = tuple[str, str, str, str]

DOC_NAMES = {"1": "National Report", "2": "UN Compilation", "3": "Stakeholders' Summary"}


def _fmt(quotes: list[Quote], sym: dict[str, str]) -> tuple[str, str]:
    ev_lines, seen = [], []
    for org, doc, para, text in quotes:
        s = sym.get(doc, f"doc/{doc}")
        ev_lines.append(f'{DOC_NAMES[doc]} ({s}), para. {para} — {org}: "{text}"')
        loc = f"{s} para. {para}"
        if loc not in seen:
            seen.append(loc)
    return "\n".join(ev_lines), "; ".join(seen)


def run(
    slug: str,
    *,
    clusters: dict[str, tuple[Grade, str, str, list[Quote]]],
    keywords: list[tuple[str, Grade, str, str, list[Quote]]],
    fallback: tuple[Grade, str, str, list[Quote]] | None = None,
) -> None:
    """clusters:  theme -> (grade, action_summary, rationale, [quotes])
    keywords:  list of (regex, grade, action_summary, rationale, [quotes]); last
               match on the recommendation text wins over the cluster default.
    """
    cfg = get(slug)
    sym = {k: v for k, v in cfg["c4_docs"].items() if v}
    fallback = fallback or (
        Grade.D, "Miscellaneous",
        "No cluster rule matched and the evidence base contains no specific "
        "information on this recommendation.", [],
    )

    def choose(theme: str, text: str):
        grade, summary, rationale, quotes = clusters.get(theme, fallback)
        for pat, g, s, r, q in keywords:
            if re.search(pat, text, re.IGNORECASE):
                grade, summary, rationale, quotes = g, s, r, q
        return grade, summary, rationale, quotes

    repo = RecommendationRepository(cfg["db"])
    rows, tally = [], {}
    for rec in repo.list():
        primary = (rec.themes or "").split(";")[0].strip()
        grade, summary, rationale, quotes = choose(primary, rec.text)
        evidence, sources = _fmt(quotes, sym)
        repo.set_grade(rec.id, grade, rationale=rationale, sources=sources,
                       evidence=evidence, action=summary)
        tally[grade.value] = tally.get(grade.value, 0) + 1
        rows.append({
            "paragraph": rec.paragraph, "recommending_state": rec.recommending_state,
            "position": rec.position.value, "primary_theme": primary,
            "action_summary": summary, "grade": grade.value,
            "grade_label": grade.label, "text": rec.text,
            "rationale": rationale, "sources": sources, "evidence_quotes": evidence,
        })
    rows.sort(key=lambda r: int(r["paragraph"].split(".")[1])
              if r["paragraph"] and "." in r["paragraph"] else 0)

    out = out_dir(slug) / f"{cfg['slug_prefix']}_implementation_assessment.csv"
    with out.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"{cfg['name']}: assessed {len(rows)} — "
          + " ".join(f"{g}:{tally[g]}" for g in ("A", "B", "C", "D", "E") if tally.get(g)))
    print(f"CSV: {out.relative_to(ROOT)}")
    repo.close()
