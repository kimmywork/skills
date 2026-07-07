# Integrity Protocol

Use when work has factual, methodological, compliance, safety, or release risk.

## Failure modes

1. Implementation or reasoning bug passing self-review.
2. Hallucinated citation or source.
3. Hallucinated result, metric, or experimental evidence.
4. Shortcut reliance: using weak proxies as proof.
5. Bug or gap reframed as insight.
6. Methodology fabrication.
7. Frame-lock: early assumption prevents later correction.

## Gate behavior

- Suspected high-impact failure blocks acceptance until fixed or explicitly overridden.
- Unknown evidence must be marked unknown, not passed.
- Overrides follow the compliance-gate override ladder.
- Append all override decisions to the delivery record.

## Integrity report

```markdown
# Integrity Check
## Standards / constraints
## Failure-mode checklist
## Evidence reviewed
## Blocks
## Warnings
## Overrides
## Recommendation
```
