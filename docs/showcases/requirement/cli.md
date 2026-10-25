# relay — CLI Requirements

> Source: [`../cli.html`](../cli.html) · Surface: CLI · Mode: Greenfield · Case 02
> Purpose: treat output as the interface: data, diagnostics, color, width, and exit codes are the product.

## 1. Problem and context

**Who:** developers deploying services from a laptop, a CI runner, or a pipe into another tool.

**Jobs:** deploy, check status, read failures, and script the same operations.

**Constraints:** the terminal may be interactive or a pipe; ANSI may be disabled; the width is unknown until runtime. The CLI controls the colors it sets only when it is allowed to set them.

## 2. Principles

| Rule | Rationale |
|---|---|
| stdout is data, stderr is commentary | Piped output stays parseable; progress and warnings never corrupt the data stream. |
| Color is a runtime decision | TTY, `NO_COLOR`, CI, and dumb terminals each change what is honest to emit; meaning never depends on color. |
| Width is read, not assumed | Wrapping and truncation follow the real terminal; 80 columns is a guess, not a contract. |
| An error ends with the next command | Recovery is part of the interface; “what happened / why / next” is one block. |
| Exit codes are a public API | Scripts branch on them; they are specified and tested like any other contract. |

## 3. Experience requirements

### Sessions

Render whole transcripts for three real scenarios: success, failure, and a pipe. These are the CLI's scenes, not isolated snippets.

### Rendering modes

The same transcripts must adapt to:

- **Auto** — color when stdout is a TTY and the terminal is capable.
- **Piped** — color off, spinners off, data only.
- **NO_COLOR** — color off, layout unchanged.
- **CI** — color off, timestamps and result fields on, spinners off.

### Width

- Read the terminal width; help and output re-wrap.
- Do not design for one magic width.
- When a pipe is possible, provide a column or table mode instead of relying on spaces.

### Errors

- **What happened:** one line, past tense, no jargon.
- **Why:** the rule or state that caused it.
- **Next:** a runnable command or a named owner.
- Errors are complete sentences, not codes alone.

### Exit codes

| Code | Meaning | Typical cause |
|---|---|---|
| 0 | success | operation completed |
| 1 | usage error | unknown flag or missing argument |
| 2 | preflight failed | environment refused the deploy |
| 3 | runtime failure | remote system failed mid-operation |
| 4 | timeout | operation exceeded `--timeout` |

### Machine mode

`--json` is a documented contract, not a debug dump:

- closed state vocabulary;
- ISO-8601 UTC timestamps;
- no diagnostics on stdout;
- the same exit codes as human mode.

## 4. Visual and content requirements

### Color

Showcase tokens: background `#12121a`, foreground `#d9d9e3`, dim `#8a8a9c`, accent `#a78bfa`, ok `#5dd47e`, warn `#e3b341`, bad `#f4807c`.

- When color is allowed, compute contrast against both common background assumptions.
- If a pair fails, change the token, not the report.
- Every role also carries a word or symbol.

### Typography

- One fixed-pitch face, one size; there is no font axis.
- The CLI owns alignment, weight, and case.
- Columns are computed in characters, never pixels.
- Do not use italics; some fonts lack them.
- Case is content, not emphasis; do not SHOUT commands or status.
- Numeric columns are tabular.

## 5. Components and states

- **Step line:** running, done, failed.
- **Result line:** success, skipped.
- **Interactive prompt:** waiting, confirmed; default answer and escape.
- **Table:** two widths of the same data; stable columns.

Every state must be reachable through the mode matrix.

## 6. Motion and accessibility

- Spinners and progress bars are the only motion; result lines never animate.
- Non-TTY, `NO_COLOR`, and CI disable spinners and animated progress.
- `prefers-reduced-motion` freezes the spinner at a static frame.
- Every status keeps a word or glyph so a screen reader hears meaning without color.
- Output is a linear stream; no cursor-addressing or two-column layout that breaks reading order.
- Errors are complete sentences with the next command.
- Wrapping respects the real terminal and never assumes 80 columns.
- Every interactive prompt has a default answer and an escape.

## 7. Verification requirements

- Exercise the full mode matrix: TTY, pipe, `NO_COLOR`, CI, dumb terminal.
- Test at more than one width.
- Assert the exit-code contract.
- Assert that `--json` is valid, has the documented state vocabulary, uses ISO-8601 UTC, and keeps diagnostics off stdout.
- Prove that no meaning depends on color.

## 8. Non-goals

- Do not design for a single 80-column terminal.
- Do not put progress or warnings on stdout.
- Do not make `--json` a debug dump.
- Do not use case as emphasis.

## 9. Open questions

- The JSON schema has no version field in the showcase; decide whether a schema version is required before the contract is published.
- Decide whether `--json` and the human output share one source of truth or separate renderers.
