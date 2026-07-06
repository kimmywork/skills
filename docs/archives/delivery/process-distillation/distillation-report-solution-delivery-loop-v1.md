# Process Distillation Report: solution-delivery-loop

## Metadata

- **Phase analyzed**: solution-delivery-loop (全局 loop 编排)
- **Skills involved**: solution-delivery-loop, implementation-execution, solution-design, requirement-discovery, delivery-acceptance, review-feedback, process-distillation
- **Source evidence**: tracks/ 下 10 个子目录（agent47, claude-code-plans, clearsight-prd, constype-track, crm, mono-services-docs, myz-track, Nekopie, ng-design, zlf）约 80+ 文件，delivery/ 下 8 个 skill 的 SKILL.md
- **Analysis date**: 2026-07-06
- **Mode**: user-approval

## Summary

- **Gaps found**: 16
- **Improvements proposed**: 16
- **New skills proposed**: 0
- **Auto-approved**: 0
- **Pending approval**: 16

---

## Source Evidence Catalog

以下列出 distillation 分析所依据的具体 tracks 文件，按项目分组。

### agent47 (Decision Workspace)

| 文件 | 提供的证据 |
|------|-----------|
| `superpower-specs/2026-06-29-decision-workspace-design.md` | 产品设计文档，展示完整的 design→plan→report 闭环 |
| `superpower-specs/2026-06-30-fullscreen-workbench-refactor-design.md` | UI 重构设计，展示 product-surface refactor 模式 |
| `superpower-specs/2026-06-30-local-agent-execution-layer-design.md` | 执行层设计，展示 research→approval→execution lifecycle |
| `superpower-plans/2026-06-29-decision-workspace-mvp.md` | MVP 实现计划，8 个 Task，每个 Task 含 Step 1-5 TDD 循环 |
| `superpower-plans/2026-06-30-fullscreen-workbench-refactor.md` | UI 重构计划，4 个 Task，展示 route-shell 拆分模式 |
| `superpower-plans/2026-06-30-local-agent-execution-layer.md` | 执行层计划，5 个 Task，展示 lifecycle model + tool adapters |
| `sdd/task-2-report.md` | RED/GREEN/Final 三段式验证记录格式 |
| `sdd/task-3-report.md` | 多轮 fix + verification 的迭代记录格式 |
| `sdd/task-5-report.md` | E2E 验证 + compliance-gap follow-up 模式 |

### claude-code-plans

| 文件 | 提供的证据 |
|------|-----------|
| `buzzing-discovering-flute.md` | ClearSight 架构重构计划，展示 Phase 分解 + 依赖图模式 |
| `calm-whistling-scott.md` | Market Simulator 服务设计，展示 config-driven 架构模式 |
| `foamy-sniffing-ullman.md` | Flutter→KMP 迁移计划，展示技术栈映射表 + 分阶段迁移模式 |
| `immutable-greeting-panda.md` | myz-bot 重构计划，6 个 Phase，展示移除+新增的重构模式 |
| `memoized-tinkering-muffin.md` | Record→DataFrame 重构，8 个 Step，展示接口优先+渐进迁移模式 |

### crm (缘录)

| 文件 | 提供的证据 |
|------|-----------|
| `discussion-summary.md` | 3 轮需求细化过程，10 个设计决策（D1-D10） |
| `personas-and-journeys.md` | 5 个 Persona，8 个 Journey Map，14 个场景 |
| `PRD-yuanlu.md` | v1 PRD：46 个需求项，含目标/非目标/术语/场景/需求清单/数据模型 |
| `PRD-yuanlu-v2.md` | v2 PRD：架构从云优先→离线优先，含技术栈对比表 |
| `PRD-yuanlu-v3.md` | v3 PRD：架构从 Tauri→PWA，含 IndexedDB schema + PWA 配置 |
| `v1-yuanlu.md` | 执行计划：8 个 Phase，35 个 E2E 测试用例，DoD Gate |
| `value-proposition.md` | 价值分析：核心/增值/高级三层价值矩阵 |
| `value-proposition-v2.md` | v2 价值分析：离线优先架构带来的新价值维度 |

### ng (NG 编译器)

| 文件 | 提供的证据 |
|------|-----------|
| `ng-refactoring_plan_2026_06.md` | 6 Phase 重构计划，每 Phase 含依赖分析→Step 分解→测试策略→提交规范 |
| `ng-design/README.md` | 15 个设计提案索引，含 feasibility rating、cross-proposal dependencies、effort summary |
| `ng-design/gap-*.md` | 15 个语言特性 gap proposal，含动机/设计/范围/依赖/验收/工作量/可行性 |

### clearsight-prd

| 文件 | 提供的证据 |
|------|-----------|
| `clearsight-prd.md` | 完整 PRD：用户画像/功能需求/非功能需求/MVP 范围/迭代方向 |

### constype-track (交易所平台)

| 文件 | 提供的证据 |
|------|-----------|
| `v1-index.md` | v1 MVP 架构索引，含服务拆分/数据隔离/验收标准/change log |
| `v2-monolith-refactor.md` | 单进程重构计划，含 Current→Target 架构图、Phase 1-4 实施计划、Verification Criteria |
| `v3-architecture-refactor.md` | 多域单进程重构，含 crate 结构/依赖关系图/领域交互矩阵/12 个用户旅程/7 Phase 实施计划 |
| `roadmap-overview.md` | v1→v1.5→v2 路线图，含技术栈演进/资源需求/风险矩阵/成功指标 |
| `ECN-0001-architecture-simplification.md` | 架构简化变更通知 |

### myz-track (Agent 系统)

| 文件 | 提供的证据 |
|------|-----------|
| `PRD-agentic-workflow.md` | 完整 PRD：17 个需求项，含目标/非目标/术语/场景/需求清单/追溯矩阵/边界条件 |
| `v22-myz-agent-restructure.md` | 多包架构重构，含 Data Model/UX Flow/依赖边界/Phase 1-4 验收标准/Gap Review 12 项 |
| `v23-agentic-loop.md` | Agentic Loop 实现，含 5 Phase 实施/数据模型(Permission/Todo/Agent)/验收标准/风险/进度更新 |

### Nekopie (游戏开发)

| 文件 | 提供的证据 |
|------|-----------|
| `PROJECT.md` | Godot 4.3 deckbuilder 项目，含 implemented 列表/architecture notes/expansion roadmap |
| `CHANGELOG.md` | 152 行变更日志，按日期记录每次变更的具体内容 |

### mono-services-docs (Java Monorepo)

| 文件 | 提供的证据 |
|------|-----------|
| `README.md` | 项目结构说明，含 Gradle composite build/目录结构/构建命令 |
| `rfcs/` | 18 个 RFC 文档，含 why-rfcs/monorepo/grpc/integration-platform 等架构决策 |
| `track/` | 20 个版本 track 文档（v1-v20），含 HTTP HTMX foundation 到 notes wikilink 演进 |
| `TODO.md` | 开发任务跟踪，含 In Progress/To Do/Done 三段式 |

### zlf (图数据库)

| 文件 | 提供的证据 |
|------|-----------|
| `prd-v1.md` | 完整 PRD：828 行，含 query language 设计/数据模型/API/14 个需求项(含 Edge Cases + Unhappy Paths)/60+ 决策记录 |
| `solution-design-v1.md` | 方案设计：Alternative 对比/Crate 结构/依赖清单/Data Schema/API Contract/Query Execution Flow/Test Strategy |
| `plan-v1.md` | 实施计划：12 个 Slice，每个含 Acceptance covered/Files/Verification/Edge Cases/Unhappy Paths/Steps |
| `delivery-record-v1.md` | 交付记录：9 个已完成 Slice，含 tests count/evidence/Issues & Fixes/Architecture Decisions |
| `2026-07-06.md` | 工作日志：含 Blockers(napi-rs build failure)/Completed Work/Next Steps |

---

## Gaps and improvements

### Improvement 1: 补充工作类型路由——loop 缺少对重构/迁移/新功能的分流

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `ng-refactoring_plan_2026_06.md` 展示了纯重构工作（从代码现状出发，不从需求出发）；`foamy-sniffing-ullman.md` 展示了技术栈迁移工作（从映射表出发）；`buzzing-discovering-flute.md` 展示了功能增强工作（从架构问题出发）；`PRD-yuanlu.md` 展示了从零开始的新功能；`v2-monolith-refactor.md` 展示了从多进程→单进程的架构迁移（无 PRD，直接从 Vision + Scope 出发）；`v22-myz-agent-restructure.md` 展示了从 monolith→multi-package 的架构重构（从 Vision 出发，跳过 requirement-discovery）。当前 loop 的 First Move 路由只有 4 条（need→discovery, needs-design→design, executable→execution, done→acceptance），没有区分工作类型。 |
| **Proposed change** | 在 `solution-delivery-loop/SKILL.md` 的 `## First move` 之前新增 `## Work type triage` 段。内容：识别当前工作属于 new-feature / bugfix / refactor / migration / enhancement 中的哪种，不同类型决定 loop 的起始 phase 和跳过规则。重构和迁移类工作从 codebase analysis 开始，可跳过 requirement-discovery 直接进入 solution-design。 |
| **Target** | `delivery/solution-delivery-loop/SKILL.md` — 在 `## First move` 之前插入新段 |
| **Principles satisfied** | agent-neutral, scope-limited, user-centric |
| **Approval** | pending |

**具体改动内容**：

```markdown
## Work type triage

Before routing to a phase, identify the work type. Different types have different entry points.

| Work type | Entry point | Skip |
|---|---|---|
| new-feature | requirement-discovery | — |
| bugfix | implementation-execution (if clear) or requirement-discovery | solution-design for trivial fixes |
| refactor | solution-design (from codebase analysis) | requirement-discovery |
| migration | solution-design (from mapping table) | requirement-discovery |
| enhancement | requirement-discovery or solution-design (from known gap) | — |

For refactor/migration: the "requirements" are the current code state + target state. Read code first, then design the path.

For bugfix: if the bug is well-understood and the fix is small (< 50 lines, < 3 files), go directly to implementation-execution with a verification plan. Otherwise, use requirement-discovery to confirm scope.
```

---

### Improvement 2: 补充 incremental commit 模式——loop 缺少粒度控制

| Field | Value |
|---|---|
| **Gap type** | missing-guardrail |
| **Evidence** | `ng-refactoring_plan_2026_06.md` Step 1-6 每步都有 "测试：现有测试全部通过" + "提交规范"；`agent47 superpower-plans` 每个 Task 的 Step 5 都是 git commit；`v1-yuanlu.md` 每个 Phase 结束有验收标准+测试；`zlf/plan-v1.md` 每个 Slice 的 Verification 段包含具体命令+结果（如 `cargo test -p zlf-core → all tests pass`）；`zlf/delivery-record-v1.md` 每个 Slice 记录 tests count + evidence 命令。但 `implementation-execution` 的 execution loop 只说 "Define expected outcome → Produce → Verify → Refine → Record"，没有明确要求每个 increment 独立可提交。 |
| **Proposed change** | 在 `implementation-execution/SKILL.md` 的 `## Execution loop` 中，在步骤 5 之后新增步骤 6。 |
| **Target** | `delivery/implementation-execution/SKILL.md` — `## Execution loop` 新增步骤 6 |
| **Principles satisfied** | agent-neutral, size-controlled, scope-limited |
| **Approval** | pending |

**具体改动内容**：

在 `## Execution loop` 现有 5 步之后追加：

```markdown
6. **Commit the increment.** Ensure all existing tests pass before committing. Use the format: `<type>(<scope>): <description>`. Each increment should be independently committable and reversible.
```

---

### Improvement 3: 补充依赖驱动的 Phase 排序——loop 缺少执行顺序指导

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `ng-refactoring_plan_2026_06.md` 明确定义 "从底层开始重构（Lexer → Parser → VM → TypeChecker → Compiler），每层完成后才进入下一层"，并附依赖关系图。`agent47 superpower-plans/2026-06-30-local-agent-execution-layer.md` Task 间有明确依赖（Task 1 model → Task 2 tools → Task 3 flow → Task 4 UI → Task 5 e2e）。但 `solution-design` 的 planning rules 只说 "Plan verifiable increments"，没有指导如何排序。 |
| **Proposed change** | 在 `solution-design/SKILL.md` 的 `## Planning rules` 中新增一条规则。 |
| **Target** | `delivery/solution-design/SKILL.md` — `## Planning rules` 新增一条 |
| **Principles satisfied** | agent-neutral, scope-limited, user-centric |
| **Approval** | pending |

**具体改动内容**：

在 `## Planning rules` 现有规则之后追加：

```markdown
- When increments have dependencies, draw the dependency graph and start from the least-dependent increment. An increment must not begin until all its predecessors have passed verification.
```

---

### Improvement 4: 补充 Stop Conditions 的具体化——loop 的 Stop 段过于模糊

| Field | Value |
|---|---|
| **Gap type** | false-guidance |
| **Evidence** | `solution-delivery-loop` 的 `## Stop conditions` 只有一句话："Pause and return to discovery/design when scope, acceptance, contract, architecture, or verification becomes unclear or changes." 但 `ng-refactoring_plan_2026_06.md` 有明确的 "测试策略" 表定义每种步骤类型的测试要求；`agent47 design specs` 有 "Non-goals" 段定义不做什么；`CRM v1-yuanlu.md` 有 DoD Gate 检查清单。 |
| **Proposed change** | 将 `## Stop conditions` 段重写为结构化的停止判定表。 |
| **Target** | `delivery/solution-delivery-loop/SKILL.md` — `## Stop conditions` 段重写 |
| **Principles satisfied** | agent-neutral, user-centric |
| **Approval** | pending |

**具体改动内容**：

替换 `## Stop conditions` 段为：

```markdown
## Stop conditions

Pause and determine the correct rollback point when any of these signals occur:

| Signal | Detection | Rollback to |
|---|---|---|
| Scope drift | New requirement, field, or step not in approved plan | requirement-discovery |
| Contract break | Interface, input, output, or data model mismatch | solution-design |
| Test failure | Existing test fails after increment | fix in current increment |
| Verification gap | Cannot define or run verification for an increment | solution-design |
| Risk threshold | Increment affects > 5 files or > 200 lines | pause, notify user |

Before resuming, write a change note (`references/change-note-template.md`) recording what changed and why.
```

---

### Improvement 5: 补充 Change Note 的触发时机——当前只在 implementation-execution 中提及

| Field | Value |
|---|---|
| **Gap type** | missing-guardrail |
| **Evidence** | `implementation-execution` 有完整的 `## Change control` 段定义 5 种 drift 信号。但 `solution-delivery-loop` 的 `## Review and feedback loop` 没有提及 change note，`solution-design` 也没有。实际上 design 阶段也可能发生 drift（如 challenge step 发现需要简化设计）。`agent47 task-3 report` 多次记录 "Review follow-up" 和 "Fix" 但没有统一的 change note 格式。 |
| **Proposed change** | 在 `solution-delivery-loop/SKILL.md` 的 `## Review and feedback loop` 段末尾新增 change note 触发规则。 |
| **Target** | `delivery/solution-delivery-loop/SKILL.md` — `## Review and feedback loop` 段新增 |
| **Principles satisfied** | agent-neutral, scope-limited |
| **Approval** | pending |

**具体改动内容**：

在 `## Review and feedback loop` 段的 Resolution 之后追加：

```markdown
After resolved, if the fix involved scope, contract, or design changes, write a change note before proceeding to the next phase. Change note template: `references/change-note-template.md`.
```

---

### Improvement 6: 补充 Verification Evidence 格式——loop 缺少证据记录规范

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `agent47 task-2-report.md` 有 "RED evidence" / "GREEN evidence" / "Final result" 三段式记录格式，包含具体命令和输出。`task-3-report.md` 同样有 "Verification" 段记录命令+结果。`task-5-report.md` 有 "Follow-up verification" 段。但 `implementation-execution` 的 execution loop 步骤 5 只说 "Record evidence and deltas"，没有定义证据的格式。 |
| **Proposed change** | 在 `implementation-execution/SKILL.md` 的 `## Execution loop` 步骤 5 中补充证据格式要求。 |
| **Target** | `delivery/implementation-execution/SKILL.md` — `## Execution loop` 步骤 5 扩展 |
| **Principles satisfied** | agent-neutral, size-controlled |
| **Approval** | pending |

**具体改动内容**：

将步骤 5 从：

```markdown
5. Record evidence and deltas.
```

改为：

```markdown
5. Record evidence and deltas. Each increment's verification record must include: (a) the command executed, (b) key output or result, (c) pass/fail conclusion. Format: `Verification: <command> → <result summary> → <pass/fail>`.
```

---

### Improvement 7: 补充 Risk Assessment 到 solution-design——loop 缺少风险前置

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `ng-refactoring_plan_2026_06.md` 每个 Step 都标注风险等级（低风险/中风险）；`agent47 superpower-plans/2026-06-29-decision-workspace-mvp.md` 的 Global Constraints 段定义了明确的约束和非目标；`v1-yuanlu.md` 有风险表。但 `solution-design` 的 `## Plan content` 列了 "Risks / rollback" 作为内容项，却没有在 `## Process` 中要求主动评估风险。 |
| **Proposed change** | 在 `solution-design/SKILL.md` 的 `## Process` 步骤 6（Challenge the design）中，在现有检查项之后新增风险评估要求。 |
| **Target** | `delivery/solution-design/SKILL.md` — `## Process` 步骤 6 扩展 |
| **Principles satisfied** | agent-neutral, user-centric |
| **Approval** | pending |

**具体改动内容**：

在 `## Process` 步骤 6 的现有检查列表之后追加：

```markdown
   - Assess each increment's risk level (low / medium / high). High-risk increments need additional verification plans or rollback paths documented in the plan.
```

---

### Improvement 8: 补充 Session Continuity 协议——loop 缺少跨 session 恢复指导

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `solution-delivery-loop` 提到 `.agents/loop-state.md` 但只说 "may help workspace-level continuity, but do not force it"。`agent47 superpower-plans` 开头标注 "REQUIRED SUB-SKILL" 但没有说明 session 断开后如何恢复。tracks 中多个项目跨越多天（NG refactoring 标注日期 2026-06-03，agent47 plans 标注 2026-06-29/30），实际执行中必然遇到 session 中断。当前 loop 没有指导如何在新 session 中恢复上下文。 |
| **Proposed change** | 在 `solution-delivery-loop/SKILL.md` 的 `## Autonomy policy` 段之后新增 `## Session continuity` 段。 |
| **Target** | `delivery/solution-delivery-loop/SKILL.md` — 新增 `## Session continuity` 段 |
| **Principles satisfied** | agent-neutral, user-centric |
| **Approval** | pending |

**具体改动内容**：

在 `## Autonomy policy` 段之后插入：

```markdown
## Session continuity

When resuming work in a new session:

1. Read `.agents/loop-state.md` (if exists), the latest delivery record, and the current track documents.
2. Determine: which phase is active, what was the last increment's verification result, what is the next increment's goal.
3. If no loop-state exists, infer from track documents (latest plan version, most recent delivery record, open change notes).
4. Confirm before proceeding: current phase, pending increments, any open blockers or unresolved review items.
```

---

### Improvement 9: 补充 Increment Granularity 指导——loop 缺少粒度判定标准

| Field | Value |
|---|---|
| **Gap type** | false-guidance |
| **Evidence** | `solution-design` 说 "Plan verifiable increments. Each increment must be reviewable and independently verifiable." 但没有定义什么粒度算一个 increment。`ng-refactoring_plan_2026_06.md` 的粒度是 "提取一个辅助函数"（约 50-150 行变更）。`agent47 plans` 的粒度是 "一个 Task 含 5 个 Step"（约 100-300 行新增代码）。`v1-yuanlu.md` 的粒度是一个 Phase（约 1 天工作量）。 |
| **Proposed change** | 在 `solution-design/SKILL.md` 的 `## Planning rules` 中新增粒度指导。 |
| **Target** | `delivery/solution-design/SKILL.md` — `## Planning rules` 新增一条 |
| **Principles satisfied** | agent-neutral, size-controlled, user-centric |
| **Approval** | pending |

**具体改动内容**：

在 `## Planning rules` 现有规则之后追加：

```markdown
- Increment granularity: an increment should be completable and verifiable within one session. For software work, one increment typically maps to one independently committable change (one helper extraction, one component addition, one interface change). If an increment is预计 to exceed 30 minutes or touch more than 3 files, consider splitting it.
```

---

### Improvement 10: 补充 Blocker 处理协议——loop 缺少阻塞时的结构化处理指导

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `zlf/2026-07-06.md` 工作日志展示了结构化的 blocker 处理：Problem（napi-rs requires Node.js context to build）→ Impact（Cannot build FFI bindings, TypeScript SDK blocked）→ Options to Fix（3 个选项：npm build / JSON FFI / neon）。`myz-track/v22-myz-agent-restructure.md` 的 Gap Review 列出 12 个 gap，每个有 Discovery + Handling。但当前 loop 的 `## Stop conditions` 只说 "Pause and return"，没有指导如何结构化地记录 blocker、评估选项、做出决策。 |
| **Proposed change** | 在 `solution-delivery-loop/SKILL.md` 的 `## Stop conditions` 段之后新增 `## Blocker handling` 段。 |
| **Target** | `delivery/solution-delivery-loop/SKILL.md` — 新增 `## Blocker handling` 段 |
| **Principles satisfied** | agent-neutral, user-centric |
| **Approval** | pending |

**具体改动内容**：

在 `## Stop conditions` 段之后插入：

```markdown
## Blocker handling

When an increment is blocked:

1. **Record**: Write the blocker with three fields:
   - **Problem**: What happened and why
   - **Impact**: What is blocked and what is not affected
   - **Options**: 2-3 concrete resolution paths, each with effort/risk estimate
2. **Decide**: Choose an option. If the decision affects scope, contract, or design, write a change note.
3. **Resume**: Continue from the next unblocked increment, or revise the plan if the blocker changes the plan structure.

Do not leave blockers undocumented. A blocked increment without a recorded resolution path is a hidden risk.
```

---

### Improvement 11: 补充 Design Decision 记录——loop 缺少决策追溯机制

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `ng-design/README.md` 有 "Key Design Decisions" 段，包含 "Conflicts Resolved" 表（冲突→解决方案→适用范围）和 "Features Deferred" 表（特性→延期原因→重新评估条件）。`constype-track/v3-architecture-refactor.md` 的 `[S5] Unified Error System` 记录了完整的错误码体系设计决策。`zlf/prd-v1.md` 的 `## 11. Decisions Made` 记录了 60+ 个设计决策及其 rationale。`myz-track/v22` 有 "Gap Review" 段记录执行中发现的 gap 和处理方式。但当前 loop 没有要求在任何 phase 记录设计决策。 |
| **Proposed change** | 在 `solution-design/SKILL.md` 的 `## Plan content` 中，将 "Alternatives and trade-offs" 扩展为包含决策记录格式。 |
| **Target** | `delivery/solution-design/SKILL.md` — `## Plan content` 扩展 |
| **Principles satisfied** | agent-neutral, size-controlled |
| **Approval** | pending |

**具体改动内容**：

将 `## Plan content` 中的 `Alternatives and trade-offs` 改为：

```markdown
- Design decisions and rationale (for each significant choice: what was chosen, what was rejected, why)
- Deferred features (what was explicitly excluded and under what condition to revisit)
```

---

### Improvement 12: 补充 Feasibility Pre-screening——loop 缺少可行性预判

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `ng-design/README.md` 对 15 个提案做了 feasibility rating（Feasible/Moderate/Redesigned），并标注了 "Codebase Quality Baseline"（28,804 行代码审计结论：no rewrite needed）。这发生在 solution-design 之前，用于判断一个提案是否需要重新设计。但当前 loop 从 requirement-discovery 直接进入 solution-design，没有可行性预判步骤。对于技术可行性不确定的工作（如新的集成方式、性能敏感的变更），缺少这个步骤可能导致 design 返工。 |
| **Proposed change** | 在 `solution-design/SKILL.md` 的 `## Process` 步骤 2（Confirm users, scope, non-goals, requirements, and acceptance are sufficient）之后新增可行性预判步骤。 |
| **Target** | `delivery/solution-design/SKILL.md` — `## Process` 新增步骤 |
| **Principles satisfied** | agent-neutral, user-centric |
| **Approval** | pending |

**具体改动内容**：

在 `## Process` 步骤 2 之后插入：

```markdown
3. Pre-screen feasibility: for each major design choice, assess whether it is Feasible (additive changes only), Moderate (targeted additions needed), or Redesigned (scope changed after analysis). If Redesigned, return to requirement-discovery to adjust scope before proceeding.
```

（原有步骤编号顺延。）

---

### Improvement 13: 补充 Acceptance Traceability——loop 缺少需求到实现的追溯表

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `zlf/plan-v1.md` 有完整的 "Acceptance Mapping" 表，将每个 REQ 映射到具体 Slice、Edge Cases、Unhappy Paths、Verification 方法。`myz-track/PRD-agentic-workflow.md` 有 "追溯矩阵" 将每个 Req ID 映射到 vN 计划、测试文件、代码路径。`CRM/v1-yuanlu.md` 有 "验收标准总览" 表将 REQ 映射到 E2E 测试和 Phase。但当前 `solution-design` 的 plan content 只列了 "Acceptance mapping" 作为内容项，没有要求具体的映射格式。 |
| **Proposed change** | 在 `solution-design/SKILL.md` 的 `## Plan content` 中，将 "Acceptance mapping" 扩展为具体的映射格式要求。 |
| **Target** | `delivery/solution-design/SKILL.md` — `## Plan content` 扩展 |
| **Principles satisfied** | agent-neutral, scope-limited |
| **Approval** | pending |

**具体改动内容**：

将 `## Plan content` 中的 `Acceptance mapping` 改为：

```markdown
- Acceptance mapping: a table mapping each requirement to its implementing increment(s), edge cases covered, verification method, and test location
```

---

## Skills modified

| Skill | Changes |
|---|---|
| `delivery/solution-delivery-loop/SKILL.md` | 新增 `## Work type triage` 段；重写 `## Stop conditions`；扩展 `## Review and feedback loop`；新增 `## Session continuity` 段；新增 `## Blocker handling` 段 |
| `delivery/implementation-execution/SKILL.md` | `## Execution loop` 步骤 5 扩展（evidence format）；新增步骤 6（incremental commit） |
| `delivery/solution-design/SKILL.md` | `## Planning rules` 新增依赖排序规则和粒度指导；`## Process` 步骤 6 扩展（risk assessment）；`## Plan content` 扩展（design decisions、deferred features、acceptance mapping format）；`## Process` 新增 feasibility pre-screening 步骤 |

## New skills created

（无）

### Improvement 14: 补充 Proposal Splitting 指导——大设计提案需要拆分为独立可交付子项

| Field | Value |
|---|---|
| **Gap type** | false-guidance |
| **Evidence** | `ng-design/gap-type-system-enhancements.md` 开头明确标注 "Restructured from 4-feature monolith into 4 independent sub-proposals. Each sub-proposal is independently estimable and deliverable." 4 个子提案各有独立的 Effort、Dependencies、Risk、Acceptance Criteria。`ng-design/gap-syntax-ergonomics.md` 同样从 "7-feature monolith" 拆为 3 个 sequential batches。但当前 `solution-design` 没有指导如何将大的设计提案拆分为独立可交付的子项。 |
| **Proposed change** | 在 `solution-design/SKILL.md` 的 `## Planning rules` 中新增一条：当一个设计提案涉及多个独立特性时，先将其拆分为独立可交付的子提案（sub-proposal），每个子提案有独立的 effort estimate、dependencies、acceptance criteria。子提案之间可以有依赖关系，但每个必须能独立验证。 |
| **Target** | `delivery/solution-design/SKILL.md` — `## Planning rules` 新增一条 |
| **Principles satisfied** | agent-neutral, size-controlled, scope-limited |
| **Approval** | pending |

**具体改动内容**：

在 `## Planning rules` 现有规则之后追加：

```markdown
- When a design proposal covers multiple independent features, split it into sub-proposals before planning increments. Each sub-proposal must have its own effort estimate, dependencies, acceptance criteria, and can be independently delivered and verified.
```

---

### Improvement 15: 补充 Rejected Alternatives 记录——loop 缺少设计决策的完整追溯

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `ng-design/gap-type-system-enhancements.md` Sub-Proposal B（`impl Trait`）被标记为 REJECTED，附带完整理由："NG's trait model already provides equivalent functionality without impl Trait"。`ng-design/gap-concurrency.md` 附带 "Why Not Async/Await?" 段，列出 4 个具体技术障碍（VM 无 suspension points、编译器不能生成新类型、GC 非并发安全、YIELD 需要帧栈重构）。`ng-design/README.md` 的 "Features Deferred" 表记录延期原因和重新评估条件。这些模式远比当前 plan content 中的 "Alternatives and trade-offs" 更结构化。 |
| **Proposed change** | 在 `solution-design/SKILL.md` 的 `## Plan content` 中，将 Design Decisions 扩展为包含 rejected alternatives 和 deferred features 的结构化格式。 |
| **Target** | `delivery/solution-design/SKILL.md` — `## Plan content` 扩展 |
| **Principles satisfied** | agent-neutral, scope-limited |
| **Approval** | pending |

**具体改动内容**：

将 `## Plan content` 中的 Design Decisions 部分改为：

```markdown
- Design decisions and rationale (for each significant choice: what was chosen, what was rejected and why, what was deferred and under what condition to revisit)
```

---

### Improvement 16: 补充 Breaking Change 迁移指导——loop 缺少破坏性变更的处理流程

| Field | Value |
|---|---|
| **Gap type** | coverage-gap |
| **Evidence** | `ng-design/gap-error-handling.md` 有完整的 "Migration: Stdlib I/O Functions" 段，包含 "Breaking Change: Files to Migrate" 表（列出了每个需要修改的文件和具体行）和 "Migration Strategy" 段（"Break once, fix all" 方法，5 步迁移计划）。`constype-track/v3-code-review.md` 有详细的 "服务功能清单与实现完整度" 表，列出每个服务的每个功能的实现状态（✅/❌/⚠️），作为迁移的基线。但当前 loop 的 implementation-execution 没有指导如何处理破坏性变更。 |
| **Proposed change** | 在 `implementation-execution/SKILL.md` 的 `## Change control` 段之后新增 `## Breaking changes` 段。 |
| **Target** | `delivery/implementation-execution/SKILL.md` — 新增 `## Breaking changes` 段 |
| **Principles satisfied** | agent-neutral, user-centric |
| **Approval** | pending |

**具体改动内容**：

在 `## Change control` 段之后插入：

```markdown
## Breaking changes

When an increment introduces a breaking change (API contract, data format, behavior change):

1. **Inventory**: List every file/module/caller that must be updated.
2. **Strategy**: Choose migration approach:
   - "Break once, fix all" — single coordinated migration (small codebase)
   - "Deprecate then remove" — old behavior works with warning, removed in next version (large codebase)
3. **Execute**: Update all identified callers in the same increment.
4. **Verify**: Run full test suite to confirm no regressions.
5. **Document**: Record the breaking change in the delivery record with affected files list.
```

---

## Deferred items

| Item | Rationale |
|---|---|
| process-distillation 自身的跨 skill 一致性检查机制 | 当前 distillation 只关注单个 skill 的 gap，跨 skill 一致性检查是更大的改动，建议独立 cycle 处理 |
| delivery-acceptance 的 evidence 格式统一 | 当前 acceptance 的 evidence 要求散落在多个 skill 中，可以考虑统一到一个 reference 文档，但不影响当前 loop 的核心流程 |
| RFC 模式提炼 | `mono-services-docs/rfcs/` 有 18 个 RFC 文档展示了架构决策的记录模式，但 RFC 更适合大型组织的正式决策，不适合所有场景。建议作为 optional reference 而非 required 流程 |
| ECN 变更通知单模式 | `constype-track/ECN-0001` 展示了正式的架构变更通知单格式（原设计→问题→新设计→影响评估→行动项→审批），比当前 change note 更结构化。但当前 loop 的 change note 场景更轻量，ECN 模式适合作为 reference 而非 required 流程 |

## Recommendations for future cycles

1. **tracks 目录应该有索引**：当前 10 个子目录没有统一索引，每次 review 都需要全量扫描。建议在 `tracks/` 下维护一个 `INDEX.md`，记录每个子目录的项目名称、状态、最后更新日期。

2. **delivery skills 之间的一致性需要定期检查**：当前 8 个 skill 有重叠的 anti-patterns 和 related skills 段，可以考虑提取共用的 reference 文档减少重复。

3. **agent47 的 task report 格式可以提炼为 reference**：RED/GREEN/Final 三段式验证记录格式非常实用，可以作为 `references/verification-evidence-template.md` 加入 implementation-execution。

4. **zlf 的 Acceptance Mapping 格式值得推广**：将每个 REQ 映射到 Slice + Edge Cases + Unhappy Paths + Verification 的表格格式，是保证 plan 可追溯性的有效手段。建议作为 `references/acceptance-mapping-template.md` 加入 solution-design。

5. **ng-design 的 Feasibility Rating 模式可以泛化**：Feasible/Moderate/Redesigned 三级评估可以帮助在 design 阶段早期识别需要重新定义 scope 的工作。建议作为 solution-design 的可选前置步骤。

6. **ng-design 的 Sub-proposal Splitting 模式值得推广**：将大型设计提案拆分为独立可交付子项的做法，可以显著降低单次交付的风险。建议在 solution-design 的 plan content 中明确要求。

7. **ng-design 的 Rejected/Deferred 追溯模式值得推广**：记录被拒绝的替代方案和被延期的特性，包含拒绝原因和重新评估条件，是保证设计决策可追溯性的有效手段。
