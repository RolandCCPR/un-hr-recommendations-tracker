"""Command-line interface for the recommendations tracker."""

from __future__ import annotations

import argparse
from pathlib import Path

from .models import Grade, Position, Recommendation
from .repository import RecommendationRepository

_GRADE_CHOICES = [g.value for g in Grade]
_POSITION_CHOICES = [p.value for p in Position]
_INDEX_URL = "https://www.ohchr.org/en/hr-bodies/upr/us-index"


def _print(rec: Recommendation) -> None:
    print(f"#{rec.id}  {rec.paragraph or '-':>7}  [{rec.grade.value}]  ({rec.position.value})")
    print(f"      {rec.text}")
    print(f"      source : {rec.citation}")
    if rec.assessment_rationale:
        print(f"      why    : {rec.assessment_rationale}")
    if rec.assessment_sources:
        print(f"      cites  : {rec.assessment_sources}")


def cmd_import(repo: RecommendationRepository, args: argparse.Namespace) -> None:
    path = Path(args.file)
    suffix = path.suffix.lower()
    if suffix == ".docx":
        from . import thematic_list as src

        rows = src.read_thematic_list(path)
    elif suffix == ".xlsx":
        from . import uhri as src

        rows = src.read_export(path)
    else:
        raise SystemExit(f"Unsupported file type: {suffix} (use .docx or .xlsx)")

    recs = [
        Recommendation(**src.row_to_kwargs(r, source_url=args.source_url))
        for r in rows
    ]
    inserted = repo.add_many(recs)
    print(f"Parsed {len(recs)} recommendations; inserted {inserted} new "
          f"(skipped {len(recs) - inserted} already present).")


def cmd_list(repo: RecommendationRepository, args: argparse.Namespace) -> None:
    recs = repo.list(
        grade=args.grade, position=args.position, theme=args.theme,
        paragraph=args.paragraph,
    )
    if not recs:
        print("No recommendations found.")
        return
    for rec in recs:
        _print(rec)
    print(f"\n{len(recs)} recommendation(s).")


def cmd_grade(repo: RecommendationRepository, args: argparse.Namespace) -> None:
    rec = repo.set_grade(
        args.id, Grade(args.grade), rationale=args.rationale, sources=args.sources
    )
    if rec is None:
        print(f"No recommendation with id {args.id}.")
        return
    print("Updated:")
    _print(rec)


def cmd_stats(repo: RecommendationRepository, _args: argparse.Namespace) -> None:
    counts = repo.count_by_grade()
    total = sum(counts.values())
    print(f"{'grade':<14} {'n':>4}   meaning")
    for g in Grade:
        n = counts.get(g.value, 0)
        print(f"{g.value:<14} {n:>4}   {g.label}")
    print(f"{'TOTAL':<14} {total:>4}")


def cmd_grades(_repo: RecommendationRepository, _args: argparse.Namespace) -> None:
    print("Adapted Human Rights Committee A-E scale (CCPR/C/108/2):")
    for g in Grade:
        print(f"  {g.value:<13} {g.label}")
        print(f"  {'':<13} (Committee: {g.committee_meaning})")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="recommendations",
        description="Track UPR recommendations to the US, their source, and the "
        "adapted Human Rights Committee A-E implementation grade.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_imp = sub.add_parser(
        "import", help="import recommendations from a .docx thematic list or .xlsx UHRI export"
    )
    p_imp.add_argument("file")
    p_imp.add_argument("--source-url", default=_INDEX_URL)
    p_imp.set_defaults(func=cmd_import)

    p_list = sub.add_parser("list", help="list recommendations")
    p_list.add_argument("--grade", choices=_GRADE_CHOICES)
    p_list.add_argument("--position", choices=_POSITION_CHOICES)
    p_list.add_argument("--theme", help="substring match on the themes field")
    p_list.add_argument("--paragraph")
    p_list.set_defaults(func=cmd_list)

    p_grade = sub.add_parser("grade", help="record an implementation grade")
    p_grade.add_argument("id", type=int)
    p_grade.add_argument("grade", choices=_GRADE_CHOICES)
    p_grade.add_argument("--rationale")
    p_grade.add_argument("--sources", help="evidence citations")
    p_grade.set_defaults(func=cmd_grade)

    p_stats = sub.add_parser("stats", help="count recommendations by grade")
    p_stats.set_defaults(func=cmd_stats)

    p_grades = sub.add_parser("grades", help="print the A-E scale")
    p_grades.set_defaults(func=cmd_grades)

    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    with RecommendationRepository() as repo:
        args.func(repo, args)


if __name__ == "__main__":
    main()
