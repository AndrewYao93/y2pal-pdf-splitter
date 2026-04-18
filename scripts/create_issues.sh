#!/bin/bash
set -euo pipefail
# Batch-create GitHub Issues from the issues/ directory.
# Reads frontmatter from each issues/NN-slug.md file, extracts title and labels,
# then creates the Issue via `gh issue create`. Skips files without a valid title.
#
# Prerequisites:
#   - gh CLI authenticated (`gh auth login`)
#   - Run from the repository root
#
# Usage:
#   bash scripts/create_issues.sh                    # process every file
#   bash scripts/create_issues.sh --dry-run          # print what would be created
#   bash scripts/create_issues.sh --limit 5          # create at most 5 issues
#   bash scripts/create_issues.sh --skip 10 --limit 8   # skip first 10, then create next 8

DRY_RUN=0
LIMIT=0
SKIP=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN=1; shift ;;
        --limit)   LIMIT="$2"; shift 2 ;;
        --skip)    SKIP="$2"; shift 2 ;;
        *) echo "Unknown arg: $1" >&2; exit 1 ;;
    esac
done

if [[ ! -d issues ]]; then
    echo "Error: issues/ directory not found. Run from repo root." >&2
    exit 1
fi

index=0
created=0
for file in issues/*.md; do
    [[ -f "$file" ]] || continue
    index=$((index + 1))

    # Skip the first N files entirely
    if [[ "$index" -le "$SKIP" ]]; then
        continue
    fi

    # Stop once the limit is hit
    if [[ "$LIMIT" -gt 0 && "$created" -ge "$LIMIT" ]]; then
        echo "(limit $LIMIT reached)"
        break
    fi

    # Extract title (line beginning with `title:` in YAML frontmatter)
    title=$(awk '/^---$/{f=!f; next} f && /^title:/{sub(/^title:[[:space:]]*/,""); gsub(/^"|"$/,""); print; exit}' "$file")
    labels=$(awk '/^---$/{f=!f; next} f && /^labels:/{sub(/^labels:[[:space:]]*/,""); print; exit}' "$file")

    if [[ -z "$title" ]]; then
        echo "SKIP  $file (no title in frontmatter)"
        continue
    fi

    # Body: everything after the closing `---` of the frontmatter
    body=$(awk 'BEGIN{f=0} /^---$/{f++; next} f>=2 {print}' "$file")

    created=$((created + 1))
    echo "[$index] $title"

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
echo "Done. $created issue(s) created."
