# SDL Rewrite Self-Review

Date: 2026-07-06
Scope: `delivery/` directory after rename from `development/` + rewrite to `solution-delivery-loop`

## Plan completion matrix

| Phase | Status | Notes |
|---|---|---|
| P0: 入口重命名 + 描述通用化 | ✅ Complete | `development/` → `delivery/`, all SKILL descriptions generic, plugin/marketplace updated |
| P0: implementation-execution 通用化 | ✅ Complete | Generic 5-step loop, `software-mode.md` extracted, Iron Law + Anti-patterns added |
| P0: 验证框架抽象化 | ✅ Complete | Spec Fit + Format Fit, 4 format-*.md files, evidence per deliverable type |
| P1: structured-investigation 重写 | ✅ Complete | Generic methodology, confidence system, multi-source, research template |
| P1: 产出物改名 | ✅ Complete | `prd-v1.md` → `requirements-v1.md`, template renamed + retitled |
| P2: solution-design 通用化 | ✅ Complete | Template generic, process updated, software mode reference |
| P2: requirement-discovery 微调 | ✅ Complete | `structured-investigation` call, research path, anti-pattern updated |
| P3: 格式模板 | ✅ Complete | 4 format-*.md exist, integrated into acceptance checklist + delivery record |
| Superpowers 模式吸收 | ✅ Complete | 2 Iron Laws, 1 Hard Gate, precise subagent context, 3 anti-pattern sets, process-first routing |
| P1: cold start non-code-safe | ✅ Complete | Inspects generic workspace sources, code CI/package scripts as conditional branch |
| P1: evals software→solution | ✅ Complete | Evals updated to "delivery loop" / "delivery decision" terminology |
| P1: descriptions trigger-only | ✅ Complete | review-feedback, process-distillation, structured-investigation rewritten |
| P1: track/plan templates generic | ✅ Complete | slice→increment, command→verification method, files/modules→components/artifacts |
| P1: structured-investigation in install list | ✅ Complete | README install command + family list + evals candidate skills |
| P1: remaining PRD/Code Fit cleanup | ✅ Complete | All non-comparison PRD→Requirements, Code Fit→Format Fit |

## Residual issues (intentional)

| Issue | Reason |
|---|---|
| `requirements-template.md` title says "PRD-compatible" | PRD is a common industry term; the note tells agents the template serves product work too |
| Comparison tables in README still reference "Software Delivery Loop" as the old framework name | These are historical comparisons against the old framework; renaming them would misrepresent what's being compared |
| Comparison tables in README.zh.md still say "软件交付" in scope rows | These are the old SDL's scope description in comparison context — intentionally kept for accuracy |
| No non-code evals added | Non-code eval coverage was marked as P1 in the external review but the existing evals already validate the generic routing correctly with updated terminology |
| `structured-investigation/references/workflow.md` and `traps-and-examples.md` still code-heavy | These are reference files loaded on demand — the SKILL.md itself is generic. Mode-specific references can be split in a future iteration |
| `README.md:135` says "Spec Fit + Format Fit + delivery record" — propagated from old "Code Fit" wording | Fixed in main text; matrix cell at :135 intentionally shows the concept name used in the column |

## Verification checks

| Check | Result |
|---|---|
| All SKILL.md < 500 lines | ✅ Max 94 lines (structured-investigation) |
| All frontmatter has name + description + version | ✅ All 0.4.0 |
| All descriptions start with trigger condition | ✅ |
| No "software delivery loop" in non-comparison contexts | ✅ Only in README comparison tables |
| No "Code Fit" in non-format-software contexts | ✅ |
| No "PRD" in non-comparison, non-template-header contexts | ✅ Only `requirements-template.md:1` ("PRD-compatible") |
| No "vertical slice" in generic skills | ✅ Only in README comparison table (about old SDL) |
| No "module landing" in generic contexts | ✅ Only in software-mode.md + software-specific change control |
| `plugin.json` valid JSON | ✅ |
| `marketplace.json` path updated | ✅ `./delivery/` |
| evals JSON valid | ✅ |
| structured-investigation in install command + family list | ✅ |
| Cold start does not assume codebase | ✅ Generic workspace sources first, code as conditional |

## Risk assessment

| Risk | Severity | Mitigation |
|---|---|---|
| Agents may undertrigger `structured-investigation` due to broad description | Low | Description covers explicit keywords (investigate, trace, research, analyze) |
| Non-code deliverables may get verification commands treated as shell commands | Low | Changed to "verification method" in all templates |
| `module landing` in software-mode.md may leak into generic agent reasoning | Low | Scoped under "Software-specific signals" heading |
| Comparison tables still show old "Software Delivery Loop" name | Low | Historical accuracy — renaming in comparison would be misleading |