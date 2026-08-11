# Templates & Directory Structure

Reference material for organizing investigation outputs. Read this when starting a new investigation and need scaffolding.

---

## Recommended Directory Structure

```
{investigation-root}/
├── 00-scope/          ← Task input: questions, scope boundaries, source plan
├── 01-sources/        ← Raw material: collected references, notes, data samples
├── 02-analysis/       ← Core findings: evidence tables, claim matrices, flow maps
├── 03-synthesis/      ← Cross-cutting conclusions: findings, gaps, recommendations
├── 04-report/         ← Final deliverable for stakeholders
└── 05-review/         ← Review feedback and revision records
```

Scale to fit: small investigations need only `scope + analysis + report`.

---

## Source Record Template

Use for each source examined during the investigation.

```markdown
## Source: <title or identifier>

- **Type**: code / document / web / data / expert / experiment
- **Origin**: <URL, file path, expert name, data location>
- **Accessed**: <date>
- **Confidence**: confirmed / cross-referenced / inferred / asserted / from-agent-knowledge

### Key Content

<what the source says, direct quotes or key data points>

### Relevance

<how this source contributes to the investigation question>
```

---

## Claim Matrix Template

Use for tracking each claim, its evidence, and gaps.

```markdown
| Claim | Confidence | Supporting sources | Conflicting sources | Gaps |
|---|---|---|---|---|
| <claim> | <label> | <source references> | <if any> | <what's unknown> |
```

---

## Synthesis Report Template

Use for the final deliverable.

```markdown
# Investigation: <Topic>

## Question

<the investigation question>

## Method

<how the investigation was conducted: sources examined, approach, limitations>

## Findings

<key findings, organized by theme or question>

### Finding 1: <title>

- Evidence: <source references>
- Confidence: <label>
- Gaps: <what remains unclear>

### Finding 2: ...

## Implications

<what the findings mean>

## Recommendations

<actionable next steps if applicable>

## Open Questions

- <what could not be resolved>
```

---

## Code/Data Flow Template (mode-specific)

Use when investigating code or data systems. Use the field/type table for each entity or flow.

```markdown
## {Entity/Flow Name}

> Source: `module/path/filename`
> Persistence/Transport: <how it is serialized, transported, stored, or consumed>
> Confidence: confirmed / cross-referenced / inferred / asserted / from-agent-knowledge

| Field | Type | Source | Description | Notes |
|-------|------|--------|-------------|-------|
| ...   | ...  | ...    | ...         | ...   |

**Edge cases:**
- {Invalid value handling}
- {Fields skipped during serialization}
- {Differences from other systems}
```

---

## Work Log Entry Template

```markdown
### {Date} — {Phase/Event}

**Completed:** What was done
**Key findings:** 3-5 most important conclusions
**Problems encountered:** Where things got stuck, which assumptions were invalidated
**Output files:** Which documents were created or updated
```

---

## Research Record Template

Use for preserving raw material under `docs/track/<feature>/research/`.

```markdown
# Research Record: <Topic>

## Metadata
- **Date**: <date>
- **Source type**: code / web / document / data / expert / experiment
- **Confidence**: confirmed / cross-referenced / inferred / asserted / from-agent-knowledge

## Source
- <URL, file path, expert name>
- Accessed: <date>

## Finding
<what was found>

## Evidence
<direct quote, screenshot, data sample>

## Cross-references
- <related findings or sources>

## Open questions
- <what remains unclear>
```