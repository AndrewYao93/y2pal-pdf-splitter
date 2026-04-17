#!/usr/bin/env python3
"""Create a conventional output directory structure for Y2Pal split PDFs.

Creates a directory tree for organizing downloaded split PDFs by category.
Useful for users who regularly split PDFs and want a consistent filing layout.

Usage:
    python3 scripts/setup_output_dir.py <base_path>
    python3 scripts/setup_output_dir.py <base_path> --preset legal
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

PRESETS: Dict[str, List[str]] = {
    "default": [
        "by-source",
        "by-date",
        "archive",
        "pending-review",
    ],
    "academic": [
        "textbooks/by-course",
        "papers/split-by-section",
        "lecture-notes/by-week",
        "archive",
    ],
    "legal": [
        "filings/by-case",
        "exhibits/split-by-number",
        "discovery/by-date",
        "archive",
    ],
    "finance": [
        "invoices/by-client",
        "statements/by-month",
        "receipts/by-year",
        "archive",
    ],
}


def create_output_structure(base_path: Path, preset: str) -> None:
    """Create the directory tree under base_path using the named preset."""
    if preset not in PRESETS:
        raise ValueError(f"unknown preset: {preset}. options: {', '.join(PRESETS)}")
    base_path.mkdir(parents=True, exist_ok=True)
    for rel in PRESETS[preset]:
        (base_path / rel).mkdir(parents=True, exist_ok=True)
        print(f"CREATED  {base_path / rel}")


def write_config(base_path: Path, preset: str) -> None:
    """Write a .y2pal-output.json marker for tooling to find the root."""
    config = {
        "preset": preset,
        "created_by": "setup_output_dir.py",
        "base_path": str(base_path.resolve()),
    }
    config_path = base_path / ".y2pal-output.json"
    config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")
    print(f"CONFIG   {config_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("base_path", type=Path, help="Root directory to create under")
    parser.add_argument(
        "--preset",
        choices=sorted(PRESETS),
        default="default",
        help="Which preset tree to create",
    )
    args = parser.parse_args()

    try:
        create_output_structure(args.base_path, args.preset)
        write_config(args.base_path, args.preset)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    print(f"\nDone. Base path: {args.base_path.resolve()}")
    print(f"Preset:    {args.preset}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
