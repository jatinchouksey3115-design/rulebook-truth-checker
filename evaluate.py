
import json, csv
from pathlib import Path
from src.rulebook import Rulebook

ROOT = Path(__file__).resolve().parent
rb = Rulebook()

sets = [
    ROOT/"tests"/"answerable_questions.json",
    ROOT/"tests"/"contradiction_questions.json",
    ROOT/"tests"/"unknown_questions.json"
]
cases = []
for p in sets:
    cases.extend(json.loads(p.read_text(encoding="utf-8")))

rows = []
for item in cases:
    out = rb.answer(item["question"])
    predicted = out["state"]
    ok = predicted == item["expected"]
    if ok and item["gold_clauses"]:
        # For contradiction cases, gold clause pair is represented by contradiction_id.
        if predicted == "CONTRADICTION":
            ok = out.get("contradiction_id") in item["gold_clauses"]
        elif predicted == "ANSWER":
            # For answerable cases, the cited evidence must contain a gold phrase.
            cited_text = " ".join(c["text"].lower() for c in out["citations"])
            phrases = [p.lower() for p in item.get("gold_phrases", [])]
            ok = any(p in cited_text for p in phrases)
    rows.append({
        "id": item["id"],
        "expected": item["expected"],
        "predicted": predicted,
        "correct": ok,
        "question": item["question"]
    })

Path(ROOT/"evaluation_results.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")

total = len(rows)
correct = sum(r["correct"] for r in rows)
print("\nRULEBOOK EVALUATION")
print("===================")
print(f"Total cases: {total}")
print(f"Correct: {correct}")
print(f"Accuracy: {correct/total:.1%}")
for state in ["ANSWER","CONTRADICTION","NO_ANSWER"]:
    group = [r for r in rows if r["expected"] == state]
    if group:
        n = sum(r["correct"] for r in group)
        print(f"{state}: {n}/{len(group)} = {n/len(group):.1%}")
print("\nHard NO_ANSWER set (25 near-misses):")
u = [r for r in rows if r["id"].startswith("U-")]
n = sum(r["correct"] for r in u)
print(f"{n}/25 = {n/25:.1%}")
print("\nMachine-readable results written to evaluation_results.json")
