# Review Feedback Report

## Metadata

- **Reviewer**: self-performed
- **Phase reviewed**: implementation-execution
- **Artifacts inspected**:
  - `loop/skills/loopy/scripts/loopy.py`
  - `loop/skills/loopy/SKILL.md`
  - `loop/skills/loopify/SKILL.md`
  - `loop/skills/loopy/references/workflow-format.md`
  - `loop/skills/loopy/references/setup.md`
  - `loop/skills/loopify/references/grilling-checklist.md`
  - `loop/.claude-plugin/plugin.json`, `loop/.codex-plugin/plugin.json`
  - `.agents/plugins/marketplace.json`, `.claude-plugin/marketplace.json`
  - `.gitignore`
- **Prior phases considered**: requirements-v2.md, solution-design-v2.md, change-note-001, research/grilling-resolutions.md
- **Review date**: 2026-07-07

## Summary

- **Total issues**: 6
- **Critical**: 0
- **Major**: 1
- **Minor**: 5
- **Fix-in-place**: 6
- **Roll-back**: 0
- **Verdict**: **conditional-pass** — one major issue (script error handling quality) that should be fixed before final acceptance. All others are minor polish.

---

## Issues

### Issue 1: Bare `except` clauses suppress SystemExit and KeyboardInterrupt

| Field | Value |
|---|---|
| **Origin phase** | implementation |
| **Severity** | major |
| **Type** | incorrect |
| **Description** | Four functions (`create_state_file`, `create_skipped_state_file`, `save_trigger_output`, `write_dispatch_log`) use bare `except:` to clean up temp files on failure. Bare `except:` catches ALL exceptions, including `SystemExit`, `KeyboardInterrupt`, and `GeneratorExit`. If a user hits Ctrl+C during a state file write, the cleanup runs but the script can't be interrupted cleanly. |
| **Evidence** | `loopy.py` lines 152-155, 179-182, 278-281, 325-328: `except: if os.path.exists(tmp): os.unlink(tmp); raise` |
| **Suggested fix** | Replace all 4 instances of `except:` with `except Exception:` — catches recoverable errors but allows interrupts to propagate. |
| **Resolution** | fix-in-place |

### Issue 2: `IOError` alias used instead of `OSError`

| Field | Value |
|---|---|
| **Origin phase** | implementation |
| **Severity** | minor |
| **Type** | inconsistent |
| **Description** | `read_all_workflows()` catches `IOError`. In Python 3.3+, `IOError` was merged into `OSError`. While `IOError` still works as an alias, modern Python code should use `OSError`. This is a code quality issue, not a functional one. |
| **Evidence** | `loopy.py` line 63: `except (ValueError, yaml.YAMLError, IOError) as e:` |
| **Suggested fix** | Replace `IOError` with `OSError`. |
| **Resolution** | fix-in-place |

### Issue 3: loopy SKILL.md script path is vague

| Field | Value |
|---|---|
| **Origin phase** | implementation |
| **Severity** | minor |
| **Type** | unclear |
| **Description** | The SKILL.md says "Run the script: `python3 <skill-root>/scripts/loopy.py`" using `<skill-root>` as a placeholder. The agent knows its own skill directory (relative to the SKILL.md file location), so the path is discoverable, but the instruction is imprecise. |
| **Evidence** | `loop/skills/loopy/SKILL.md` step 1 |
| **Suggested fix** | Change to: "Run the script at `scripts/loopy.py` (path relative to this SKILL.md) from the project root." |
| **Resolution** | fix-in-place |

### Issue 4: loopy SKILL.md doesn't tell agent to check `script_errors` before executing

| Field | Value |
|---|---|
| **Origin phase** | implementation |
| **Severity** | minor |
| **Type** | missing |
| **Description** | The SKILL.md explains how to parse the dispatch JSON's `due`, `script_errors`, and `not_due` arrays, but doesn't instruct the agent what to do with `script_errors`. If there are script errors (YAML parse failure, trigger timeout), the agent should investigate and possibly report them before proceeding to execute due workflows. |
| **Evidence** | `loop/skills/loopy/SKILL.md` step 2 |
| **Suggested fix** | Add a note after step 2: "If `script_errors` is non-empty, investigate and resolve those workflow setup issues before executing due workflows." |
| **Resolution** | fix-in-place |

### Issue 5: loopy SKILL.md doesn't reference `workflow-format.md` for body conventions

| Field | Value |
|---|---|
| **Origin phase** | implementation |
| **Severity** | minor |
| **Type** | missing |
| **Description** | The SKILL.md tells the agent to read the workflow body from `workflows/<name>.md`, but doesn't reference `references/workflow-format.md` for body conventions (success condition, free-form format, goal-only bodies per REQ-011). The reference list has `workflow-format.md` but the execution steps don't mention consulting it. |
| **Evidence** | `loop/skills/loopy/SKILL.md` step 3a, references list |
| **Suggested fix** | In step 3a, append: "Refer to `references/workflow-format.md` for body conventions and success condition expectations." |
| **Resolution** | fix-in-place |

### Issue 6: `--run` mode silently drops non-error, non-targeted workflows from dispatch log

| Field | Value |
|---|---|
| **Origin phase** | implementation |
| **Severity** | minor |
| **Type** | scope |
| **Description** | When `--run <name>` is used, non-targeted workflows that have no trigger errors are silently dropped (`return None`). They don't appear in `not_due` or any other dispatch array. The dispatch log therefore shows an incomplete picture for that invocation. This is acceptable for the user-facing stdout output (focused on the force-run), but the dispatch log should ideally record that other workflows were present but skipped. |
| **Evidence** | `loopy.py` lines 353-360: `elif force_name: ... if has_trig: ... return None` |
| **Suggested fix** | Minor scope issue — the dispatch log is already present for scheduled invocations, and `--run` is an ad-hoc tool. Current behavior is acceptable. Log for awareness; no fix needed unless consistency is important for the dispatch log archive. |
| **Resolution** | fix-in-place (optional — see suggestion) |

---

## Fix-in-place items

| # | Item | Severity | Producer |
|---|---|---|---|
| 1 | Replace bare `except:` with `except Exception:` in 4 locations | major | script |
| 2 | Replace `IOError` with `OSError` | minor | script |
| 3 | Clarify script path instruction in loopy SKILL.md | minor | SKILL.md |
| 4 | Add `script_errors` guidance to loopy SKILL.md | minor | SKILL.md |
| 5 | Reference `workflow-format.md` in loopy SKILL.md step 3a | minor | SKILL.md |
| 6 | `--run` dispatch log completeness (optional) | minor | script |

No rollback needed.

---

## Positive observations

1. **Contract fidelity is high.** The state file schema, dispatch output schema, and NNN sequence all match the requirements and design documents exactly. No drift.
2. **All edge cases tested.** Empty dispatch, trigger fires, empty output, non-zero exit, timeout, parse errors, collision detection, force-run, list — each verified with real script runs during implementation.
3. **SKILL.md line counts** are well within the 100-line limit (38 and 33 lines). Both are focused and readable.
4. **Atomic writes** implemented correctly via temp-file-rename pattern in all file-writing functions.
5. **Trigger output isolation** via temp files keeps the dispatch JSON lean, matching the design intent.
6. **Error isolation** between workflows is correct — one workflow's trigger failure doesn't block others from dispatching.

---

## Open questions

None.