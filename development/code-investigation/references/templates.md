# Templates & Directory Structure

Reference material for organizing investigation outputs. Read this when starting a new investigation and need scaffolding.

---

## Recommended Directory Structure

```
{investigation-root}/
├── 00-intake/        ← Task input: requirements, constraints, initial questions
├── 01-plan/          ← Investigation plan: steps, priorities, timeline
├── 02-materials/     ← Collected references: existing docs, meeting notes, screenshots
├── 03-analysis/      ← Core findings: code structure, data models, protocols, flows
│   ├── {domain-a}/   ← Organized by domain/module/system
│   └── {domain-b}/
├── 04-synthesis/     ← Cross-cutting conclusions: mappings, diffs, proposed solutions
├── 05-reports/       ← Final deliverables for different audiences
├── 06-reviews/       ← Cross-review feedback and revision records
└── 07-logs/          ← Work log: daily progress, discoveries, corrections, reflections
```

**Directory roles:**

| Directory | Content | Audience |
|-----------|---------|----------|
| `00-intake` | Why and What: investigation goals, success criteria, business constraints | Everyone |
| `01-plan` | How: step breakdown, priorities, resource allocation | Investigators |
| `02-materials` | External inputs (not authored by you): existing docs, email excerpts, diagrams | Investigators |
| `03-analysis` | **Core deliverable**: per-domain analysis results, data models, flow diagrams | Technical team |
| `04-synthesis` | Cross-domain conclusions: system mappings, diff tables, technical proposals | Decision makers |
| `05-reports` | Audience-specific final deliverables: executive summary, detailed report | Stakeholders |
| `06-reviews` | Review feedback and revision tracking | Investigators |
| `07-logs` | Process record: daily log, error corrections, reflections | Future self / handoff |

Scale to fit: small investigations need only `plan + analysis + report + log`.

---

## Analysis Document Template

Use this for each data entity or flow documented in `03-analysis/`:

```markdown
## {Entity/Flow Name}

> Source: `module/path/filename`
> Persistence/Transport: {how it's serialized, stored, or sent}
> Confidence: Confirmed / Inferred (needs verification)

| Field | Type | Source | Description | Notes |
|-------|------|--------|-------------|-------|
| ...   | ...  | ...    | ...         | ...   |

**Edge cases:**
- {Invalid value handling}
- {Fields skipped during serialization}
- {Differences from other systems}

**Open questions:**
- {What couldn't be verified and why}
```

---

## Work Log Entry Template

```markdown
### {Date} — {Phase/Event}

**Completed:** What was done (which modules read, what was discovered)
**Key findings:** 3-5 most important conclusions
**Problems encountered:** Where things got stuck, which assumptions were invalidated
**Reflection:** Why the error happened, what the correct approach should have been
**Output files:** Which documents were created or updated
```

---

## Multi-Perspective Review Template

For each reviewer perspective, structure feedback as:

```markdown
## {Perspective} Review

**Score:** X/10
**Justification:** {why this score}

### P0 Issues (blockers)
- ...

### P1 Issues (important)
- ...

### P2 Suggestions (nice-to-have)
- ...

### Conflicting Recommendations
- {where this perspective conflicts with another, and suggested resolution}
```
