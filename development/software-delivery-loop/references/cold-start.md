# Cold Start

Use when a workspace has no delivery-loop structure yet.

## Process

1. Inspect existing project docs, code layout, tests, package scripts, CI, and conventions.
2. Identify whether the current task is simple, normal feature, multi-project, or broad PRD-level work.
3. Propose the minimal doc layout needed:

```text
.agents/loop-state.md              # optional workspace-level loop state
docs/track/                        # feature/bugfix delivery tracks
docs/knowledge/                    # cross-feature durable knowledge
docs/logs/YYYY-MM-DD.md            # operational work logs
```

4. Ask before creating folders/files unless the user has already approved setup.
5. For the current task, create the smallest appropriate track note.
6. Record discovered commands and conventions in the track note or `docs/knowledge` only when they will be reused.

## Minimal first track

- Problem / goal
- Scope
- Non-goals
- Acceptance criteria
- Verification plan
- Next action

Avoid bootstrapping a large documentation system before there is real work to anchor it.
