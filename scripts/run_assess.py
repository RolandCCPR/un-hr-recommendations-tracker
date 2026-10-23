"""Run or verify a country's assess.py by slug (works for hyphenated folder names).

    python scripts/run_assess.py <slug>            # grade: DB + CSV
    python scripts/run_assess.py <slug> --verify   # check every quote is verbatim in the documents
"""
from __future__ import annotations

import importlib.util
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.countries import get  # noqa: E402


def load(slug: str):
    spec = importlib.util.spec_from_file_location(f"assess_{slug.replace('-', '_')}", ROOT / "countries" / slug / "assess.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def norm(s: str) -> str:
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u00ad", "").replace("\u2011", "-").replace("\u2010", "-")
    s = re.sub(r"-\s*\n\s*", "-", s)
    return re.sub(r"\s+", " ", s).strip()


def quotes(mod):
    for theme, (g, s, r, qs) in mod.CLUSTERS.items():
        for q in qs:
            yield f"cluster '{theme}'", q
    for pat, g, s, r, qs in mod.KEYWORDS:
        for q in qs:
            yield f"keyword /{pat[:40]}/", q
    fb = getattr(mod, "FALLBACK", None)
    if fb:
        for q in fb[3]:
            yield "fallback", q


def verify(slug: str) -> int:
    cfg = get(slug)
    mod = load(slug)
    texts = {}
    for k in ("1", "2", "3"):
        f = cfg["evidence_dir"] / f"A_HRC_WG.6_53_{cfg['code']}_{k}-EN.txt"
        if not f.exists():
            f = cfg["evidence_dir"] / f"A_HRC_WG.6_52_{cfg['code']}_{k}-EN.txt"
        texts[k] = norm(f.read_text(encoding="utf-8")) if f.exists() else None
    bad = 0
    n = 0
    for where, (org, doc, para, text) in quotes(mod):
        n += 1
        t = texts.get(doc)
        if t is None:
            print(f"  NO DOCUMENT {doc}: {where}: {text[:70]}")
            bad += 1
            continue
        for seg in re.split(r"\s*(?:\.\.\.|\u2026)\s*", norm(text)):
            seg = seg.strip(" .")
            if len(seg) > 3 and seg not in t:
                print(f"  NOT FOUND ({where}, doc {doc} para {para}): {seg[:100]}")
                bad += 1
    print(f"{slug}: {n} quotes checked, {bad} problems")
    return bad


if __name__ == "__main__":
    slug = sys.argv[1]
    if "--verify" in sys.argv:
        sys.exit(1 if verify(slug) else 0)
    mod = load(slug)
    from scripts.assess import run
    run(slug, clusters=mod.CLUSTERS, keywords=mod.KEYWORDS, fallback=getattr(mod, "FALLBACK", None))
