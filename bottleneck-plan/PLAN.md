# Finding a bottleneck worth an AI product: the plan

## Verdict
Do the discovery sprint before choosing anything. Don't pick an idea yet, and don't write product code yet.
- 35% confident (Tier D) that within 45 days you find a problem where at least 3 of 15 interviewed companies agree to a paid pilot.
- About 5% confident (Tier E, speculative) that any specific idea reaches $1M/year revenue within 3 years. The base rate is roughly half of all new businesses surviving 5 years (BLS), and only a small minority of software startups ever reach $1M/year.

The sprint exists to raise that second number cheaply before you spend real money.

## The method (each step is a known, tested practice)
1. **Look where you have an unfair view: your own industry and company.** Founders who come from inside an industry see problems that outsiders can't. Run a Theory-of-Constraints scan (Goldratt) on Wilkinson: which single step limits the throughput of jobs or cash? Priced in dollars.
2. **Follow the money and the hours.** List every task that is (a) repeated weekly, (b) done by expensive people, (c) based on documents or data, and (d) costly when it goes wrong. AI is good at jobs like that.
3. **Run 15 Mom Test interviews** (Rob Fitzpatrick, *The Mom Test*). Ask about past behavior, never "would you buy this?". The script is below.
4. **Score each candidate** with `python score.py opportunities.csv`, using the numbers from your interviews in place of my guesses.
5. **Sell before you build (a concierge pilot).** Deliver the result by hand (you plus me plus spreadsheets) for 3 paying pilots. Automate only the steps you repeat.
6. **Build the narrow AI system.** I write the code (document extraction + LLM + rules + a simple web app), and your pilot data becomes the test set.
7. **Grow by repeating what worked:** referrals inside the trade, associations (AGC/ABC/ASA), and case studies with dollar figures.

## Interview script (20 minutes: PMs, estimators, office managers, owners at GCs and subs)
1. "Walk me through last week. What took the most hours that you wish you didn't have to do?"
2. "Tell me about the last time [that task] went wrong. What did it cost?" (Get a dollar amount or hours.)
3. "How do you handle it today? What tools or people?" (If they've never tried to fix it, it isn't painful enough.)
4. "What have you paid for or tried to fix it? Why did you stop?"
5. "Who else deals with this? Can you introduce me?"
6. Close: "If I did this for you by hand on your next job for $X, would you try it?" A yes with money or a date counts as a commitment. A compliment doesn't count.

Record every interview in `interviews.csv`: date, role, company size, problem, cost in $/hrs, current fix, commitment (Y/N).

## Current shortlist (Stage 1 scores are Tier D priors, to be replaced by interview data)
| Idea | Score /65 | Main issue |
|---|---|---|
| GC bid leveling | 49 | Procore, BuildingConnected, Bidi and Buildr already ship AI bid leveling |
| AI certified translation (Ace Translate) | 48 | Fastest revenue, but it competes mostly on price |
| Specialty-sub T&M / change-order capture | 47 | eSUB, Rhumbix and Clearstory already exist |
| Submittal review AI | 37 | Crowded, plus liability if it approves a wrong spec |
| Generic AP/invoice AI | 33 | Saturated, and you have no insider edge |

Honest takeaway: the obvious construction-AI niches were already crowded in 2026. Your advantage is access to find a problem that isn't on vendors' lists, one that only shows up from inside a GC.

## Plan comparison (Plan Quality Score, out of 95)
| Plan | Score | Why |
|---|---|---|
| A. Pick an idea now and build an app | 29 | No outside view, no early feedback, expensive to reverse |
| B. Discovery sprint, then concierge pilot, then build (recommended) | 80 | Reality can prove it wrong within days, and each step is cheap |
| C. Productize Ace Translate first as a bridge for cash | 69 | Fast revenue, lower ceiling; can run alongside B |

## Risk register (score = P x I x S x W/3)
| Risk | P | I | S | W | Score | Class | Playbook | Early warning |
|---|---|---|---|---|---|---|---|---|
| Employer conflict (IP, confidentiality, non-compete with Wilkinson) | 3 | 5 | 2 | 4 | 40 | Real | Read your employment agreement, never use Wilkinson data without written OK, consider offering Wilkinson a stake or pilot | Any clause on inventions or outside work |
| Crowded market / incumbent ships a feature | 4 | 4 | 3 | 2 | 32 | Real | Go narrower (one trade, one document type) and win on service | Interviewees name an existing tool they like |
| AI error causes customer loss / liability | 2 | 4 | 2 | 5 | 27 | Friction | Human review, disclaimers, keep AI as an assistant rather than the approver | Near-miss in a pilot |
| Never starting or finishing | 4 | 5 | 2 | 1 | 13 | Friction | If-then schedule below, weekly check-in | Fewer than 3 interviews in week 1 |
| Building before selling | 4 | 4 | 1 | 2 | 11 | Friction | Rule: no code until 3 paid pilots | Asking to build before pilots exist |

## First 14 days (if-then steps)
- If it's tonight: fill in PROFILE.md (hours per week, money you can risk, what your employment contract says).
- If it's Monday 7am: write down the 10 most-repeated painful tasks at Wilkinson, with hours per week for each.
- If it's Tuesday lunch: message 5 people (PMs, estimators, subs you know) asking for 20 minutes about their week.
- If an interview is booked: use the script above and log it within one hour.
- If it's Friday 4pm: update interviews.csv and rescore opportunities.csv. Send it to Claude for a rescore.
- If it's day 14 and you have fewer than 8 interviews: the problem is outreach volume, not the idea. Double the messages.

## Kill criteria
- Day 45: fewer than 3 of 15 interviewees are paying or committed on any single problem → drop that problem and take the next one on the list.
- Day 120: no paid pilot → stop the construction track and run Plan C only.
- Revenue milestones get set after the pilots. Right now they would be guesses.

## About "millions per day"
$1M/day is $365M/year, a large public-company scale that very few companies ever reach. A realistic ladder is $10k/month (proof), then $100k/month ($1.2M/year, a real company), then more. At $500/month per customer, $1M/year takes about 167 customers and $1M/month takes about 2,000.

## Who does what
- **Claude:** code, data pipelines, AI models, analysis, scoring, drafts of outreach, contracts to review, support docs and support bots.
- **You:** interviews, selling, customer relationships, legal and company setup. I can't talk to customers for you, and that is the part that decides the outcome.
