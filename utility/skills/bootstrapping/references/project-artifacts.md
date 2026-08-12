# Project Artifacts

Artifact catalog by priority (P0-P3). Each entry includes its purpose, audience, and suggested content. For existing projects, skip artifacts already present.

## P0 — Must have

| Artifact | Purpose | Audience | Content |
|---|---|---|---|
| README.md | Project identity, install, use, develop | Everyone | Elevator pitch, tech stack, quick start, dev setup, link to docs |
| .gitignore | Ignore build artifacts, deps, secrets | Git | Language/OS/IDE defaults |
| LICENSE | Code copyright, use boundaries, copyleft | Legal / community | Chosen license full text |
| AGENTS.md | Agent project briefing | AI agents | Structure, conventions, constraints, skills, MCP |
| Directory structure | Where to put what | All contributors | src/, tests/, docs/, scripts/ |
| Lint/format config | Automated code quality | CI / dev | ESLint, Prettier, ruff, etc. |

## P1 — Establish early

| Artifact | Purpose | Audience | Content |
|---|---|---|---|
| CONTRIBUTING.md | Contribution workflow | Contributors | Commit convention, branch strategy, PR process, review expectations |
| CI pipeline | Automatic test + lint on push | CI system | .github/workflows/ci.yml or equivalent |
| docs/ directory | Knowledge base | Contributors | ADR, architecture notes, domain models, contracts |
| ADR template | Architecture decision record | Contributors | Context, decision, consequences, status |
| Test framework config | Run tests | Test runner | Jest, pytest, vitest, etc. |
| Coding conventions | Style, naming, file organization | Contributors | Language/team-specific rules |

## P2 — Add with scale

| Artifact | Purpose | Audience | Content |
|---|---|---|---|
| Issue/PR templates | Structured issue and PR submission | Contributors | .github/ISSUE_TEMPLATE/, .github/PULL_REQUEST_TEMPLATE.md |
| Review checklist | Spec Fit + Format Fit checklist | Reviewers | Acceptance criteria, quality gates |
| CHANGELOG.md | Release notes | Users / contributors | Keep a Changelog format |
| CD pipeline | Automatic deploy | CI system | .github/workflows/deploy.yml |
| MCP config | Agent tool access | Agent runtime | .mcp.json |
| Skills directory | Agent skill definitions | Agent | skills/<name>/SKILL.md |

## P3 — Large / multi-agent projects

| Artifact | Purpose | Audience | Content |
|---|---|---|---|
| Multi-agent orchestration | Agent role boundaries | Agents | Task delegation, tool permissions, escalation rules |
| Security review process | Vulnerability scanning | Security | OWASP checklist, dependency audit |
| Skills lock file | Skill version pinning | Agent runtime | skills-lock.json |
| Code of Conduct | Community behavior baseline | Community | CODE_OF_CONDUCT.md |
| Governance model | Project decision-making | Maintainers | GOVERNANCE.md |