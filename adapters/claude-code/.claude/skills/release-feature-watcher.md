# Release Feature Watcher

When asked to watch a technical change, PR, release, model/API update, package version, docs/API change, bugfix, or changelog, use this skill.

## Doctrine

A watcher is not a reminder. A watcher is an automated readiness check.

Do not create noisy reminders. Create a quiet check that stays silent while nothing is actionable, alerts only when ready or broken, includes the next action, and removes/expires itself after success when appropriate.

## Required fields

Before creating the watcher, identify:

1. Source: authoritative URL/API/registry/repo.
2. Condition: exact ready state.
3. Baseline: current state.
4. Action: what to do once ready.
5. Silence rule: no update unless actionable or broken.
6. Cleanup rule: remove when done or expire when stale.

## Defaults

- Schedule: daily.
- Noise: quiet/no-change silence.
- Evidence: require official release/docs/changelog/API/registry evidence for install/use actions.
- Cleanup: self-remove after success.

## Common readiness conditions

- GitHub PR merged and released after merge.
- Issue closed and included in release notes.
- Changelog contains a specific feature/fix phrase.
- Package registry version reaches target semver.
- API docs expose a requested endpoint/field/model/capability.
- Provider model list or pricing page shows availability.
- Security advisory has patched version available.

## Ask only if needed

If the user is vague, ask one short numbered question:

```text
Watch for what?
1. PR merged
2. Official release after merge/fix
3. Specific feature/fix mention
4. Installable package/version
5. API/model availability
```

Otherwise infer the sensible default: specific feature/fix plus installable or API-usable release.

## Success message

```text
Ready: <watched thing>
Evidence: <official source/version/release URL>
Baseline: <old state>
Current: <new ready state>
Next action: <concrete command or next step>
Cleanup: <removed/expired/still watching reason>
```

Canonical full reference: https://github.com/abe238/community-skills/blob/main/agents/release-feature-watcher.md
