#!/bin/bash
set -euo pipefail
# Batch-create all GitHub Issues from the issues/ directory.
# Reads frontmatter from each issues/NN-slug.md file, extracts title and labels,
# then creates the Issue via `gh issue create`. Skips files that error.
#
# Prerequisites:
#   - gh CLI authenticated (`gh auth login`)
#   - Run from the repository root
#
# Usage:
#   bash scripts/create_issues.sh
#   bash scripts/create_issues.sh --dry-run
#   bash scripts/create_issues.sh --limit 5       # create only the first 5 files

DRY_RUN=0
LIMIT=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN=1; shift ;;
        --limit) LIMIT="$2"; shift 2 ;;
        *) echo "Unknown arg: $1" >&2; exit 1 ;;
    esac
done

if [[ ! -d issues ]]; then
    echo "Error: issues/ directory not found. Run from repo root." >&2
    exit 1
fi

count=0
for file in issues/*.md; do
    [[ -f "$file" ]] || continue

    # Extract title (line beginning with `title:` in YAML frontmatter)
    title=$(awk '/^---$/{f=!f; next} f && /^title:/{sub(/^title:[[:space:]]*/,""); gsub(/^"|"$/,""); print; exit}' "$file")
    labels=$(awk '/^---$/{f=!f; next} f && /^labels:/{sub(/^labels:[[:space:]]*/,""); print; exit}' "$file")

    if [[ -z "$title" ]]; then
        echo "SKIP  $file (no title in frontmatter)"
        continue
    fi

    # Body: everything after the closing `---` of the frontmatter
    body=$(awk 'BEGIN{f=0} /^---$/{f++; next} f>=2 {print}' "$file")

    count=$((count + 1))
    if [[ "$LIMIT" -gt 0 && "$count" -gt "$LIMIT" ]]; then
        echo "(limit $LIMIT reached)"
        break
    fi

    echo "[$count] $title"

    if [[ "$DRY_RUN" -eq 1 ]]; then
        echo "       DRY: would create with labels=$labels"
        continue
    fi

    gh issue create \
        --title "$title" \
        --body "$body" \
        ${labels:+--label "$labels"}
done

echo ""
echo "Done. $count issue file(s) processed."
