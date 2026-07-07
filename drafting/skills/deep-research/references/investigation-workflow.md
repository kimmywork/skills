# Investigation Workflow

Use for research, root cause analysis, source tracing, system mapping, due diligence, and evidence synthesis.

## Mode choice

- Quick mode: one focused question, limited sources, answer needed fast.
- Full mode: broad question, high-stakes decision, conflicting evidence, or formal deliverable.
- Systematic mode: literature/evidence review requiring explicit inclusion/exclusion criteria.

## Quick mode

1. Locate strongest available source.
2. Trace one level upstream and downstream.
3. Confirm with an independent reference when possible.
4. State confidence and gaps.

## Full workflow

1. Define question, boundaries, and decision use.
2. Choose methodology pattern.
3. Build source plan and source-quality criteria.
4. Gather primary sources before secondary summaries.
5. Preserve raw material or source notes under the active track when work is long-lived.
6. Record source metadata: type, origin, date, access path, relevance, limitations.
7. Trace source -> transformation -> delivery -> storage/consumption when applicable.
8. Extract claims and evidence.
9. Cross-check important claims independently.
10. Separate findings, interpretations, and speculation.
11. Label confidence.
12. Document contradictions, unknowns, and next searches.
13. Run quality-review before acceptance.

## Interaction checkpoints

For full investigations, checkpoint after Scope, Gather, Analyze, Document, and Review when user decisions affect direction. In quick mode, proceed without repeated confirmation but record assumptions and stop on scope/risk ambiguity.

## Raw material preservation

For track-based work, use:

```text
<tracks>/<track>/research/raw/       # source excerpts, notes, exported data
<tracks>/<track>/research/evidence/  # evidence tables and calculations
<tracks>/<track>/research/report.md  # final investigation report
```

If the project has a different track convention, follow it.

## Confidence labels

| Label | Meaning |
|---|---|
| confirmed | directly verified from primary evidence |
| likely | supported by strong evidence but not direct proof |
| uncertain | plausible but under-evidenced |
| contradicted | reliable evidence conflicts |
| unknown | cannot determine from available evidence |

## Evidence table

| Claim | Evidence | Source/path | Quality | Confidence | Notes |
|---|---|---|---|---|---|

## Output

Investigation report sections:
- Question
- Scope
- Method
- Source quality summary
- Key findings
- Evidence table
- Contradictions and gaps
- Confidence summary
- Implications / next steps
