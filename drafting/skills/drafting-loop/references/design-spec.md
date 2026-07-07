# Drafting Loop Design Spec

This bundle implements a universal work loop: Sense -> Clarify -> Shape -> Design -> Build -> Verify -> Record -> Continue/Stop.

## Review of the design

Strong parts retained:
- Work kinds are cognitive modes, not deliverable labels.
- Mandatory checkpoints preserve human state ownership.
- Evidence-based acceptance prevents confidence-only delivery.
- Ground-truth isolation separates building from evaluation.
- Scope discipline and change notes prevent silent drift.

Corrections applied in this implementation:
- The orchestrator is agent-neutral: it can load skills inline, not only dispatch agents.
- Skip table is expressed as allowed fast-pass, not permission to bypass gates silently.
- Review, audit, fact verification, compliance, and acceptance are separated by outcome.
- Advisory mechanisms never block; only evidence gates and user decisions block.
- All external reference ideas are distilled into in-bundle references.

## Work kinds

| Kind | Primary mode | Typical output |
|---|---|---|
| Crafting | making systems or artifacts | code, configuration, prototype, operational change |
| Composing | synthesizing communication | report, proposal, documentation, presentation |
| Evaluating | assessing existing work | audit, review, fact-check, compliance result |
| Investigating | discovering truth | root-cause analysis, research brief, system map |
| Creating | imagining new concepts | story, brand, experience, concept design |

## Phase skip policy

All loops run Sense, Clarify, Verify, Record, Continue/Stop. Shape, Design, and Build may be lightweight when the kind warrants it, but the handoff must still state what was done and why it is sufficient.
