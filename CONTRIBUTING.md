# Contributing

Thank you for your interest in improving Y2Pal PDF Splitter.

This repository hosts documentation, helper scripts, and community resources for the Y2Pal PDF Splitter online tool. The core service itself is a hosted product; contributions focus on docs, scripts, and community support.

## How to Contribute

### Reporting Bugs

[Open an issue](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=bug_report.md) with:

- Browser name and exact version.
- Operating system and version.
- The split mode used (page range / bookmark / every N pages).
- Source PDF characteristics (size, page count, encrypted, scanned, born-digital).
- Steps to reproduce.
- Expected vs actual behavior.
- Screenshots (remove identifying info first).

### Requesting Features

[Submit a feature request](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=feature_request.md) describing:

- The problem you're trying to solve.
- Your proposed solution.
- Alternatives you've considered.
- Approximate usage volume (helps prioritize).

### Improving Documentation

1. Fork this repository.
2. Edit the relevant Markdown file in `README.md`, `docs/`, or `issues/`.
3. Submit a pull request with a short description of the change.

Documentation PRs are especially welcome for:

- Clarifications to existing guides.
- Adding use-case examples for specific industries.
- Translations (the `docs/` folder is English-only; per-language repos are separate).

### Helper Scripts

The `scripts/` directory contains community-maintained utilities:

- `check_version.py` — GitHub API release checker.
- `download_helper.py` — verify, organize, and report on downloaded PDFs.
- `install.sh` — one-command browser launch for the tool.
- `setup_output_dir.py` — create a filing-system directory tree for split output.
- `create_issues.sh` — batch-create repository Issues from `issues/*.md`.

Contributions welcome for:

- Integrations with cloud drives (fetch from Dropbox / Google Drive / OneDrive).
- File-organization workflows for specific industries (legal exhibit numbering, academic citation format).
- Build helpers for generating per-language variants of this repository.

## Code Style

**Python** (`scripts/*.py`): PEP 8, docstrings, type hints, Python 3.8+.

**Shell** (`scripts/*.sh`): `#!/bin/bash` with `set -euo pipefail`, usage comments, macOS + Linux compatible (Windows via Git Bash or WSL).

**Markdown** (`docs/`, `issues/`): GitHub-flavored Markdown, sentence-per-line for clean diffs, tables for structured comparisons.

## What's Not Accepted

- Pull requests adding marketing language or promotional copy to README/docs.
- PRs that add specific prices or discount codes.
- PRs that increase external link count above the documented limits.

## Questions?

Open a [question issue](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=faq-question.md) or email `contact@y2pal.com`.
