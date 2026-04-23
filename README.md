# FNLLA Documentation

Official documentation repository for the FNLLA ecosystem.

## Why This Repository Exists

`fnlla/docs` is a dedicated public docs repository, separated from framework runtime code.
This keeps documentation releases, contribution flow, and publishing lifecycle independent.

## Scope

- Product documentation for application teams.
- Framework guides for engineers.
- Operations and deployment references.
- Versioned docs (`1.x`, upcoming `2.x`, etc.).

## Local Development

1. Install Python 3.11+.
2. Install docs dependencies:
   ```bash
   pip install mkdocs mkdocs-material
   ```
3. Start docs server:
   ```bash
   mkdocs serve
   ```
4. Open `http://127.0.0.1:8000`.

## Repository Layout

- `docs/` markdown source files
- `mkdocs.yml` docs structure and theme
- `.github/workflows/` CI and Pages deploy pipelines

## Governance

- Security policy: see `.github/SECURITY.md` in org defaults.
- Contribution standards: pull requests + review gates.
- Docs changes can ship independently from framework releases.
