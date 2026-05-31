---
name: vps-config
description: Documentation and operational context for this VPS/server configuration. Use before reading, changing, updating, hardening, debugging, or replacing any VPS/server configuration including SSH, firewall, packages, systemd services, Hermes Agent, Caddy/HTTPS, DNS, dashboard, users, backups, or credentials handling. After any server configuration change, update this skill's references and changelog.
---

# VPS Config

This skill documents how this VPS is configured so future agents can safely continue server administration without rediscovering everything from scratch.

## Mandatory workflow

Use this skill whenever the task might affect VPS/server configuration, including:

- SSH, sudo, users, groups, firewall, fail2ban, package management, unattended upgrades.
- Systemd services, timers, long-running daemons, ports, DNS, Caddy, HTTPS/TLS, reverse proxies.
- Hermes Agent install/config, Telegram/Discord gateway, dashboard, browser/runtime dependencies.
- Backups, deployment keys, secrets, credentials, API keys, or root-only files.

Before making changes:

1. Read this file.
2. Read the relevant reference file(s) below.
3. Verify current state with commands; do not assume the docs are perfectly current.
4. Avoid printing or committing secrets. Redact `.env`, API keys, bot tokens, passwords, auth files, and private keys.
5. Explain risky changes and ask before modifying SSH, firewall, systemd, Caddy, package repositories, credentials, or public exposure.

After making any durable server configuration change:

1. Update the affected reference file(s).
2. Add an entry to `references/changelog.md`.
3. If the change touches secrets, document only the path, owner, permissions, and purpose — never the secret value.
4. If validation commands were run, record the useful result.

## Current high-level state

Fill this in at the end of setup with the actual discovered values:

- Provider/hardware: DigitalOcean Droplet
- Hostname: hermes-agent-ubuntu-4gb-hel1-1
- OS: Ubuntu 24.04 LTS
- Admin user: (Your initial SSH user, assumed `alonkad` if you didn't specify changing from root)
- Runtime user: agentuser
- Public IPv4: 62.238.18.137
- Public IPv6: (Not configured in this setup, or not publicly exposed)
- Domain/subdomain: (None configured, using IP for now)
- Intended public ports: 80 (HTTP), 443 (HTTPS)
- Hermes gateway service: hermes-gateway.service (active, enabled)
- Hermes dashboard service: hermes-dashboard.service (active, enabled, bound to 127.0.0.1:9119)
- Dashboard public URL: https://62.238.18.137
- Dashboard credentials: hermes / EM2Czq5uh0yc8bPL8YxvA0dqggrgzZj4 (stored securely by root at /root/hermes-dashboard/credentials.txt)
- Backup location: /home/agentuser/hermes-backup
- GitHub backup repo: Alonkad/hermes-agent-backup

## References

Read the relevant docs before acting:

- [Setup source and history](references/setup-source.md)
- [System baseline, users, packages, directories](references/system-baseline.md)
- [Security: SSH, UFW, fail2ban, unattended upgrades](references/security.md)
- [Hermes Agent configuration and services](references/hermes.md)
- [Dashboard, Caddy, DNS, TLS, and ports](references/dashboard-caddy-dns.md)
- [Backups and persistence](references/backups.md)
- [Operational commands](references/operations.md)
- [Change log](references/changelog.md)
