# Loopy Setup

## Dependencies

- Python 3.10+
- PyYAML
- croniter
- IANA timezone data available to Python; install `tzdata` where the OS does not provide it

```bash
python3 -m pip install pyyaml croniter tzdata
```

## Invocation

Resolve the installed skill path and pass the target project explicitly:

```bash
LOOPY=/absolute/path/to/loopy
PROJECT=/absolute/path/to/project
python3 "$LOOPY/scripts/loopy.py" --project-root "$PROJECT" --validate
python3 "$LOOPY/scripts/loopy.py" --project-root "$PROJECT" --dry-run
python3 "$LOOPY/scripts/loopy.py" --project-root "$PROJECT"
```

## Environment

| Variable | Default | Purpose |
|---|---:|---|
| `LOOPY_TRIGGER_TIMEOUT` | 30 seconds | Maximum trigger-command runtime |
| `LOOPY_LEASE_SECONDS` | 86400 seconds | Default run lease when `timeout_minutes` is absent |

Trigger commands run via `/bin/sh` from the project root. Provide only the minimum PATH and credentials authorized by the workflow. Do not place secrets in workflow files or trigger output.

## Scheduling

A platform scheduler should invoke the agent with the project and loopy skill available. Avoid directly running the scanner from cron without an agent capable of executing and finalizing the returned dispatch.

Examples include Codex Automations, Claude scheduled tasks, or a cron-launched agent CLI.

## Repository hygiene

Add:

```gitignore
workflows/.state/
```

Do not commit dispatch logs, trigger output, locks, or run state.
