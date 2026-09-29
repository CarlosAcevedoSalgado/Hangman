"""Monte Carlo forecast for one proposal, plus what a pay-for-growth fee would earn you.

Every input is a range (low, likely, high) instead of a single number, because a single
number hides how uncertain it is. We sample each range thousands of times and report the
spread of outcomes: P10 (pessimistic), P50 (median), P90 (optimistic).

Run:  python3 forecast.py
Edit the PROPOSAL and FEE dictionaries below to model a real proposal.
Standard library only.
"""
import random
import statistics

RUNS = 20_000
random.seed(7)

# Example proposal: "Add preventive maintenance on Line 3 to cut unplanned downtime."
# Each value: (low, most likely, high). Replace with the customer's real (fact-checked) data.
PROPOSAL = {
    "downtime_hours_per_year_now": (380, 450, 520),
    "share_of_downtime_removed": (0.10, 0.30, 0.45),   # the most uncertain input
    "contribution_margin_per_hour": (1_800, 2_500, 3_200),  # $ lost per hour of downtime
    "annual_program_cost": (250_000, 300_000, 400_000),
}
TARGET_NET_GAIN = 0  # "Does it at least pay for itself?"

# Pay-for-growth contract: base fee + share of verified net gain above the agreed baseline.
FEE = {"base_fee": 20_000, "success_share": 0.15, "success_cap": 60_000}


def tri(low, mode, high):
    return random.triangular(low, high, mode)


def simulate_once():
    p = {k: tri(*v) for k, v in PROPOSAL.items()}
    hours_saved = p["downtime_hours_per_year_now"] * p["share_of_downtime_removed"]
    gain = hours_saved * p["contribution_margin_per_hour"]
    return gain - p["annual_program_cost"]


def pct(values, q):
    return values[int(q * (len(values) - 1))]


def main():
    nets = sorted(simulate_once() for _ in range(RUNS))
    p_hit = sum(n > TARGET_NET_GAIN for n in nets) / RUNS
    print("Net annual gain of the proposal")
    print(f"  P10 ${pct(nets, .10):>12,.0f}   (1 in 10 chance it's worse than this)")
    print(f"  P50 ${pct(nets, .50):>12,.0f}")
    print(f"  P90 ${pct(nets, .90):>12,.0f}   (1 in 10 chance it's better than this)")
    print(f"  Chance it pays for itself: {p_hit:.0%}")

    fees = sorted(
        FEE["base_fee"] + min(FEE["success_cap"], max(0, n) * FEE["success_share"])
        for n in nets
    )
    print("\nYour fee under the pay-for-growth contract")
    print(f"  P10 ${pct(fees, .10):>10,.0f}   P50 ${pct(fees, .50):>10,.0f}   "
          f"P90 ${pct(fees, .90):>10,.0f}   mean ${statistics.mean(fees):,.0f}")

    # Which input drives the uncertainty most? Swing each one low->high, others at mode.
    print("\nWhat drives the uncertainty (swing low -> high, others held at most-likely)")
    base = {k: v[1] for k, v in PROPOSAL.items()}
    for key, (low, _, high) in PROPOSAL.items():
        outs = []
        for val in (low, high):
            p = dict(base, **{key: val})
            outs.append(p["downtime_hours_per_year_now"] * p["share_of_downtime_removed"]
                        * p["contribution_margin_per_hour"] - p["annual_program_cost"])
        print(f"  {key:<32} swing ${abs(outs[1] - outs[0]):>10,.0f}")
    print("\nMeasure the biggest-swing input first: that's where a small test buys the most certainty.")


if __name__ == "__main__":
    main()
