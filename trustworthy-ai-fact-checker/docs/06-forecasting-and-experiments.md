# 6. Forecasting and testing: how to know if an action will grow the company

You asked: can I just simulate it with math, or do I have to test it for real? **Both, in that
order.** A simulation tells you what your assumptions imply and which assumption matters most.
Only a real test tells you whether the assumptions are true. A simulation cannot prove cause
and effect; it can only tell you where to point the test.

## The loop (the "system" you described)

```
1. Baseline   – measure where the company is now (the numbers the fee will be judged against)
2. Forecast   – for each action: a range (P10/P50/P90) and a probability of hitting the target
3. Pre-register – write the forecast down, dated, BEFORE acting (see docs/07)
4. Test small – pilot with a comparison group where possible
5. Measure    – same metrics, same method as the baseline
6. Score      – how close was the forecast? (Brier score, sim/brier.py)
7. Decide     – scale it, change it, or kill it; update the next forecast
```

This is the same loop as Deming's Plan-Do-Study-Act and the Lean Startup's build-measure-learn.
What makes yours different is steps 3 and 6: every forecast is recorded and graded, so over time
you (and the company's leaders) build a measurable track record.

## What the research says works for forecasting

| Method | What it is | Source to check |
|---|---|---|
| **Reference-class forecasting ("outside view")** | Start from how similar projects actually turned out, then adjust. The biggest single fix for over-optimism. | Kahneman & Tversky; Bent Flyvbjerg, *How Big Things Get Done* (2023) |
| **Superforecasting practices** | Break questions down, give probabilities not words, update often in small steps, keep score with Brier scores. | Philip Tetlock & Dan Gardner, *Superforecasting* (2015); Good Judgment Project |
| **Combine several forecasts** | The average of several independent forecasts usually beats any single one. | Makridakis M-competitions (M4, M5); Armstrong, *Principles of Forecasting* (2001) |
| **Simple beats complex for business time series** | Simple statistical methods are hard to beat; start there. | Hyndman & Athanasopoulos, *Forecasting: Principles and Practice* (free online) |
| **Monte Carlo on a driver tree** | Break the result into drivers (hours × rate × margin − cost), give each a range, simulate. | Douglas Hubbard, *How to Measure Anything* (3rd ed. 2014) |
| **Value of information** | Measure the most uncertain, highest-impact input first; measuring the rest is often wasted effort. | Hubbard, same book |

## What the research says works for testing cause and effect

| Method | When to use it | Source |
|---|---|---|
| **Randomized experiment** | You can randomly choose which teams/lines/sites get the change | Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments* (2020) |
| **Difference-in-differences** | One site gets the program, a similar one doesn't; compare the change over time in both | Angrist & Pischke, *Mastering 'Metrics* (2014) |
| **Synthetic control** | Only one unit is treated (e.g. the whole company); build a comparison from a weighted mix of similar units | Abadie, Diamond & Hainmueller (2010) |
| **Before/after only** | Last resort; can't separate your effect from the economy or seasons | – |

The best real evidence that *management practices* cause productivity gains is a randomized
experiment in Indian textile firms: Bloom, Eifert, Mahajan, McKenzie & Roberts, "Does Management
Matter? Evidence from India," *Quarterly Journal of Economics* (2013). It's also a model for how
you could prove your own service works.

## Evidence on employee participation specifically (read before selling it)

- Employee ownership and profit-sharing show **small positive** average effects on productivity and
  firm survival, larger when paired with real participation in decisions:
  Kruse, Freeman & Blasi, *Shared Capitalism at Work* (NBER / Univ. of Chicago Press, 2010);
  O'Boyle, Patel & Gonzalez-Mulé, "Employee ownership and firm performance: a meta-analysis,"
  *Human Resource Management Journal* (2016).
- **Counter-evidence:** Germany's board-level worker representation had small effects, not large
  ones: Jäger, Schoefer & Heining, "Labor in the Boardroom," *QJE* (2021). Employee voice isn't a
  magic lever; how it's designed and what information voters get seems to matter.
- Corporate prediction markets (letting employees bet play-money on outcomes) have been run at
  Google, HP and others with forecasts competitive with official ones: Cowgill & Zitzewitz,
  "Corporate Prediction Markets," *Review of Economic Studies* (2015).

These give you the honest pitch: *small, real effects on average, and our system is designed
around the conditions where the effects are largest.*

## Try it

`python3 sim/forecast.py` runs a worked example. With made-up but plausible inputs, a preventive
maintenance proposal comes out a **coin flip (≈49% chance it pays for itself)**, and one input,
*how much downtime it really removes*, drives most of the uncertainty. So the next step is not
"approve" or "reject". It is "pilot it on one line for 8 weeks and measure that one number."
That is the system working.
