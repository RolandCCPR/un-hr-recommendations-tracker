"""Read an OHCHR "Thematic List of Recommendations" ``.docx`` (the table with
columns: Recommendation | Position | Full list of themes | Assessment...).

Dependency-free: ``zipfile`` + ``xml.etree`` only.
"""

from __future__ import annotations

import re
import shutil
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
_PARA_RE = re.compile(r"^(\d+(?:\.\d+)+)\s*(.*)$", re.DOTALL)
_SRC_RE = re.compile(r"Source of Position:\s*(.*)$", re.IGNORECASE | re.DOTALL)
_STATE_TAIL_RE = re.compile(r"\s*((?:\([^()]+\)\s*)+);?\s*$")
# literal "&nbsp;" plus assorted non-breaking / zero-width spaces seen in source
_NBSP_RE = re.compile(r"(?:&nbsp;|[\xa0  ​﻿])+")


def _text_of(el) -> str:
    raw = "".join(t.text or "" for t in el.iter(_W + "t"))
    return _NBSP_RE.sub(" ", raw)


def _read_document_xml(docx_path: str | Path) -> bytes:
    try:
        with zipfile.ZipFile(docx_path) as zf:
            return zf.read("word/document.xml")
    except PermissionError:
        # Word / OneDrive can hold a read lock on the file; read from a copy.
        tmp = Path(tempfile.gettempdir()) / "thematic_list_copy.docx"
        shutil.copy2(docx_path, tmp)
        with zipfile.ZipFile(tmp) as zf:
            return zf.read("word/document.xml")


def _iter_table_rows(docx_path: str | Path):
    root = ET.fromstring(_read_document_xml(docx_path))
    for tbl in root.iter(_W + "tbl"):
        for tr in tbl.findall(_W + "tr"):
            cells = [
                " ".join(
                    _text_of(p).strip() for p in tc.findall(_W + "p")
                ).strip()
                for tc in tr.findall(_W + "tc")
            ]
            yield cells


def _split_themes_blob(blob: str) -> tuple[str | None, str | None, str | None]:
    """Split 'themes ... SDGs: ... Affected persons: ...' into three fields."""
    affected = None
    sdgs = None
    m = re.search(r"Affected persons:\s*", blob, re.IGNORECASE)
    if m:
        affected = blob[m.end():].strip() or None
        blob = blob[: m.start()].strip()
    m = re.search(r"SDGs:\s*", blob, re.IGNORECASE)
    if m:
        sdgs = blob[m.end():].strip() or None
        blob = blob[: m.start()].strip()
    themes = _norm_bullets(blob)
    return themes, _norm_bullets(sdgs), _norm_bullets(affected)


def _norm_bullets(s: str | None) -> str | None:
    if not s:
        return None
    parts = [p.strip() for p in re.split(r"\s*-\s+", s) if p.strip()]
    return "; ".join(parts) or None


def _parse_recommendation_cell(cell: str) -> dict:
    """'26.1 Consider ... (Somalia); Source of Position: A/HRC/46/15/Add.1 - Para.20'"""
    cell = _NBSP_RE.sub(" ", cell).strip()

    position_source = None
    m = _SRC_RE.search(cell)
    if m:
        position_source = re.sub(r"\s+", " ", m.group(1)).strip()
        cell = cell[: m.start()].strip()

    paragraph = None
    body = cell
    m = _PARA_RE.match(cell)
    if m:
        paragraph, body = m.group(1), m.group(2).strip()

    states: list[str] = []
    m = _STATE_TAIL_RE.search(body)
    if m:
        states = re.findall(r"\(([^()]+)\)", m.group(1))
        body = body[: m.start()].strip()
    body = body.rstrip(";").strip()

    return {
        "paragraph": paragraph,
        "text": re.sub(r"\s+", " ", body).strip(),
        "recommending_state": "; ".join(s.strip() for s in states) or None,
        "position_source": position_source,
    }


def read_thematic_list(docx_path: str | Path) -> list[dict]:
    """Return one dict per recommendation row, in document order, each carrying
    its primary ``theme`` (from the preceding 'Theme:' heading row)."""
    rows: list[dict] = []
    current_theme: str | None = None
    for cells in _iter_table_rows(docx_path):
        nonempty = [c for c in cells if c]
        if not nonempty:
            continue
        first = nonempty[0]
        if first.lower().startswith("theme:"):
            current_theme = first.split(":", 1)[1].strip()
            continue
        if first.lower().startswith("recommendation") and len(nonempty) > 1:
            continue  # header row
        if not re.match(r"^\d+\.\d+", first):
            continue

        parsed = _parse_recommendation_cell(cells[0])
        position = (cells[1].strip() if len(cells) > 1 else "") or None
        themes, sdgs, affected = _split_themes_blob(
            cells[2] if len(cells) > 2 else ""
        )
        existing_assessment = (cells[3].strip() if len(cells) > 3 else "") or None
        rows.append(
            {
                **parsed,
                "primary_theme": current_theme,
                "position": position,
                "themes": themes,
                "sdgs": sdgs,
                "affected_persons": affected,
                "existing_assessment": existing_assessment,
            }
        )
    return rows


def row_to_kwargs(
    row: dict,
    *,
    country: str = "United States of America",
    cycle: int | None = 3,
    session: str | None = "36th",
    document_symbol: str | None = "A/HRC/46/15",
    date_issued: str | None = "2020-12-15",
    source_url: str | None = None,
) -> dict:
    themes = row.get("themes")
    if row.get("primary_theme"):
        themes = row["primary_theme"] + (f"; {themes}" if themes else "")
    return dict(
        text=row["text"],
        country=country,
        mechanism="UPR",
        cycle=cycle,
        session=session,
        document_symbol=document_symbol,
        paragraph=row.get("paragraph"),
        recommending_state=row.get("recommending_state"),
        position=row.get("position"),
        themes=themes,
        affected_persons=row.get("affected_persons"),
        sdgs=row.get("sdgs"),
        date_issued=date_issued,
        annotation_id=None,
        source_url=source_url,
    )
