# Purposeful Widget

Daily quote home-screen widget for [@becomingpurposeful](https://instagram.com/becomingpurposeful).
Live at https://forgedreams-ai.github.io/purposeful-widget/

## How it works

- `quotes.json` — every quote ever posted. The daily pipeline appends new ones.
- `tools/build_today.py` — picks today's quote (`index = days_since_epoch % len(quotes)`) and writes `today.json`. Run daily.
- `today.json` — `{"quote","author","date"}`. Widget apps (Widgy, KWGT) fetch this URL.
- `index.html` — the page. Fetches `today.json` for the hero, `quotes.json` for the archive.

## Appending a quote (daily pipeline)

Add one object to `quotes.json`:

```json
{"text": "The full quote text.", "author": "Name or Source", "date": "YYYY-MM-DD"}
```

Then run `python3 tools/build_today.py` and commit. Never remove entries —
removing one shifts every future day's quote.
