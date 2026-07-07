# Mode Spectrum

Mode controls how much structure, template load, and verification pressure to apply. Choose mode by risk and cognitive shape, not by deliverable name.

## Modes

| Mode | Template load | Use when | Main risk | Control |
|---|---|---|---|---|
| Fidelity | Heavy | audits, compliance, bug fixes, citations, format conversion, safety-critical work | overfitting to checklist | allow explicit fast-pass only with reason |
| Balanced | Medium | default for scoped implementation, reports, docs, plans | missing domain-specific constraint | load core criteria and one relevant reference |
| Originality | Light | open-ended investigation, concepting, creative exploration | vague output without criteria | shape constraints and acceptance before finalizing |

## Defaults by kind

| Kind | Default | Override |
|---|---|---|
| Crafting | Balanced | Fidelity for fixes/migrations; Originality for architecture exploration |
| Composing | Balanced | Fidelity for regulated docs; Originality for creative briefs |
| Evaluating | Fidelity | Use Originality only for exploratory critique requested by user |
| Investigating | Originality | Use Fidelity for systematic review, legal, scientific, or source-critical work |
| Creating | Originality | Use Balanced when a concrete production brief exists |

## Reference loading

- Fidelity: load rubrics, schemas, templates, and acceptance checklists before work.
- Balanced: load the phase template, criteria, and one domain reference.
- Originality: ask better questions first; delay heavy templates until Shape converges.

## Mode changes

A mode change is allowed when evidence shows the current mode is wrong:
- Fidelity -> Balanced when checklist overhead blocks simple work.
- Balanced -> Fidelity when verification risk rises.
- Originality -> Balanced when the creative direction becomes a deliverable.
- Any mode -> Clarify when user intent changes.

Record mode changes in the handoff.
