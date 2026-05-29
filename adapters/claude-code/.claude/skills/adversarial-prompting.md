# Adversarial Prompting

When facing a complex problem that needs multiple solution approaches and validated fixes before implementation, use this skill.

## Doctrine

Do not commit to the first plausible solution. Generate several, attack each for how it fails, fix the weaknesses, prove the fixes hold, then rank. Surface failure modes before they cost real time or money.

Use for high-stakes or multi-path decisions. Skip for obvious problems or decisions too urgent to analyze.

## Seven phases

1. Generate 3-7 distinct solutions (reasoning + strategy + steps each).
2. Critique each: edge cases, failure modes, security, bottlenecks, scaling, hidden assumptions, resource limits, unintended/catastrophic outcomes.
3. Fix each weakness at the root cause; explain integration.
4. Validate each fix: does it resolve the weakness, does it add new problems, what trade-offs remain.
5. Consolidate complementary elements into stronger combined approaches.
6. Rank viable options by feasibility, impact, risk, resource cost.
7. Recommend the top choice with rationale, next steps, success metrics, and early warning signs.

## Output

Three sections: detailed walkthrough (phases 1-5), ranked summary of options (phase 6), final recommendation (phase 7). Export the full analysis to a Markdown file when the environment allows.

Canonical full reference: https://github.com/abe238/community-skills/blob/main/agents/adversarial-prompting.md
