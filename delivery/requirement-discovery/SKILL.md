---
name: requirement-discovery
description: Use when a request, feature idea, bug report, refactor, workflow change, or user-facing behavior is not yet shaped into clear users, scenarios, scope, non-goals, requirements, acceptance criteria, and verification expectations.
license: MIT
metadata:
  author: kenpusney
  version: "0.4.0"
---

# Requirement Discovery

Shape intent before design or production.

## Process

1. Read existing track docs, requirements/PRDs, delivery records, `docs/knowledge`, `docs/logs`, and relevant source artifacts (code, data, prior work).
2. Identify elevator pitch, user/persona, scenario, real need, current pain, and why now.
3. Challenge vague words, overloaded terms, hidden assumptions, and over-engineering.
4. Ask one focused question at a time only when context cannot answer it.
5. Propose 2–3 approaches when choices matter; recommend one with trade-offs.
6. Write or update the smallest durable track artifact.
7. When deep research is needed (market analysis, technical feasibility, domain exploration), call `structured-investigation` to produce research findings. Results go into `docs/track/<feature>/research/`.
8. Preserve research raw material and final results under `docs/track/<feature>/research/`:
   - Interview notes, persona docs, discussion summaries
   - Data analysis, competitive research, user feedback
   - Any context too detailed for the requirements/track note

## Output scale

- Simple feature/bugfix: compact note under `docs/track/features/` or `docs/track/bugfix/`.
- Normal feature: `docs/track/<feature>/requirements-v1.md`.
- Multi-project feature: `docs/track/<project>/<feature>/requirements-v1.md`.
- Broad, user-facing, multi-module, ambiguous, or long-lived work: requirements doc required. Use `references/requirements-template.md`.

## Requirement syntax

Use User Stories for high-level needs:

`As a <persona>, I want <capability>, so that <benefit>.`

Use EARS or Given/When/Then for detailed requirements and acceptance. See `references/requirements-syntax.md`.

## Required shaped-work content

- Elevator pitch / problem
- Persona, journey, or scenario
- Scope and non-goals
- Requirements and acceptance criteria
- Contract or data model if behavior crosses a boundary
- Verification plan
- Risks / rollback
- Open questions

## Related skills

- Next: use `solution-design` after users, scope, non-goals, requirements, and acceptance are clear.
- Return here when later phases reveal unclear intent, scope, users, or acceptance.

## Anti-patterns

- Starting from architecture before user/scenario
- Treating “better UX” or “cleaner code” as acceptance criteria
- Accepting broad scope without non-goals
- Writing a full requirements doc when a compact track note is enough
- Asking the user questions before reading available docs/code

## After this phase

Output inspected by `review-feedback` (cumulative with prior phases). Resolution:
- Fix in place: correct issues, re-review.
- Roll back: return to earliest affected phase, correct there, re-execute forward.

After resolved, `process-distillation` may follow (auto under `full-autonomy`).
