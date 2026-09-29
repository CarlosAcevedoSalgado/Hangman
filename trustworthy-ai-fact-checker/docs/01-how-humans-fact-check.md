# 1. How humans fact-check

Before automating anything, copy the process that professionals already trust.

## The professional workflow (newsrooms and dedicated fact-checking orgs)

Organizations such as PolitiFact, Full Fact (UK), AFP Fact Check and others that sign the
**IFCN Code of Principles** (International Fact-Checking Network, hosted by Poynter) follow
roughly the same loop:

1. **Monitor** – watch a stream of content (speeches, articles, social posts, reports).
2. **Select check-worthy claims** – not every sentence is checkable. A claim is worth checking
   if it is *factual* (not opinion), *specific* (numbers, dates, named entities), and
   *consequential* (people will act on it).
3. **Decompose** – split a compound statement into atomic claims that can each be true or false.
   "Our plant cut injuries 40% and saved $2M" is two claims.
4. **Find the original source** – trace a statistic back to where it was first published, not
   the article that repeated it.
5. **Lateral reading** – instead of judging a source by its own website, leave it and check
   what *other* reliable sources say about it. (Stanford research by Wineburg & McGrew found
   professional fact-checkers do this and outperform academics and students.)
6. **Seek independent corroboration** – two sources that copied each other count as one.
7. **Contact the claimant / experts** – ask for their evidence.
8. **Rate and explain** – give a verdict on a defined scale (e.g. True / Mostly true / Half true /
   Mostly false / False / Unverifiable) *with* the reasoning and every source linked.
9. **Editorial review** – a second person checks the check before publishing.
10. **Corrections policy** – publicly fix mistakes. This is what sustains trust over time.

## The quick version: SIFT (Mike Caulfield)

- **S**top – notice your emotional reaction; don't share yet.
- **I**nvestigate the source – who is behind it, what's their expertise and agenda?
- **F**ind better coverage – what do other trusted sources say?
- **T**race claims to the original context – quotes, images and numbers often get distorted.

## IFCN principles (why people trust a fact-checker)

Non-partisanship and fairness · transparency of sources · transparency of funding and
organization · transparency of methodology · open and honest corrections.

**Takeaway for us:** trust doesn't come from being right once; it comes from showing your work,
using the same method every time, and correcting mistakes openly. An AI fact-checker must
be designed around those five principles, not bolted on afterwards.

## What's hard for humans (and therefore where software helps most)

| Step | Human cost | Automatable? |
|---|---|---|
| Monitoring / claim spotting | High volume, tedious | Yes – very well |
| Decomposition | Moderate | Yes – well |
| Finding original sources | Slow (the biggest time sink) | Mostly – search + retrieval |
| Lateral reading / source reputation | Needs judgment | Partly – reputation lists + model reasoning |
| Contacting people | Slow | No (but can draft the request) |
| Verdict + write-up | Moderate | Yes, with human review for high stakes |
| Editorial review | Expensive | Partly – a second, independent model pass, then human sampling |

## Existing tools and research worth knowing

- **ClaimBuster** (UT Arlington) – scores sentences for check-worthiness.
- **Google Fact Check Explorer / ClaimReview markup** – a searchable index of already-published
  fact-checks. First step for any claim: has someone already checked it?
- **FEVER** dataset – an academic benchmark for claim verification against evidence; useful for
  measuring our accuracy.
- **Full Fact AI tools** – production monitoring tools used by fact-checkers in several countries.
