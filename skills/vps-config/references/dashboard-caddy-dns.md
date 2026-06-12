# Dashboard, Caddy, DNS, TLS, and Ports

This reference documents the web architecture of this VPS and how the Hermes Agent Dashboard, Caddy, static assets, and custom public-facing pages are configured and served.

## Architecture Overview

1. **Caddy (Reverse Proxy):** Runs as a systemd service (`caddy.service`) listening on ports `80` (HTTP) and `443` (HTTPS).
   - Port 80: Permanently redirects all traffic to HTTPS.
   - Port 443: Protects the dashboard with Basic Authentication and reverse proxies all traffic to port `9119`.
   - TLS Certificates: Managed by Caddy at `/etc/caddy/certs/hermes-dashboard.crt` (and key).
2. **Hermes Web Dashboard (FastAPI Backend):** Runs on port `9119` via systemd service `hermes-dashboard.service`.
   - Root executable: `/home/agentuser/.local/bin/hermes dashboard --host 127.0.0.1 --port 9119 --no-open --skip-build`
   - Active user/group: `agentuser:agentuser`

---

## Serving Custom Interactive HTML Pages

Because modifying `/etc/caddy/Caddyfile` directly requires root/sudo privileges (which `agentuser` does not have by default) and carries service disruption risks, the most robust way to serve one-off interactive HTML pages (like learning sheets, games, mockups, or dashboards for the family) is to utilize the existing static assets mount of the Hermes Dashboard.

### 1. Static Assets Folder Route
The FastAPI dashboard mounts its built-in static directory `WEB_DIST / "assets"` to `/assets` using FastAPI's `StaticFiles`.
- Absolute local path: `/home/agentuser/.hermes/hermes-agent/hermes_cli/web_dist/assets/`
- Owner: `agentuser:agentuser` (fully writable by the agent session without root/sudo!)

### 2. Deployment Recipe
To serve a custom html page (e.g., `family-practice.html`):
1. Write or copy the file directly to `/home/agentuser/.hermes/hermes-agent/hermes_cli/web_dist/assets/family-practice.html`.
2. Ensure the HTML has built-in styling, scripts (JavaScript), and interactive logic (no separate backend needed).
3. The page will immediately be accessible online at:
   `https://62.238.18.137/assets/family-practice.html`

### 3. Password-Free Phone/Tablet Link (Embedded Auth)
Since Caddy enforces Basic Authentication at the root of port `443`, users would normally be prompted for a username and password. 
To bypass this prompt on mobile devices or tablets for a seamless user experience, use HTTP Basic Auth inline URL parameters:
- Format: `https://<username>:<password>@<ip_or_domain>/assets/<filename>`
- Active credentials:
  - Username: `hermes`
  - Password: `EM2Czq5uh0yc8bPL8YxvA0dqggrgzZj4`
- Pre-authenticated Live URL:
  `https://hermes:EM2Czq5uh0yc8bPL8YxvA0dqggrgzZj4@62.238.18.137/assets/family-practice.html`

When clicked, the browser logs the user in automatically, keeping the experience clean and frictionless for non-technical family members or kids (like Liat, Eitan, or Tamar).

---

## Diagnostics & Operations

To verify or troubleshot web serving:
- Check Caddy status: `systemctl status caddy`
- Check Hermes Dashboard status: `systemctl status hermes-dashboard`
- Read dashboard logs: `journalctl -u hermes-dashboard --no-pager -n 50`
- Test-render any asset locally in headless browser before sharing: `browser_navigate(url="file:///home/agentuser/.hermes/hermes-agent/hermes_cli/web_dist/assets/family-practice.html")`
