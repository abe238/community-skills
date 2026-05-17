# AGENTS.md — release-feature-watcher

Use this instruction block for Codex/OpenAI-style coding agents and any agent that reads `AGENTS.md`.

## Trigger

When the user asks to watch, monitor, check daily, tell them when something ships, or wait until a technical feature/fix/model/API/package/release is available, follow this rule.

## Rule

A watcher is not a reminder. A watcher is an automated readiness check.

Create quiet, deterministic checks. Do not send no-change updates. Notify only when the readiness condition is met or the check is truly broken.

## Required watcher shape

Every watcher must define:

- source: authoritative URL/API/repo/registry/changelog/docs page
- condition: exact state that means ready
- baseline: current state at creation time
- action: what the user should do once ready
- silence_rule: no output unless actionable or broken
- cleanup_rule: remove/self-disable after success or expire when stale

## Evidence standard

Prefer official sources: GitHub releases, package registries, official API docs, official changelogs, provider model lists, pricing/limits pages, advisories/status pages.

Do not alert on rumors or generic page diffs unless the user explicitly asked for early awareness.

## Implementation guidance

- For cron/watchdog scripts, print nothing when not ready.
- Print a concise success message when ready.
- Exit nonzero only for real check/config failures.
- Store config as JSON/YAML with source, baseline, condition, action, and cleanup fields.
- Include a self-removal path if the scheduler supports it.

## Success message

```text
Ready: <thing watched>
Evidence: <official URL/version/release>
Baseline: <old state>
Current: <new ready state>
Next action: <install/update/use command or concrete step>
Cleanup: <watcher removed/expired/still monitoring reason>
```

Full reference: https://github.com/abe238/community-skills/blob/main/agents/release-feature-watcher.md
