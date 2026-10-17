#!/usr/bin/env python3
"""Pick today's quote and write today.json.

Deterministic: index = (days since Unix epoch) % number_of_quotes.
Run daily (the morning pipeline does this after appending new quotes).
Do NOT remove entries from quotes.json — that shifts every future day's quote.
"""
import json
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def main():
    quotes = json.loads((ROOT / "quotes.json").read_text())
    if not quotes:
        raise SystemExit("quotes.json is empty")
    days = (datetime.now(timezone.utc).date() - date(1970, 1, 1)).days
    q = quotes[days % len(quotes)]
    today = {
        "quote": q["text"],
        "author": q["author"],
        "date": datetime.now(timezone.utc).date().isoformat(),
    }
    (ROOT / "today.json").write_text(json.dumps(today, indent=2) + "\n")
    print(f"today.json -> {q['author']}: {q['text'][:60]}...")

if __name__ == "__main__":
    main()
