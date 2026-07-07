# Cross-Validation Protocol

Use cross-validation to reduce blind spots in high-stakes, uncertain, or disputed work. It is advisory unless a separate compliance or acceptance gate makes a finding blocking.

## Validation modes

| Mode | Use when | Independence level |
|---|---|---|
| Same-agent adversarial | no independent reviewer/model/tool exists | low |
| Fresh-perspective review | a separate reviewer or fresh context exists | medium |
| Cross-model review | another model/runtime is available | high |
| Domain-lens panel | distinct expertise lenses matter more than model independence | medium/high |

## Setup

1. Freeze the artifact.
2. Freeze the review question and criteria.
3. Provide only required artifacts and criteria to each perspective.
4. Do not provide prior conclusions unless the task is explicit re-review.
5. Require evidence for every finding.

## Default perspectives

Choose 2-4 lenses, not all lenses by default.

| Lens | Checks |
|---|---|
| Correctness | Does it work or state true things? |
| Evidence | Are claims supported by primary or strong sources? |
| Consistency | Do sections, names, numbers, and decisions agree? |
| Risk | What can cause harm, security exposure, compliance failure, or bad decisions? |
| Usability | Can the intended audience use the artifact? |
| Maintainability | Is the solution understandable and sustainable? |
| Style/craft | Does it fit brief, voice, and audience impact? |

## Comparison

Classify outputs:

```yaml
cross_validation_result:
  consensus_findings: []
  divergent_findings: []
  unique_findings: []
  false_positives_or_deferred: []
  unresolved_risks: []
  independence_level: low|medium|high
  recommendation: proceed|revise|rollback|escalate|defer
```

## Divergence rules

- Do not average incompatible judgments.
- If one perspective reports a critical evidence-backed issue, investigate it even if others miss it.
- If perspectives disagree, compare evidence quality, not confidence.
- If independence is low, state the limitation and avoid overclaiming.

## Escalation

Escalate to user or compliance gate when:
- critical/high-risk findings conflict;
- evidence is insufficient but decision impact is high;
- proceeding requires accepting known risk;
- a finding changes scope, contract, or acceptance criteria.

## Output

```markdown
# Cross Validation

## Setup
- Artifact:
- Criteria:
- Perspectives:
- Independence level:

## Consensus findings
## Divergences
## Unique findings
## Unresolved risks
## Recommendation
## Independence limitations
```
