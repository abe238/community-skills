# Community Skills agent instructions

This repository contains portable Markdown skills for AI agents.

## Available portable skills

- `agents/release-feature-watcher.md`: use when the user wants to monitor a technical feature, bugfix, model/API update, changelog, release, package version, PR, issue, or docs/API change until a concrete readiness condition is met.
- `agents/prompt-optimizer.md`: use when the user wants to improve a prompt, raise output quality/consistency, or turn a basic prompt into a structured high-performance prompt.
- `agents/adversarial-prompting.md`: use when the user faces a complex problem or high-stakes decision that needs multiple solution approaches, failure-mode critique, validated fixes, and ranked recommendations.
- `agents/rapid-domain-mastery.md`: use when the user needs to understand a new field fast from multiple sources — exam prep, research onboarding, program handover, or rapid topic mastery.

## Agent rules

- If a user asks to "watch," "tell me when this ships," "monitor this PR," "let me know when this model/API is available," or "check daily until this is fixed," load and follow `agents/release-feature-watcher.md`. A watcher is not a reminder; it is a quiet automated readiness check that notifies only when actionable or broken.
- If a user asks to "optimize this prompt," "improve this prompt," "score this prompt," or "make this prompt better," load and follow `agents/prompt-optimizer.md`. Compound proven techniques rather than adding one trick.
- If a user wants a complex problem or proposal stress-tested — "what could go wrong," "analyze these options," "adversarially critique" — load and follow `agents/adversarial-prompting.md`. Attack each solution and validate every fix before ranking.
- If a user wants to master a new field from several sources — "build a field map," "help me onboard to," "get me up to speed on" — load and follow `agents/rapid-domain-mastery.md`. Map the field, not the page; mark gaps honestly.

## Hermes-native skills

Hermes Agent users should install the canonical Hermes skills:

```bash
hermes skills install https://raw.githubusercontent.com/abe238/community-skills/main/skills/productivity/release-feature-watcher/SKILL.md
hermes skills install https://raw.githubusercontent.com/abe238/community-skills/main/skills/prompting/prompt-optimizer/SKILL.md
hermes skills install https://raw.githubusercontent.com/abe238/community-skills/main/skills/prompting/adversarial-prompting/SKILL.md
hermes skills install https://raw.githubusercontent.com/abe238/community-skills/main/skills/learning/rapid-domain-mastery/SKILL.md
```

## Cross-agent use

For agents without a native skill registry, copy or reference the portable `agents/<skill>.md` in the agent's instruction system:

- Claude Code: copy `adapters/claude-code/.claude/skills/<skill>.md` into `.claude/skills/` or `~/.claude/skills/`.
- Codex/OpenAI-style agents: copy `adapters/codex/<skill>.AGENTS.md` into the project root or append its contents to the existing `AGENTS.md`.
- OpenClaw/other Markdown-first agents: copy `adapters/openclaw/<skill>.AGENTS.md` into the project root or paste `agents/<skill>.md` into the agent's custom instructions.
