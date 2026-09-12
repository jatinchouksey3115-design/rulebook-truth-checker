# Rulebook Truth Checker

I built this for the IT Geeks Vibe Coding Round.

The problem I focused on is simple to describe but a little harder to get right: university rules are usually spread across long documents, and sometimes two parts of the same rulebook do not agree. A normal chatbot can give a nice sounding answer even when the document does not support it. I wanted the demo to do the opposite.

This project reads a small synthetic university rulebook and puts every retrieved piece of evidence next to the result. It has three possible outcomes:

- `ANSWER` — the rulebook contains enough information to answer.
- `CONTRADICTION` — two planted rules give incompatible answers.
- `NO_ANSWER` — the question is plausible, but the supplied rulebook does not establish an answer.

The last case is important. The system is deliberately allowed to say that it does not know.

## What is included

The `corpus/` folder contains:

- a long Markdown handbook (6,000+ words)
- a separate fee-deadline Markdown table
- a project notice
- a PDF medical-absence annex

There are exactly three planted contradictions. They are listed in `contradictions.md`.

The `tests/` folder contains:

- 10 answerable questions
- 3 contradiction questions
- 25 hard near-miss questions that the corpus does not answer

`evaluate.py` runs all of them and prints the actual numbers instead of making a claim about accuracy.

## How it works

The core is intentionally small. I did not want a black-box chatbot to decide whether a sentence exists in the rulebook.

1. The Markdown files and PDF are loaded.
2. The text is split into traceable clauses.
3. A TF-IDF search retrieves the most relevant clauses.
4. The system checks the three known contradiction pairs explicitly.
5. If there is enough evidence, the best supporting clause is returned.
6. If the evidence is too weak, the result is `NO_ANSWER`.
7. The UI shows the source file and locator for every returned clause.

This makes the result easy to inspect during the demo.

## Run it locally

I used Python 3.10+.

Create a virtual environment if you want to keep the packages separate:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the web app:

```bash
streamlit run app.py
```

A browser window should open with the Rulebook Truth Checker.

You can also run the command-line version:

```bash
python src/rulebook.py
```

And run the evaluation:

```bash
python evaluate.py
```

The evaluation also writes `evaluation_results.json`.

## Questions to try in the demo

### 1. Normal answer

> What attendance percentage is normally required to sit the end-term examination?

This should return an `ANSWER` and show the attendance rule.

### 2. Contradiction

> What attendance percentage is required for examination eligibility when a student has an approved medical absence?

This should return `CONTRADICTION` and show the 75% rule from the handbook and the 65% rule from the PDF annex.

There are two other planted conflicts:

- 15 September vs 20 September for the same tuition category
- prior approval required vs 48-hour late-submission window for a final project

### 3. No answer

> What happens if I miss an end-term examination because I am attending my sister's wedding?

The handbook discusses medical absence and examination absence, but it does not give a rule for a family wedding. The correct result for this corpus is therefore `NO_ANSWER`.

## Why the citations matter

The result is not just a sentence generated from the whole document. The app returns the actual clause that was used, including its source file and locator.

For example:

`PDF-2-1 — medical_annex.pdf (page 2)`

The UI then prints the original text below that identifier. This is intentional: a reviewer should be able to check the answer without trusting the application.

## Evaluation

I separated the test set into the three states instead of using one big accuracy number only.

The important part of the evaluation is the 25 hard `NO_ANSWER` questions. They are not nonsense questions. They are realistic questions that are close to topics covered by the handbook but ask for a rule that is actually missing.

Run:

```bash
python evaluate.py
```

and use the numbers printed by the program in the submission. I would not replace those numbers with a hand-written claim.

## Demo video

For the submission video I would keep it around 90 seconds.

1. Start on the web app and show that the corpus is loaded.
2. Ask the normal attendance question and open the evidence.
3. Ask the medical attendance question and show the `CONTRADICTION` state with both sources.
4. Ask the wedding absence question and show `NO_ANSWER`.
5. Briefly show `contradictions.md` and `evaluate.py`.
6. Run the evaluation and show the measured result.

The main point of the demo is not the UI. It is showing that the application can answer, refuse, and detect a conflict without hiding the evidence.

## Project structure

```text
rulebook_truth_project/
├── app.py
├── evaluate.py
├── requirements.txt
├── contradictions.md
├── README.md
├── corpus/
│   ├── handbook.md
│   ├── fee_schedule.md
│   ├── project_notice.md
│   └── medical_annex.pdf
├── tests/
│   ├── answerable_questions.json
│   ├── contradiction_questions.json
│   └── unknown_questions.json
└── src/
    └── rulebook.py
```

## One limitation

The contradiction detector in this demo is intentionally deterministic because the three contradictions are known test cases. That makes the result reproducible for the placement evaluation, but it is not a general-purpose theorem prover. If I continued the project, the next step would be to add a general contradiction candidate detector and an NLI model, while keeping the final answer traceable to the original clauses.

The corpus is synthetic and created only for this coding challenge. It should not be treated as an actual university policy.
