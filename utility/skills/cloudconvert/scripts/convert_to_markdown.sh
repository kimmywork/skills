#!/usr/bin/env bash
set -euo pipefail

usage() {
    echo "Usage: $0 <input-file> [output-directory] [--force]" >&2
}

[[ $# -ge 1 ]] || { usage; exit 1; }
input=$1
shift
output_dir=.
output_dir_set=false
force=false

for argument in "$@"; do
    if [[ "$argument" == "--force" ]]; then
        force=true
    elif [[ "$output_dir_set" == false ]]; then
        output_dir=$argument
        output_dir_set=true
    else
        usage
        exit 1
    fi
done

[[ -f "$input" ]] || { echo "Input file does not exist: $input" >&2; exit 1; }
command -v cloudconvert >/dev/null 2>&1 || { echo "cloudconvert CLI is not installed" >&2; exit 1; }
[[ -n "${CLOUDCONVERT_API_KEY:-}" ]] || { echo "CLOUDCONVERT_API_KEY is not set" >&2; exit 1; }

filename=$(basename "$input")
basename=${filename%.*}
output_dir=$(mkdir -p "$output_dir" && cd "$output_dir" && pwd)
output_file="$output_dir/$basename.md"

if [[ -e "$output_file" && "$force" == false ]]; then
    echo "Output already exists: $output_file" >&2
    echo "Re-run with --force only after overwrite approval." >&2
    exit 1
fi

if [[ "$force" == true ]]; then
    rm -f "$output_file"
fi

echo "Uploading to CloudConvert and converting: $input" >&2
cloudconvert convert -f md --output-dir "$output_dir" "$input"

[[ -s "$output_file" ]] || { echo "Conversion did not create a non-empty Markdown file: $output_file" >&2; exit 1; }
printf '%s\n' "$output_file"
