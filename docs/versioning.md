# Documentation Versioning

FNLLA docs use major-line folders under `docs/`.

## Current Convention

- Active line: `docs/1.x/`
- Next line example: `docs/2.x/`

## Create New Docs Line

Run from repository root:

```bash
bash scripts/new-version.sh 2.x
```

This copies the current active line as baseline for the new one.

## Navigation Update

After creating a new line:

1. Add nav entries in `mkdocs.yml`.
2. Update landing docs to mention supported lines.
3. Add migration notes between lines.

## Quality Gates

`docs-ci` enforces:

- snippet structure validation,
- internal relative link validation,
- strict MkDocs build.
