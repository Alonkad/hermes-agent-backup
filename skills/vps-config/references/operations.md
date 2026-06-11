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
