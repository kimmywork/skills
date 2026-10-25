# Presentation Decks

Eight fictional decks from the `presentation` skill, plus a gallery and an inferred requirements document for each case.

- **Gallery:** [`index.html`](index.html)
- **Requirements:** [`requirement/README.html`](requirement/README.html)
- **Image credits:** [`assets/CREDITS.html`](assets/CREDITS.html)

## Cases

| Deck | Type | Time |
|---|---|---|
| [`academic-defense.html`](academic-defense.html) | Academic defense | 20 + 5 |
| [`series-a-pitch.html`](series-a-pitch.html) | Series A pitch | 10 + 5 |
| [`incident-postmortem.html`](incident-postmortem.html) | Incident postmortem | 15 + 10 |
| [`architecture-review.html`](architecture-review.html) | Architecture review | 25 + 10 |
| [`keynote.html`](keynote.html) | Keynote | 12 |
| [`workshop.html`](workshop.html) | Workshop | 90 |
| [`business-review.html`](business-review.html) | Business review | 20 + 10 |
| [`product-launch.html`](product-launch.html) | Product launch | 8 + 5 |

## Build

The decks are generated from `build_decks.py`; the gallery and requirement documents are generated from `build_site.py`.

```bash
python3 docs/presentations/build_decks.py
python3 docs/presentations/build_site.py
```

The generated decks are self-contained HTML files. Images are embedded as data URIs at build time; source images live in `assets/` with credits in `assets/CREDITS.md`.

## Notes

- Every case is fictional. Numbers, companies, and people are invented for the showcase; replace them with sourced facts before a real delivery.
- Use `←` / `→` to navigate, `N` for speaker notes, and print to PDF for a handout.
- The requirements documents use `.html` links because they are published through Jekyll.
