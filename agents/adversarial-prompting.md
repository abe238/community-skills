# Adversarial Prompting

Use this when a user faces a complex problem — technical or not — that needs thorough analysis, multiple solution approaches, and validation of fixes before committing.

## Core doctrine

Do not commit to the first plausible solution. Generate several, attack each one for how it fails, fix the weaknesses, prove the fixes hold, then rank. The value is in surfacing failure modes before they cost real time or money.

## When to use

- Architecture decisions, debugging, performance, or strategic/business choices with multiple viable paths.
- High-stakes decisions where failure modes must be understood up front.
- Any proposal you want stress-tested before implementation.

Not for: simple problems with an obvious answer, time-critical decisions that cannot wait for analysis, or exploratory work where iteration beats upfront analysis.

## Seven-phase process

1. **Solution generation**: produce 3-7 distinct approaches; for each, give reasoning, core strategy, and key steps.
2. **Adversarial critique**: for each solution, surface edge cases, failure modes, security risks, bottlenecks, scaling limits, hidden assumptions, resource constraints, unintended consequences, and catastrophic scenarios.
3. **Fix development**: for each weakness, propose a specific mitigation, explain why it addresses the root cause, and how it integrates.
4. **Validation check**: verify each fix actually resolves the weakness, introduces no new problems, and flag remaining trade-offs.
5. **Consolidation**: integrate complementary elements across solutions, remove redundancy, combine into stronger approaches.
6. **Summary of options**: rank viable approaches by feasibility, impact, risk, and resource cost; one paragraph each on trade-offs.
7. **Final recommendation**: state the top choice (or combination) with rationale, concrete next steps, success metrics, and early warning signs.

## Output shape

Present in three sections:

1. **Detailed walkthrough** — phases 1-5 with reasoning visible.
2. **Summary of options** — ranked list (phase 6).
3. **Final recommendation** — top choice with implementation guidance (phase 7).

When the environment allows file output, export the full analysis to a Markdown file for later reference.

## Canonical phrase

> Attack every solution before you trust it; a fix is not done until it survives its own critique.
