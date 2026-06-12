Hermes Agent runs under user 'agentuser'. Active systemd services: hermes-gateway and hermes-dashboard (reverse proxied via Caddy on https://62.238.18.137, port 9119).
§
Git backup synced hourly by `hermes-git-backup.timer` to private GitHub repo `Alonkad/hermes-agent-backup`.
§
Git backup tracks `config.yaml`, `SOUL.md`, `cron/`, `memories/`, and `skills/`.
§
Git backup explicitly does *not* track `.env`, logs, caches, auth files, gateway lock/state files, or raw secrets.
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
§
The user sends voice messages in Hebrew, so the speech-to-text (STT) configuration should be forced/locked to Hebrew to prevent incorrect language auto-detection on short audio recordings.
§
Interactive English practice sheet for Eitan is located at ~/.hermes/hermes-agent/hermes_cli/web_dist/assets/practice.html and live on https://62.238.18.137/assets/practice.html. Update this file on the VPS whenever Alon shares Niki's weekly English summaries.
§
User prefers to manually run the restart command (/restart or hermes gateway restart) if a change requires restarting the gateway, rather than the agent using raw kill commands.