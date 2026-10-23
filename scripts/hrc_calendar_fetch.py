"""Download every Human Rights Committee concluding-observations (CO) document.

For each country code the script probes the OHCHR Treaty Body Database
(`Download.aspx?symbolno=CCPR/C/<A3>/CO/<n>`) for n = 1, 2, ... and saves the
English file of each CO that exists.  Raw files go to the cache directory
(given on the command line; not part of the repository) and a manifest
`manifest.json` records what was found.

    python scripts/hrc_calendar_fetch.py <cache_dir> [A3 A3 ...]
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = "https://tbinternet.ohchr.org/_layouts/15/treatybodyexternal/Download.aspx?symbolno={sym}&Lang=en"
STORE = "https://docstore.ohchr.org/SelfServices/"
LINK_RE = re.compile(r'FilesHandler\.ashx\?enc=[^"\']+')
MAX_N = 12


def get(url: str, tries: int = 3) -> bytes | None:
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception:
            time.sleep(1.5 * (i + 1))
    return None


def links(symbol: str) -> list[str]:
    html = get(PAGE.format(sym=urllib.parse.quote(symbol, safe="")))
    if not html:
        return []
    return [STORE + l for l in LINK_RE.findall(html.decode("utf-8", "replace"))]


def kind(blob: bytes) -> str:
    if blob[:4] == b"PK\x03\x04":
        return "docx"
    if blob[:4] == b"\xd0\xcf\x11\xe0":
        return "doc"
    if blob[:4] == b"%PDF":
        return "pdf"
    return "other"


def fetch_country(a3: str, cache: Path) -> dict:
    found = []
    for n in range(1, MAX_N + 1):
        # the plain symbol, and the "/Add.1" form used when the first CO of a
        # State was an absence-of-report document (e.g. Belize, Cabo Verde)
        for sym in (f"CCPR/C/{a3}/CO/{n}", f"CCPR/C/{a3}/CO/{n}/Add.1"):
            ls = links(sym)
            if not ls:
                continue
            blob = get(ls[0])  # index 0 is the English file
            if not blob:
                found.append({"n": n, "symbol": sym, "file": None})
                continue
            ext = kind(blob)
            fn = f"{a3}_{sym.split('/CO/')[1].replace('/', '_')}.{ext}"
            (cache / fn).write_bytes(blob)
            found.append({"n": n, "symbol": sym, "file": fn, "kind": ext, "links": len(ls)})
    return {"a3": a3, "cos": found}


def main() -> None:
    cache = Path(sys.argv[1])
    cache.mkdir(parents=True, exist_ok=True)
    codes = sys.argv[2:] or [c["a3"] for c in json.loads(
        (ROOT / "site/public/data/countries.json").read_text(encoding="utf-8"))] + [
        "CHN-HKG", "CHN-MAC"]  # Hong Kong and Macau have their own CO symbols
    with ThreadPoolExecutor(max_workers=6) as ex:
        res = list(ex.map(lambda c: fetch_country(c, cache), codes))
    (cache / "manifest.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    hit = [r for r in res if r["cos"]]
    print(f"{len(codes)} codes probed, {len(hit)} with at least one CO, "
          f"{sum(len(r['cos']) for r in hit)} documents")


if __name__ == "__main__":
    main()
