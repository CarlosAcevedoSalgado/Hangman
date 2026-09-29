# 7. Making leadership's claims checkable ("can we trust what they tell us?")

Nothing is literally irrefutable. What you *can* build is a system where every claim is
**checkable, recorded, and scored**, so trust comes from a track record anyone can inspect,
not from who said it.

## Four mechanisms, from easiest to hardest

1. **Claims with receipts.** Every number in a plan or announcement links to its source
   (the report, the dataset, the query). The AI fact-checker (docs/02) checks each claim
   against that source and flags anything unsupported *before* employees vote.
2. **Pre-registered forecasts.** Every plan put to a vote must state its predictions up front:
   "This will cut costs $X by date Y, 70% confident." Dated and locked before the vote.
   Afterwards the outcome is recorded next to it. (Borrowed from pre-registration in science.)
3. **Public scorecards.** Each forecaster (the CEO, department heads, employee proposal teams)
   gets a Brier score over time (`sim/brier.py`). Leaders who forecast well earn credibility;
   the scorecard, not rhetoric, decides whose plans get the benefit of the doubt.
4. **Tamper-evident records + independent audit.** The claim/forecast log is append-only and
   each entry is hashed together with the previous one, so any later edit is detectable. The key
   numbers are confirmed by the company's existing external auditor or an agreed third party.
   (A blockchain isn't needed; a hash-chained log plus an outside auditor is enough and far simpler.)

## How this ties into the vote

Employees vote on the plan, and they vote knowing (a) which claims in it were verified,
(b) the forecast they are signing up for, and (c) the author's forecasting track record.
Related idea worth reading: Robin Hanson's "futarchy": *vote on values, bet on beliefs*.
Employees decide what they want (goals); forecasts and evidence decide which plan is most likely
to get there.

## Limits (say these out loud to customers)

- The system can verify that a claim matches the company's data; it can't guarantee the data
  itself wasn't falsified upstream. That's what the independent audit is for.
- Scoring forecasts creates an incentive to predict only safe things. Counter it by having the
  voters, not the forecaster, choose which questions get forecast.
