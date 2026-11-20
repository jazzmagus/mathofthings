#!/usr/bin/env python3
"""Insert the GoatCounter tag before </body> in every static HTML file. Idempotent."""
import re
import sys
from pathlib import Path

TAG = ('<script data-goatcounter="https://mathofthings.goatcounter.com/count"\n'
       '        async src="//gc.zgo.at/count.js"></script>\n')
ROOT = Path(__file__).resolve().parent.parent / "static"
dry = "--dry" in sys.argv

done = skipped = missing = 0
for path in sorted(ROOT.rglob("*.html")):
    text = path.read_text(encoding="utf-8", newline="")
    if "goatcounter" in text:
        skipped += 1
        continue
    matches = list(re.finditer(r"</body>", text, re.I))
    if not matches:
        print("no </body>:", path.relative_to(ROOT.parent))
        missing += 1
        continue
    i = matches[-1].start()
    if not dry:
        path.write_text(text[:i] + TAG + text[i:], encoding="utf-8", newline="")
    done += 1

print(f"{'would patch' if dry else 'patched'}: {done}, already ok: {skipped}, no body: {missing}")
