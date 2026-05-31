Hermes Agent runs as Linux user `agentuser`.
§
Hermes home/config/data directory: `/home/agentuser/.hermes`.
§
Code installed at: `/home/agentuser/.hermes/hermes-agent`.
§
Hermes Gateway runs continuously via systemd service `hermes-gateway.service`.
§
Hermes web dashboard runs via `hermes-dashboard.service` at `127.0.0.1:9119`, exposed at `https://62.238.18.137`.
§
Local Git backup repo: `/home/agentuser/hermes-backup`.
§
Git backup synced hourly by `hermes-git-backup.timer` to private GitHub repo `Alonkad/hermes-agent-backup`.
§
Git backup tracks `config.yaml`, `SOUL.md`, `cron/`, `memories/`, and `skills/`.
§
Git backup explicitly does *not* track `.env`, logs, caches, auth files, gateway lock/state files, or raw secrets.
§
Manual Git backup sync script: `/home/agentuser/hermes-backup/sync-hermes-backup.sh`.
§
VPS is intended as a long-running agent host.