# Requirements: Universalize delivery/ Skills

## Metadata
- Status: active
- Source: verification report from distillation analysis

## Elevator Pitch

The delivery/ skills were built from software project evidence. They need to work for any project type: research, analysis, review, design, creation, development.

## Scope

Universalize the improvements identified in the verification report: 12 from the distillation report (after 3 deferrals and 1 merge) + 3 from the article-creation-workflow, removing software-specific language and making all new sections domain-agnostic.

## Non-Goals

- Do not change software-mode.md or software-specific references (they stay as-is)
- Do not create new skills (all changes go into existing skills)
- Do not change the core phase sequence (requirement-discovery → solution-design → implementation-execution → delivery-acceptance)

## Requirements

### R1: Work type triage
The loop must route different work types (new, fix, restructure, migrate, enhance) to appropriate entry points.

### R2: Stop conditions specificity
Stop conditions must be a structured table with signal/detection/rollback, not a single sentence.

### R3: Session continuity
A 4-step recovery protocol for resuming work across sessions.

### R4: Blocker handling
A Problem/Impact/Options structure for documenting blockers.

### R5: Change note triggers
Change notes must be triggered from the review-feedback loop, not just implementation-execution.

### R6: Research/output separation
Track documentation must distinguish internal working docs from deliverables.

### R7: Feasibility pre-screening
Solution design must pre-screen feasibility (Feasible/Moderate/Redesigned) before detailed design.

### R8: Dependency-driven ordering
Increments with dependencies must follow a dependency graph.

### R9: Risk assessment
Each increment must be assessed for risk level in the challenge step.

### R10: Design decisions
Plan content must record chosen/rejected/deferred decisions with rationale.

### R11: Evidence format
Verification records must include what/result/conclusion.

### R12: Incremental save
Each increment must be independently saveable and reversible.

### R13: Contract changes
A structured protocol for handling interface/contract changes.

### R14: Reference-chain checking
Fixing an artifact must check all references to modified content.

### R15: Multi-pass review
Complex multi-part deliverables need distinct review passes (accuracy/validity/consistency).

## Acceptance Criteria

- All 15 changes applied to the correct skills
- No software-specific language in new universal sections
- All files under 500 lines
- Cross-references between skills intact
- Track documentation exists for this feature

## Verification

- `wc -l` on all modified SKILL.md files
- Grep for software-specific terms in new sections
- Grep for cross-skill references to confirm integrity
