# Generic agent adapter

Use this folder when an agent does not have a native skill/plugin registry.

## Install pattern

1. Copy `../../agents/release-feature-watcher.md` into the agent's project instructions, memory, rules, or custom-instructions area.
2. If the agent reads `AGENTS.md`, use one of the adapter files:
   - `../codex/AGENTS.md` for Codex/OpenAI-style agents.
   - `../openclaw/AGENTS.md` for OpenClaw/Markdown-first agents.
3. If the agent supports slash commands or prompt snippets, create a command named `release-feature-watcher` whose body is the portable skill text.

## Trigger phrase to test

```text
Watch https://github.com/example/project/pull/123 and tell me only when it is merged and included in an official release. Stay silent until actionable and remove the watcher after success.
```

The correct behavior is a watcher config/card with source, condition, baseline, success action, quiet=true, and self_remove=true — not a generic reminder.
