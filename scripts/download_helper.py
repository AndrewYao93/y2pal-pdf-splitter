#!/usr/bin/env python3
"""Local utilities for managing split PDFs downloaded from Y2Pal PDF Splitter.

After splitting a large PDF into many output files, users often want to verify
the downloads, organize them by date, and check disk usage. This script bundles
those utilities in one place.

Usage:
    python3 scripts/download_helper.py verify <directory>
    python3 scripts/download_helper.py organize <directory>
    python3 scripts/download_helper.py report <directory>
    python3 scripts/download_helper.py check-space <path> [--min-gb N]
"""

from __future__ import annotations

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path

PDF_MIN_BYTES = 67  # Smallest possible valid PDF per the spec
PDF_SIGNATURE = b"%PDF-"


def verify_download(filepath: Path) -> tuple[bool, str]:
    """Return (is_valid, reason) for a single PDF file."""
    if not filepath.exists():
        return False, "file does not exist"
    if filepath.stat().st_size < PDF_MIN_BYTES:
        return False, f"file too small ({filepath.stat().st_size} bytes)"
    if filepath.suffix.lower() != ".pdf":
        return False, f"unexpected extension: {filepath.suffix}"
    with filepath.open("rb") as fh:
        head = fh.read(5)
    if head != PDF_SIGNATURE:
        return False, "missing PDF signature header"
    return True, "ok"


def verify_directory(directory: Path) -> int:
    """Verify every .pdf in a directory. Returns process exit code."""
    pdfs = sorted(directory.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {directory}")
        return 1
    failures = 0
    for pdf in pdfs:
        ok, reason = verify_download(pdf)
        marker = "OK " if ok else "BAD"
        print(f"{marker}  {pdf.name}: {reason}")
        if not ok:
            failures += 1
    print(f"\n{len(pdfs) - failures} / {len(pdfs)} files valid")
    return 0 if failures == 0 else 2


def organize_by_date(directory: Path) -> int:
    """Move each PDF into a YYYY-MM-DD subfolder based on mtime."""
    pdfs = sorted(directory.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {directory}")
        return 1
    moved = 0
    for pdf in pdfs:
        date_str = datetime.fromtimestamp(pdf.stat().st_mtime).strftime("%Y-%m-%d")
        target_dir = directory / date_str
        target_dir.mkdir(exist_ok=True)
        target = target_dir / pdf.name
        if target.exists():
            print(f"SKIP  {pdf.name} (exists in {date_str}/)")
            continue
        pdf.rename(target)
        moved += 1
        print(f"MOVE  {pdf.name} -> {date_str}/")
    print(f"\nOrganized {moved} file(s).")
    return 0


def generate_report(directory: Path) -> int:
    """Print a summary table for a directory of PDFs."""
    pdfs = sorted(directory.glob("**/*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {directory}")
        return 1
    total_bytes = sum(p.stat().st_size for p in pdfs)
    print(f"Directory: {directory}")
    print(f"Files:     {len(pdfs)}")
    print(f"Total:     {total_bytes / (1024 * 1024):.2f} MB")
    print(f"Avg size:  {total_bytes / len(pdfs) / 1024:.1f} KB")
    print(f"Largest:   {max(pdfs, key=lambda p: p.stat().st_size).name}")
    print(f"Smallest:  {min(pdfs, key=lambda p: p.stat().st_size).name}")
    return 0


def check_disk_space(path: Path, min_gb: float) -> int:
    """Verify at least `min_gb` of free space under `path`."""
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    print(f"Path:   {path}")
    print(f"Free:   {free_gb:.2f} GB")
    print(f"Needed: {min_gb:.2f} GB")
    return 0 if free_gb >= min_gb else 3


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    sub_verify = sub.add_parser("verify", help="Verify PDFs in a directory")
    sub_verify.add_argument("directory", type=Path)

    sub_org = sub.add_parser("organize", help="Move PDFs into YYYY-MM-DD subfolders")
    sub_org.add_argument("directory", type=Path)

    sub_report = sub.add_parser("report", help="Print directory statistics")
    sub_report.add_argument("directory", type=Path)

    sub_space = sub.add_parser("check-space", help="Check free disk space")
    sub_space.add_argument("path", type=Path)
    sub_space.add_argument("--min-gb", type=float, default=1.0)

    args = parser.parse_args()

    if args.command == "verify":
        return verify_directory(args.directory)
    if args.command == "organize":
        return organize_by_date(args.directory)
    if args.command == "report":
        return generate_report(args.directory)
    if args.command == "check-space":
        return check_disk_space(args.path, args.min_gb)
    return 1


if __name__ == "__main__":
    sys.exit(main())
