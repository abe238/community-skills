# Generic agent adapter

Use this folder when an agent does not have a native skill/plugin registry.

## Available portable skills

- `release-feature-watcher` — watch a technical change/PR/release/model/package until a readiness condition is met.
- `prompt-optimizer` — improve a prompt or turn a basic prompt into a structured high-performance one.
- `adversarial-prompting` — generate, critique, fix, validate, and rank solutions to a complex problem.
- `rapid-domain-mastery` — build a field map (mental models, debates, assumptions, study plan) from multiple sources.

## Install pattern

1. Copy `../../agents/<skill>.md` into the agent's project instructions, memory, rules, or custom-instructions area.
2. If the agent reads `AGENTS.md`, use one of the per-skill adapter files:
   - `../codex/<skill>.AGENTS.md` for Codex/OpenAI-style agents.
   - `../openclaw/<skill>.AGENTS.md` for OpenClaw/Markdown-first agents.
3. If the agent supports slash commands or prompt snippets, create a command named `<skill>` whose body is the portable skill text.

## Trigger phrases to test

```text
release-feature-watcher: Watch https://github.com/example/project/pull/123 and tell me only when it is merged and included in an official release. Stay silent until actionable and remove the watcher after success.

prompt-optimizer: Optimize this prompt — "Summarize this document and tell me the key points."

adversarial-prompting: Adversarially analyze whether we should migrate our volunteer tracking from spreadsheets to a custom integration.

rapid-domain-mastery: Here are 5 documents on our Food Security program. Build a field map: key concepts, stakeholders, open debates, and a 1-week study plan.
```

The correct behavior is the skill's defined output — a watcher card, an optimized prompt with rationale, a ranked adversarial analysis, or a field map — not a generic reminder or plain summary.
