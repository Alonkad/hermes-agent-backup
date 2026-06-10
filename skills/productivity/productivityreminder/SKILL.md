---
name: productivityreminder
title: Reminder Management in Hermes Agent
summary: Best practices and workflows for managing scheduled reminders and WhatsApp notifications with Hermes Agent.
description: Skill for managing reminders in Hermes Agent, focusing on WhatsApp cronjob integration best practices and pitfalls.
category: productivity
---

# Reminder Management in Hermes Agent

This skill provides best practices, pitfalls, and workflows for effectively managing scheduled reminders and notifications within Hermes Agent, especially focused on WhatsApp delivery integrations.

## Overview

Hermes Agent uses an integrated cron subsystem capable of handling both one-shot and recurring scheduled tasks. It is deeply integrated with the Hermes Gateway to provide session-context-aware message delivery.

## Best Practices

- Use the native Hermes `cron` mechanism (or the programmatic `cronjob` tool) instead of external scripts for reminder delivery.
- Set `deliver: "origin"` or omit the parameter entirely to automatically deliver back to the origin context (e.g. the active WhatsApp conversation thread/topic), preserving the precise channel and thread routing.
- Deliver reminders to specific external targets by specifying the `deliver` field with a targets value (e.g., `whatsapp:<user_id>`).
- Define schedules using standard cron expressions, intervals, or ISO timestamps as supported.
- Ensure the Hermes CLI cron commands use `hermes cron create` with accurate parameters.
- Avoid shell wrappers like `echo` or `sleep` for reminder logic as they do not interface with Hermes Gateway.
- Always test cron commands interactively before scheduling.

## Pitfalls

- Misusing commands like `hermes send_message` instead of `hermes send` will cause failures.
- Running reminders outside of Hermes Gateway context leads to delivery failures.
- **Specifying timezone in cron schedules:** When calling `cron` (especially with the `create` action), always parse or specify the date/time using an explicit RFC 3339/ISO 8601 offset (e.g. `2026-06-05T09:05:00+03:00`). This ensures the cron engine maps the scheduled run precisely to local family time, avoiding offset drift or UTC-conversion errors.
- Ensure PATH and environment context are appropriate if using any scripting.

## Workflow

1. Clear any existing cron jobs that might conflict.
2. Use the Hermes `cron` tool to create reminders with accurate schedule and delivery target.
3. Monitor reminder status and logs for failures.
4. Adjust schedules or messages as needed using `hermes cron edit` or `remove`.

## Tips

- When specifying times, use local timezone consistently (e.g., Israel Standard Time), to avoid confusion.
- Use repeat counts for recurring reminders or one-shot for single alerts.

## References

- See `references/whatsapp-cron-integration.md` for detailed guidance and troubleshooting for WhatsApp reminders via Hermes cron.
