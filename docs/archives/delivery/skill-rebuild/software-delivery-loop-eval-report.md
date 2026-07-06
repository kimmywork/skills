# Software Delivery Loop Eval Report

Date: 2026-07-03

## Scope

This report summarizes validation for the `software-delivery-loop` skill family and its phase skills:

- `software-delivery-loop`
- `requirement-discovery`
- `solution-design`
- `implementation-execution`
- `delivery-acceptance`

The validation covered static structure, semantic coverage, explicit behavior with and without skill access, model override behavior, and trigger-description routing.

## Final Skill State

Current main skill version:

```yaml
name: software-delivery-loop
version: "0.3.0"
```

Final optimization applied:

- Added right-sized context inspection guidance:
  - read enough to resolve the current phase and risk;
  - stop when more context is unlikely to change the next action.
- Strengthened the top-level description for:
  - end-to-end delivery;
  - phase triage;
  - continuation from request to shipment;
  - existing track/PRD/plan work.
- Post-review patch `0.2.3`: aligned the main SKILL track-layout example with the README by including `solution-design-v1.md`.
- Rename patch `0.3.0`: renamed the family from its former product-scoped name to `software-delivery-loop`, removed product-limited wording, and updated docs/evals/reports without keeping a deprecated alias.

Final static check:

| Skill | Word count | Result |
|---|---:|---|
| software-delivery-loop | 463 | pass |
| requirement-discovery | 308 | pass |
| solution-design | 301 | pass |
| implementation-execution | 304 | pass |
| delivery-acceptance | 275 | pass |

All active SKILL.md files remain under 500 words and include required frontmatter.

## Iteration 1 — Explicit Behavior Eval, Default Model

Static validation:

- 47/47 structure checks passed.
- 18/18 semantic static assertions passed.

Behavior benchmark:

| Configuration | Assertions passed |
|---|---:|
| with_skill | 18/18 |
| without_skill | 7/18 |

Notes:

- With-skill outputs consistently used phase routing, context inspection, track notes, verification evidence, and self-improvement approval semantics.
- Baseline outputs were often generic and missed phase names, evidence discipline, or full-autonomy semantics.
- Eval 5 initially timed out when the subagent over-inspected workspace state; retry succeeded with stricter no-shell/no-git constraints.

Key runs:

- Eval 1 pilot: `0ba8a353`
- Eval 2–5 batch: `c345ef26`
- Eval 5 retry + Eval 6 pair: `077e56fb`

## Iteration 2 — Explicit Behavior Eval, `sensenova/deepseek-v4-flash`

Model override:

- `.pi/settings.json` configured builtin subagents to `sensenova/deepseek-v4-flash`.
- Confirmed with `subagent({ action: "models" })`.

Run strategy:

- Initial parallel run `d5b3bd61` failed mostly with `429 rpm exhausted`.
- Serial execution completed all evals.

Behavior benchmark:

| Configuration | Assertions passed |
|---|---:|
| with_skill | 18/18 |
| without_skill | 8/18 |

Per-eval results:

| Eval | with_skill | without_skill |
|---|---:|---:|
| Eval 1 | 3/3 | 2/3 |
| Eval 2 | 3/3 | 1/3 |
| Eval 3 | 3/3 | 0/3 |
| Eval 4 | 3/3 | 2/3 |
| Eval 5 | 3/3 | 1/3 |
| Eval 6 | 3/3 | 2/3 |

Completed runs:

| Eval | Mode | Run |
|---|---|---|
| Eval 1 | with_skill | `637c7382` → resume `ff30c03c` |
| Eval 1 | baseline | `d02a8edb` → resume `f4d4fc68` |
| Eval 2 | with_skill | `b2ed2ba7` |
| Eval 2 | baseline | `e9db8abc` |
| Eval 3 | with_skill | `1339d54f` |
| Eval 3 | baseline | `d9076e48` |
| Eval 4 | with_skill | `dc70c6ca` |
| Eval 4 | baseline | `294d1a4c` |
| Eval 5 | with_skill | `69c16223` |
| Eval 5 | baseline | `26ddd994` |
| Eval 6 | with_skill | `97a5b0cd` |
| Eval 6 | baseline | `18f31f39` |

Notes:

- `sensenova/deepseek-v4-flash` is sensitive to provider RPM limits; serial eval execution is recommended.
- The model sometimes over-explores or writes slowly unless prompts restrict file/tool use and output length.
- With-skill behavior stayed stable at 18/18.

## Trigger Eval

Added trigger eval definitions:

- `myz-skills/software-delivery-loop/evals/trigger-evals.json`

Coverage:

| Category | Cases |
|---|---:|
| software-delivery-loop | 3 |
| requirement-discovery | 3 |
| solution-design | 3 |
| implementation-execution | 3 |
| delivery-acceptance | 3 |
| negative / should not trigger | 3 |
| Total | 18 |

Trigger eval results:

| Iteration | Run | Result | Note |
|---|---|---:|---|
| trigger-eval-1 | `34314948` | 17/18 | T01 routed to `requirement-discovery`; top-level end-to-end trigger was not explicit enough. |
| trigger-eval-2 | `b8892be2` | 18/18 | Passed after strengthening the `software-delivery-loop` description. |

## Overall Result

Final status: validated for current scope.

| Validation | Result |
|---|---:|
| Static structure checks | 47/47 |
| Semantic static coverage | 18/18 |
| Iteration 1 with-skill behavior | 18/18 |
| Iteration 2 with-skill behavior | 18/18 |
| Trigger description eval 2 | 18/18 |

## Conclusions

1. The skill family produces materially better behavior than baseline agents.
2. The strongest improvements are in phase routing, verification discipline, delivery records, cold-start structure, and self-improvement approval semantics.
3. The final `0.3.0` description keeps the end-to-end and phase-triage trigger while broadening the scope from product-only work to software delivery work.
4. Right-sized inspection guidance addresses observed over-exploration without weakening the requirement to inspect relevant context before asking the user.
5. For `sensenova/deepseek-v4-flash`, evals should run serially to avoid RPM failures.

## Limitations

- Behavior grading was heuristic and should be manually reviewed for final publication.
- Explicit behavior evals prompted subagents to read skill files directly.
- Trigger eval was a description-routing simulation, not a full runtime implicit skill-loading test from an installed skill directory.

## Recommended Next Step

Install or expose the skill family in the actual runtime skill discovery path and run a small implicit-loading smoke test with normal user prompts.
