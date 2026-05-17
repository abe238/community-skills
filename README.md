# Community Skills

A collection of Skills I either created or found useful that I think others would like too.

## Skills

- [`release-feature-watcher`](skills/productivity/release-feature-watcher/) — watch technical features, fixes, model/API updates, changelogs, releases, and packages until a specific change is actionable.

## Hermes install

Install the canonical Hermes skill directly from its `SKILL.md` URL:

```bash
hermes skills install https://raw.githubusercontent.com/abe238/community-skills/main/skills/productivity/release-feature-watcher/SKILL.md
```

Or add this repository as a tap:

```bash
hermes skills tap add https://github.com/abe238/community-skills
hermes skills search release-feature-watcher
```

## Claude Code install

Claude Code can use the portable Markdown adapter as a project or user skill.

Project-local:

```bash
mkdir -p .claude/skills
curl -fsSL https://raw.githubusercontent.com/abe238/community-skills/main/adapters/claude-code/.claude/skills/release-feature-watcher.md \
  -o .claude/skills/release-feature-watcher.md
```

User-level:

```bash
mkdir -p ~/.claude/skills
curl -fsSL https://raw.githubusercontent.com/abe238/community-skills/main/adapters/claude-code/.claude/skills/release-feature-watcher.md \
  -o ~/.claude/skills/release-feature-watcher.md
```

## Codex / OpenAI-style agents

Use the `AGENTS.md` adapter:

```bash
curl -fsSL https://raw.githubusercontent.com/abe238/community-skills/main/adapters/codex/AGENTS.md \
  -o AGENTS.release-feature-watcher.md
```

Then append it to your project `AGENTS.md`, or reference it from your agent instructions.

## OpenClaw / Markdown-first agents

Use the OpenClaw adapter:

```bash
curl -fsSL https://raw.githubusercontent.com/abe238/community-skills/main/adapters/openclaw/AGENTS.md \
  -o AGENTS.release-feature-watcher.md
```

If the agent supports custom instructions but not `AGENTS.md`, paste in the portable skill:

```bash
curl -fsSL https://raw.githubusercontent.com/abe238/community-skills/main/agents/release-feature-watcher.md
```

## Portable agent skill

The agent-neutral version lives at:

- [`agents/release-feature-watcher.md`](agents/release-feature-watcher.md)

Core doctrine:

> A watcher is not a reminder. A watcher is an automated readiness check.
