# 2. AI fact-checker architecture

The design principle: **the model never grades a claim from memory.** Every verdict must be
grounded in retrieved evidence that a human can click on. Memory-only answers are where AI
"hallucinates."

## Pipeline

```
input (document / proposal / transcript)
  │
  ▼
1. Claim extraction ──► atomic, self-contained claims
  │
  ▼
2. Check-worthiness triage ──► skip opinions & trivia; tag stakes (low / medium / high)
  │
  ▼
3. Prior-check lookup ──► already checked? (our own cache, ClaimReview index)
  │
  ▼
4. Evidence retrieval ──► web search + internal company data (financials, safety logs, HR data)
  │
  ▼
5. Source assessment ──► reputation, independence, primary vs. secondary, recency
  │
  ▼
6. Verification ──► claim vs. evidence: supports / refutes / not enough info, with quotes
  │
  ▼
7. Adversarial second pass ──► a separate model call tries to break the verdict
  │
  ▼
8. Confidence + routing ──► high confidence & low stakes → auto-publish
  │                         low confidence or high stakes → human reviewer queue
  ▼
9. Report ──► verdict, explanation, every source linked, date checked
  │
  ▼
10. Feedback loop ──► human corrections become test cases; accuracy tracked over time
```

## Key design decisions (and why)

- **Atomic claims.** Verification accuracy drops sharply on compound statements; decomposing first
  is the cheapest accuracy gain available.
- **Internal data is a first-class source.** For the employee-voice use case most claims are about
  the company itself ("this machine causes 30% of downtime"). The checker needs read access to
  the relevant systems, not just the web. This is also the biggest integration cost.
- **"Not enough evidence" is a valid verdict.** Forcing true/false creates false confidence.
- **Separate verifier from critic.** A second, independently prompted pass that argues the other side
  catches a meaningful share of errors cheaply.
- **Human-in-the-loop by stakes, not by default.** This is what makes the economics work (see `03`).
- **Everything logged.** Each verdict stores claim, evidence, model version, and reviewer, so the
  system can be audited – required for trust and for the corrections policy.

## Measuring "best fact-checker"

"Best" has to be a number, or it's marketing:

- **Accuracy** against a labelled set (start with FEVER-style public data, then build a company-specific set from reviewed claims).
- **Calibration** – when it says 90% confident, is it right ~90% of the time?
- **Coverage** – share of claims it can resolve without a human.
- **Cost and latency per claim.**
- **Correction rate** after publication.

## Likely tech stack (prototype)

- A frontier LLM API for extraction, verification and critique (structured JSON outputs).
- A web search API + page fetching for evidence.
- A small database (e.g. Postgres/Supabase) for claims, evidence, verdicts, reviews.
- A simple review UI for human checkers.
