# Rename / Terminology Change Checklist

Use when changing a term or name across the skill family. Prevents the common failure of partial rename — updating some files while leaving others with the old term.

## Before the rename

- [ ] Inventory all files containing the old term:
  ```bash
  grep -rn "<old-term>" ./ --include="*.md" --include="*.json"
  ```
- [ ] Classify each hit: to-rename / intentional / false positive.
- [ ] Confirm the new term does not already appear in the codebase in a conflicting meaning.

## After the rename

- [ ] Re-grep for the old term — confirm zero relevant hits.
- [ ] Check each file category:
  - SKILL.md files (all `skills/delivery/*/SKILL.md`)
  - Reference files (`skills/delivery/*/references/*.md`)
  - README files (`skills/delivery/README.md`)
  - Template files (`skills/delivery/*/references/*template*.md`)
  - Config/JSON files (`.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `.agents/plugins/marketplace.json`)
- [ ] Classify any remaining hits: intentional (e.g., comparison table) / false positive / needs fix.

## Verification

- [ ] For self-review: confirm each "✅" claim with actual file evidence (grep output or specific line reference).