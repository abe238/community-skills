# Release Feature Watcher

Use this when a user wants to monitor a technical feature, bugfix, model/API update, changelog, release, package version, PR, issue, or docs/API change and be notified only when a specific actionable condition is met.

## Core doctrine

A watcher is not a reminder. A watcher is an automated readiness check.

Stay silent while nothing is actionable. Alert only when the condition is met or the check is truly broken. Include the next useful action. Remove or expire the watcher after success when appropriate.

## Required watcher fields

Every watcher needs:

1. **Source**: the authoritative place to check.
2. **Condition**: the exact state that means ready.
3. **Baseline**: the current state when the watcher is created.
4. **Action**: what to do once ready.
5. **Silence rule**: no update unless actionable or broken.
6. **Cleanup rule**: remove when done, expire when stale.

If the condition cannot be stated precisely, ask one concise clarifying question before creating the watcher.

## Good watcher targets

- GitHub PR merged and included in an official release.
- GitHub issue closed and fixed in a release.
- Changelog mentions a specific feature/fix and version.
- Package registry reaches a target version.
- API docs expose a new field, endpoint, model, or capability.
- Provider/model list includes a requested model.
- Security advisory has a patched version available.

## Not a good fit

- Generic news monitoring.
- Vague curiosity with no action path.
- Page-diff alerts without a readiness condition.
- Personal reminders, calendar events, or chores.
- Broad research digests.

## Source reliability

Strong evidence: official API docs, official changelog, GitHub release, package registry, pricing/limits page, advisory/status page.

Medium evidence: official blog, maintainer/founder post, docs PR, forum announcement by maintainer.

Weak evidence: rumor, random social post, screenshot, third-party blog without a primary source.

Alert only when evidence is strong enough for the requested action.

## Default implementation

1. Inspect the source.
2. Classify the watcher: GitHub PR/issue/release, changelog, model/provider, package/version, docs/API, or security/fix.
3. Infer the readiness condition if obvious.
4. Record baseline state.
5. Create a deterministic script or scheduled check that prints nothing while not ready.
6. Notify only on ready/broken.
7. Include the next action in the success message.
8. Self-remove or expire the watcher after success.

Default schedule: daily.
Default noise mode: quiet.
Default cleanup: self-remove after success.

## Success message shape

```text
Ready: <thing watched>
Evidence: <official source/version/release URL>
Baseline: <old state>
Current: <new ready state>
Next action: <install/update/use command or concrete next step>
Cleanup: watcher removed/expired or still monitoring because <reason>
```

## Canonical phrase

Use this line in implementations and docs:

> A watcher is not a reminder. A watcher is an automated readiness check.
