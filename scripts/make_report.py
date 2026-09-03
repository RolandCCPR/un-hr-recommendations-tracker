"""Generate the Markdown assessment report from a country's database.

    python -m scripts.make_report [slug]     (default: united-states)

Layout: grouped by OHCHR theme; within a theme the largest block (the main
assessment) first, then exceptions. Each block heading has collapsed
recommendation ranges plus a short action phrase; then the grade, an
**Evidence:** list quoting each source, and a reasoned **Assessment:** line.
"""

from __future__ import annotations

import collections
import sys

from recommendations.models import Grade
from recommendations.repository import RecommendationRepository

from scripts.countries import ROOT, get, out_dir


def _para_key(p: str | None) -> int:
    if p and "." in p:
        try:
            return int(p.split(".")[1])
        except ValueError:
            return 0
    return 0


def _collapse_ranges(paras: list[str]) -> str:
    paras = [p for p in paras if p and "." in p]
    if not paras:
        return ""
    pref = paras[0].split(".")[0]
    nums = sorted({int(p.split(".")[1]) for p in paras})
    parts: list[str] = []
    i = 0
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


def _evidence_bullets(evidence: str | None) -> list[str]:
    if not evidence:
        return ["- *No specific information in the evidence base.*"]
    return [f"- {ln.strip()}" for ln in evidence.splitlines() if ln.strip()]


def build(slug: str) -> None:
    cfg = get(slug)
    repo = RecommendationRepository(cfg["db"])
    recs = repo.list()
    total = len(recs)
    by_grade = repo.count_by_grade()

    blocks: dict[tuple, list] = collections.defaultdict(list)
    for r in recs:
        primary = (r.themes or "—").split(";")[0].strip()
        blocks[(primary, r.action_summary or "", r.grade.value,
                r.assessment_rationale or "", r.assessment_evidence or "")].append(r)

    theme_min: dict[str, int] = {}
    for (theme, *_), items in blocks.items():
        m = min(_para_key(r.paragraph) for r in items)
        theme_min[theme] = min(theme_min.get(theme, m), m)

    L: list[str] = []
    L.append(f"# {cfg['name']} — Implementation of {cfg['cycle3_review'][:4]} "
             f"(3rd cycle) UPR Recommendations")
    L.append("")
    L.append(f"Assessment of {cfg['name']}'s implementation of the {total} "
             f"recommendations received in the 3rd UPR cycle "
             f"({cfg['cycle3_symbol']}, {cfg['cycle3_session']} session, "
             f"{cfg['cycle3_review']}), using the Human Rights Committee A–E "
             f"grading system (CCPR/C/108/2). Evidence is the 4th-cycle "
             f"pre-sessional documentation ({cfg['cycle4_review']} review).")
    L.append("")
    L.append("**Sources**")
    L.append("")
    for s in cfg["sources"]:
        L.append(f"- {s}")
    L.append("")
    L.append("Grades: **A** largely satisfactory · **B** partially satisfactory "
             "· **C** not satisfactory / no relevant action · **D** no "
             "information · **E** measures contrary to, or rejection of, the "
             "recommendation.")
    L.append("")
    L.append("This is a **first-pass assessment for expert review**. "
             "Recommendations are grouped by their OHCHR theme; within a theme, "
             "near-identical asks share a grade, with separate blocks where the "
             "substance (and grade) differ. Each block notes the position "
             f"{cfg['name']} took at the review (supported / noted / "
             "supported-noted); a *noted* recommendation was not accepted.")
    L.append("")
    L.append("## Summary")
    L.append("")
    L.append("| Grade | Count | Share |")
    L.append("|---|---:|---:|")
    for g in Grade:
        n = by_grade.get(g.value, 0)
        if n:
            L.append(f"| **{g.value}** — {g.label} | {n} | {n / total:.0%} |")
    L.append(f"| **Total** | {total} | 100% |")
    if cfg.get("headline"):
        L.append("")
        L.append(cfg["headline"])
    L.append("")

    L.append("## Assessment by theme")
    for theme in sorted(theme_min, key=lambda t: theme_min[t]):
        L.append("")
        L.append(f"## {theme}")
        theme_blocks = sorted(
            [(k, v) for k, v in blocks.items() if k[0] == theme],
            key=lambda kv: (-len(kv[1]), min(_para_key(r.paragraph) for r in kv[1])),
        )
        for (_theme, summary, grade_v, rationale, evidence), items in theme_blocks:
            items.sort(key=lambda r: _para_key(r.paragraph))
            nums = _collapse_ranges([r.paragraph for r in items])
            pos = collections.Counter(r.position.value for r in items)
            pos_str = ", ".join(f"{n} {p.replace('_', '-')}" for p, n in pos.items())
            word = "Recommendation" if len(items) == 1 else "Recommendations"
            grade = Grade(grade_v)
            heading = f"### {word} {nums}"
            if summary:
                heading += f" ({summary})"
            L.append("")
            L.append(heading)
            L.append("")
            L.append(f"*{len(items)} of {total} — position: {pos_str}.*")
            L.append("")
            L.append(f"**Grade: {grade.value} — {grade.committee_meaning}**")
            L.append("")
            L.append("**Evidence:**")
            L.extend(_evidence_bullets(evidence))
            L.append("")
            L.append(f"**Assessment:** {rationale}")
        L.append("")
        L.append("---")

    L.append("")
    L.append("## Full detail")
    L.append("")
    L.append(f"Per-recommendation grade, rationale, citations and quotes: the "
             f"`{cfg['slug_prefix']}_implementation_assessment.csv`, the filled "
             f"`{cfg['thematic_out']}` (column 4), and the database.")
    L.append("")

    out = out_dir(slug) / f"{cfg['slug_prefix']}_implementation_report.md"
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"Report: {out.relative_to(ROOT)}  ({len(blocks)} blocks, {total} recs)")
    repo.close()


if __name__ == "__main__":
    for s in sys.argv[1:] or ["united-states"]:
        build(s)
