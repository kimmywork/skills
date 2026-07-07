# Setup

## Dependencies

The `loopy.py` script requires:

- **Python 3.8+**
- **PyYAML** — usually pre-installed on macOS/Linux
- **croniter** — install via pip:

```bash
pip install croniter
```

Verify:

```bash
python3 -c "import croniter; print('OK')"
```

## Trigger command environment

Trigger commands run via `/bin/sh -c` from the project root. Ensure `$PATH`, `$HOME`, and authentication tokens are available to the shell.

For cron jobs, set environment variables explicitly:

```cron
# Example crontab
LOOPY_TRIGGER_TIMEOUT=60
HOME=/Users/username
PATH=/usr/local/bin:/usr/bin:/bin
0 9 * * * cd /path/to/project && pi -p "run loopy"
```

Workflow trigger examples:
- `gh pr list --state open --json number,title,updatedAt` — GitHub CLI
- `ls docs/` — check for new files
- `curl -s http://status.example.com/api` — HTTP health check

## Configuration

| Env var | Default | Description |
|---|---|---|
| `LOOPY_TRIGGER_TIMEOUT` | 30 | Trigger command timeout in seconds |

## Gitignore

Add to `.gitignore`:

```
workflows/.state/
```

## Scheduling

The `loopy` skill is invoked by the agent. Configure periodic invocation via your agent platform:

- **Codex**: Automations tab → pick project, prompt, cadence
- **Claude Code**: `/loop` or scheduled tasks
- **cron + agent CLI**: `0 9 * * * cd /project && pi -p "run loopy"`

## Marketplace registration

If distributing as a plugin, register in both marketplace manifests:

- `.agents/plugins/marketplace.json`
- `.claude-plugin/marketplace.json`