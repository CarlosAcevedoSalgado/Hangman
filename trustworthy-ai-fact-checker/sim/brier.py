"""Score a log of predictions so forecasters (and leadership) build a track record.

Brier score = average of (probability - outcome)^2, where outcome is 1 if it happened, 0 if not.
0.00 is perfect; 0.25 is what you get by always saying 50%; lower is better.

Run:  python3 brier.py predictions.csv
CSV columns: who,claim,probability,outcome   (outcome blank = not resolved yet)
"""
import csv
import sys
from collections import defaultdict


def main(path):
    scores = defaultdict(list)
    open_count = 0
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if row["outcome"].strip() == "":
                open_count += 1
                continue
            p, o = float(row["probability"]), int(row["outcome"])
            scores[row["who"]].append((p - o) ** 2)
    print(f"{'who':<24}{'resolved':>9}{'brier':>8}")
    for who, s in sorted(scores.items(), key=lambda kv: sum(kv[1]) / len(kv[1])):
        print(f"{who:<24}{len(s):>9}{sum(s) / len(s):>8.3f}")
    print(f"\n{open_count} prediction(s) still open.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "predictions.csv")
