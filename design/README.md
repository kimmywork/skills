# Design

A bundle for design quality and audience-facing communication.

## Skill inventory

| Skill | Purpose |
|---|---|
| [`design`](skills/design/SKILL.md) | Build, extract, rebuild, or govern a design system; review a product or design artifact and produce an issue register, fix plan, and guard rules. |
| [`presentation`](skills/presentation/SKILL.md) | Create a live, written, or hybrid presentation — talk, sharing session, demo, panel, pitch, workshop, report, or one-pager — with narrative, language, timing, visual, and accessibility discipline. |

## Design

- **One capability per skill:** `design` owns design quality; `presentation` owns audience-facing communication. References stay inside each skill.
- **Evidence over invention:** recovered values carry their path; findings carry evidence; designed values are marked.
- **Traceable reasoning:** stance → principle → rule → token/behavior → check; finding → criterion → evidence → acceptance.
- **Hints, not encyclopedias:** references are short prompt packs; `checklist.md` is the only full coverage sweep.
- **System and review are directions, not separate skills:** the same standards govern both.
- **Presentation consumes, does not own:** it uses an existing design system when one exists; otherwise it starts from `skills/presentation/references/minimal-visual-system.md` as an adaptable example and adjusts it to the topic, setting, audience, and medium. It does not force a dependency on the `design` skill.

## Validation

```bash
for f in design/skills/*/SKILL.md; do
  test "$(wc -l < "$f")" -le 100 || echo "$f too long"
  rg -n '[一-龥]' "$f" && echo "$f contains Chinese characters"
done
```

Also verify that plugin JSON parses, every `references/...` path exists inside its skill, and `.agents/skills` symlinks resolve.

## Migration

`design-system` moved here from the `drafting` bundle. Its surface references now live in `skills/design/references/`; the skill itself is `design`.
