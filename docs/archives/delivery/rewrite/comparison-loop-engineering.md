# Comparison: SDL vs Loop Engineering

**Reference**: [Loop Engineering](https://addyosmani.com/blog/loop-engineering/) by Addy Osmani (June 2026)
**SDL**: Software Delivery Loop skill family (current state)

---

## Five Primitives Comparison

The reference defines five primitives + state. Here's how SDL maps:

| Primitive | Loop Engineering | SDL | Status |
|---|---|---|---|
| **Automations** | Scheduled discovery + triage; `/goal` run-until-done with independent verifier | Autonomy policy allows autonomous execution but no scheduling; no explicit "run until condition met" pattern | **Missing: no scheduled automation** |
| **Worktrees** | Git worktree per parallel agent to avoid file collision | Explicitly not required; left to user/environment | **Design difference** — SDL is agent-neutral |
| **Skills** | `SKILL.md` with instructions + metadata | Full skill family (7 skills + references) | **Aligned** |
| **Plugins/Connectors** | MCP-based: issue tracker, DB, Slack, staging API | Not mentioned; cold-start records discovered commands/ad-hoc | **Missing: no connector pattern** |
| **Sub-agents** | Maker/checker split; different models per role | `review-feedback` + `implementation-execution` recommend maker/checker split | **Aligned** (review-feedback is this) |
| **State / Memory** | Markdown file as "the spine of the loop"; survives between runs | `.agents/loop-state.md` optional; "do not force it" | **Design difference** — SDL minimizes required ceremony |

---

## Principle Differences

### 1. Proactive vs Reactive

**Loop Engineering**: Starts with automations. "An automation runs every morning... finds the work, hands it out, checks it." The loop finds work and surfaces it.

**SDL**: Starts with a user request. "First move: inspect existing context... route to the next phase." The loop waits for work to be given.

**Implication**: SDL has no "triage" pattern. CI failures, stale issues, rotting dependencies — none of these trigger a discovery phase automatically. The cold-start guide assumes the user has already decided to start something.

### 2. Ceremony floor

**Loop Engineering**: High ceremony floor. Worktrees, connectors, sub-agents, scheduled automations, state file — all expected for a "real loop."

**SDL**: Low ceremony floor. "Simple feature: compact track note." "Do not force loop state." "Do not create speculative scaffolding." The user can start with nothing and add ceremony as needed.

**Implication**: SDL is easier to start, loop-engineering has more guardrails for scale.

### 3. Stop conditions

**Loop Engineering**: `"/goal" keeps going until a condition you wrote is actually true. A separate small model checks whether you are done." The loop runs until verified done.

**SDL**: "Pause and return to discovery/design when scope, acceptance, contract, architecture, or verification becomes unclear." The loop stops on uncertainty.

**Implication**: SDL prioritizes safety (stop when unclear) over throughput (run until done). These are complementary — `/goal` is for well-defined conditions, SDL's stop conditions are for ambiguous ones.

### 4. Self-improvement

**Loop Engineering**: Does not mention self-improving skills. The loop is designed once and stays that way.

**SDL**: `process-distillation` is a built-in mechanism for the loop to improve its own skills. The loop gets better over time.

**Implication**: This is SDL's unique contribution. Loop-engineering doesn't address the problem of "the loop design becomes stale as the project evolves."

---

## What SDL Has That Loop Engineering Doesn't

| Feature | SDL | Loop Engineering |
|---|---|---|
| **Self-improving skills** | `process-distillation` analyzes cycles and updates SKILL.md | Not mentioned |
| **Phased delivery** | requirement-discovery → solution-design → implementation → delivery-acceptance | Not structured this way |
| **Cumulative review** | `review-feedback` inspects all prior phases, not just current output | Maker/checker split exists but not cumulative |
| **Evidence-based acceptance** | "Acceptance is evidence, not confidence" — delivery record with verification evidence | Verification is "still on you" |
| **Track documentation** | Standardized track docs (PRD, solution design, plan, delivery record, change notes) | "A markdown file" — no structure specified |
| **Cold start** | Explicit guide for starting from zero | Not addressed |

---

## What Loop Engineering Has That SDL Doesn't

| Feature | Loop Engineering | SDL Gap |
|---|---|---|
| **Scheduled automations** | "An automation runs every morning... finds the work, hands it out, checks it" | No concept of scheduled discovery/triage |
| **`/goal` pattern** | "Keep going until condition is true. Separate model checks if done." | Autonomous execution exists but no "run until verified condition" |
| **Connectors / MCP** | "A loop that can only see the filesystem is a tiny loop" | No integration with issue trackers, CI, Slack, etc. |
| **Comprehension debt** | "The faster the loop ships code you did not write, the bigger the gap between what exists and what you actually understand." | Not mentioned |
| **Cognitive surrender** | "When the loop runs itself, it's very tempting to stop having an opinion and just take whatever it gives back." | Not mentioned |

---

## What We Should Consider Adopting

### P0: Add comprehension debt and cognitive surrender as risks

These are the most important insights from the reference. SDL's autonomy policy currently has no warnings about the human cost of autonomous execution. Adding them to the "Stop conditions" or "Autonomy policy" section of `software-delivery-loop/SKILL.md` would cost 2-3 lines.

**Suggested text**: "Autonomous execution accelerates delivery but creates comprehension debt: the faster the loop ships code you did not write, the less you understand the codebase. Review the loop's output with the same rigor you apply to human contributions. Do not fall into cognitive surrender — accepting whatever the loop produces because it's easier than forming an opinion."

### P1: Lightweight "/goal" pattern reference

The `review-feedback` + `implementation-execution` loop already approximates `/goal`: a separate reviewer checks the maker's output. But SDL doesn't have a "run until condition X is true" pattern. Adding a note in `software-delivery-loop/SKILL.md` that "for well-defined conditions, you can set a verification condition and loop until it passes, with `review-feedback` as the independent verifier" would bridge this gap.

### P2: State as a stronger recommendation

Loop-engineering treats state as "the spine of the whole thing." SDL treats it as optional. For multi-session or autonomous work, `.agents/loop-state.md` should be more strongly recommended. This is a minor wording change.

### Not Adopting (design differences)

- **Worktrees**: SDL is agent-neutral. Worktrees are a tool-specific feature.
- **Connectors/MCP**: SDL is agent-neutral. Connectors are implementation-specific.
- **Scheduled automations**: This would require a runtime/scheduler, which violates agent-neutrality.

---

## Summary

| Dimension | SDL Position | Loop Engineering Position | Action |
|---|---|---|---|
| Structure | Small atomic skills, phase routing | Five primitives, no routing | **Different, not wrong** — SDL is more structured for delivery |
| Ceremony | Start low, scale up | Start with full structure | **Different, not wrong** — SDL is more accessible |
| Proactivity | Reactive (user request → route) | Proactive (schedule → find work) | **Gap** — consider adding a "triage" pattern |
| Human risks | Not mentioned | Strong warnings (comprehension debt, cognitive surrender) | **Adopt** — add 2-3 lines to autonomy/stop conditions |
| Self-improvement | Built-in (`process-distillation`) | Not mentioned | **SDL advantage** — unique feature |
| State | Optional | Spine of the loop | **Minor** — strengthen recommendation for multi-session work |
| `review-feedback` | Cumulative, independent reviewer | Maker/checker split | **Aligned** — SDL's version is more thorough |