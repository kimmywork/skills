---
name: requirement-discovery
description: Use when a request, feature idea, bug report, refactor, workflow change, or user-facing behavior is not yet shaped into clear users, scenarios, scope, non-goals, requirements, acceptance criteria, and verification expectations.
license: MIT
metadata:
  author: kenpusney
  version: "0.6.0"
---

# Requirement Discovery

Shape intent before design or production.

## Process

1. Read existing track docs, requirements/PRDs, delivery records, `docs/knowledge`, `docs/logs`, and relevant source artifacts (code, data, prior work).
2. Identify elevator pitch, user/persona, scenario, real need, current pain, and why now.
3. Challenge vague words, overloaded terms, hidden assumptions, and over-engineering.
4. Ask one focused question at a time only when context cannot answer it.
5. Propose 2–3 approaches when choices matter; recommend one with trade-offs.
6. **Split if needed**: if the requirement is broad, multi-module, or spans multiple user scenarios, split into independently executable stages before writing. See "Scope splitting" below.
7. Before creating a new track doc, search in-progress track docs (`status: in_progress`) for overlapping scope. Extend existing docs — don't duplicate. Then write or update the smallest durable track artifact.
8. When deep research is needed (market analysis, technical feasibility, domain exploration), call `structured-investigation` to produce research findings. Results go into `docs/track/<track-name>/research/`.
9. Preserve research raw material and final results under `docs/track/<track-name>/research/`:
   - Interview notes, persona docs, discussion summaries
   - Data analysis, competitive research, user feedback
   - Any context too detailed for the requirements/track note

## Scope splitting

When a requirement is too large for a single increment:

1. Identify independent stages: each must be verifiable without completing the others.
2. Create a parent track folder (`scope_type: parent`) with `scope-map.md` (see `../solution-delivery-loop/references/track-document-structure.md`).
3. Each stage gets its own sub-folder (`scope_type: stage`, `parent_id` → parent).
4. Parent `requirements-v1.md` contains the scope-map table and inherited non-goals.
5. Each stage adds its own acceptance criteria and may refine non-goals.

## Output scale

- Simple work: standalone note (`scope_type: standalone`).
- Normal work: track folder with `requirements-v1.md`.
- Large/split work: parent folder with scope-map + stage sub-folders.
- Multi-project: resolve path from `loop-state.md` projects[].track_root.

See `../solution-delivery-loop/references/track-document-structure.md` for naming, paths, and frontmatter schema.

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

## Anti-patterns

- Starting from architecture before user/scenario
- Treating "better UX" or "cleaner code" as acceptance criteria
- Accepting broad scope without non-goals
- Writing a full requirements doc when a compact track note is enough
- Asking the user questions before reading available docs/code
- Writing one monolithic requirement for multi-stage work

## Related

- Next: `solution-design` after users, scope, non-goals, requirements, and acceptance are clear.
- Return here when later phases reveal unclear intent, scope, users, or acceptance.

See `solution-delivery-loop` for review-feedback resolution protocol.
