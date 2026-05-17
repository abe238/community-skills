# AGENTS.md — release-feature-watcher for OpenClaw and Markdown-first agents

This repository's portable skill is `../../agents/release-feature-watcher.md`.

## When to use

Use it when the user asks to monitor a technical feature, bugfix, PR, issue, release, changelog, package version, provider/model/API update, docs/API change, or security fix until it becomes actionable.

## Non-negotiable rule

A watcher is not a reminder. A watcher is an automated readiness check.

The agent should not send routine "still watching" updates. It should check the source, compare against the baseline and condition, and stay silent until the condition is met or the check is broken.

## Required output when creating a watcher

Return or store a watcher card:

```yaml
kind: github_pr_release | github_issue | changelog | provider_model | package_version | docs_api | security_fix
source: <authoritative source>
condition: <exact ready state>
baseline: <current state>
success_action: <what to do once ready>
quiet: true
self_remove: true
expires_at: <date or null>
```

## Evidence

Strong evidence: official docs, official changelog, GitHub release, package registry, provider model/API list, pricing/limits page, status/advisory page.

Medium evidence: official blog, maintainer/founder post, docs PR, maintainer forum announcement.

Weak evidence: rumor, screenshot, third-party post without primary source.

Require strong evidence for install/update/use actions unless the user asked for early awareness.

## Success message

```text
Ready: <watched thing>
Evidence: <official source/version/release URL>
Baseline: <old state>
Current: <new ready state>
Next action: <concrete next step>
Cleanup: <removed/expired/still monitoring reason>
```
