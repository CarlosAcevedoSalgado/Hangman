# 8. Getting paid for growth (performance-based pricing)

## The model that already works: energy-savings contracts

Energy Service Companies (ESCOs) have sold "we only get paid if you save" for decades. The key
is not the promise; it is the **measurement protocol** both sides sign up front: the
International Performance Measurement and Verification Protocol (IPMVP, from the Efficiency
Valuation Organization). It defines the baseline, how to adjust it for things outside anyone's
control (weather, production volume), and who measures. Copy this structure.

## Recommended structure: base fee + success fee

| Part | Example | Why |
|---|---|---|
| Base fee | $15K–$25K | Covers your cost; protects you if the market tanks for reasons unrelated to your work |
| Success fee | 10–20% of verified net gain above baseline, capped | Aligns you with the company's growth, which is the point of your pitch |
| Cap | e.g. $60K–$100K year one | Makes it easy for a CFO to approve |
| Measurement plan | Signed before work starts | Prevents the argument at the end |

`sim/forecast.py` shows what this means for you: on a coin-flip proposal your fee mostly lands
at the base, so **a pure success-fee deal would make your income a coin flip too.** Keep the base.

## The hard part: attribution

"The company grew" isn't proof *you* caused it. Revenue moves with the economy, prices and
seasons. Protect both sides by:

- paying on **metrics the program directly touches** (cost savings from funded proposals,
  downtime, turnover, safety incidents) rather than total company revenue;
- adjusting the baseline for volume and market (the IPMVP idea);
- using a comparison site or department where possible (docs/06, difference-in-differences).

## Pushback

A one-person firm carrying multiple success-fee contracts can get squeezed on cash flow: you do
the work now and get paid 12+ months later. The first one or two deals probably need a larger
base fee, or a mid-year payment on leading indicators.
