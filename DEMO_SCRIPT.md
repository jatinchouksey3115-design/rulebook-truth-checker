# 90-second demo script

**0:00–0:10** — “This is my Rulebook Truth Checker. It has three outcomes: answer, contradiction, and no answer.”

**0:10–0:25** — Ask: “What attendance percentage is normally required to sit the end-term examination?” Show `ANSWER` and the cited handbook clause.

**0:25–0:50** — Ask: “What attendance percentage is required for examination eligibility when a student has an approved medical absence?” Show `CONTRADICTION`. Open both evidence boxes: 75% in the handbook and 65% in the PDF annex.

**0:50–1:05** — Ask: “What happens if I miss an end-term examination because I am attending my sister's wedding?” Show `NO_ANSWER`. Explain that the corpus does not contain a family-wedding rule, so the system does not invent one.

**1:05–1:20** — Open `contradictions.md` and `tests/`. Show that the conflicts and the 25 near-miss questions are recorded in files, not hidden in the UI.

**1:20–1:30** — Run `python evaluate.py`. Show the measured scores and finish with: “The important part is that every answer can be checked against the source text.”
