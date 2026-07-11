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
- Use standard cron expressions, intervals, or ISO timestamps as supported.
- **WhatsApp Bridge Session Loss:** When the WhatsApp bridge disconnects or loses authentication, it will transition into a logged-out crash loop. Address this promptly using the troubleshooting guide in references.
- **Explicit Family Context in Multi-User Environments:** In shared family environments (like a family WhatsApp), always draft reminders with explicit context. Clearly state who the reminder is addressed to (e.g., 'היי ליאת') and which family member is the subject of the reminder (e.g., 'מסיבת הסיום של תמר'). Avoid generic pronouns ("you", "your") to prevent identity confusion.
- **Proactive Context Resolution:** When executing interactive or action-based reminders (e.g., "print documents about X" or "review form Y"), do not just repeat the text of the reminder. Actively scan for the referenced materials in Google Drive, Gmail, local directories, or past conversation threads (via `session_search`) using bilingual keywords and synonyms. If the documents are found, present them; if not, state clearly where you searched and offer exact instructions on how the user can share them with you (e.g. forwarding to the agent's email address).
## Proactive WhatsApp Integration for Family (New!)
In multi-user family settings, WhatsApp group connectivity can be volatile. To ensure critical notifications (like the 'סיכום שבועי משפחתי') aren't missed:
- **Redundancy:** Always configure critical cronjob reminders to deliver to both the `origin` (Hermes chat thread) AND explicit individual WhatsApp DM numbers for key family members (e.g., `whatsapp:972523321092`, `whatsapp:972544516977`).
- **Target Formatting:** When updating cron deliveries, format the targets explicitly: `deliver: "origin,whatsapp:<num1>,whatsapp:<num2>"`. 
- **Verification:** After updating, always run `list` to verify the `deliver` field contains the expanded list of explicit WhatsApp endpoints.


## Pitfalls

- Misusing commands like `hermes send_message` instead of `hermes send` will cause failures.
- Running reminders outside of Hermes Gateway context leads to delivery failures.
- **Specifying timezone in cron schedules is mandatory, not optional.** The server runs on UTC. Without an explicit offset, `2026-07-07T14:00:00` is interpreted as UTC (17:00 Israel), not Israel time. Always use the `+03:00` suffix (or `+02:00` in winter) for one-shot ISO timestamps.
- **Always verify `next_run_at` is non-null after create/update.** If the API returns `"next_run_at": null`, the job will NEVER fire. This happens when the scheduled datetime has already passed relative to the server's clock. Treat `next_run_at: null` as immediate failure.
- **Do NOT use `schedule` update on a broken one-shot job.** Updating `schedule` on a `once at` job that has `next_run_at: null` silently fails — the job stays dead. The reliable recovery pattern is: `remove` the broken job, then `create` a new one with the correct timestamp and timezone offset.
- Ensure PATH and environment context are appropriate if using any scripting.
- **Passive posture trap:** Do not wait for family members to message you first. If WhatsApp is configured with family numbers and a member has never contacted you, proactively reach out, introduce yourself, and offer concrete examples of how you can help. The default is proactive, not reactive.

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
- See `references/cron-debugging.md` for diagnostic commands and common failure patterns (null next_run_at, timezone mismatches, dead one-shot jobs).
