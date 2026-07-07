# Drafting Process Audit

Date: 2026-07-07
Scope: audit of the current `drafting/` skill bundle and the improvement process that produced it.

## Context gathered

Artifacts reviewed:
- `drafting/COVERAGE_MATRIX.md`
- `drafting/DELIVERY_SKILL_COVERAGE.md`
- `drafting/IMPROVEMENT_PLAN.md`
- all `drafting/skills/*/SKILL.md`
- key references added under `drafting/skills/**/references/`
- `drafting/skills/drafting-loop/scripts/track_parser.py`

Verification performed:
- SKILL line counts
- SKILL Chinese-character check
- SKILL internal-reference check
- plugin JSON parse check
- track CLI help check
- semantic checks for phase review, multi-stage, style extraction, distillation, delivery SKILL coverage
- generated-artifact scan

## Gap classification

| Dimension | Present? | Evidence | Fix / decision |
|---|---|---|---|
| Coverage gap | yes | `implementation-execution` and `requirement-discovery` SKILL-level semantics were initially under-covered | Added `execution-control.md`, `discovery-process.md`, `loop-operations.md`, and updated coverage matrix |
| False guidance | no | No current instruction found that directs wrong behavior | No change |
| Missing guardrail | yes | Running track CLI produced `__pycache__` inside bundle | Removed generated directory and added `__pycache__/` to `.gitignore` |
| Repeated improvisation | yes | Multiple manual semantic checks were needed after user pointed out missing dimensions | Created `COVERAGE_MATRIX.md` and `DELIVERY_SKILL_COVERAGE.md` as reusable audit artifacts |
| Atomic extraction | no | Current new material fits existing skills/references | No new skill proposed |
| Context overhead | possible | Coverage matrices are large but top-level audit artifacts, not loaded by normal skills | Keep outside SKILL.md; no runtime load path |
| Trigger misfire | no evidence | Skill descriptions not yet evaluated in real prompts | Defer to eval/dogfood phase |
| Scope boundary | yes | Concrete cross-model runner, document annotation scripts, web-search agents are tool/runtime-specific | Kept in deferred list |
| User-specific preference | no | Requirements came from framework design goals, not personal style preference | No change |

## Issues found

### PA-001 — Generated Python cache inside skill bundle

- Origin phase: Build/Verify
- Severity: minor
- Type: missing guardrail
- Description: Running `track_cli.py` generated `drafting/skills/drafting-loop/scripts/__pycache__/`, which should not be part of the skill bundle.
- Evidence: generated-artifact scan found `drafting/skills/drafting-loop/scripts/__pycache__`.
- Fix: removed directory and added `__pycache__/` to `.gitignore`.
- Resolution: fix-in-place.

### PA-002 — Link checker noise in top-level audit artifacts

- Origin phase: Verify
- Severity: minor
- Type: unclear
- Description: Top-level coverage artifacts cite source paths and shorthand filenames that are not intended as in-bundle runtime references. A naive markdown-link checker reports them as missing.
- Evidence: broad markdown scan flagged source paths in `COVERAGE_MATRIX.md` and `DELIVERY_SKILL_COVERAGE.md`.
- Fix: no framework change. Treat coverage matrices as audit artifacts; SKILL.md reference checks remain authoritative for runtime bundle integrity.
- Resolution: defer with documented rationale.

## Verification after fixes

- `__pycache__` removed from drafting bundle.
- `.gitignore` now includes `__pycache__/` and `*.pyc`.
- `SKILL.md` files remain under 100 lines.
- `SKILL.md` files contain no Chinese characters.
- SKILL internal references exist.
- Plugin JSON parses.
- Track CLI runs.

## Recommendation

The drafting bundle is ready for dogfood/eval. Further process changes should come from real task runs, not speculative expansion.
