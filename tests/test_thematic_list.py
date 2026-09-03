"""Tests for the OHCHR thematic-list .docx parser, run against the real file
shipped in the project root."""

from pathlib import Path

import pytest

from recommendations import thematic_list as tl

DOCX = Path(__file__).resolve().parent.parent / (
    "UPR36_United_States_of_America_Thematic_List_of_Recommendations.docx"
)

pytestmark = pytest.mark.skipif(not DOCX.exists(), reason="thematic list docx not present")


@pytest.fixture(scope="module")
def rows():
    return tl.read_thematic_list(DOCX)


def test_parses_all_347_recommendations(rows):
    assert len(rows) == 347
    assert len({r["paragraph"] for r in rows}) == 347


def test_first_row_fields(rows):
    first = next(r for r in rows if r["paragraph"] == "26.1")
    assert first["text"] == "Consider ratifying all remaining human rights conventions"
    assert first["recommending_state"] == "Somalia"
    assert first["position"] == "Supported"
    assert first["primary_theme"] == "Ratification of & accession to international instruments"
    assert "A/HRC/46/15/Add.1" in first["position_source"]


def test_multi_state_recommendation(rows):
    r = next(r for r in rows if r["paragraph"] == "26.49")
    assert "Switzerland" in r["recommending_state"]
    assert "Morocco" in r["recommending_state"]


def test_noted_recommendations_present(rows):
    noted = [r for r in rows if r["position"] == "Noted"]
    assert len(noted) >= 60


def test_row_to_kwargs_defaults(rows):
    kw = tl.row_to_kwargs(rows[0])
    assert kw["document_symbol"] == "A/HRC/46/15"
    assert kw["cycle"] == 3
    assert kw["country"] == "United States of America"
    assert kw["themes"].startswith("Ratification of & accession to international instruments")
