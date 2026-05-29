# AGENTS.md — prompt-optimizer for OpenClaw and Markdown-first agents

This repository's portable skill is `../../agents/prompt-optimizer.md`.

## When to use

Use it when the user wants to improve a prompt, raise output quality/consistency, or turn a basic prompt into a structured high-performance prompt.

## Non-negotiable rule

A good prompt is clear, contextual, and structured. Compound multiple proven techniques rather than adding one clever trick.

Golden Rule: a competent colleague should be able to follow the prompt with no extra context. If not, it is not ready.

## Core techniques (priority order)

1. Be clear and direct — context, audience, workflow, success criteria. (always)
2. Use examples — 3-5 diverse, progressive, edge-case examples. (format matters)
3. Let the model think — structured chain of thought. (complex reasoning)
4. Use XML tags — separate parts into cognitive containers. (multi-part)
5. Give a role — specific expert persona. (domain expertise)
6. Prefill / format control — guide output shape. (strict format)
7. Chain prompts — sequential steps. (multi-step workflows)

## Three-pass method

1. Coverage: clarity assessment + technique selection.
2. Structure: XML, examples, chain of thought; mark `[VERIFY]` for uncertainties.
3. Polish: latest-model best practices, reduce markdown overuse, hallucination guards, strip `[VERIFY]`.

## Output

```text
Optimized prompt: <rewritten prompt>
Techniques applied: <which of the 7, and why>
What changed: <key improvements over the original>
Quality score: <1-10 with weakest remaining area>
```
