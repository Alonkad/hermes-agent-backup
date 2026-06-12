# Hermes Gateway & Messaging Platform Tuning

This document records how the Hermes Gateway and platform-specific display settings are tuned for the Kaduri family.

## Executive Summary: Verbosity & Noise Reduction

The Kaduri family (and particularly Alon, SVP Engineering) prefers ultra-efficient, clean communication. Intermediate thought steps, tool calls, and status progress spam the chat. By default, messaging platforms are tiered by capability, causing some platforms (like WhatsApp, which is classified as `_TIER_MEDIUM`) to send live tool progress, interim assistant chatter, and detailed loops:

- **WhatsApp Default Behavior:** Live "⏳ Calling tool..." progress block, assistant thought commentary while calling tools, and verbose heartbeat messages step-by-step.
- **Telegram Default Behavior:** High-tier quiet state (hides tool-progress and verbose iterations).

### Configured WhatsApp Silence Settings

To align with the ultra-efficient communication requirements, the following platform-specific overrides are set in `config.yaml` to silence intermediate noise and deliver only the clean, final answer:

```yaml
display:
  platforms:
    whatsapp:
      tool_progress: false
      interim_assistant_messages: false
      busy_ack_detail: false
```

- `tool_progress: false`: Shuts off the live progress messages for tool executions.
- `interim_assistant_messages: false`: Suppresses the raw LLM thought commentary and mid-turn prose during loops.
- `busy_ack_detail: false`: Hides the detailed step counter and heartbeats.

## Gateway Restart & Loop Prevention

When modifications are made to `config.yaml` or `.env`, the `hermes-gateway.service` must be restarted to load the new values.

### The Restart Trap (Self-Restart Prevention)
Running the systemd restart command (`hermes gateway restart`) directly from within a tool call (like `terminal()`) inside an active gateway session is **explicitly blocked** by the CLI to prevent crash-restart recursion loops.

### The Correct Graceful Restart Paths
1. **From WhatsApp/Telegram:** Tell the user to send the slash command `/restart` directly in the chat. The gateway connection will safely close and reboot natively.
2. **From Server Core CLI:** Run the official systemd controller directly outside the gateway context:
   ```bash
   hermes gateway restart
   ```

Do not use raw process execution hacks (like `kill -9` or custom subprocess killers) which create orphaned socket locks or broken gateway state.
