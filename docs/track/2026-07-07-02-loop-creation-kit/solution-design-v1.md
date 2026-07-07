---
status: draft
created: 2026-07-07
version: 1
---

# Solution Design v1: Loop Creation Kit

## Source Requirements

- Requirements doc: `docs/track/2026-07-07-02-loop-creation-kit/requirements-v1.md`
- Requirement IDs: REQ-001 through REQ-019

## Design Principles

1. **Agent is the executor, script is the dispatcher.** The script does deterministic scheduling math (cron parsing, trigger evaluation, state file inspection). The agent does everything that requires judgment (interpreting workflows, making decisions, handling failures). Never burn tokens on logic a script can do.

2. **Workflows are self-contained autonomous units.** No manual input during execution. No dependency on other skills being installed. The workflow body contains everything the agent needs to execute — context, steps, success conditions. If it needs data, it fetches it via trigger commands or external tools.

3. **State files are the single source of truth.** No redundant registries, no separate "last run" tracking. The state directory IS the history. The script reads it to determine scheduling; the agent reads it for context and deduplication.

4. **Clarity over completeness.** `loopify`'s primary job is ensuring the workflow spec is unambiguous from an agent's perspective. A shorter, clearer spec beats a longer, comprehensive one. Every step must be executable without guessing.

5. **Loose coupling, tight contracts.** `loopify` and `loopy` are independent skills that share a contract: the workflow markdown format. Neither depends on the other's internals. The workflow format is the only shared interface.

6. **Agent neutrality.** No assumption about which agent CLI is available. The script doesn't invoke agents — the executing agent (which invoked `loopy` as a skill) handles its own execution mechanism.

## Alternatives

| Option | Summary | Pros | Cons | Decision |
|---|---|---|---|---|
| A: Script dispatches to agent CLI | Script runs `codex --prompt "..."` per workflow | Simple, deterministic | Tied to specific CLI; agent context lost | Rejected |
| B: Skill with embedded script (chosen) | Script handles scheduling, returns dispatch list to agent | Agent-neutral; agent owns execution; script is thin | Script output must be well-structured | Chosen |
| C: Pure agent (no script) | Agent reads all workflows, checks schedules itself | Zero infrastructure | Burns tokens on scheduling; fragile schedule logic in LLM | Rejected |

## Recommended Solution

Two skills in the `@loop/` plugin bundle:

### `loopify` — Agent-assisted workflow creation

**Interaction model**: Iterative refinement. User describes workflow → agent grills for clarity → agent drafts spec → user confirms → agent writes file.

**Grilling protocol**:
1. Parse user's description for vague terms ("check things", "handle it", "make sure")
2. Ask one focused question at a time to resolve ambiguity
3. Probe specifically for: trigger conditions, step boundaries, success criteria, edge cases (0 items, errors), what NOT to do
4. After 2-3 rounds, produce a draft and present for confirmation
5. On confirmation, write to `workflows/<name>.md`

**Output validation**:
- `name` field exists and matches filename
- At least one of `schedule` or `trigger` is present
- Body includes a success condition
- Each step is concrete enough for an agent to execute without guessing

### `loopy` — Workflow scheduling and execution

**Architecture**: Skill with embedded script.

**Execution flow**:
1. Agent invokes `loopy` skill (manually or via cron/systemd calling the script)
2. Script reads all `workflows/*.md` files, parses front-matter
3. For each workflow: determine if due
   - Schedule-only: compare last run timestamp against cron schedule
   - Trigger-only: execute trigger command, check if output is non-empty and exit code is 0
   - Both present (AND): workflow is due only when schedule is due AND trigger produces output
4. Script outputs JSON dispatch list
5. Agent iterates over due workflows, executing each sequentially with full context
6. Agent writes run record to state directory after each workflow

**Script responsibilities** (deterministic, no LLM):
- Parse YAML front-matter from markdown files
- Parse cron expressions and compute next run time
- Execute trigger commands with timeout
- Read state directory for last run timestamp
- Compute NNN sequence number for new state file
- Output structured JSON dispatch list

**Agent responsibilities** (judgment-based):
- Interpret workflow body and execute steps
- Make decisions when steps are ambiguous (within workflow's intent)
- Handle failures (retry, skip, or restart based on state)
- Write run record with status and results
- Access prior state files for dedup/comparison when workflow requires it

## Deliverable Structure

```
loop/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── .codex-plugin/
│   └── plugin.json              # Plugin manifest
└── skills/
    ├── loopify/
    │   └── SKILL.md             # Workflow creation skill
    └── loopy/
        ├── SKILL.md             # Workflow execution skill
        ├── scripts/
        │   └── loopy.py         # Scheduling/dispatch script (Python)
        └── references/
            └── workflow-format.md  # Workflow spec reference
```

## Interfaces & Contracts

### Workflow contract (shared between loopify and loopy)

**Front-matter fields**:
| Field | Required | Type | Description |
|---|---|---|---|
| `name` | Yes | string | Workflow identity, must match filename (without `.md`) |
| `description` | No | string | Human-readable summary |
| `schedule` | Conditional* | string | Cron expression (5-field) |
| `trigger` | Conditional* | string | Shell command; fires when output is non-empty and exit 0 |

*At least one of `schedule` or `trigger` must be present. When both are present, AND semantics applies: the workflow fires only when BOTH the schedule is due AND the trigger command produces non-empty output with exit code 0.

**Body**: Free-form markdown. Must include a success condition (verifiable by agent).

### State contract

**Path**: `workflows/.state/<name>/<YYYY-MM-DD-NNN>.json`

**NNN sequence**: Zero-padded daily counter. First run of the day = `001`, second = `002`, etc.

**Required fields**: `workflow`, `run_id`, `started_at`, `completed_at`, `status`, `items_processed`

**Optional fields**: `trigger_output`, `skip_reason` (required when `status=skipped`), `failure` (with `step`, `error`, `partial_results`)

### Script I/O contract

**Input**: None (reads from `workflows/` directory and `workflows/.state/`)

**Output** (JSON to stdout):
```json
{
  "due": [{"name": "...", "trigger_output": "...", "state_dir": "..."}],
  "not_due": [{"name": "...", "reason": "..."}]
}
```

**Flags**:
- `--run <name>`: Force-run specific workflow
- `--list`: Show all workflows and status
- `--dry-run`: Show what would run without executing

## Primary Flow

### Creation flow (loopify)

```
User: "I want a workflow that checks for stale PRs every morning"
  ↓
Agent: "What counts as stale? No activity for N days? Failed CI? Both?"
  ↓
User: "No activity for 7 days"
  ↓
Agent: "Should it comment on the PR, or just produce a report?"
  ↓
User: "Post a summary comment"
  ↓
Agent: [drafts spec] "Here's the workflow — does this look right?"
  ↓
User: "Yes"
  ↓
Agent: writes workflows/stale-pr-check.md
```

### Execution flow (loopy)

```
loopy script runs (via cron or manual invocation)
  ↓
Script parses all workflows/*.md
  ↓
For each workflow:
  ├── Schedule-based: check last state file timestamp + cron
  └── Trigger-based: execute command, check output
  ↓
Script outputs JSON dispatch list
  ↓
Agent receives dispatch list + project context
  ↓
For each due workflow (sequentially):
  ├── Read workflow body
  ├── Read state directory (if workflow needs history)
  ├── Execute steps
  ├── Write run record to state file
  └── Move to next workflow
```

## Verification Strategy

| Requirement | Verification Method |
|---|---|
| REQ-001 (loopify grills) | Create workflow with vague description; verify agent asks clarifying questions |
| REQ-002 (draft confirmation) | Verify draft is presented before file write |
| REQ-003 (file location) | Verify file exists at correct path with matching name |
| REQ-004 (schedule parsing) | Create 3 test workflows (due, not due, triggered); verify script output |
| REQ-005 (agent context) | Verify agent receives body + state path + project context |
| REQ-006 (state files) | Execute workflow; verify state file exists with correct format and NNN |
| REQ-007 (schedule check) | Create workflow with 8h interval; verify due/not-due at different times |
| REQ-008 (trigger fire) | Create trigger workflow; verify fires when command has output |
| REQ-009 (trigger skip) | Create trigger workflow; verify skips when command has no output |
| REQ-010 (sequential) | Create 3 due workflows; verify execution order |
| REQ-011 (flexible body) | Create goal-only workflow; verify agent executes without explicit steps |
| REQ-012 (success condition) | Verify agent checks success condition before marking complete |
| REQ-013 (no user input) | Verify no prompts appear during execution |
| REQ-014 (--run flag) | Run `loopy --run <name>` on non-due workflow; verify it executes |
| REQ-015 (--list flag) | Run `loopy --list`; verify output matches expected |
| REQ-016 (--dry-run) | Run `loopy --dry-run`; verify no execution occurs |
| REQ-017 (state access) | Create workflow that reads prior runs; verify agent accesses history |
| REQ-018 (failure handling) | Create workflow that fails at step 3; verify state records failure and next run retries |
| REQ-019 (concurrent skip) | Set workflow A to run at 09:00; manually start it; trigger schedule again at 09:05; verify skip state file created with `status: "skipped"` |

## Rollback / Revision Strategy

- Workflows are markdown files — delete or edit to remove/modify
- State files are in `.state/` — delete directory to reset history
- `loopy` script is stateless — remove or replace without side effects
- `loopify` writes one file per workflow — no database, no registry to clean up

## Deployment Considerations

- **Development**: Install plugin from local path. Skills available immediately.
- **Distribution**: Package as plugin bundle. Users install via plugin manager.
- **Scheduling**: Users configure their own cron/systemd/GitHub Actions to invoke `loopy`. The skill documents example crontab entries.

## Resolved Design Questions

| ID | Question | Decision | Rationale |
|---|---|---|---|
| RDQ-001 | Script language? | Python | Better JSON/YAML/cron parsing; maintainability over minimalism |
| RDQ-002 | Body conventions? | Free-form | Agent interprets if content is clear; no structural requirements beyond trigger rule |
| RDQ-003 | Concurrent run handling? | Skip + record `skipped` state | Avoid resource contention; state file records the skip for visibility |
