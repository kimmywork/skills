---
status: accepted
scope_type: standalone
created: 2026-07-07
version: 2
---

# Requirements v2: Loop Creation Kit

## 0. Metadata

- Owner: Kimmy Liu
- Status: draft
- Last updated: 2026-07-07

## 1. Elevator Pitch

For developers who have recurring tasks (CI triage, security scans, daily summaries), the Loop Creation Kit provides two skills — `loopify` and `loopy` — that turn described workflows into autonomous, scheduled automations. `loopify` agent-assists the creation of workflow specs through iterative refinement. `loopy` executes those workflows on schedule or trigger, running them as agent-driven loops without human intervention.

## 2. Background / Problem

- Current pain: Developers repeat the same multi-step tasks manually or write fragile bash scripts that break when context changes. There's no middle ground between "do it by hand every time" and "maintain a brittle automation script forever."
- Why now: Agent capabilities (tool use, code reading, web search, CLI execution) have matured enough that an agent can execute complex multi-step workflows reliably. The loop engineering paradigm (Osmani, Steinberger, Cherny) has validated that designing systems that prompt agents is more leveraged than prompting agents directly.
- Existing constraints: Must work within the existing plugin/skill ecosystem. Must be agent-neutral (work with Codex and Claude Code). Must not depend on `@delivery/` skills being installed.

## 3. User Persona

| Persona | Situation | Need | Constraint |
|---|---|---|---|
| Solo developer | Has 5-10 recurring tasks per week (triage, review, summaries) | Automate repetitive workflows without writing fragile scripts | Limited time to maintain automations |
| Team lead | Needs consistent processes across the team (code review triage, release prep) | Codify team workflows as auditable, version-controlled specs | Workflows must be reviewable by the team |
| DevOps engineer | Monitors CI/CD, security alerts, dependency updates | Event-driven and scheduled automations with clear audit trails | Must integrate with existing tooling (GitHub, CI systems) |

## 4. User Journey

| Stage | User action | System response | Pain / risk |
|---|---|---|---|
| Creation | User invokes `loopify` and describes a workflow in natural language | Agent asks clarifying questions to refine the spec | User might describe something too vague to execute |
| Refinement | Agent produces draft spec, user reviews | Agent iterates until spec is unambiguous | Premature finalization leads to unreliable workflows |
| Storage | Agent writes workflow markdown to `workflows/<name>.md` | File created with front-matter and body | Name/filename mismatch, missing trigger |
| Scheduling | User invokes `loopy` or it runs via cron/systemd | Script checks all workflows, determines which are due | Incorrect schedule parsing, missed runs |
| Execution | Agent receives due workflow + context | Agent executes steps, writes results | Agent misinterprets ambiguous steps |
| State | Agent writes run record to state directory | `<YYYY-MM-DD-NNN>.json` created per run | State corruption, sequence collision |
| Review | User inspects workflow history | State files provide full audit trail | Too many files, no summarization |

## 5. User Story Map

| Activity | User Story | Priority |
|---|---|---|
| Create workflow | As a developer, I want to describe a workflow in natural language and have the agent refine it into a clear spec, so that I don't have to write structured markdown myself. | P0 |
| Store workflow | As a developer, I want workflow specs saved as version-controlled markdown files, so that the team can review and edit them. | P0 |
| Schedule workflow | As a developer, I want to set a cron schedule or trigger command on a workflow, so that it runs automatically without manual invocation. | P0 |
| Execute workflow | As a developer, I want workflows executed by an agent that follows the spec, so that complex multi-step tasks happen reliably. | P0 |
| Track state | As a developer, I want each workflow run recorded with its status and output, so that I can audit what happened and retry failures. | P0 |
| Inspect history | As a developer, I want to see past runs of a workflow, so that I can verify it's working correctly and debug failures. | P1 |
| Force run | As a developer, I want to manually trigger a workflow regardless of schedule, so that I can test it or run it on-demand. | P1 |
| Dry run | As a developer, I want to see which workflows would run without actually executing them, so that I can verify scheduling logic. | P2 |

## 6. Scope

### In scope

- `loopify` skill: agent-assisted workflow creation through iterative questioning
- `loopy` skill: workflow scheduling and execution via embedded script
- Workflow markdown format with front-matter (name, schedule/trigger, description)
- Per-run state files for audit trail and deduplication
- Dispatch logging: every `loopy` invocation recorded to `workflows/.state/dispatch/`
- State file as lock: script creates `status: "scheduled"`, agent writes final status; collision detected by presence of incomplete state file
- Schedule-based triggers (cron expressions, 5-field)
- Event-based triggers (shell command output)
- AND semantics when both schedule and trigger are present
- Sequential workflow execution
- Project-root `workflows/` directory convention

### Out of scope

- Parallel workflow execution (may come later)
- Manual input injection into running workflows
- Workflow composition (calling other workflows)
- GUI or web interface for workflow management
- Cloud-hosted scheduling (users bring their own cron/systemd/GitHub Actions)
- Integration with `@delivery/` skills (independent, but composable if both installed)

## 7. Non-Goals

| ID | Non-Goal | Reason |
|---|---|---|
| NG1 | Build a workflow orchestration engine | The agent IS the orchestrator; we just dispatch to it |
| NG2 | Support arbitrary agent CLIs | The executing agent decides its own invocation mechanism |
| NG3 | Provide a workflow marketplace | Scope too large for v1; workflows are project-local |
| NG4 | Guarantee exactly-once execution | Sequential + state files make re-runs idempotent, but distributed execution is out of scope |
| NG5 | Replace cron/systemd | `loopy` is invoked BY these systems, not a replacement |

## 8. Requirements

| Req ID | Requirement | Acceptance Criteria | Verification | Priority | Dependencies |
|---|---|---|---|---|---|
| REQ-001 | When a user invokes `loopify` with a workflow description, the agent shall ask clarifying questions until the spec is unambiguous. | Given a vague description, when agent grills, then at least 2 clarifying questions are asked before drafting. | Manual test with vague input | P0 | — |
| REQ-002 | When `loopify` produces a draft spec, the agent shall present it for user confirmation before writing the file. | Given a refined spec, when agent drafts, then user sees the draft and confirms before file creation. | Manual test | P0 | — |
| REQ-003 | When `loopify` writes a workflow, the file shall be at `<project-root>/workflows/<name>.md` with `name` in front-matter matching the filename. | Given workflow name "daily-triage", when written, then file is `workflows/daily-triage.md` and front-matter has `name: daily-triage`. | File exists, front-matter parses correctly | P0 | — |
| REQ-004 | When `loopy` runs, the embedded script shall parse all workflow front-matter and determine which are due based on schedule or trigger. | Given 3 workflows (1 due, 1 not due, 1 triggered with output), when script runs, then output JSON lists only the due and triggered workflows. | Script output matches expected dispatch list | P0 | — |
| REQ-005 | When `loopy` determines a workflow is due, the agent shall execute it with the workflow body, state directory path, and project context. | Given a due workflow, when agent executes, then it receives body + state path + project context. | Agent receives correct context objects | P0 | — |
| REQ-006 | When a workflow run is scheduled, the script shall write a run record to `workflows/.state/<name>/<YYYY-MM-DD-NNN>.json` with `status: "scheduled"`. On completion, the agent shall update the status. | Given a scheduled run, when script creates state file, then file exists with `status: "scheduled"`, no `completed_at`. When agent completes, status is `success`/`failed`/`partial` with `completed_at`. | State file transitions through correct statuses | P0 | — |
| REQ-007 | When checking schedule, the script shall use the latest state file's timestamp to determine last run time. | Given a workflow with `schedule: '0 9 * * *'` and last run at 2026-07-06 09:00, when checked at 2026-07-07 08:59, then workflow is not due; when checked at 2026-07-07 09:00, then workflow is due. | Schedule calculation matches expected | P0 | — |
| REQ-008 | When a trigger command produces non-empty output, the workflow shall fire. | Given trigger `gh pr list --state open`, when 3 PRs exist, then workflow fires with trigger output in context. | Trigger output appears in agent context | P0 | — |
| REQ-009 | When a trigger command produces empty output or non-zero exit, the workflow shall not fire. The script shall record the outcome in `workflows/.state/dispatch/<YYYY-MM-DD-NNN>.json` but not create a per-workflow state file. | Given trigger with 0 results, when checked, then workflow is not in dispatch list, but dispatch log records it with reason. | Workflow not in dispatch list; dispatch log contains entry with reason | P0 | — |
| REQ-010 | `loopy` shall execute due workflows sequentially, not in parallel. | Given 3 due workflows, when executed, then each completes before the next starts. | Execution order is sequential | P0 | — |
| REQ-011 | A workflow body shall support both step-by-step instructions and goal-oriented descriptions. | Given a workflow with goal description only, when agent executes, then it figures out steps autonomously. | Agent completes goal without explicit steps | P0 | — |
| REQ-012 | A workflow body shall include a success condition that the agent can verify. | Given a workflow, when body includes success condition, then agent checks it before marking run complete. | Agent verifies success condition | P0 | — |
| REQ-013 | The system shall not require manual user input during workflow execution. | Given a running workflow, when it needs data, then it obtains it from trigger output, state files, or external commands — never from the user. | No user prompts during execution | P0 | — |
| REQ-014 | `loopy` shall provide `--run <name>` flag to force-run a specific workflow. | Given `loopy --run daily-triage`, when invoked, then that workflow executes regardless of schedule. | Workflow executes on --run flag | P1 | — |
| REQ-015 | `loopy` shall provide `--list` flag to show workflows and their next run time. | Given `loopy --list`, when invoked, then output shows each workflow name, schedule, and next run. | Output matches expected list | P1 | — |
| REQ-016 | `loopy` shall provide `--dry-run` flag to show what would run without executing. | Given `loopy --dry-run`, when invoked, then output shows due workflows but nothing executes. | No state files created, no agent invocations | P2 | — |
| REQ-017 | The executing agent may access prior run state to make decisions (e.g. dedup, comparison, retry). | Given a workflow that needs history, when agent reads state dir, then it can access any prior run file. | Agent reads historical state files | P0 | REQ-006 |
| REQ-018 | When a workflow run fails, the agent shall write failure details to the state file and decide on retry/skip/restart for the next run. | Given step 3 of 5 fails, when agent writes state, then failure details are recorded. On next run, agent reads state and decides. | State file contains failure info; agent makes retry decision | P0 | REQ-006 |
| REQ-019 | When a workflow is still running when the next schedule fires, the script shall check the latest state file: if `status: "scheduled"` and no `completed_at`, the workflow is in progress. The script shall create a new state file with `status: "skipped"` and `skip_reason`, and not put it in the dispatch list. | Given workflow A running at 09:00 (state file has `status: "scheduled"`, no `completed_at`), when 09:05 schedule fires again, then a new state file with `status: "skipped"` is created, and workflow A is not in dispatch list. | State file exists with skip_reason; dispatch list does not contain workflow A | P0 | REQ-006 |

## 9. Contracts / Data Model

### Workflow Markdown Format

```yaml
---
name: <string>              # Required, must match filename
description: <string>       # Optional
schedule: "<cron expr>"     # Optional, cron format (5-field)
trigger: "<shell command>"  # Optional, command whose output triggers execution
# When both schedule and trigger are present, AND semantics applies:
# workflow fires only when BOTH the schedule is due AND trigger produces output
---
<free-form body: steps, goals, context, success condition>
```

### State File Format

```json
{
  "workflow": "<name>",
  "run_id": "<YYYY-MM-DD-NNN>",
  "started_at": "<ISO-8601>",
  "completed_at": "<ISO-8601 or null>",
  "status": "scheduled | success | failed | partial | skipped",
  "items_processed": <int or null>,
  "trigger_output_file": "<path to trigger output file or null>",
  "skip_reason": "<string, only when status=skipped>",
  "failure": {
    "step": "<step identifier>",
    "error": "<error message>",
    "partial_results": "<what was completed>"
  }
}
```

### Dispatch Output (shared schema)

Both the stdout output and the dispatch log share this structure. The only difference: the dispatch log has an `invoked_at` timestamp at the root level. `due` and `script_errors` arrays are always present (may be empty). `trigger_output_file` is absent when no trigger is configured. One workflow's error does not block others.

```json
{
  "due": [
    {
      "name": "<workflow name>",
      "trigger_output_file": "workflows/.state/<name>/trigger-YYYY-MM-DD-NNN.txt",
      "state_file": "workflows/.state/<name>/YYYY-MM-DD-NNN.json"
    }
  ],
  "script_errors": [
    {
      "name": "<workflow name>",
      "reason": "trigger command failed / YAML parse error / timeout",
      "state_file": "workflows/.state/<name>/YYYY-MM-DD-NNN.json"
    }
  ],
  "not_due": [
    {
      "name": "<workflow name>",
      "reason": "<schedule not due / trigger empty / trigger failed>"
    }
  ]
}
```

- **stdout version**: Script writes this JSON directly to stdout. No `invoked_at`.
- **dispatch log version**: Script writes to `workflows/.state/dispatch/<YYYY-MM-DD-NNN>.json` with an added `invoked_at` field at root level.

## 10. Constraints

- Performance / scale: A single `loopy` invocation handles tens of workflows, not thousands. Each workflow runs in seconds to minutes.
- Platform / compatibility: Must work on Linux/macOS. Script is Python with `croniter` dependency (documented in `references/setup.md`). Must work with both `codex` and `claude` agent CLIs (or any future agent).
- Agent neutrality: No assumption about which agent CLI is available. The executing agent decides its own invocation mechanism (fork, subagent, direct execution).

## 11. Risks / Rollback

| Risk | Impact | Mitigation / Rollback |
|---|---|---|
| Agent misinterprets ambiguous workflow steps | Workflow produces wrong output or fails silently | `loopify` stress-tests clarity during creation; success conditions provide verification |
| State file corruption (partial write, crash) | Next run gets wrong dedup state | State files are atomic writes (write to temp, rename); agent can detect and skip corrupt files |
| Trigger command hangs or takes too long | `loopy` blocks on one workflow | Script sets timeout on trigger commands; agent execution has inherent time limits |
| Too many workflows create scheduling noise | User overwhelmed by automation output | Workflows are opt-in; user can disable by removing schedule/trigger from front-matter |
| Agent token cost per workflow run | Expensive if workflows run frequently | `loopy` script filters non-due workflows before invoking agent; trigger commands reduce unnecessary runs |

## 12. Resolved Questions

| ID | Question | Decision | Rationale |
|---|---|---|---|
| RQ-001 | Script language: bash or Python? | Python | Better JSON/cron parsing; maintainability over minimalism |
| RQ-002 | Workflow body conventions? | Free-form | No structural requirements beyond trigger rule; agent interprets if content is clear |
| RQ-003 | Workflow still running when next schedule fires? | Skip, record `skipped` run state | Avoid resource contention; state file records the skip for visibility |
| RQ-004 | Collision detection mechanism? | State file as lock | Script creates `status: \"scheduled\"` atomically; if latest state file lacks `completed_at`, workflow is in progress |
| RQ-005 | Trigger output format? | File path in dispatch list | Full stdout saved to `.state/<name>/trigger-<date>.txt`; dispatch list only carries the path |
| RQ-006 | Error isolation between workflows? | Per-workflow `script_errors` array | One workflow's trigger/YAML failure doesn't block others |

## 13. Discussion Log

This section records the research and design discussion that shaped the requirements.

### Source material

- Addy Osmani, "Loop Engineering" (June 2026): Defined the five loop primitives (automations, worktrees, skills, plugins, sub-agents) and the paradigm shift from "prompting agents" to "designing systems that prompt agents." Core insight: the leverage point moved from prompt quality to system design.
- Peter Steinberger: "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."
- Boris Cherny (Anthropic): "I don't prompt Claude anymore. I have loops running that prompt Claude."
- Existing `@delivery/` skill set: Validates the pattern of composable, focused skills with agent-neutral contracts. The delivery loop's structured workflow (requirements → design → implement → verify) informed the design of `loopify`'s refinement process.

### Grilling session: design decisions

**Q1: Workflow location** — Project-root `workflows/` (Option B). Workflows are project-scoped, version-controlled, and have a predictable location. Plugin-level is wrong (not project-specific); user-chosen adds unnecessary ceremony.

**Q2: Execution architecture** — Hybrid: script for scheduling, agent for execution (Option C). Scheduling logic (cron parsing, "is this due?") is deterministic and shouldn't burn tokens. Workflow execution (interpreting steps, making decisions) is where the agent adds value.

**Q3: Front-matter contract** — `name` required and must match filename. `description` optional. At least one of `schedule` or `trigger` required. The name-filename coupling enables predictable file lookup and unambiguous workflow identification.

**Q4: Event-based triggers** — Included in v1 via shell commands. The trigger command produces output; if non-empty and exit 0, the workflow fires. When both `schedule` and `trigger` are present, AND semantics applies: both conditions must be satisfied. The agent interprets the trigger output as context. Simple, composable, no external webhook infrastructure needed.

**Q5: Workflow state** — Per-run files: `workflows/.state/<name>/<YYYY-MM-DD-NNN>.json`. NNN is zero-padded daily sequence. Full audit trail, natural deduplication, no redundant registries. State files ARE the history — no separate "last run" tracking.

**Q6: Workflow output** — Hybrid: `loopy` writes run metadata (status, duration, items) to state file. Actual workflow output (reports, PR comments, files) goes wherever the workflow body instructs. State file is bookkeeping; workflow owns its output.

**Q7: loopify interaction model** — Iterative refinement (Option A with twist). Agent grills naturally (not rigidly templated), produces draft after 2-3 rounds, user confirms. Key insight: `loopify`'s job is stress-testing executability — "can I do this step without ambiguity?"

**Q8: History access** — Workflow-decided (Option C). `loopy` provides the state directory path; the workflow body specifies how much history to read. Most workflows only need the latest run; some need a window. Let the workflow decide.

**Q9: Failure handling** — Agent decides (Option C). Agent writes failure details to state file; on next run, agent reads state and decides retry/skip/restart. Keeps script thin; agent uses judgment. The state file is the communication channel between runs.

**Q10: Execution order** — Sequential for v1 (Option A). Predictable, no resource contention, no worktree isolation needed. Parallelism is easy to add later; starting simple avoids premature complexity.

**Q11: Relationship to @delivery/** — Independent (Option A). `loop` owns recurring automation; `delivery` owns one-shot delivery. A workflow body CAN reference delivery skills as steps, but no formal coupling. Don't guarantee delivery capabilities in loop context.

**Q12: loopy's nature** — Skill with embedded script, not a standalone CLI. The script handles scheduling/dispatch; the agent (which invoked the skill) handles execution. Entry point is skill invocation.

**Q13: Agent context** — Body + state path + project context (Option C). Workflow body owns workflow-specific context; state path enables history access; project context prevents cold-start on every run.

**Q14: Manual input** — None, fully autonomous (Option A). Workflows are self-contained loops. If it needs human input, it's not a loop workflow. The workflow determines its own inputs via trigger commands or external tools.

**Q15: File location** — Fixed `workflows/<name>.md` (Option A). If you have dozens of workflows, the problem isn't organization — it's over-automation.

**Q16: Agent CLI invocation** — Agent decides (no script involvement). `loopy` is invoked BY an agent; the agent already knows how to fork, spawn subagents, or execute directly. The script doesn't need to know about agent CLIs.

**Q17: Inter-run state** — From state files (Option A). The script lists the state directory, finds the latest run, compares against schedule. No redundant state, no sync issues.

**Q18: Script output format** — JSON dispatch list with `due` and `not_due` arrays. `not_due` replaces the earlier "skipped" label to avoid confusion with the state file's `skipped` status (which means "was due but already running"). Structured, unambiguous for agent parsing. Includes trigger output and state directory path per workflow.

**Q19: Script language** — Python. Better JSON/YAML/cron parsing. Maintainability over minimalism.

**Q20: Body conventions** — Free-form. No structural requirements beyond trigger rule. Agent interprets if content is clear enough.

**Q21: Concurrent run handling** — Skip, record `skipped` state. Avoids resource contention; state file provides visibility into what was skipped and why.
