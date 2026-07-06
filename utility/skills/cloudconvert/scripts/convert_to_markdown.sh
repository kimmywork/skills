#!/bin/bash

# Document to Markdown converter using CloudConvert
# Usage: convert_to_markdown.sh <input_file> [output_dir]

set -e

INPUT_FILE="$1"
OUTPUT_DIR="${2:-.}"

if [ -z "$INPUT_FILE" ]; then
    echo "Usage: $0 <input_file> [output_dir]"
    echo ""
    echo "Converts documents (PDF, DOC, DOCX, EPUB, etc.) to Markdown"
    echo ""
    echo "Examples:"
    echo "  $0 document.pdf"
    echo "  $0 document.docx /output/path"
    exit 1
fi

if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: File '$INPUT_FILE' does not exist"
    exit 1
fi

# Check if CLOUDCONVERT_API_KEY is set
if [ -z "$CLOUDCONVERT_API_KEY" ]; then
    echo "Error: CLOUDCONVERT_API_KEY environment variable is not set"
    echo ""
    echo "Please set your API key:"
    echo "1. Get your API key from: https://cloudconvert.com/dashboard/api/v2/keys"
    echo "2. Set it as an environment variable:"
    echo "   export CLOUDCONVERT_API_KEY=your_key_here"
    exit 1
fi

# Get the file extension and base name
FILENAME=$(basename "$INPUT_FILE")
BASENAME="${FILENAME%.*}"
EXTENSION="${FILENAME##*.}"

echo "Converting $INPUT_FILE to Markdown..."

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Use cloudconvert to convert to markdown
cloudconvert convert -f md --output-dir "$OUTPUT_DIR" "$INPUT_FILE"

OUTPUT_FILE="$OUTPUT_DIR/$BASENAME.md"

if [ -f "$OUTPUT_FILE" ]; then
    echo "✓ Conversion successful: $OUTPUT_FILE"
else
    echo "✗ Conversion failed"
    exit 1
fi