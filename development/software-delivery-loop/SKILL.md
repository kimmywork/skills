---
name: software-delivery-loop
description: Use when software work needs end-to-end delivery, phase triage, or continuation from request to accepted outcome: requirements, design, implementation planning, coding, bugfixes, refactors, maintenance, validation, delivery records, autonomous loops, or existing track/PRD/plan work.
license: MIT
metadata:
  author: kenpusney
  version: "0.3.0"
---

# Software Delivery Loop

Run an inspectable delivery loop:

`Sense → Shape → Design → Build → Verify → Record → Continue/Stop`

Start from user, scenario, and real need. Creativity is welcome; delivery requires commitments, evidence, and acceptance results.

## First move

1. Inspect existing context: `.agents/loop-state.md`, track docs, PRDs, plans, delivery records, `docs/knowledge`, `docs/logs`, code, tests.
2. Right-size inspection: read enough to resolve the current phase and risk; stop when more context is unlikely to change the next action.
3. If no loop state exists, mention that `.agents/loop-state.md` can help workspace-level continuity, but do not force it.
4. Route to the next phase:
   - unclear need, users, behavior, or scope → use `requirement-discovery`
   - clear requirements needing solution/plan → use `solution-design`
   - executable plan or evidence-backed small fix with clear verification → use `implementation-execution`
   - implementation done, completion claim, release, or review → use `delivery-acceptance`

If docs/code can answer a question, read first. Ask the user only after context search leaves real ambiguity. Ask one focused question at a time.

## Autonomy policy

Autonomous execution is allowed when evidence is sufficient and user input is not needed. `.agents/loop-state.md` may define whether the loop can run fully autonomously for this workspace. Autonomy does not waive track notes, verification, delivery records, or change notes.

Use subagents when available and valuable: explorer, maker, checker, reviewer. For risky or multi-file changes, separate maker and checker. If unavailable, perform a fresh review pass yourself and record the limitation.

## Track documentation

Prefer feature-scoped track folders:

- Single project: `docs/track/<feature-name>/prd-v1.md`, `solution-design-v1.md`, `plan-v1.md`, `delivery-record-v1.md`
- Multi-project: `docs/track/<project-name>/<feature-name>/...`
- Simple feature: `docs/track/features/<feature-name>.md`
- Simple bugfix: `docs/track/bugfix/<bug-description>.md`

Every behavior-changing feature, bugfix, or delivery-relevant maintenance task needs a track note. PRDs are for broad, user-facing, multi-module, ambiguous, or long-lived work.

Use `docs/knowledge` for cross-feature knowledge: ADRs, architecture notes, domain terms, reusable contracts, durable decisions. Use `docs/logs/YYYY-MM-DD.md` for operational work logs. Docs can be stale; when docs, code, and tests disagree, verify the truth and write the accurate result back to docs.

## Loop improvement

If a phase is repeatedly blocked, skipped, misunderstood, or produces recurring failures:

1. Summarize the pattern from past runs.
2. Draft concrete skill/template improvements.
3. Present optional improvements to the user.
4. Apply them only after approval.

Self-improvement is ask-first unless `.agents/loop-state.md` sets Autonomy to `full-autonomy`. Under `full-autonomy`, apply safe skill/template refinements and record the change.

## Stop conditions

Pause and return to discovery/design when scope, acceptance, contract, architecture, or verification becomes unclear or changes. Record drift as a change note before continuing.
