# CloudConvert Skill

Convert approved non-text documents to Markdown through the external CloudConvert service.

## Important

The input file is uploaded to CloudConvert. Do not use this skill for confidential, regulated, sensitive, or unknown material without explicit approval for third-party processing.

## Setup

```bash
utility/skills/cloudconvert/scripts/check_environment.sh
utility/skills/cloudconvert/scripts/check_api_key.sh
```

If installation is approved:

```bash
utility/skills/cloudconvert/scripts/install_cli.sh
```

Set `CLOUDCONVERT_API_KEY` in the shell environment; never paste it into chat or commit it.

## Convert

```bash
utility/skills/cloudconvert/scripts/convert_to_markdown.sh document.pdf /output/path
```

The script refuses to overwrite an existing Markdown file. Use `--force` only after explicit overwrite approval.

See `references/cloudconvert_reference.md` for limitations and CLI details.

Version: 1.2.0
