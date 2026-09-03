"""SQLite connection helpers and schema management."""

from __future__ import annotations

import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB_PATH = PROJECT_ROOT / "recommendations.db"

# `grade` follows the adapted Human Rights Committee A-E scale (CCPR/C/108/2);
# see https://ccprcentre.org/follow-up-and-assessment
SCHEMA = """
CREATE TABLE IF NOT EXISTS recommendations (
    id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    text                 TEXT NOT NULL,
    country              TEXT NOT NULL DEFAULT 'United States of America',
    mechanism            TEXT NOT NULL DEFAULT 'UPR',
    cycle                INTEGER,
    session              TEXT,
    document_symbol      TEXT,
    paragraph            TEXT,
    recommending_state   TEXT,
    position             TEXT NOT NULL DEFAULT 'unknown'
        CHECK (position IN ('supported', 'noted', 'supported_noted', 'unknown')),
    themes               TEXT,
    affected_persons     TEXT,
    sdgs                 TEXT,
    date_issued          TEXT,
    annotation_id        TEXT UNIQUE,
    source_url           TEXT,
    grade                TEXT NOT NULL DEFAULT 'not_assessed'
        CHECK (grade IN ('not_assessed', 'A', 'B', 'C', 'D', 'E')),
    action_summary       TEXT,
    assessment_rationale TEXT,
    assessment_sources   TEXT,
    assessment_evidence  TEXT,
    assessed_at          TEXT,
    created_at           TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at           TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE (document_symbol, paragraph)
);

CREATE INDEX IF NOT EXISTS idx_recommendations_grade
    ON recommendations (grade);
CREATE INDEX IF NOT EXISTS idx_recommendations_paragraph
    ON recommendations (paragraph);
"""


def connect(db_path: str | Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """Open a connection with row access by column name and FK enforcement."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path: str | Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """Open a connection and create the schema if it does not exist yet."""
    conn = connect(db_path)
    with conn:
        conn.executescript(SCHEMA)
        _migrate(conn)
    return conn


def _migrate(conn: sqlite3.Connection) -> None:
    """Add columns introduced after a database was first created."""
    have = {row["name"] for row in conn.execute("PRAGMA table_info(recommendations)")}
    for column, ddl in (("assessment_evidence", "TEXT"), ("action_summary", "TEXT")):
        if column not in have:
            conn.execute(f"ALTER TABLE recommendations ADD COLUMN {column} {ddl}")
