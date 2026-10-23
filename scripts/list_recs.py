"""Print a country's cycle-3 recommendations grouped by primary theme (for authoring assess.py)."""
import sqlite3, sys, collections
slug = sys.argv[1]; width = int(sys.argv[2]) if len(sys.argv) > 2 else 120
con = sqlite3.connect(f"countries/{slug}/{slug}.db")
by = collections.OrderedDict()
for pid, text, pos, th, st in con.execute("select paragraph,text,position,themes,recommending_state from recommendations order by id"):
    t = (th or "").split(";")[0].strip()
    by.setdefault(t, []).append((pid, pos, text, st))
for t, rs in sorted(by.items(), key=lambda kv: -len(kv[1])):
    print(f"## {t} ({len(rs)})")
    for pid, pos, text, st in rs:
        print(f"  {pid} [{pos[0]}] {text[:width].strip()}")
