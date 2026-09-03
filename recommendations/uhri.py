"""Read a Universal Human Rights Index (UHRI) ``.xlsx`` export with no
third-party dependencies (``zipfile`` + ``xml.etree`` only).

UHRI: https://uhri.ohchr.org  --  "Export to Excel" on a search result.
"""

from __future__ import annotations

import re
import zipfile
from datetime import date, timedelta
from pathlib import Path
from xml.etree import ElementTree as ET

_NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
_CELL_RE = re.compile(r"^([A-Z]+)(\d+)$")
_PARA_RE = re.compile(r"^\s*(\d+(?:\.\d+)+)\b")
_EXCEL_EPOCH = date(1899, 12, 30)  # accounts for the Lotus 1900 leap-year bug


def _col_to_index(col: str) -> int:
    n = 0
    for ch in col:
        n = n * 26 + (ord(ch) - ord("A") + 1)
    return n - 1


def _cell_text(text: str | None) -> str:
    return "" if text is None else text


def read_export(path: str | Path) -> list[dict[str, str]]:
    """Return the sheet as a list of ``{header: value}`` dicts (row 1 = header)."""
    with zipfile.ZipFile(path) as zf:
        shared = _read_shared_strings(zf)
        sheet_name = next(
            n for n in zf.namelist()
            if n.startswith("xl/worksheets/") and n.endswith(".xml")
        )
        with zf.open(sheet_name) as fh:
            tree = ET.parse(fh)

    rows: list[list[str]] = []
    width = 0
    for row_el in tree.iterfind(f".//{_NS}sheetData/{_NS}row"):
        cells: dict[int, str] = {}
        for c in row_el.iterfind(f"{_NS}c"):
            ref = c.get("r", "")
            m = _CELL_RE.match(ref)
            idx = _col_to_index(m.group(1)) if m else len(cells)
            ctype = c.get("t")
            if ctype == "s":
                v = c.findtext(f"{_NS}v")
                value = shared[int(v)] if v is not None else ""
            elif ctype == "inlineStr":
                value = "".join(
                    _cell_text(t.text) for t in c.iterfind(f".//{_NS}t")
                )
            else:
                value = _cell_text(c.findtext(f"{_NS}v"))
            cells[idx] = value
        width = max(width, (max(cells) + 1) if cells else 0)
        rows.append([cells.get(i, "") for i in range(width)])

    if not rows:
        return []
    headers = [h.strip() for h in rows[0]]
    headers += [f"col{i}" for i in range(len(headers), width)]
    out = []
    for raw in rows[1:]:
        raw = raw + [""] * (len(headers) - len(raw))
        out.append({headers[i]: raw[i] for i in range(len(headers))})
    return out


def _read_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    with zf.open("xl/sharedStrings.xml") as fh:
        tree = ET.parse(fh)
    strings = []
    for si in tree.iterfind(f"{_NS}si"):
        strings.append("".join(_cell_text(t.text) for t in si.iterfind(f".//{_NS}t")))
    return strings


def _clean(value: str | None) -> str | None:
    """Trim a single-valued UHRI cell (``- Foo`` -> ``Foo``)."""
    if value is None:
        return None
    v = value.strip()
    if v.startswith("-"):
        v = v[1:].strip()
    return v or None


def _clean_list(value: str | None) -> str | None:
    """Normalise a multi-line UHRI cell into newline-separated bullet-free lines."""
    if not value:
        return None
    lines = [ln.strip().lstrip("-").strip() for ln in value.splitlines()]
    lines = [ln for ln in lines if ln]
    return "\n".join(lines) or None


def _excel_serial_to_iso(value: str | None) -> str | None:
    if not value:
        return None
    try:
        serial = float(value)
    except ValueError:
        return None
    return (_EXCEL_EPOCH + timedelta(days=int(serial))).isoformat()


def extract_paragraph(text: str) -> str | None:
    m = _PARA_RE.match(text or "")
    return m.group(1) if m else None


# Maps a UHRI export row to Recommendation kwargs. Imported lazily by callers
# that already have the models module.
def row_to_kwargs(
    row: dict[str, str],
    *,
    cycle: int | None = None,
    source_url: str | None = None,
) -> dict:
    text = (row.get("Text") or "").strip()
    session = _clean(row.get("UPR Session"))
    if session:
        session = session.replace(" Session", "").strip()
    return dict(
        text=text,
        country=_clean(row.get("Countries Concerned")) or "United States of America",
        mechanism=_clean(row.get("Reccomending Body")) or "UPR",
        cycle=cycle,
        session=session,
        document_symbol=_clean(row.get("Document Symbol")),
        paragraph=extract_paragraph(text),
        recommending_state=_clean(row.get("UPR Reccomending States")),
        position=_clean(row.get("UPR Position")),
        themes=_clean_list(row.get("Themes")),
        affected_persons=_clean_list(row.get("Affected Persons")),
        sdgs=_clean_list(row.get("Sdgs")),
        date_issued=_excel_serial_to_iso(row.get("Document Publication Date")),
        annotation_id=_clean(row.get("OHCHR Annotation Id")),
        source_url=source_url,
    )
