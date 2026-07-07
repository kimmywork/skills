# Handoff Schemas

Every phase-to-phase transition carries a universal envelope plus a phase payload. Handoffs are compact, auditable, and versioned.

## Universal envelope

```yaml
handoff:
  id: <phase>-to-<phase>-v<n>
  from: Sense|Clarify|Shape|Design|Build|Verify|Record
  to: Clarify|Shape|Design|Build|Verify|Record|ContinueStop
  kind: crafting|composing|evaluating|investigating|creating|mixed
  mode: Fidelity|Balanced|Originality
  deliverables: []
  status: VERIFIED|UNVERIFIED|STALE
  phase_review: PASS|STABLE|REVISION|FAIL
  process_audit: no_change|distillation_needed|distillation_done
  version: v1
  hash: sha256:<optional>
  depends_on: []
  changes: []
  open_questions: []
  next_action: <explicit next step>
```

## Sense -> Clarify

```yaml
sense_output:
  kind: <detected kind>
  confidence: high|medium|low
  materials: []
  material_phases: []
  current_phase_guess: <phase>
  ambiguous: true|false
  questions: []
  risks: []
```

## Clarify -> Shape

```yaml
clarify_output:
  kind: <confirmed kind>
  phases: []
  preferences: {mode: full|quick|guided}
  constraints: []
  direct_mode: true|false
  assumptions: []
```

## Shape -> Design

```yaml
shape_output:
  goal: <outcome>
  in_scope: []
  out_of_scope: []
  audience: []
  requirements: []
  acceptance_criteria: []
  verification_plan: []
  stage_split: []
  risks: []
  open_questions: []
```

## Design -> Build

```yaml
design_output:
  principles: []
  approach: {chosen: "", rejected: [], deferred: []}
  feasibility: Feasible|Moderate|Redesigned
  structure: []
  contracts: []
  dependencies: []
  verification: []
  increments: []
  acceptance_map: []
  rollback: []
```

## Build -> Verify

```yaml
build_output:
  deliverable: <artifact>
  path: <location>
  status: complete|partial|blocked
  evidence: []
  drift: []
  limitations: []
  changed_artifacts: []
  checks_run: []
```

## Verify -> Record

```yaml
verify_output:
  verdict: PASS|CONDITIONAL|FAIL|REVISION|STABLE
  issues: []
  routing: {fix_in_place: [], rollback_to: null, deferred: []}
  dimensions: {}
  recommendation: proceed|revise|rollback|defer
  confidence: high|medium|low
```

## Record -> Continue/Stop

```yaml
record_output:
  verdict: delivered|partial|blocked|needs-review|rolled-back
  evidence: []
  coverage: {total: 0, done: 0, deferred: 0, failed: 0}
  deliverables: []
  child_records: []
  next: continue|iterate|split|stop
  observations: []
```

## Rules

- If payload status is UNVERIFIED, the next phase must treat it as risk.
- If `changes` is non-empty, link to a change note.
- If `phase_review` is REVISION or FAIL, do not advance.
- If `process_audit` is `distillation_needed`, create or link a distillation handoff.
