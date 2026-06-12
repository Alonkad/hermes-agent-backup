# Operations

This file documents common operational procedures and diagnostics for the Hermes VPS and services.

## Services Diagnostics

### Hermes Gateway (`hermes-gateway.service`)
- Status Check:
  ```bash
  systemctl status hermes-gateway.service
  ```
- **Read systemd logs:**
  ```bash
  journalctl -u hermes-gateway.service -n 100 --no-pager
  ```
- **Read log files directly:**
  - Standard exit and shutdown diagnostic: `/home/agentuser/.hermes/logs/gateway-exit-diag.log` / `gateway-shutdown-diag.log`
  - Current gateway stdout/stderr: `/home/agentuser/.hermes/logs/gateway.log`
  - WhatsApp bridge log: `/home/agentuser/.hermes/whatsapp/bridge.log`

### Hermes Update Mechanism
- **Manual update:** Run `hermes update --yes` (the `-y` or `--yes` flag will bypass interactive requests).
- **Restart strategy on update:** Running `hermes update` with the update script terminates the gateway process with code `1` (or SIGTERM). Systemd unit `hermes-gateway.service` handles this automatically through its `Restart=always` definition, rising back up under a fresh subprocess instantly. There is no need for sudo privileges/systemctl restarts to complete an update cycle.
- **Automated update / Timer:** Updates can be scheduled using a Hermes internal cronjob by calling the command `hermes update --yes`. This is cleaner than setting up external cron entries, avoiding privilege elevation issues since the update does not require root access to perform its repository pulls, dependencies installations, web-UI building, and gateway restarts.

### Tracking Graceful Restarts (SIGTERM / Updates)
- Unattended Upgrades running in the background can upgrade security-critical system packages (like OpenSSL / `libssl`), triggering a systemd/dpkg package reload.
- Dpkg log file: `/var/log/dpkg.log`
- Example pattern of a reboot/restart triggered by unattended upgrades:
  ```bash
  grep -i "unpacked" /var/log/dpkg.log
  ```
- If `openssl` or other dependency restarts services, a SIGTERM is sent to the Gateway. The Gateway gracefully shuts down (disconnecting Telegram and WhatsApp) and exits with code `1`, which is captured by systemd `'Restart=on-failure'` to safely bring the gateway back up in seconds.

## Muting Verbose Intermediate Gateway Output and Tool Progress

By default, messaging platforms like WhatsApp use intermediate default settings (Tier Medium) which results in active tool execution updates (e.g., "⏳ Calling web_search...") and intermediate thought comments being sent to the chat.

To completely silence intermediate output so that only the final matted response is sent to WhatsApp, run:
```bash
hermes config set display.platforms.whatsapp.tool_progress false
hermes config set display.platforms.whatsapp.interim_assistant_messages false
hermes config set display.platforms.whatsapp.busy_ack_detail false
```

Telegram can be similarly configured if needed:
```bash
hermes config set display.platforms.telegram.tool_progress false
hermes config set display.platforms.telegram.interim_assistant_messages false
hermes config set display.platforms.telegram.busy_ack_detail false
```

## Proper Gateway Restart Strategy

Always perform a graceful restart of the Gateway. **Never use raw kill commands.**

1. **Inside Chat (Telegram/WhatsApp):**
   Send the slash command:
   ```
   /restart
   ```
   The gateway process will gracefully clean up resources, disconnect clients, and restart of its own accord.

2. **From Terminal (SSH/CLI):**
   Run the official command:
   ```bash
   hermes gateway restart
   ```
   *Note:* Running `hermes gateway restart` from a terminal process *inside* the gateway is blocked by the CLI to prevent recursive restart loops. If you need to restart from within the gateway session, ask the user to type `/restart` in their chat.

## Serving Custom Interactive Web Pages/HTML Files

To serve custom web pages (e.g., interactive exercises, personal pages, or dashboards) to the family publicly over the internet without setting up raw Caddy routing or dealing with root permissions:

1. **Upload Assets:** Save the HTML/JS/CSS assets to the static directory of the Hermes Dashboard:
   `~/.hermes/hermes-agent/hermes_cli/web_dist/assets/` (e.g., `assets/practice.html`).
2. **Access URL:** The assets are served statically at:
   `https://<VPS_IP>/assets/<filename>`
3. **Bypassing Basic Auth:** The VPS serves the dashboard on port 443 under Basic Auth. To allow family members/children to access the page without typing passwords, share the URL with embedded basic-auth credentials:
   `https://hermes:EM2Czq5uh0yc8bPL8YxvA0dqggrgzZj4@62.238.18.137/assets/<filename>`

