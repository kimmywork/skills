---
name: cloudconvert
description: "Convert non-text documents (PDF, DOC/DOCX, EPUB) to Markdown via CloudConvert CLI to save processing tokens. Skip .txt/.md/.json/.csv which are already agent-readable."
metadata:
  author: "Kimmy Liu"
  version: "1.1"
---

# CloudConvert Document Conversion

## Overview
Convert documents to Markdown using CloudConvert CLI for efficient text-based processing of complex document formats (PDF, DOC/DOCX, EPUB, etc.).

## Quick Start

### 1. Check Environment
First, verify the CloudConvert CLI is installed and API key is set:

```bash
# Check and install CLI
./scripts/check_and_install.sh

# Check API key
./scripts/check_api_key.sh
```

### 2. Convert Documents
Convert any supported document to Markdown:

```bash
# Basic conversion
./scripts/convert_to_markdown.sh document.pdf

# Convert to specific output directory
./scripts/convert_to_markdown.sh document.docx /output/path
```

## Workflow Decision Tree

### When to Use This Skill
- **User asks to "process", "read", "query", or "analyze" a document**
- **Document is in complex format (PDF, DOC/DOCX, EPUB, etc.)**
- **Need to save processing tokens by converting to Markdown first**

### Document Conversion Process

1. **Check Environment**
   - Verify CloudConvert CLI is installed (`./scripts/check_and_install.sh`)
   - Verify API key is set (`./scripts/check_api_key.sh`)

2. **Convert Document**
   - Use `./scripts/convert_to_markdown.sh` to convert to Markdown
   - Output file will be saved with `.md` extension

3. **Process Markdown**
   - Use the generated Markdown file for further processing
   - Delete temporary files if needed

## Supported Formats

### Input Formats
- PDF (`.pdf`)
- Microsoft Word (`.doc`, `.docx`)
- EPUB (`.epub`)
- Rich Text Format (`.rtf`)
- HTML (`.html`, `.htm`)
- And more...

### Not Needed (Agent-readable)
- Plain Text (`.txt`)
- Markdown (`.md`)
- JSON / YAML / CSV and other structured text

### Output Format
- Markdown (`.md`)

## Advanced Usage

### Convert with Parameters
```bash
# Convert specific pages
cloudconvert convert -f md --pages=1-5 document.pdf

# Convert with custom parameters
cloudconvert convert -f md --width=800 document.pdf
```

### Batch Conversion
```bash
# Convert multiple files
cloudconvert convert -f md file1.pdf file2.docx file3.epub
```

### Check Account Status
```bash
cloudconvert credits
```

## Troubleshooting

### Common Issues
1. **CLI not installed**: Run `./scripts/check_and_install.sh`
2. **API key not set**: Run `./scripts/check_api_key.sh`
3. **Conversion failed**: Check if input format is supported

### Debug Mode
```bash
# Use JSON output for debugging
cloudconvert convert -f md --json document.pdf
```

## Resources
- [CloudConvert CLI Reference](references/cloudconvert_reference.md)
- [API Documentation](https://cloudconvert.com/docs)
- [CLI Repository](https://github.com/cloudconvert/cloudconvert-cli)