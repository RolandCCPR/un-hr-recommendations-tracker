"""CRUD and query operations for recommendations."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .db import DEFAULT_DB_PATH, init_db
from .models import Grade, Position, Recommendation

# Columns written on insert.
_COLUMNS = (
    "text",
    "country",
    "mechanism",
    "cycle",
    "session",
    "document_symbol",
    "paragraph",
    "recommending_state",
    "position",
    "themes",
    "affected_persons",
    "sdgs",
    "date_issued",
    "annotation_id",
    "source_url",
    "grade",
    "assessment_rationale",
    "assessment_sources",
    "assessed_at",
)


def _params(rec: Recommendation) -> dict:
    row = {col: getattr(rec, col) for col in _COLUMNS}
    row["grade"] = Grade(rec.grade).value
    row["position"] = Position(rec.position).value
    return row


class RecommendationRepository:
    """A thin data-access layer over the ``recommendations`` table."""

    def __init__(self, db_path: str | Path = DEFAULT_DB_PATH) -> None:
        self.conn = init_db(db_path)

    # -- create ---------------------------------------------------------
    def add(self, rec: Recommendation) -> Recommendation:
        placeholders = ", ".join(f":{c}" for c in _COLUMNS)
        with self.conn:
            cur = self.conn.execute(
                f"INSERT INTO recommendations ({', '.join(_COLUMNS)}) "
                f"VALUES ({placeholders})",
                _params(rec),
            )
        return self.get(cur.lastrowid)

    def add_many(self, recs: list[Recommendation]) -> int:
        """Insert many recommendations, skipping rows whose ``annotation_id``
        already exists. Returns the number actually inserted."""
        placeholders = ", ".join(f":{c}" for c in _COLUMNS)
        before = self.conn.total_changes
        with self.conn:
            self.conn.executemany(
                f"INSERT OR IGNORE INTO recommendations ({', '.join(_COLUMNS)}) "
                f"VALUES ({placeholders})",
                [_params(r) for r in recs],
            )
        return self.conn.total_changes - before

    # -- read ---------------------------------------------------------
    def get(self, rec_id: int) -> Recommendation | None:
        row = self.conn.execute(
            "SELECT * FROM recommendations WHERE id = ?", (rec_id,)
        ).fetchone()
        return Recommendation.from_row(row) if row else None

    def list(
        self,
        grade: Grade | str | None = None,
        position: Position | str | None = None,
        theme: str | None = None,
        paragraph: str | None = None,
    ) -> list[Recommendation]:
        clauses: list[str] = []
        params: list[object] = []
        if grade is not None:
            clauses.append("grade = ?")
            params.append(Grade(grade).value)
        if position is not None:
            clauses.append("position = ?")
            params.append(Position(position).value)
        if theme is not None:
            clauses.append("themes LIKE ?")
            params.append(f"%{theme}%")
        if paragraph is not None:
            clauses.append("paragraph = ?")
            params.append(paragraph)
        where = f" WHERE {' AND '.join(clauses)}" if clauses else ""
        rows = self.conn.execute(
            f"SELECT * FROM recommendations{where} ORDER BY id", params
        ).fetchall()
        return [Recommendation.from_row(r) for r in rows]

    def count_by_grade(self) -> dict[str, int]:
        rows = self.conn.execute(
            "SELECT grade, COUNT(*) AS n FROM recommendations "
            "GROUP BY grade ORDER BY grade"
        ).fetchall()
        return {r["grade"]: r["n"] for r in rows}

    # -- update ---------------------------------------------------------
    def set_grade(
        self,
        rec_id: int,
        grade: Grade | str,
        rationale: str | None = None,
        sources: str | None = None,
        evidence: str | None = None,
        action: str | None = None,
    ) -> Recommendation | None:
        """Record an implementation grade with the short action summary, the
        rationale, source citations and the supporting quotes (``evidence``)."""
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        with self.conn:
            self.conn.execute(
                "UPDATE recommendations SET "
                "  grade = ?, "
                "  action_summary = COALESCE(?, action_summary), "
                "  assessment_rationale = COALESCE(?, assessment_rationale), "
                "  assessment_sources = COALESCE(?, assessment_sources), "
                "  assessment_evidence = COALESCE(?, assessment_evidence), "
                "  assessed_at = ?, "
                "  updated_at = datetime('now') "
                "WHERE id = ?",
                (Grade(grade).value, action, rationale, sources, evidence, now, rec_id),
            )
        return self.get(rec_id)

    # -- delete ---------------------------------------------------------
    def delete(self, rec_id: int) -> bool:
        with self.conn:
            cur = self.conn.execute(
                "DELETE FROM recommendations WHERE id = ?", (rec_id,)
            )
        return cur.rowcount > 0

    # -- lifecycle ----------------------------------------------------
    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "RecommendationRepository":
        return self

    def __exit__(self, *exc) -> None:
        self.close()
