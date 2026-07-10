# Hermes Cron Job Debugging Guide

## Common Failure Patterns

### 1. `next_run_at: null`
**Symptom:** Job exists with `"next_run_at": null`.
**Root Cause:** Scheduled datetime has already passed relative to the server's UTC clock.
**Fix:** `remove` the broken job, then `create` a new one with future timestamp and explicit timezone offset.

### 2. Timezone Offset Mismatch
**Symptom:** Reminder fires 2-3 hours off.
**Root Cause:** Server runs on UTC. ISO timestamps without offset (`T14:00:00`) are treated as UTC.
**Fix:** Always use explicit offset: `+03:00` (IDT/summer) or `+02:00` (IST/winter).

### 3. `schedule` Update on `once at` Jobs
**Symptom:** After updating `schedule`, `next_run_at` stays `null`.
**Root Cause:** Cron engine can't re-evaluate a missed one-shot job.
**Fix:** Remove + Recreate only.

## Diagnostic Commands

```bash
# Check if cron jobs actually ran
grep "cron.scheduler: Running job" ~/.hermes/logs/agent.log | tail -20

# Check delivery
grep "delivered to whatsapp" ~/.hermes/logs/agent.log | tail -20

# Gateway status (crons depend on it)
systemctl status hermes-gateway
```