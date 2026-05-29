# AGENTS.md — prompt-optimizer

Use this instruction block for Codex/OpenAI-style coding agents and any agent that reads `AGENTS.md`.

## Trigger

When the user asks to optimize, improve, rewrite, or score a prompt, or wants a basic prompt turned into a structured high-performance prompt, follow this rule.

## Rule

A good prompt is clear, contextual, and structured. Compound multiple proven techniques rather than adding one trick. Golden Rule: a competent colleague should understand the prompt with no extra context.

## Core techniques (priority order)

1. Be clear and direct — context, audience, workflow, success criteria. (always)
2. Use examples — 3-5 diverse, progressive, edge-case examples. (format matters)
3. Let the model think — structured chain of thought. (complex reasoning)
4. Use XML tags — separate parts into cognitive containers. (multi-part)
5. Give a role — specific expert persona. (domain expertise)
6. Prefill / format control — guide output shape. (strict format)
7. Chain prompts — sequential steps. (multi-step workflows)

Add a constraint hierarchy when useful: hard (must satisfy), soft (preferred), anti (avoid).

## Three-pass method

1. Coverage: clarity assessment + technique selection.
2. Structure: XML organization, examples, chain of thought; mark `[VERIFY]` for uncertain spots.
3. Polish: latest-model best practices, reduce markdown overuse, add hallucination guards, strip `[VERIFY]` tags.

## Output

```text
Optimized prompt: <rewritten prompt>
Techniques applied: <which of the 7, and why>
What changed: <key improvements over the original>
Quality score: <1-10 with weakest remaining area>
```

Full reference: https://github.com/abe238/community-skills/blob/main/agents/prompt-optimizer.md
