#!/usr/bin/env python3
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

FENCE = re.compile(r"^```")

errors = []

for md in DOCS.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    fence_count = sum(1 for line in text.splitlines() if FENCE.match(line.strip()))
    if fence_count % 2 != 0:
        errors.append(f"{md}: unmatched fenced code block markers")

    for match in re.finditer(r"```([a-zA-Z0-9_-]+)?\n(.*?)\n```", text, flags=re.DOTALL):
        snippet = match.group(2).strip()
        if snippet == "":
            errors.append(f"{md}: empty code fence")

if errors:
    print("Snippet validation failed:")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print("Snippet validation passed.")
