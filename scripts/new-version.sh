#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: bash scripts/new-version.sh <version-folder>"
  echo "Example: bash scripts/new-version.sh 2.x"
  exit 1
fi

target="$1"
source="docs/1.x"
destination="docs/${target}"

if [[ ! -d "$source" ]]; then
  echo "Source docs line not found: $source"
  exit 1
fi

if [[ -e "$destination" ]]; then
  echo "Destination already exists: $destination"
  exit 1
fi

cp -R "$source" "$destination"
echo "Created new docs line at $destination"
