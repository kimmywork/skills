---
name: bootstrapping
description: Start a new project — establish its conventions, principles,
structure, and infrastructure. Use when setting up a new repository or
project skeleton: deciding what to create, then generating the agreed
artifacts. For existing projects, scan the workspace first to discover
what already exists before recommending additions. Works for software
projects and general knowledge work.
---

# Bootstrapping

Guide a project from intent to a working skeleton. Decide what to
build, then generate it.

## Workflow

1. **Probe / Scan.** If the project already exists, scan the workspace
   first — read existing README, AGENTS.md, CONTRIBUTING.md, .gitignore,
   CI/CD config, directory structure, and any conventions already in
   place. Summarize what exists and what is missing. If the project is
   new, probe the user for project type, scale, tech stack, and existing
   preferences, style guides, or conventions.
2. **Recommend.** Based on the scan or probe results, propose a set of
   artifacts to create and their priority (P0-P3). For existing projects,
   skip artifacts already present. Read `references/project-artifacts.md`
   for the catalog.
3. **Confirm.** Align the scope with the user. Let the user choose which
   artifacts to create and adopt or override the recommended principles.
4. **Generate.** Create the agreed artifacts, one at a time. Apply the
   principles in `references/core-principles.md`, the conventions in
   `references/software-conventions.md` for software projects, and the
   artifact catalog in `references/project-artifacts.md`.

## References

- `references/core-principles.md` — Universal principles: SMART, Occam's
  Razor, YAGNI, Chesterton's Fence, DRY vs WET, Postel's Law, Gall's Law,
  Linus's Law, etc.
- `references/project-artifacts.md` — Artifact catalog by priority (P0-P3),
  with purpose, audience, and suggested content for each.
- `references/software-conventions.md` — Software-specific conventions:
  commit style, branching, CI/CD, testing, coding standards, architecture
  principles.

## Constraints

- Apply restraint: only create artifacts that match the project's current
  scale and the user's confirmed needs. Do not generate P2/P3 artifacts
  for a small project.
- If the user has existing preferences, style guides, or conventions, use
  them. The reference files are suggestions, not requirements.
- Generate one artifact at a time, confirm with the user before moving to
  the next.