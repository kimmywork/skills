#!/usr/bin/env bash
set -euo pipefail

if ! command -v cloudconvert >/dev/null 2>&1; then
    echo "cloudconvert CLI is not installed" >&2
    echo "Install after approval with: npm install -g cloudconvert-cli" >&2
    exit 1
fi

cloudconvert --version
