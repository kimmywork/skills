# Design Methods

Read this when you know what you are making or reviewing but not what you still need to learn. Pick methods by uncertainty, not by habit.

## Frame first

Answer these before choosing a method:

- What problem, for whom, in what context?
- What does success look like, and what would failure look like?
- What is fixed (constraints) and what is free?
- What is the biggest uncertainty: desirability, usability, structure, flow, visual direction, coherence, risk, priority, or causality?
- What decision does this work support, and what would change your mind?

If you cannot name the uncertainty, you are not ready to choose a method.

## Uncertainty to method

| Uncertainty | Methods | Output |
|---|---|---|
| People, context, real constraints | contextual inquiry, interviews, diary study, jobs-to-be-done | scenarios, jobs, constraints |
| Structure, terms, findability | content audit, card sort, tree test | information architecture, term table |
| Flow, state, handoff | journey map, service blueprint, task analysis, state model | flow and state specification |
| Visual direction | competitive audit, moodboard, critique, prototype | direction and rationale |
| System coherence | component inventory, token audit, drift check | gap and drift list |
| Risk, ethics, harm | pre-mortem, red team, dark-pattern audit, accessibility audit | risk register |
| Current experience quality | heuristic evaluation, cognitive walkthrough, usability test, analytics | findings with behavioral evidence |
| Priority | impact/effort, risk matrix, RICE (with caution) | ordered work |
| Causal claim | experiment, A/B test | causal evidence |

## Classic methods

Use each only when its condition holds.

| Method | Use when | Misuse |
|---|---|---|
| Double Diamond | Shaping a project: diverge, then converge | Treating it as a mandatory four-phase ritual |
| Design thinking | The problem is ambiguous and human-centered | Applying it to well-defined execution |
| Jobs-to-be-done | Scope and language are unclear | Using it as a persona substitute |
| Contextual inquiry | You need real context | Running it as a focus group |
| Journey map | Pain crosses channels or handoffs | Making a decorative poster |
| Card sort / tree test | Structure and vocabulary are in question | Choosing a visual style |
| Heuristic evaluation | You need a fast expert sweep | Calling it user testing |
| Cognitive walkthrough | A new user must complete a task | Treating it as a full usability study |
| Usability test | You need observed behavior | Polling opinions |
| Design critique | Direction is open and needs multiple views | Using it as sign-off |
| Pre-mortem / red team | A decision is risky | Using it as negativity |
| A/B test | Traffic and a causal hypothesis exist | Testing a novel idea with no traffic |
| Design rationale / ADR | A major trade-off was made | Producing documentation theatre |
| Component / token audit | System health is in question | A one-time cleanup |

## Adopt before inventing

Check whether a mature system or platform convention already solves this: Fluent 2, Material 3, Apple HIG, IBM Carbon, Shopify Polaris, GitHub Primer, GOV.UK, USWDS. If you adopt one, record the source and every deviation. If you do not, say why it is insufficient. A borrowed pattern still has to pass this product's stance and principles.

## Decision record

For each major trade-off, keep six lines: context, options, criteria, decision, consequences, and the condition that would reopen it. This is what makes a later change a decision rather than a drift.

## Method log

Record: uncertainty, method, evidence, what you learned, what you did not learn. A method that produced no decision is a cost, not a credential.

## Anti-patterns

- Running every method to look thorough.
- Research with no decision attached.
- Treating a framework name as evidence.
- Confusing a preference for a finding.
- Skipping the method because the answer feels obvious.

## Sources

Double Diamond (Design Council); design thinking; jobs-to-be-done; contextual inquiry; Nielsen's heuristic evaluation; cognitive walkthrough; usability testing; design critique; pre-mortem. Use the method, not the brand.
