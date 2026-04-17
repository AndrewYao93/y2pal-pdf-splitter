#!/usr/bin/env python3
"""Check the latest Y2Pal PDF Splitter release on GitHub.

Queries the GitHub Releases API and prints the most recent release's
tag, title, publish date, and URL. Useful for scripting version checks
or for notifying users when the server-side build has advanced.

Usage:
    python3 scripts/check_version.py
    python3 scripts/check_version.py --json
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from typing import Optional, TypedDict

REPO = "AndrewYao93/y2pal-pdf-splitter"
API_URL = f"https://api.github.com/repos/{REPO}/releases/latest"


class Release(TypedDict):
    version: str
    name: str
    published: str
    url: str


def get_latest_release() -> Optional[Release]:
    """Fetch the latest release metadata from the GitHub API."""
    req = urllib.request.Request(
        API_URL,
        headers={
            "User-Agent": "y2pal-pdf-splitter-version-check",
            "Accept": "application/vnd.github+json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}", file=sys.stderr)
        return None
    except urllib.error.URLError as e:
        print(f"Network error: {e.reason}", file=sys.stderr)
        return None
    except (KeyError, ValueError) as e:
        print(f"Parse error: {e}", file=sys.stderr)
        return None

    return {
        "version": data["tag_name"],
        "name": data.get("name") or data["tag_name"],
        "published": data["published_at"][:10],
        "url": data["html_url"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    release = get_latest_release()
    if release is None:
        print("Could not fetch release information.", file=sys.stderr)
        return 1

    if args.json:
        json.dump(release, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print(f"Latest: {release['version']} ({release['published']})")
        print(f"Name:   {release['name']}")
        print(f"URL:    {release['url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
