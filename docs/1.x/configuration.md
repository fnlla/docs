# Configuration

Configuration is stored in `config/` and grouped by domain.

Recommended process:

1. Keep environment-specific values in `.env`.
2. Keep secure defaults in code.
3. Validate critical settings in CI and startup checks.
