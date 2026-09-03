"""Domain model for a UPR recommendation and its implementation assessment."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Grade(str, Enum):
    """Implementation grade, adapted from the Human Rights Committee's A-E
    follow-up assessment scale (CCPR/C/108/2).

    Reference: https://ccprcentre.org/follow-up-and-assessment

    The Committee grades a State's *reply*; here the same letters grade the
    *level of implementation* of a UPR recommendation on the strength of the
    UN and stakeholder reports submitted for the next cycle.
    """

    NOT_ASSESSED = "not_assessed"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"

    def __str__(self) -> str:
        return self.value

    @property
    def label(self) -> str:
        return _GRADE_LABELS[self]

    @property
    def committee_meaning(self) -> str:
        return _COMMITTEE_MEANINGS[self]


# Short labels used in this project's implementation analysis.
_GRADE_LABELS: dict[Grade, str] = {
    Grade.NOT_ASSESSED: "Not yet assessed",
    Grade.A: "Largely implemented / action largely satisfactory",
    Grade.B: "Partially implemented / steps taken, further action needed",
    Grade.C: "Not implemented / no relevant action taken",
    Grade.D: "No information available on implementation",
    Grade.E: "Contrary measures taken, or recommendation rejected",
}

# Verbatim Human Rights Committee criteria (CCPR/C/108/2).
_COMMITTEE_MEANINGS: dict[Grade, str] = {
    Grade.NOT_ASSESSED: "Not yet assessed",
    Grade.A: "Information/action largely satisfactory",
    Grade.B: "Information/action partially satisfactory",
    Grade.C: "Information/action not satisfactory",
    Grade.D: "No cooperation with the Committee",
    Grade.E: (
        "Information or measures taken are contrary to, or reflect rejection "
        "of, the recommendation"
    ),
}


class Position(str, Enum):
    """The State's response to the recommendation at the review."""

    SUPPORTED = "supported"
    NOTED = "noted"
    SUPPORTED_NOTED = "supported_noted"  # partially supported, partially noted
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def parse(cls, raw: str | None) -> "Position":
        if not raw:
            return cls.UNKNOWN
        key = raw.strip().lstrip("-").strip().lower().replace(" ", "").replace("/", "_")
        return {
            "supported": cls.SUPPORTED,
            "noted": cls.NOTED,
            "supported_noted": cls.SUPPORTED_NOTED,
        }.get(key, cls.UNKNOWN)


@dataclass
class Recommendation:
    """A single UPR recommendation and its implementation assessment.

    Source fields follow the Universal Human Rights Index export
    (https://uhri.ohchr.org). ``grade`` follows the adapted Human Rights
    Committee A-E scale (see :class:`Grade`).
    """

    text: str
    country: str = "United States of America"
    mechanism: str = "UPR"
    cycle: int | None = None
    session: str | None = None
    document_symbol: str | None = None
    paragraph: str | None = None
    recommending_state: str | None = None
    position: Position = Position.UNKNOWN
    themes: str | None = None
    affected_persons: str | None = None
    sdgs: str | None = None
    date_issued: str | None = None
    annotation_id: str | None = None
    source_url: str | None = None
    grade: Grade = Grade.NOT_ASSESSED
    action_summary: str | None = None
    assessment_rationale: str | None = None
    assessment_sources: str | None = None
    assessment_evidence: str | None = None
    assessed_at: str | None = None
    id: int | None = None
    created_at: str | None = None
    updated_at: str | None = None

    def __post_init__(self) -> None:
        self.grade = Grade(self.grade)
        self.position = (
            self.position
            if isinstance(self.position, Position)
            else Position.parse(self.position)
        )

    @property
    def citation(self) -> str:
        parts = [p for p in ("UPR", self.document_symbol) if p]
        if self.paragraph:
            parts.append(f"para. {self.paragraph}")
        if self.recommending_state:
            parts.append(f"({self.recommending_state})")
        return ", ".join(parts)

    @classmethod
    def from_row(cls, row) -> "Recommendation":
        return cls(
            id=row["id"],
            text=row["text"],
            country=row["country"],
            mechanism=row["mechanism"],
            cycle=row["cycle"],
            session=row["session"],
            document_symbol=row["document_symbol"],
            paragraph=row["paragraph"],
            recommending_state=row["recommending_state"],
            position=Position(row["position"]),
            themes=row["themes"],
            affected_persons=row["affected_persons"],
            sdgs=row["sdgs"],
            date_issued=row["date_issued"],
            annotation_id=row["annotation_id"],
            source_url=row["source_url"],
            grade=Grade(row["grade"]),
            action_summary=row["action_summary"],
            assessment_rationale=row["assessment_rationale"],
            assessment_sources=row["assessment_sources"],
            assessment_evidence=row["assessment_evidence"],
            assessed_at=row["assessed_at"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )
