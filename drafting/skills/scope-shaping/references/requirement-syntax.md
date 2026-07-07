# Requirement Syntax

Use the lightest syntax that makes acceptance verifiable.

## User Story

```text
As a <persona>, I want <capability>, so that <benefit>.
```

Use for user-facing or workflow needs. Add scenario and non-goals.

## EARS

Use for precise behavioral requirements:

- Ubiquitous: The system shall <response>.
- Event-driven: When <trigger>, the system shall <response>.
- State-driven: While <state>, the system shall <response>.
- Optional: Where <feature>, the system shall <response>.
- Unwanted behavior: If <condition>, then the system shall <response>.

## Given/When/Then

Use for acceptance checks:

```gherkin
Given <precondition>
When <action>
Then <observable result>
```

## Splitting broad scope

Split when one request contains multiple users, modules, artifacts, risk levels, or independently valuable outcomes.
Each stage needs its own acceptance criteria and verification method.

## Overlap check

Before creating a new track, scan active tracks for overlapping scope. Extend or link the existing track when it is the same user outcome.
