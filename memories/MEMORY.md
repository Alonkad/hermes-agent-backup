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
§
The `web_search` tool uses the Tavily API.
§
משפחת כדורי מתגוררת בישראל. כל הפעולות והבקשות צריכות להתבצע לפי אזור הזמן של ישראל, אלא אם נאמר אחרת במפורש.
§
הדרך הנכונה לעבוד עם תזכורות ב-Hermes היא להשתמש במנגנון המובנה cronjob עם Gateway ל-WhatsApp, ללא צורך בסקריפטים חיצוניים.
§
The main family Google calendar is identified by calendar ID family08415384193829322896@group.calendar.google.com. Interactions with this calendar use direct API event listing and patching by calendar ID due to limitations in the calendar list API call. This calendar is the default family calendar for all related actions.
§
The correct and efficient way to access events from the shared Google calendar ('Kaduri Family') using Hermes is through the built-in Google Workspace skill integrated with Hermes Gateway, using precise API queries that respect timezone settings (Asia/Jerusalem) and full access permissions. This avoids issues with filtering or token scopes and ensures reliable event retrieval.