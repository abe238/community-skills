# Prompt Optimizer

Use this when a user wants to improve a prompt, raise output quality/consistency, or transform a basic prompt into a high-performance structured prompt.

## Core doctrine

A good prompt is clear, contextual, and structured. Apply the compound effect of multiple proven techniques rather than one trick — XML structure + examples + chain of thought + role + constraints multiply quality.

The Golden Rule: would a competent colleague understand this prompt with no extra context? If not, it is not ready.

## When to use

- A basic prompt needs optimization.
- Output is inconsistent, low quality, or wrong format.
- Complex reasoning needs better structure.
- Domain expertise or strict output format must be enforced.

Not for: writing brand-new content from scratch, general chat, or single trivial instructions that already work.

## Core techniques (apply in priority order)

1. **Be clear and direct** (always): add context, audience, workflow, and success criteria.
2. **Use examples** (format matters): 3-5 diverse, relevant, progressive examples covering edge cases.
3. **Let the model think** (complex reasoning): add structured chain of thought — thinking → alternatives → evaluation → answer.
4. **Use XML tags** (multi-part prompts): separate parts into meaningful cognitive containers.
5. **Give a role** (domain expertise): add a specific expert persona when specialized knowledge is needed.
6. **Prefill / format control** (strict output): guide the response shape.
7. **Chain prompts** (multi-step workflows): break dependent tasks into sequential steps.

Add constraint hierarchy where useful: hard constraints (must satisfy), soft constraints (preferred), anti-constraints (avoid).

## Three-pass method

1. **Coverage**: assess clarity, select techniques by task type, add context/role/success criteria.
2. **Structure**: organize with XML, add examples and chain of thought, layer context, mark uncertain spots with `[VERIFY]`.
3. **Polish**: apply latest model best practices, remove markdown overuse, add hallucination guards, resolve and strip `[VERIFY]` tags.

## Output shape

```text
Optimized prompt: <the rewritten prompt with techniques applied>
Techniques applied: <which of the 7, and why>
What changed: <key improvements over the original>
Quality score: <1-10 with the weakest remaining area>
```

## Canonical phrase

> Optimize prompts by compounding proven techniques, not by adding one clever trick.
