# contradictions.md

The corpus intentionally contains exactly three planted contradictions. These are the gold cases for the contradiction state.

## C-01 — Attendance
- Clause A: `handbook.md`, §2 / Rule 2.1: **75% attendance is required** for end-term examination eligibility.
- Clause B: `medical_annex.pdf`, page 2, Annex A.4: **65% attendance is sufficient** for a student with an approved medical absence.
- Why this is a contradiction: the two clauses give different thresholds for a medical case. The system should surface both clauses and avoid choosing one silently.

## C-02 — Tuition deadline
- Clause A: `handbook.md`, §9 / Rule 9.2: **15 September** is the standard tuition deadline.
- Clause B: `fee_schedule.md`, row `F-03`: **20 September** is listed for the same undergraduate standard tuition category.
- Why this is a contradiction: the same charge category has two different deadlines in the corpus.

## C-03 — Final project late submission
- Clause A: `handbook.md`, §15 / Rule 15.3: a final project after the deadline is not accepted unless an extension was approved before the deadline.
- Clause B: `project_notice.md`, §P-7: a final project can be submitted within **48 hours after the deadline without prior approval**, with a late penalty.
- Why this is a contradiction: the two clauses disagree about whether prior approval is required for a late final project.

Do not add another contradiction to the demo corpus without updating the evaluation set. The intended count is exactly three.
