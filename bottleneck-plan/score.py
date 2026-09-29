"""Opportunity + plan scorer (calibrated-business-planner rubrics).

Usage:
    python score.py opportunities.csv      # Stage 1: rank problems/ideas (max 65)
    python score.py --risk P I S W         # Stage 5: score one risk

Every input is 0-5 (risk inputs 1-5). Edit the CSV as interviews give you evidence;
scores only change when an input changes.
"""
import csv
import sys

WEIGHTS = {  # factor: weight   (0 = bad, 5 = good)
    "pain": 3,         # 0 merely complain ... 5 already pay to solve it today
    "advantage": 2,    # 0 no edge ... 5 rare skill/network/access that applies directly
    "entry_cost": 1,   # 0 heavy capital/credentials ... 5 nearly free to start
    "time_to_rev": 2,  # 0 a year+ ... 5 under a month
    "learnability": 2, # 0 years of apprenticeship ... 5 buildable with AI + practice
    "failure_cost": 2, # 0 mistakes = lawsuits/harm ... 5 cheap, reversible mistakes
    "competition": 1,  # 0 saturated/price war ... 5 clearly underserved
}


def score_row(row):
    return sum(int(row[k]) * w for k, w in WEIGHTS.items())


def rank(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    # Ties break on failure cost: early mistakes must be cheap tuition.
    rows.sort(key=lambda r: (score_row(r), int(r["failure_cost"])), reverse=True)
    print(f"{'score':>5}  {'verdict':<18} idea")
    for r in rows:
        s = score_row(r)
        verdict = "strong" if s >= 50 else "viable" if s >= 40 else "likely fails"
        print(f"{s:>5}  {verdict:<18} {r['idea']}")


def risk(p, i, s, w):
    score = p * i * s * (w / 3)
    cls = ("Ghost fear" if score < 8 else "Friction" if score <= 30
           else "Real risk" if score <= 75 else "Killer")
    print(f"{score:.1f} -> {cls}")


if __name__ == "__main__":
    if sys.argv[1] == "--risk":
        risk(*map(int, sys.argv[2:6]))
    else:
        rank(sys.argv[1])
