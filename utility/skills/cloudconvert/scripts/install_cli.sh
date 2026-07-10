#!/usr/bin/env bash
set -euo pipefail

if command -v cloudconvert >/dev/null 2>&1; then
    cloudconvert --version
    exit 0
fi

if ! command -v npm >/dev/null 2>&1; then
    echo "npm is required. Install Node.js/npm first." >&2
    exit 1
fi

if [[ "${1:-}" != "--yes" ]]; then
    printf 'This will run a global installation: npm install -g cloudconvert-cli\nContinue? [y/N] '
    read -r answer
    case "$answer" in
        y|Y|yes|YES) ;;
        *) echo "Installation cancelled"; exit 1 ;;
    esac
fi

npm install -g cloudconvert-cli
cloudconvert --version
