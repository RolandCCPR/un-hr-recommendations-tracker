"""Set the report headline of a country in scripts/countries.py:  python scripts/set_headline.py <slug> "<text>" """
import sys
from pathlib import Path

p = Path(__file__).resolve().parent / "countries.py"
s = p.read_text(encoding="utf-8")
slug, text = sys.argv[1], sys.argv[2]
i = s.index(f'    "{slug}": dict(')
j = s.index("\n    ),\n", i)
k = s.index("        headline=", i, j)
e = s.index("\n", k)
s = s[:k] + "        headline=" + repr(text) + "," + s[e:]
p.write_text(s, encoding="utf-8")
print("headline set for", slug)
