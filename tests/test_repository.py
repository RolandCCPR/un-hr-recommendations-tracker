import sqlite3

import pytest

from recommendations.models import Grade, Position, Recommendation
from recommendations.repository import RecommendationRepository


@pytest.fixture
def repo(tmp_path):
    with RecommendationRepository(db_path=tmp_path / "test.db") as r:
        yield r


def _sample(**overrides) -> Recommendation:
    data = dict(
        text="Ratify the Convention on the Rights of the Child.",
        paragraph="26.49",
        recommending_state="Switzerland",
        position="Supported",
        document_symbol="A/HRC/46/15",
        cycle=3,
        session="36th",
        themes="Ratification of & accession to international instruments",
        date_issued="2020-12-15",
    )
    data.update(overrides)
    return Recommendation(**data)


def test_add_and_get(repo):
    rec = repo.add(_sample())
    assert rec.id is not None
    assert rec.grade is Grade.NOT_ASSESSED
    assert rec.position is Position.SUPPORTED

    fetched = repo.get(rec.id)
    assert fetched.text == rec.text
    assert fetched.paragraph == "26.49"
    assert fetched.citation == "UPR, A/HRC/46/15, para. 26.49, (Switzerland)"


def test_position_parsing_variants():
    assert Recommendation(text="x", position="- Supported/Noted").position is Position.SUPPORTED_NOTED
    assert Recommendation(text="x", position="Noted").position is Position.NOTED
    assert Recommendation(text="x", position=None).position is Position.UNKNOWN


def test_set_grade_records_rationale_and_sources(repo):
    rec = repo.add(_sample())
    updated = repo.set_grade(
        rec.id, Grade.C,
        rationale="CRC still not ratified; no Senate action in the review period.",
        sources="A/HRC/WG.6/50/USA/2, para. 4",
    )
    assert updated.grade is Grade.C
    assert updated.grade.label.startswith("Not implemented")
    assert updated.assessment_rationale.startswith("CRC still not ratified")
    assert updated.assessment_sources == "A/HRC/WG.6/50/USA/2, para. 4"
    assert updated.assessed_at is not None


def test_add_many_is_idempotent_on_symbol_and_paragraph(repo):
    first = repo.add_many([_sample(), _sample(paragraph="26.50", text="Other")])
    assert first == 2
    again = repo.add_many([_sample(), _sample(paragraph="26.51", text="Third")])
    assert again == 1  # 26.49 already present, only 26.51 is new
    assert len(repo.list()) == 3


def test_list_filters(repo):
    a = repo.add(_sample(paragraph="26.1", position="Supported",
                         themes="Ratification of & accession to international instruments"))
    b = repo.add(_sample(paragraph="26.194", position="Noted", themes="Death penalty"))
    repo.set_grade(a.id, Grade.B)

    assert [r.id for r in repo.list(grade=Grade.B)] == [a.id]
    assert [r.id for r in repo.list(position=Position.NOTED)] == [b.id]
    assert [r.id for r in repo.list(theme="Death penalty")] == [b.id]
    assert [r.id for r in repo.list(paragraph="26.1")] == [a.id]


def test_invalid_grade_rejected_by_model():
    with pytest.raises(ValueError):
        Recommendation(text="x", grade="Z")


def test_check_constraint_guards_db(repo):
    with pytest.raises(sqlite3.IntegrityError):
        with repo.conn:
            repo.conn.execute(
                "INSERT INTO recommendations (text, grade) VALUES ('x', 'Z')"
            )


def test_count_by_grade(repo):
    repo.add_many([_sample(paragraph=f"26.{i}", text=f"r{i}") for i in range(5)])
    for rec in repo.list()[:2]:
        repo.set_grade(rec.id, Grade.A)
    counts = repo.count_by_grade()
    assert counts.get("A") == 2
    assert counts.get("not_assessed") == 3
