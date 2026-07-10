# CloudConvert CLI Reference

CloudConvert is an external processing service. Files passed to its CLI are uploaded under the user's CloudConvert account and applicable retention policy. Confirm that external processing is allowed before conversion.

## Install

```bash
npm install -g cloudconvert-cli
```

This is a global npm installation and requires user approval when initiated by an agent.

## Authentication

Create a key in the CloudConvert dashboard and set it outside the conversation:

```bash
export CLOUDCONVERT_API_KEY=your_key_here
```

Never print, persist, or request the key in chat.

## Conversion

```bash
cloudconvert convert -f md --output-dir /output/path document.pdf
```

Common candidate inputs include PDF, DOC, DOCX, EPUB, and RTF. Actual conversion support depends on CloudConvert's current format matrix and account configuration. Verify support and inspect the produced Markdown rather than assuming fidelity.

Do not upload text formats that can be read directly, including Markdown, plain text, JSON, YAML, and CSV. HTML is normally directly readable; convert it only when the user specifically needs Markdown normalization.

## Operational checks

```bash
cloudconvert --version
cloudconvert credits
cloudconvert parameters convert --input-format pdf --output-format md
```

Conversion may lose page layout, footnotes, tables, images, formulas, comments, tracked changes, or document metadata. Treat the Markdown as a derived artifact and retain the source.

## Resources

- https://cloudconvert.com/docs
- https://github.com/cloudconvert/cloudconvert-cli
