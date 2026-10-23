# Terminal Surfaces (TUI and CLI)

The terminal is a host-owned surface: the emulator or the user owns the palette, the font, and the cell grid. Read this with the main skill and the checklist; it adds binding constraints and derivation prompts, not a separate process.

## Palette and contrast

- Tokens name roles (`foreground`, `dim`, `accent`, `warning`, `error`, and so on), never RGB values. The system cannot read or set the host palette.
- Meaning never depends on a host color: every colored element also carries a word or a glyph.
- The redundant label must itself use the default foreground. A label painted in a low-contrast role voids the redundancy.
- No ANSI role is legible on both a light and a dark host background. Provide a monochrome high-contrast path built from the host's default foreground plus weight, never a "brighter" color.
- Scope every high-contrast choice to the background it assumes. If the host scheme cannot be detected, state the assumption or do not ship it.
- Measurement is advisory. Pick one named reference palette, report the numbers against it, and prove legibility structurally: color is redundant, and the fallback path exists. Do not present advisory numbers as a guarantee.

## TUI

- The cell is the layout unit: fixed-row gaps, N-cell indents, truncation with a visible ellipsis, status content collapsing from the outside in. No horizontal scroll.
- Type control is weight, dim, and italic only; there is no font axis. Focus must be visible without color.
- Emoji are not an icon system: variable width and host-dependent. Keep a glyph table with ASCII fallbacks, and let the user or locale choose the set.
- Every keybinding is discoverable from inside the interface (status line, help overlay); never require memorized sequences.
- Whole-screen states are the TUI equivalent of scenes: empty, loading, error, dialog, and help appear as full frames in the showcase, not as isolated lines.

## CLI

- Output is the interface. `stdout` carries data, `stderr` carries diagnostics and progress; a pipe must receive clean data.
- Color is a runtime decision: detect a TTY, respect `NO_COLOR` and `--no-color`, honor CI and dumb terminals, and keep meaning independent of color.
- Width is a runtime fact: read the terminal width and wrap or truncate deliberately. Never assume 80 columns.
- Help is a layout: usage line first, examples before the exhaustive flag list, one consistent option grammar, one primary action.
- Errors state what happened, the cause, and the next command; exit codes are part of the interface and are specified.
- Offer a machine-readable mode (`--json`) as a documented contract, and keep human and machine output under one consistency check.
- Showcase CLI screens as full transcripts, including prompts, pipes, and exit status.

## Verification

- Enumerate contrast pairs only for values the system sets; label the reference palette.
- Assert the structural fallbacks: a no-color rendering for every state, a monochrome rendering for every semantic role, and an ASCII rendering for the glyph set.
- For CLI, test at two or more widths and in TTY, pipe, and `NO_COLOR` modes.
