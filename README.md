# Community Skills

A collection of Skills I either created or found useful that I think others would like too.

Each skill ships in several forms so it works across agents: a canonical Hermes `SKILL.md`, a portable agent-neutral version under `agents/`, and per-agent adapters under `adapters/` (Claude Code, Codex/OpenAI-style, OpenClaw/Markdown-first, and a generic fallback).

## Skills

| Skill | What it does |
| --- | --- |
| [`release-feature-watcher`](skills/release-feature-watcher/) | Watch a feature, fix, model/API update, changelog, release, package, or PR and alert only when a specific change is actionable. |
| [`prompt-optimizer`](skills/prompt-optimizer/) | Improve prompt effectiveness and turn basic prompts into structured high-performance prompts (XML, examples, chain of thought, roles). |
| [`adversarial-prompting`](skills/adversarial-prompting/) | Generate multiple solutions to a complex problem, critique each for failure modes, validate fixes, and rank recommendations. |
| [`rapid-domain-mastery`](skills/rapid-domain-mastery/) | Build a field map from multiple sources: mental models, debates, assumptions, prerequisites, diagnostic questions, and study sprints. |

Each install section below uses `<skill>` as a placeholder — swap in any skill name from the table.

## Hermes install

Install a canonical Hermes skill directly from its `SKILL.md` URL (paths are `skills/<skill>/SKILL.md`):

```bash
hermes skills install https://raw.githubusercontent.com/abe238/community-skills/main/skills/release-feature-watcher/SKILL.md
hermes skills install https://raw.githubusercontent.com/abe238/community-skills/main/skills/prompt-optimizer/SKILL.md
hermes skills install https://raw.githubusercontent.com/abe238/community-skills/main/skills/adversarial-prompting/SKILL.md
hermes skills install https://raw.githubusercontent.com/abe238/community-skills/main/skills/rapid-domain-mastery/SKILL.md
```

Or add this repository as a tap:

```bash
hermes skills tap add https://github.com/abe238/community-skills
hermes skills search release-feature-watcher
```

## Claude Code install

Claude Code can use the portable Markdown adapters as project or user skills.

Project-local:

```bash
mkdir -p .claude/skills
curl -fsSL https://raw.githubusercontent.com/abe238/community-skills/main/adapters/claude-code/.claude/skills/<skill>.md \
  -o .claude/skills/<skill>.md
```

User-level:

```bash
mkdir -p ~/.claude/skills
curl -fsSL https://raw.githubusercontent.com/abe238/community-skills/main/adapters/claude-code/.claude/skills/<skill>.md \
  -o ~/.claude/skills/<skill>.md
```

## Codex / OpenAI-style agents

Use the per-skill `AGENTS.md` adapter:

```bash
curl -fsSL https://raw.githubusercontent.com/abe238/community-skills/main/adapters/codex/<skill>.AGENTS.md \
  -o AGENTS.<skill>.md
```

Then append it to your project `AGENTS.md`, or reference it from your agent instructions.

## OpenClaw / Markdown-first agents

Use the per-skill OpenClaw adapter:

```bash
curl -fsSL https://raw.githubusercontent.com/abe238/community-skills/main/adapters/openclaw/<skill>.AGENTS.md \
  -o AGENTS.<skill>.md
```

If the agent supports custom instructions but not `AGENTS.md`, paste in the portable skill:

```bash
curl -fsSL https://raw.githubusercontent.com/abe238/community-skills/main/agents/<skill>.md
```

## Portable agent skills

The agent-neutral versions live in [`agents/`](agents/):

- [`agents/release-feature-watcher.md`](agents/release-feature-watcher.md)
- [`agents/prompt-optimizer.md`](agents/prompt-optimizer.md)
- [`agents/adversarial-prompting.md`](agents/adversarial-prompting.md)
- [`agents/rapid-domain-mastery.md`](agents/rapid-domain-mastery.md)

Core doctrines:

> **release-feature-watcher** — A watcher is not a reminder. A watcher is an automated readiness check.
>
> **prompt-optimizer** — Optimize prompts by compounding proven techniques, not by adding one clever trick.
>
> **adversarial-prompting** — Attack every solution before you trust it; a fix is not done until it survives its own critique.
>
> **rapid-domain-mastery** — Map the field, not the page — model the debates and the gaps, not just the consensus.
