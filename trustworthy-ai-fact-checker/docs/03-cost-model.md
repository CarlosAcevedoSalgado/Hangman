# 3. Cost model: can $10 become 1 cent?

Short answer: **for the routine majority of claims, roughly yes; for high-stakes claims, no –
and you shouldn't want it to.** The business win is the blended cost.

All numbers below are **assumptions to be replaced with measured values** in Phase 1.

## Human baseline (estimate)

| Item | Assumption |
|---|---|
| Time per claim (find source, verify, write up) | 15 min (simple) to 2+ hrs (complex) |
| Loaded cost of an analyst/researcher | ~$40–$60 / hr |
| **Cost per claim** | **~$10 (simple) to $100+ (complex)** |

## AI cost per claim (estimate)

`cost = (input tokens × input price + output tokens × output price) + search API calls`

A single claim typically needs a few model calls (extract, verify, critique) plus a few searches.
Depending on model choice and how much evidence is read, that is plausibly **a fraction of a cent
to ~$0.25 per claim**. Use a small, cheap model for extraction/triage and reserve the strongest
model for verification. *Verify against current API pricing before quoting any customer.*

## Blended cost with tiered human review

| Tier | Share of claims (assumed) | Handling | Cost / claim |
|---|---|---|---|
| Low stakes, high confidence | 70% | AI only, humans sample 5% | ~$0.05 + sampling |
| Medium | 25% | AI + quick human confirm (3 min) | ~$3 |
| High stakes / low confidence | 5% | Full human check, AI-prepared dossier cuts time ~50% | ~$25 |

Blended ≈ **$2 per claim vs. ~$15–$20 fully manual** – roughly a 90% reduction, with
humans still on everything that matters. The "1 cent" figure applies to the bottom tier only.

## Where the cost actually goes (warning)

The model calls are cheap. The expensive parts are:

1. **Integrating internal data** (ERP, safety, HR, finance systems) – one-time per customer, often weeks.
2. **Human reviewers** for the high-stakes tier.
3. **Building trust** – the audit log, corrections process, and change management.

Price the service around those, not around token cost.
