"""Set the headline, fill the Word list and write the report for a graded country.

    python scripts/finish_country.py <slug> "<headline>"
"""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
slug, headline = sys.argv[1], sys.argv[2]
py = sys.executable
subprocess.run([py, str(ROOT / "scripts/set_headline.py"), slug, headline], check=True)
env = {**__import__("os").environ, "PYTHONPATH": str(ROOT), "PYTHONIOENCODING": "utf-8"}
subprocess.run([py, "-m", "scripts.fill_thematic_list", slug], check=True, cwd=ROOT, env=env)
subprocess.run([py, "-m", "scripts.make_report", slug], check=True, cwd=ROOT, env=env)
