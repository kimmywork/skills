# vN-<topic> 需求与计划模板

## Vision
- 一句话说明目标与价值（避免空泛）
- 示例：让用户在 3 步内完成 X，并保持成功率 ≥ 95%

## Background / Motivation
- 为什么要做（问题现状 + 影响）
- 示例：现流程需要 8 步且经常超时，导致用户流失

## Scope
- 做什么（列清楚“包含/不包含”）
- 示例：包含 A/B/C，不包含历史数据回填

## Non‑Goals
- 不做什么（明确边界）
- 示例：不支持离线模式；不改动鉴权流程

## Data Model (schema-first)
- 关键实体与字段（含类型与可空性）
- 约束与默认值（长度/范围/枚举）
- 兼容性/迁移策略（如新增字段默认值）

## UX / Flow
- 关键流程步骤（主路径）
- 主要交互点（按钮、表单、反馈）

## Dependencies / Constraints
- 依赖模块/外部系统
- 约束与假设（例如最大体积/限流）

## Acceptance Criteria
- 可二元判定的验收条目（Given/When/Then）
- 示例：Given 未配置 X，当进入页面时，Then 显示提示且按钮禁用

## Verification Plan
- 单元/集成/手动验证路径（覆盖主路径 + 边界）

## Risks / Rollback
- 风险点与回退方案（可执行）

## Use Cases / Scenarios
- 主路径（至少 1 条）
- 边界路径（至少 2 条）
- 失败路径（至少 1 条）

## Boundary Conditions
- 空值/缺失字段
- 最大长度/数量
- 权限不足/不可用
- 网络失败/超时

## Open Questions
- 仍待确认的问题清单
