# Plan: Universalize delivery/ Skills

## Increments

### Slice 1: solution-delivery-loop (6 changes)
**Status**: done
**Files**: `delivery/solution-delivery-loop/SKILL.md`
**Changes**:
1. Add `## Work type triage` before `## First move`
2. Rewrite `## Stop conditions` as signal/detection/rollback table
3. Add `## Blocker handling` after stop conditions
4. Add `## Session continuity` after autonomy policy
5. Add change note trigger to review-feedback loop
6. Add research/output separation to track documentation

**Verification**: `wc -l` shows 124 lines (was 74). All new sections domain-agnostic.

### Slice 2: solution-design (4 changes)
**Status**: done
**Files**: `delivery/solution-design/SKILL.md`
**Changes**:
1. Add feasibility pre-screening step (new step 3)
2. Add dependency-driven ordering rule to planning rules
3. Add risk assessment to challenge step
4. Replace "Alternatives and trade-offs" with expanded design decisions

**Verification**: `wc -l` shows 72 lines (was 69). Step numbering corrected (1-9).

### Slice 3: implementation-execution (4 changes)
**Status**: done
**Files**: `delivery/implementation-execution/SKILL.md`
**Changes**:
1. Expand step 5 (evidence format: what/result/conclusion)
2. Add step 6 (incremental save: commit for code, version marker for other)
3. Add `## Contract changes` section
4. Add reference-chain anti-pattern

**Verification**: `wc -l` shows 94 lines (was 80). No software-specific terms in new sections.

### Slice 4: review-feedback (1 change)
**Status**: done
**Files**: `delivery/review-feedback/SKILL.md`
**Changes**:
1. Add multi-pass review guidance (accuracy/validity/consistency)

**Verification**: `wc -l` shows 54 lines (was 49). Optional guidance, not required.

## Verification Commands

```bash
wc -l delivery/*/SKILL.md
git diff --stat
grep -rn "git\|commit\|code\|test\|file" delivery/solution-delivery-loop/SKILL.md delivery/solution-design/SKILL.md
```
