"""Import a country's 3rd-cycle recommendations from its OHCHR thematic list.

    python -m scripts.build_country denmark
"""

from __future__ import annotations

import sys

from recommendations import thematic_list as tl
from recommendations.models import Recommendation
from recommendations.repository import RecommendationRepository

from scripts.countries import get


def build(slug: str) -> None:
    cfg = get(slug)
    rows = tl.read_thematic_list(cfg["thematic"])
    recs = [
        Recommendation(
            **tl.row_to_kwargs(
                r,
                country=cfg["name"],
                cycle=3,
                session=cfg["cycle3_session"],
                document_symbol=cfg["cycle3_symbol"],
                date_issued=cfg["cycle3_review"],
                source_url=f"https://www.ohchr.org/en/hr-bodies/upr/"
                f"{cfg['code'][:2].lower()}-index",
            )
        )
        for r in rows
    ]
    cfg["db"].parent.mkdir(parents=True, exist_ok=True)
    with RecommendationRepository(cfg["db"]) as repo:
        inserted = repo.add_many(recs)
    print(f"{cfg['name']}: parsed {len(recs)}, inserted {inserted} "
          f"(db: {cfg['db'].relative_to(cfg['db'].parents[2])})")


if __name__ == "__main__":
    for s in sys.argv[1:] or ["denmark", "namibia", "paraguay"]:
        build(s)
