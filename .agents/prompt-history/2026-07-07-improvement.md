接下来我希望能对 delivery/skills 里的整体结构做一个完整的提升：

 - 支持多项目声明。如果这是一个多项目的 workspace，需要明确标注多项目。比如在loop-state里。这样才能更好定位 docks/track 文档的层级
 - track 文档中的 <feature> 需要日期+日期内的sequence作为前缀，方便定位最新添加的feature。日期不需要变更，只需要使用创建该feature tracking 文档的日期就行
 - 过大的requirement，在discovery的阶段就需要split成可独立执行独立验证的小feature，在该feature内部嵌套来组织和维护
