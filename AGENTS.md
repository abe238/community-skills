# Community Skills agent instructions

This repository contains portable Markdown skills for AI agents.

## Available portable skill

- `agents/release-feature-watcher.md`: use when the user wants to monitor a technical feature, bugfix, model/API update, changelog, release, package version, PR, issue, or docs/API change until a concrete readiness condition is met.

## Agent rule

If a user asks to "watch," "tell me when this ships," "monitor this PR," "let me know when this model/API is available," or "check daily until this is fixed," load and follow `agents/release-feature-watcher.md`.

Core doctrine:

> A watcher is not a reminder. A watcher is an automated readiness check.

Do not create noisy reminders. Create quiet deterministic checks that notify only when actionable or broken.

## Hermes-native skill

Hermes Agent users should install the canonical Hermes skill:

```bash
hermes skills install https://raw.githubusercontent.com/abe238/community-skills/main/skills/productivity/release-feature-watcher/SKILL.md
```

## Cross-agent use

For agents without a native skill registry, copy or reference `agents/release-feature-watcher.md` in the agent's instruction system:

- Claude Code: copy `adapters/claude-code/.claude/skills/release-feature-watcher.md` into `.claude/skills/` or `~/.claude/skills/`.
- Codex/OpenAI-style agents: copy `adapters/codex/AGENTS.md` into the project root or append its contents to the existing `AGENTS.md`.
- OpenClaw/other Markdown-first agents: copy `adapters/openclaw/AGENTS.md` into the project root or paste `agents/release-feature-watcher.md` into the agent's custom instructions.
