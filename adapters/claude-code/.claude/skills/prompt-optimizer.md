# Prompt Optimizer

When asked to improve a prompt, raise output quality/consistency, or turn a basic prompt into a structured high-performance one, use this skill.

## Doctrine

A good prompt is clear, contextual, and structured. Compound multiple proven techniques rather than adding one trick. Golden Rule: a competent colleague should understand the prompt with no extra context.

## Core techniques (priority order)

1. Be clear and direct — context, audience, workflow, success criteria. (always)
2. Use examples — 3-5 diverse, progressive, edge-case examples. (format matters)
3. Let the model think — structured chain of thought. (complex reasoning)
4. Use XML tags — separate parts into cognitive containers. (multi-part)
5. Give a role — specific expert persona. (domain expertise)
6. Prefill / format control — guide output shape. (strict format)
7. Chain prompts — sequential steps. (multi-step workflows)

Add constraint hierarchy when useful: hard / soft / anti-constraints.

## Three-pass method

1. Coverage: clarity assessment + technique selection.
2. Structure: XML, examples, chain of thought, mark `[VERIFY]` for uncertainties.
3. Polish: latest-model best practices, reduce markdown overuse, add hallucination guards, strip `[VERIFY]` tags.

## Output

```text
Optimized prompt: <rewritten prompt>
Techniques applied: <which, and why>
What changed: <key improvements>
Quality score: <1-10 + weakest remaining area>
```

Canonical full reference: https://github.com/abe238/community-skills/blob/main/agents/prompt-optimizer.md
