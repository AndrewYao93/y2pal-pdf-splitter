#!/bin/bash
set -euo pipefail
# Y2Pal PDF Splitter "installer" — opens the browser-based tool in the default browser.
# Because this is a cloud service, there is nothing to install locally; this script
# is a convenience wrapper so CLI-first users can launch the tool with one command.

URL="https://y2pal.com/split-pdf"
OS="$(uname -s)"

open_url() {
    local url="$1"
    case "$OS" in
        Darwin)
            open "$url"
            ;;
        Linux)
            if command -v xdg-open >/dev/null 2>&1; then
                xdg-open "$url"
            elif command -v gnome-open >/dev/null 2>&1; then
                gnome-open "$url"
            else
                echo "No URL opener found. Visit manually: $url"
                return 1
            fi
            ;;
        MINGW*|MSYS*|CYGWIN*)
            start "$url"
            ;;
        *)
            echo "Unknown OS: $OS. Visit manually: $url"
            return 1
            ;;
    esac
}

main() {
    echo "Y2Pal PDF Splitter is a browser-based tool — no local install required."
    echo "Opening $URL ..."
    if open_url "$URL"; then
        echo "Done. If the browser did not open automatically, visit $URL manually."
    else
        exit 1
    fi
}

main "$@"
