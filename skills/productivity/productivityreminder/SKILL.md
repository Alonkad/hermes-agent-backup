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

- Use the native Hermes cronjob mechanism instead of external scripts for reminder delivery.
- Deliver reminders directly via the Gateway to WhatsApp by specifying the `deliver` field with the WhatsApp target (e.g., `whatsapp:<user_id>`).
- Define schedules using standard cron expressions, intervals, or ISO timestamps as supported.
- Ensure the Hermes CLI cronjob commands use `hermes cronjob create` with accurate parameters.
- Avoid shell wrappers like `echo` or `sleep` for reminder logic as they do not interface with Hermes Gateway.
- Always test cronjob reminder commands interactively before scheduling.

## Pitfalls

- Misusing commands like `hermes send_message` instead of `hermes send` will cause failures.
- Running reminders outside of Hermes Gateway context leads to delivery failures.
- Ensure PATH and environment context are appropriate if using any scripting.

## Workflow

1. Clear any existing cron jobs that might conflict.
2. Use the Hermes cronjob tool to create reminders with accurate schedule and delivery target.
3. Monitor reminder status and logs for failures.
4. Adjust schedules or messages as needed using `cronjob update` or `remove`.

## Tips

- When specifying times, use local timezone consistently (e.g., Israel Standard Time), to avoid confusion.
- Use repeat counts for recurring reminders or one-shot for single alerts.

## References

- See `references/whatsapp-cron-integration.md` for detailed guidance and troubleshooting for WhatsApp reminders via Hermes cron.
