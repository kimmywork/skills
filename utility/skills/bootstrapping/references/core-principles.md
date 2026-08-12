# Core Principles

Universal principles for project work. Apply to any
project type. Each principle includes its AI-era interpretation.

## Tasking

### SMART
Specific, Measurable, Achievable, Relevant, Time-bound. Write prompts and
issues as deterministic instructions, not vague requests. "Optimize this"
is not SMART. "Convert list rendering to virtual list, support 10k items
without lag, use react-window" is SMART.

### INVEST
Independent, Negotiable, Valuable, Estimable, Small, Testable. Break large
tasks into atomic units. Each unit must be independently testable. Small
reduces hallucination risk; Testable enables automated verification.

### Occam's Razor
Entities must not be multiplied beyond necessity. Among competing solutions,
prefer the one with the fewest assumptions and dependencies. Do not add
layers, abstractions, or alternatives the current requirement does not need.

### Pareto Principle (80/20)
Deliver the 20% of functionality that covers 80% of normal scenarios first.
Let the user handle corner cases later. Do not let edge cases block the
core deliverable.

## Design and code

### SOLID
- **SRP:** One module, one responsibility. Keep controllers, business logic,
  and data access in separate files.
- **OCP:** Open for extension, closed for modification. Favor composition
  over modifying existing tested code.
- **LSP:** Subtypes must be substitutable for their base types.
- **ISP:** Keep interfaces small and focused. Do not force clients to depend
  on methods they do not use.
- **DIP:** Depend on abstractions, not concretions.

### YAGNI
You Aren't Gonna Need It. Implement only the current requirement. Do not
add extension points, abstract interfaces, or config options for future
needs. Future requirements are cheaper to add when they are real.

### KISS
Keep It Simple. The simplest solution that satisfies the requirement is the
best solution. Favor straightforward code over clever patterns. Readability
is the primary quality metric.

### SoC (Separation of Concerns)
Keep UI rendering, state management, network requests, and data access in
separate layers. When one layer changes, the agent only needs to read that
layer's context.

### LoD (Law of Demeter)
Limit chain depth. Do not write `a.getB().getC().doSomething()`. Encapsulate
interfaces so that a change in one module does not cascade through the
call chain.

## Evolution and refactoring

### Chesterton's Fence
Before removing or rewriting any code, understand why it was written in the
first place. Read the Git blame, associated issues, and ADRs. Do not assume
old code is wrong just because it looks unusual.

### DRY vs WET
Prefer DRY, but recognize that over-abstraction harms agent comprehension.
A moderate amount of duplication (WET) is acceptable when it keeps related
code in the same file and within the agent's context window. Extract only
when the same pattern appears in three or more places.

### Boy Scout Rule
Leave the code cleaner than you found it. When modifying a file, fix lint
warnings, update stale comments, and add missing type annotations as a
side effect — but only within the scope of the change.

### Fail Fast
Validate inputs at function entry. Throw clear errors immediately on
invalid input. Do not let invalid state propagate through the system.

## Interaction and systems

### Postel's Law (Robustness Principle)
Be conservative in what you send, be liberal in what you accept. When
calling external APIs, strictly follow the protocol. When receiving
untrusted data, handle errors gracefully with fallbacks and degradation.

### Gall's Law
A complex system that works evolved from a simple system that worked. Start
with an MVP. Iterate. Do not try to build the full system in one shot.

### Conway's Law
System architecture mirrors communication structure. Align module boundaries
with team and agent responsibilities. Each agent team owns a bounded context
with a clear API contract.

## Review and quality

### Linus's Law
Given enough eyes, all bugs are shallow. Use multi-agent cross-validation:
a coder agent, a reviewer agent, and a security agent. Different prompts
catch different blind spots.

### Murphy's Law
Anything that can go wrong will go wrong. After generating code, explicitly
review error paths, network timeouts, null/undefined states, and edge cases.
Do not assume the happy path is the only path.