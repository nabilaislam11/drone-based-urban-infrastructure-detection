#!/usr/bin/env python3
"""Validate the structure and local links of the academic research repository."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    "README.md",
    "CITATION.cff",
    "bestv8.pt",
    "docs/reproducibility-guide.md",
    "docs/research-overview.md",
]
for item in required:
    target = ROOT / item
    if not target.is_file():
        errors.append(f"Missing expected research artifact: {item}")
    elif target.stat().st_size == 0:
        errors.append(f"Empty research artifact: {item}")

notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
if len(notebooks) < 4:
    errors.append(f"Expected at least four research notebooks, found {len(notebooks)}")
for path in notebooks:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data.get("cells"), list) or not data.get("nbformat"):
            errors.append(f"Invalid Jupyter structure: {path.relative_to(ROOT)}")
    except (ValueError, UnicodeError) as exc:
        errors.append(f"Invalid notebook {path.relative_to(ROOT)}: {exc}")

link_pattern = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
for md in [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]:
    contents = md.read_text(encoding="utf-8")
    for raw in link_pattern.findall(contents):
        link = raw.split(" \"", 1)[0].strip().strip("<>")
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or not parsed.path or link.startswith("#"):
            continue
        dest = (md.parent / unquote(parsed.path)).resolve()
        try:
            dest.relative_to(ROOT)
        except ValueError:
            errors.append(f"Link outside repository: {md.relative_to(ROOT)} -> {link}")
            continue
        if not dest.exists():
            errors.append(f"Broken local link: {md.relative_to(ROOT)} -> {link}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Research checks passed: {len(notebooks)} notebooks and local Markdown links.")
