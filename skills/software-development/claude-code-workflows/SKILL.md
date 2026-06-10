---
name: claude-code-workflows
title: Claude Code Configuration & Workflows
summary: Best practices, CLI commands, and hidden configuration parameters (Auto-dream, auto-memory, KAIROS) for Anthropic's Claude Code CLI.
description: Master the advanced engine settings of Claude Code, including Auto-memory, Auto-dream, KAIROS daemon mode, and settings.json overrides.
category: software-development
---

# Claude Code Configuration & Workflows

This skill governs the advanced configuration, engine overrides, and hidden features of Anthropic's `claude-code` CLI, detailing how memory and background tasks interact.

## Engine Architecture

Claude Code features a modular state structure designed to persist and consolidate knowledge over time across multiple independent sessions.

### 1. Auto-Memory (Daytime Brain)
Saves local insights, corrections, and project context dynamically during active sessions.
- **Location**: `~/.claude/projects/<project-id>/memory/`
- **Primary files**:
  - `MEMORY.md`: The main index file loaded at the startup of every session. Must be kept **under 200 lines** to load successfully.
  - Topic-specific files (e.g. `build.md`, `tests.md`).
  - Daily Logs: Append-only files written to `<autoMemPath>/logs/YYYY/MM/YYYY-MM-DD.md`.

### 2. Auto-Dream (REM Sleep Core)
A background sub-agent process that runs asynchronously to consolidate memories, prune stale notes, fix contradictions, and maintain the 200-line limit of `MEMORY.md`. 
- **The 4 Phase Cycle**:
  1. **Orient**: Scan the memory directory and read the `MEMORY.md` index.
  2. **Gather**: Perform narrow, targeted grep-style searches over `.jsonl` session logs.
  3. **Consolidate**: Merge new signals into topic files, convert relative dates (e.g., "yesterday") to absolute timestamps, and delete obsolete facts.
  4. **Prune**: Re-index `MEMORY.md` and remove stale pointers.

- **Trigger Conditions (3-Tier Gating)**:
  - **Time Gate (`minHours: 24`)**: Must be at least 24 hours since the last run.
  - **Session Gate (`minSessions: 5`)**: At least 5 new sessions must accumulate.
  - **Lock Gate**: Checks and writes `.consolidate-lock` (via `consolidationLock.ts` tracking `lastConsolidatedAt`).

---

## Configuration & Activation

### Managing via JSON Settings
To configure memory and dreaming settings, edit the global configuration file (`~/.claude/settings.json`) or project-scoped configuration (`.claude/settings.json`):

```json
{
  "autoDreamEnabled": true,
  "assistant": true
}
```
*(Turning on `"assistant": true` activates the `KAIROS` persistent background daemon, bypassing standard cron expirations).*

### Feature Flags & Gating
Auto-dream is gated behind a server-side GrowthBook feature flag codenamed **`tengu_onyx_plover`**. 
- If `Auto-dream: off` is displayed in the `/memory` interface despite configuring `"autoDreamEnabled": true` in `settings.json`, the account is restricted by server-side rollout gating.
- KAIROS persistent daemon gating uses **`tengu_kairos`**. Pass `--assistant` flag in command line to bypass.

---

## Useful Slash Commands
- `/memory` - Inspect current memory state and view the raw Auto-dream toggle status.
- `/dream` (Alias: `/learn`) - Manually trigger a memory consolidation dream pass. (Requires `userInvocable: true`). Use `Shift + Down` inside the interactive terminal to open the detailed Dream dialog (`DreamDetailDialog.tsx`).
- `/exit` - Gracefully terminate an interactive Claude session.
