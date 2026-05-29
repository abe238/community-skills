# AGENTS.md — adversarial-prompting for OpenClaw and Markdown-first agents

This repository's portable skill is `../../agents/adversarial-prompting.md`.

## When to use

Use it when the user faces a complex problem, a high-stakes decision, or a proposal that should be stress-tested before implementation.

## Non-negotiable rule

Do not commit to the first plausible solution. Generate several, attack each for how it fails, fix the weaknesses, prove the fixes hold, then rank.

Skip for obvious problems, urgent decisions that cannot wait for analysis, or exploratory work where iteration beats upfront analysis.

## Seven-phase process

1. Generate 3-7 distinct solutions (reasoning + core strategy + key steps each).
2. Critique each: edge cases, failure modes, security risks, bottlenecks, scaling limits, hidden assumptions, resource constraints, unintended/catastrophic outcomes.
3. Fix each weakness at the root cause; explain how it integrates.
4. Validate each fix: does it resolve the weakness, does it add new problems, what trade-offs remain.
5. Consolidate complementary elements into stronger combined approaches.
6. Rank viable options by feasibility, impact, risk, and resource cost.
7. Recommend the top choice with rationale, next steps, success metrics, and early warning signs.

## Required output

Three sections:

1. Detailed walkthrough — phases 1-5 with reasoning visible.
2. Summary of options — ranked list (phase 6).
3. Final recommendation — top choice with implementation guidance (phase 7).

When the environment allows file output, export the full analysis to a Markdown file for later reference.
