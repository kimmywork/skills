#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${CLOUDCONVERT_API_KEY:-}" ]]; then
    echo "CLOUDCONVERT_API_KEY is not set." >&2
    echo "Create a key at https://cloudconvert.com/dashboard/api/v2/keys and export it in your shell environment." >&2
    exit 1
fi

echo "CLOUDCONVERT_API_KEY is set"
