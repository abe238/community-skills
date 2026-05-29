# AGENTS.md — adversarial-prompting

Use this instruction block for Codex/OpenAI-style coding agents and any agent that reads `AGENTS.md`.

## Trigger

When the user faces a complex problem, a high-stakes decision, or a proposal that should be stress-tested before implementation, follow this rule.

## Rule

Do not commit to the first plausible solution. Generate several, attack each one for how it fails, fix the weaknesses, prove the fixes hold, then rank. The value is surfacing failure modes before they cost real time or money.

Skip for obvious problems, urgent decisions that cannot wait for analysis, or exploratory work where iteration beats upfront analysis.

## Seven-phase process

1. Generate 3-7 distinct solutions (reasoning + core strategy + key steps each).
2. Critique each: edge cases, failure modes, security risks, bottlenecks, scaling limits, hidden assumptions, resource constraints, unintended/catastrophic outcomes.
3. Fix each weakness at the root cause; explain how it integrates.
4. Validate each fix: does it resolve the weakness, does it add new problems, what trade-offs remain.
5. Consolidate complementary elements across solutions into stronger combined approaches.
6. Rank viable options by feasibility, impact, risk, and resource cost.
7. Recommend the top choice (or combination) with rationale, next steps, success metrics, and early warning signs.

## Output

Three sections: detailed walkthrough (phases 1-5), ranked summary of options (phase 6), final recommendation (phase 7). Export the full analysis to a Markdown file when the environment allows.

Full reference: https://github.com/abe238/community-skills/blob/main/agents/adversarial-prompting.md
