---
name: cloudconvert
description: Convert non-text documents such as PDF, DOC, DOCX, EPUB, and RTF to Markdown with the CloudConvert CLI. Use when a document must become agent-readable and external upload to CloudConvert is acceptable; skip formats already readable as text.
---

# CloudConvert

Convert a document to Markdown through the external CloudConvert service.

## Privacy boundary

CloudConvert uploads the input to a third party. Before conversion, determine whether the file is public, non-sensitive, or explicitly approved for external processing. For sensitive, confidential, regulated, or unknown material, disclose the upload and obtain approval; otherwise use an approved local method or stop.

Never expose the API key in output, commands, logs, or generated files.

## Process

1. Confirm that conversion is needed. Read `.txt`, `.md`, `.json`, `.yaml`, `.csv`, HTML, and other directly readable text without uploading them.
2. Inspect the file type, sensitivity, desired output location, and overwrite risk.
3. Resolve this skill directory and check the environment:

```bash
<skill>/scripts/check_environment.sh
<skill>/scripts/check_api_key.sh
```

4. If the CLI is missing, show the installation command. Run `install_cli.sh` only after the user approves a global npm installation.
5. Convert one file at a time unless the user explicitly requests a batch:

```bash
<skill>/scripts/convert_to_markdown.sh <input-file> <output-directory>
```

6. Verify that the expected Markdown file exists and is non-empty before using it.
7. Report the output path and any conversion limitations in the user's language. Do not delete the source or unrelated files.

## Failure handling

- Missing CLI: request installation approval or offer an approved alternative.
- Missing API key: explain how to set `CLOUDCONVERT_API_KEY`; never request that the user paste it into chat.
- Existing output: stop rather than overwrite; use the script's `--force` flag only with explicit approval.
- Failed or empty conversion: preserve the source, report the error, and do not claim success.

## Reference

Read `references/cloudconvert_reference.md` for installation, supported inputs, and CLI details.
