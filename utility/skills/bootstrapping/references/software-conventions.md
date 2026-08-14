# Software Conventions

Software-specific conventions for commit, branching, CI/CD, testing, architecture, and coding standards. Apply only when the project type is software.

## Commit convention

Use Conventional Commits with SemVer:

```
<type>(<scope>): <description>

[optional body]

[optional footer: BREAKING CHANGE, Closes #NNN]
```

Types: feat, fix, chore, docs, refactor, test, style, perf, ci, build. Breaking changes: add `BREAKING CHANGE` footer or `!` after type/scope. Scope: the module or area the change affects (optional).

## Branch strategy

- `main`: production-ready, protected
- `develop`: integration branch (optional for small projects)
- `feature/<name>`: branched from main/develop
- `fix/<name>`: bug fixes
- `hotfix/<name>`: urgent production fixes (branched from main)

Use Git Worktrees for parallel development without stashing.

## CI/CD

- **CI:** Run on every push to any branch. Steps: lint → type check → unit test → build. Fail fast on first error.
- **CD:** Run on push to main or tagged release. Steps: CI → integration test → deploy staging → (manual approval) → deploy production.
- **Quality gates:** No lint warnings, no type errors, all tests pass, coverage threshold (set per project, minimum 70%).

## Testing strategy

- **Unit tests:** Cover individual functions and modules. Fast, isolated. Aim for 80%+ coverage of core logic.
- **Integration tests:** Cover module interactions, API endpoints, and database access. Use test fixtures, not production data.
- **E2E tests:** Cover critical user journeys. Minimal set, slow, run nightly or pre-release.
- **Static analysis & linting:** Run a language-appropriate static analyzer and linter on every change (ESLint, Ruff, Pylint, golangci-lint, etc.). Fail the gate on warnings.
- **Style checks:** Enforce the project style guide with an auto-formatter (Prettier, Black, gofmt, clang-format, etc.) and a style check in CI.

## Architecture principles

Apply the principles in `core-principles.md` — SOLID, YAGNI, DRY vs WET, SoC, LoD, Chesterton's Fence, Fail Fast. Software-specific additions:

- **SRP:** one file, one responsibility.
- **YAGNI:** add interfaces only when a second implementation exists.

## Coding standards

- **Naming:** PascalCase for types/classes, camelCase for functions/variables, UPPER_CASE for constants, kebab-case for files. Adjust for language conventions.
- **Style:** Use the project's language-specific style guide (Google Style Guide for most languages, PEP 8 for Python, etc.). Enforce with auto-formatter.
- **Type checking:** Use static typing (TypeScript, mypy, etc.). Run type checker in CI.
- **Comments:** Explain *why*, not *what*. Code expresses the *what*. Update comments when code changes.

## Code review

Follow Google's Code Review best practices:
- Reviewers: check design, functionality, complexity, tests, naming, comments, style, documentation.
- Authors: keep changes small and focused. Respond to comments promptly.
- Use Conventional Comments format: `suggestion:`, `issue:`, `question:`, `nitpick:`, `praise:`.
- One review round should take < 24 hours for small PRs.