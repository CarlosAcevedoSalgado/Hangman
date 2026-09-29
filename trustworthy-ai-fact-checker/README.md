# Trustworthy AI Fact-Checker

> Working name. This folder is self-contained so it can be lifted into its own repository
> (`trustworthy-ai-fact-checker`) as soon as GitHub access allows creating one.

## The idea in one paragraph

Build an AI system whose only job is to be the best fact-checker it can be, and use it as the
**trust layer** for a bigger service: helping mid-to-large, community-rooted companies
(Louisville examples: UPS, Humana, LG&E, GE Appliances, Ford) let their long-tenured employees
propose and vote on how part of the company's budget and plans are spent. Employee voice only
works if everyone is arguing from the same verified facts; the fact-checker is what makes that
possible cheaply, at a cost per checked claim that is cents instead of dollars.

## Two products, one engine

| Layer | What it is | Who pays |
|---|---|---|
| **Engine** – AI fact-checker | Extracts claims, gathers evidence, grades each claim with citations, routes risky ones to humans | Usable on its own (internal comms, proposals, reports, marketing review) |
| **Service** – Employee-voice governance | Design + run a program where eligible employees propose and vote on a slice of the annual plan / capex, with every proposal fact-checked | Company engagement ($30K–$50K target, see `docs/04`) |

The engine is the part that is software and scales. The service is the part that is sold and
proves the engine's value.

## Where to read next

1. [`docs/01-how-humans-fact-check.md`](docs/01-how-humans-fact-check.md) – how professionals actually do it (the process we automate)
2. [`docs/02-ai-fact-checker-architecture.md`](docs/02-ai-fact-checker-architecture.md) – the pipeline, step by step
3. [`docs/03-cost-model.md`](docs/03-cost-model.md) – the "$10 becomes 1 cent" math, and where it doesn't hold
4. [`docs/04-business-model.md`](docs/04-business-model.md) – the employee-voice service, customers, pricing, prior art
5. [`docs/05-risks-and-open-questions.md`](docs/05-risks-and-open-questions.md) – pushback, unknowns, things to validate
6. [`docs/06-forecasting-and-experiments.md`](docs/06-forecasting-and-experiments.md) – forecast, test, score, adapt (with literature)
7. [`docs/07-verifiable-leadership-claims.md`](docs/07-verifiable-leadership-claims.md) – how employees can trust what leadership tells them
8. [`docs/08-pay-for-growth-pricing.md`](docs/08-pay-for-growth-pricing.md) – getting paid for results without betting your income on a coin flip
9. [`docs/09-master-plan.md`](docs/09-master-plan.md) – the staged plan, gates, and where I disagree with the vision
10. [`docs/10-definition-v2.md`](docs/10-definition-v2.md) – **current definition** after your feedback (read this first)
11. [`ROADMAP.md`](ROADMAP.md) – what to build and validate, in order

## Tools you can run now (Python 3, no installs)

- `python3 sim/forecast.py` – Monte Carlo forecast of a proposal + your pay-for-growth fee
- `python3 sim/brier.py sim/predictions.csv` – scores a prediction log (who forecasts well?)

## Status

Research and design stage. No code yet; the first build milestone is a prototype of the
fact-checking pipeline (see `ROADMAP.md`, Phase 1).
