# Drafting

A bundle of independent, agent-neutral skills for general knowledge work. Each skill can be invoked directly; the bundle has no orchestrator, required stage sequence, state machine, checkpoint protocol, or cross-skill routing contract.

## Skill inventory

| Skill | Purpose |
|---|---|
| [`probing`](skills/probing/SKILL.md) | Explore uncertain goals and competing directions with the user. |
| [`challenge`](skills/challenge/SKILL.md) | Pressure-test an existing artifact, plan, idea, conclusion, or decision. |
| [`increment`](skills/increment/SKILL.md) | Confirm requirements, plan verifiable increments, and optionally execute them. |
| [`align`](skills/align/SKILL.md) | Keep project documentation aligned after knowledge, implementation, decision, or evidence changes. |
| [`vnv`](skills/vnv/SKILL.md) | Verify and validate results from the perspectives relevant to the task. |
| [`deep-research`](skills/deep-research/SKILL.md) | Derive answers from sources, tracing, comparison, and synthesis. |
| [`distillation`](skills/distillation/SKILL.md) | Run a retrospective and decide whether reusable skill guidance should change. |
| [`restraint`](skills/restraint/SKILL.md) | Act with restraint — do what the user wants, nothing more; avoid over-engineering. |
| [`prune`](skills/prune/SKILL.md) and [Rationale](skills/prune/README.md) | Subtract what is unnecessary — obsolete workspace clutter and overgrowth in a drafted design or plan — keeping the smallest necessary and sufficient set. |
| [`worklog`](skills/worklog/SKILL.md) | Record traceable workspace changes and maintain current work state. |

`style-calibration` is maintained in the `utility` bundle because it is an optional writing utility rather than part of this bundle.

## Design

- **Independent:** no skill depends on a central router or another skill.
- **General:** instructions apply across software, documents, research, analysis, design, and other knowledge work.
- **Focused:** each skill has a direct trigger and bounded outcome.
- **Adaptive:** output structure and process depth follow the task rather than a mandatory framework.
- **Verifiable:** plans and conclusions identify the evidence needed to support them.

## Validation

Before publishing:

```bash
for f in drafting/skills/*/SKILL.md; do
  test "$(wc -l < "$f")" -le 100 || echo "$f too long"
  rg -n '[一-龥]' "$f" && echo "$f contains Chinese characters"
done
```

Also verify that plugin JSON parses, internal references exist, and `.agents/skills` symlinks resolve.
