# CloudConvert CLI Reference

## Installation
```bash
npm install -g cloudconvert-cli
```

## Environment Variables
```bash
export CLOUDCONVERT_API_KEY=your_key_here
```

## Basic Usage

### Convert files
```bash
cloudconvert convert -f <output-format> <input-files>
```

### Examples
```bash
# Convert PDF to Markdown
cloudconvert convert -f md document.pdf

# Convert DOCX to Markdown
cloudconvert convert -f md document.docx

# Convert EPUB to Markdown
cloudconvert convert -f md book.epub

# Convert multiple files
cloudconvert convert -f md file1.pdf file2.docx file3.epub

# Convert with specific parameters
cloudconvert convert -f md --pages=1-5 document.pdf
```

## Supported Input Formats
- PDF (`.pdf`)
- Microsoft Word (`.doc`, `.docx`)
- EPUB (`.epub`)
- Rich Text Format (`.rtf`)
- HTML (`.html`, `.htm`)
- And many more...

### Not Needed (Agent-readable, no conversion required)
- Plain Text (`.txt`)
- Markdown (`.md`)
- JSON / YAML / CSV and other structured text

## Output Formats
- Markdown (`.md`)
- HTML (`.html`)
- Plain Text (`.txt`)
- PDF (`.pdf`)
- Microsoft Word (`.docx`)
- And many more...

## Common Parameters

### Page Selection
```bash
cloudconvert convert -f md --pages=1-5 document.pdf
```

### Image Parameters (for image conversion)
```bash
cloudconvert convert -f jpg --width=800 --height=600 image.png
```

## PDF Operations
```bash
# Optimize PDF
cloudconvert optimize document.pdf

# Merge PDFs
cloudconvert merge file1.pdf file2.pdf

# OCR (for scanned PDFs)
cloudconvert pdf/ocr -p.language.0=eng document.pdf

# Extract pages
cloudconvert pdf/extract-pages --pages=1,2,3 document.pdf
```

## Advanced Usage

### Check account credits
```bash
cloudconvert credits
```

### List available parameters
```bash
cloudconvert parameters convert --input-format pdf --output-format md
```

### Use JSON output
```bash
cloudconvert convert -f md --json document.pdf
```

## Troubleshooting

### Common Issues
1. **API Key not set**: Ensure `CLOUDCONVERT_API_KEY` environment variable is set
2. **File not found**: Check the file path and ensure the file exists
3. **Conversion failed**: Check if the input format is supported for conversion to the desired output format

### Debug Mode
```bash
cloudconvert convert -f md --json document.pdf
```

## Resources
- [API Documentation](https://cloudconvert.com/docs)
- [CLI Repository](https://github.com/cloudconvert/cloudconvert-cli)
- [CloudConvert Blog](https://cloudconvert.com/blog)