# Prune — Rationale

A short explanation of why `prune` is designed the way it is. The executable
guidance lives in [`SKILL.md`](SKILL.md); read this file to understand the
design and where it fits alongside the other skills in this bundle. It is a
rationale, not a review: it records the reasoning behind the design so a reader
or a future maintainer can tell why a decision was made, and revisit it when the
evidence changes.

## What it is, and its boundary

`prune` is a subtraction skill. Across both domains it answers one question —
"what can be removed?" — and removes only what clears two gates: the thing is no
longer required, and it is not protected (not active guidance, not the current
plan, not content the user asked to keep, not still-useful reference or
published material). When a candidate is ambiguous it is preserved and the
question is put back to the user.

What `prune` is *not* is just as important. It does not decide whether a
document is currently still meaningful — that requires knowing what the
document changed with, which is a classification and reference task handled at
the point a document is introduced or updated. It does not rewrite the plan to
be better; it only shrinks what has already been drafted. It does not judge
quality, give a correctness verdict, or do a broad evidence investigation —
those are other skills' work. `prune` is deliberately narrow so its trigger
stays crisp and its action stays reversible and reviewable.

## Why one skill instead of two

`prune` covers two superficially different activities in a single skill:

- **File and workspace pruning** — deleting obsolete, abandoned, or
  reproducible content from a working copy (documents, experiments, fixtures,
  caches no longer needed).
- **Plan and design pruning** — trimming a drafted design or plan back to what
  the task actually requires (duplicated sections, speculative branches,
  excess abstraction, over-analysis).

These look unrelated at first: one removes files, the other shortens prose. But
they are the same operation applied to different objects. Whether the excess
lives as bytes on disk or as clauses in a plan, the work is identical: decide
what is no longer necessary, keep the smallest set that remains necessary and
sufficient, and defend that judgment. Splitting them into two skills would
duplicate the shared judgment ("is this still needed?") and the shared safety
rules (never remove what is protected, ask when uncertain), forcing an agent to
choose between two overlapping playbooks for one recurring decision.

A single skill also keeps triggering unambiguous. Both activities are invoked
at the same kind of moment — before syncing a branch, when forming a plan, when
a decision is about to land — where the agent is deciding not to carry
something forward. One description, one trigger, one set of gates.

## Why less is more

Removing is not a loss of value; it is how value is concentrated. Excess rarely
stays inert — a stale file, a dead branch, or an unneeded plan section that is
left in place continues to be read, maintained, and mistaken for current
guidance. The cheapest—and often the only truthful—way to keep the remaining
content useful is to cut the material that is no longer true or no longer
needed. Less inventory means less to verify, less to reconcile when knowledge
changes, and less risk that an agent follows guidance that is no longer
supposed to apply.

`prune` applies this principle to both files and plans. A working copy is the
source of current truth; retaining historical context there invites agents to
treat the outdated as current. A plan accumulates scope the same way a disk
does. Both need the same habit of trimming.

## Why a single source of truth

When a fact, decision, or reference exists in more than one place, the copies
drift, and nobody can say which is authoritative. `prune` therefore keeps one
current rendering of each decision or reference and removes duplicate snapshots
rather than updating every copy. Historical value is not thrown away — it is
moved where it belongs, into the version history, so the live material stays
small and consistent. This is subtraction as information hygiene: fewer copies,
less drift, one place an agent looks for the truth.

## How it works

The mechanism is deliberately spare, and the same in both domains:

- **Two gates, applied in order.** A candidate must be not required *and* not
  protected. Protection is checked first because it needs no judgment — active
  instructions, the current plan or workstate, approved requirements,
  acceptance criteria, still-useful references, and published or long-term
  reference material (post-mortems, lessons learned, retrospectives) are never
  removed without an explicit user request.
- **Judgment is stated, not assumed.** Age alone never proves something is
  obsolete; claiming that an artifact is no longer needed is a decision the
  agent must be able to defend, and ambiguous cases revert to the user rather
  than to deletion.
- **History is not deleted, it is moved.** Valuable committed content is kept in
  version history and removed from the live copy in the same act. Uncommitted
  experiments are discarded only when abandonment is explicit and no
  source-of-truth fact is lost.
- **Generated content needs a before and an after.** For files, the agent must
  know the source and the regeneration command before deleting, and verify the
  tree still rebuilds after deletion. Verification is scaled to the cleanup
  type: build or fixed-point checks for artifacts on the build or generation
  chain, reference and working-tree checks for pure documentation cleanup.
- **Plans are verified against their source.** Because there is no build to
  re-run, trimming a plan or design is checked by comparing the trimmed result
  with the origin task and requirements to confirm nothing necessary was
  dropped; the output is the trimmed material itself, not an archive.
- **Removal is explicit and reviewable.** The pruned result is committed or left
  ready for review rather than silently discarded, so a decision can always be
  audited or undone.

## Pairing with the other skills

`prune` is subtraction; the surrounding skills supply restraint, judgment, and
learning on the same axis.

- **[`restraint`](../restraint/SKILL.md)** — prevents over-engineering and scope creep *before* work is
  created. Use it to keep the initial design or plan minimal. `prune` is the
  after-side of the same principle: when a plan, design, or workspace has
  already grown beyond what is needed, `restraint` alone cannot shrink it —
  trimming what has accumulated is `prune`'s job.
- **[`align`](../align/SKILL.md)** — decides whether a document is current, superseded, or archival,
  and keeps references consistent when knowledge changes. Use it to label and
  identify documents that are genuinely outdated before deleting them, so that
  `prune` only acts on material whose stale status is established rather than
  assumed. `align` judges; `prune` removes.
- **[`distillation`](../distillation/SKILL.md)** — turns execution experience into durable lessons and
  decides whether a skill should change. Run it to capture what `prune` revealed
  about recurring clutter — which mistakes appear again and again — and feed the
  lesson back instead of repeating the same cleanup each cycle.

The distinction that separates them is *when the judgment happens*: `restraint`
and `align` prevent or clarify before removal; `prune` carries out verified
subtraction; `distillation` makes the pattern reusable. Together they keep work
minimal, current, and self-improving.

## Design decisions and trade-offs

- **Naming stays `prune`.** The word already means "cut the excess from a
  living thing", which fits both removing files and trimming a plan. Renaming to
  a more abstract term (for example "minimize" or "subtract") would have signalled
  the unified principle more literally, but at the cost of a new identifier and
  a loss of the concrete gardening image; the existing name was kept.
- **One skill beats two on trigger clarity.** Splitting file cleanup from plan
  trimming would give each a cleaner `description`, but the two share a single
  decision moment (carrying less forward before a sync, a plan, or a landing)
  and identical safety rules. One entry point reduces the chance an agent picks
  the wrong half or misses the shared judgment.
- **The `description` favours brevity over completeness.** Trigger discovery
  reads the `description`, so it stays short and names the recurring moments
  ("syncing, planning, or landing decisions") at the cost of not enumerating
  every file or clutter variety; the full scenario list lives in the body, where
  a triggered agent reads it. This is a deliberate trade-off of exhaustiveness
  for signal. An earlier, longer trigger sentence was dropped after review found
  it too long to be carried reliably.
- **Reference and published content is protected by default.** The strongest
  risk pruning poses is deleting something that looks outdated but is still
  load-bearing — a current plan mistaken for an old one, or a retrospective
  someone still mines for lessons. Making these protected by default, removable
  only on explicit request, biases the skill toward under-removal, which is the
  safe direction for irreversible action.
- **Distinction is written as skill roles, not `restraint`'s timing.** In the
  bundle, `restraint` is the discipline applied *before* creating work and
  `align` judges staleness *before* removal. The `README` can name those skills
  because it is for human readers; the `SKILL.md` body deliberately stays
  self-contained and references no sibling skill, so the executable guidance
  does not depend on which skills are installed.

## Sources and evidence

The reasoning above comes from this workspace's own history rather than
external sources. The unified-subtraction conclusion follows from reviewing the
skill draft against its sibling playbooks in this bundle and finding the two
candidate domains shared the same judgment and safety rules. The "never delete
a current or in-flight plan" and "do not drop retrospective or published
content without an explicit request" rules were added in direct response to
review feedback. The shortened `description` reflects review feedback that the
longer trigger sentence was too verbose to be a reliable trigger. Where this
rationale conflicts with future evidence, the design should change; this file
should then be updated so the recorded decision does not go stale.
