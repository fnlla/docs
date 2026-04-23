#!/usr/bin/env python3
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
errors = []

for md in DOCS.rglob("*.md"):
    content = md.read_text(encoding="utf-8")
    for link in LINK_PATTERN.findall(content):
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue

        clean = link.split("#", 1)[0].strip()
        if clean == "":
            continue

        target = (md.parent / clean).resolve()
        if target.is_file() or target.is_dir():
            continue

        errors.append(f"{md}: broken relative link -> {link}")

if errors:
    print("Relative link validation failed:")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print("Relative link validation passed.")
