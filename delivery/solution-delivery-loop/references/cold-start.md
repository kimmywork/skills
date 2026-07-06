# Cold Start

Use when a workspace has no delivery-loop structure yet.

## Process

1. Inspect existing workspace sources: project docs, existing artifacts, source repositories (if present), data/document stores, external references, conventions, and verification mechanisms.
2. For software deliverables, also inspect code layout, tests, package scripts, CI, and conventions.
3. Identify whether the current task is simple, normal feature, multi-project, or broad requirements-doc-level work.
4. Propose the minimal doc layout needed:

```text
.agents/loop-state.md              # optional workspace-level loop state
docs/track/                        # feature/bugfix delivery tracks
docs/knowledge/                    # cross-feature durable knowledge
docs/logs/YYYY-MM-DD.md            # operational work logs
```

5. Ask before creating folders/files unless the user has already approved setup.
6. For the current task, create the smallest appropriate track note.
7. Record discovered verification methods, reusable commands, and conventions in the track note or `docs/knowledge` only when they will be reused.

## Minimal first track

- Problem / goal
- Scope
- Non-goals
- Acceptance criteria
- Verification plan
- Next action

Avoid bootstrapping a large documentation system before there is real work to anchor it.
