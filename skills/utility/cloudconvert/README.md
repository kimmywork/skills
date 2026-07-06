# CloudConvert Skill

Convert non-text documents (PDF, DOC/DOCX, EPUB) to Markdown using CloudConvert CLI.

## Installation

```bash
npx skills add kimmywork/skills --skill cloudconvert
```

## Setup

1. Get your API key from [CloudConvert Dashboard](https://cloudconvert.com/dashboard/api/v2/keys)

2. Set the environment variable:

```bash
export CLOUDCONVERT_API_KEY=your_api_key
```

Add to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.) for persistence.

## Usage

### Check Environment

```bash
./scripts/check_and_install.sh    # Verify/install CLI
./scripts/check_api_key.sh        # Verify API key
```

### Convert Documents

```bash
# Basic conversion
./scripts/convert_to_markdown.sh document.pdf

# Specify output directory
./scripts/convert_to_markdown.sh document.docx /output/path
```

## Supported Formats

| Input | Output |
|-------|--------|
| PDF (.pdf) | Markdown (.md) |
| Word (.doc, .docx) | Markdown (.md) |
| EPUB (.epub) | Markdown (.md) |
| RTF (.rtf) | Markdown (.md) |
| HTML (.html, .htm) | Markdown (.md) |

## Author

Kimmy Liu

## Version

0.1