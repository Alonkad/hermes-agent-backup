Hermes Agent runs under user 'agentuser'. Active systemd services: hermes-gateway and hermes-dashboard (reverse proxied via Caddy on https://62.238.18.137, port 9119).
§
Git hourly backup via systemd tracks config.yaml, SOUL.md, cron/, memories/, skills/ to private repo Alonkad/hermes-agent-backup; ignores env/logs/caches/secrets.
§
VPS is intended as a long-running agent host.
§
הדרך הנכונה לעבוד עם תזכורות ב-Hermes היא להשתמש במנגנון המובנה cronjob עם Gateway ל-WhatsApp, ללא צורך בסקריפטים חיצוניים.
§
כל פעולה הקשורה לזמנים (תזכורות, יומן) חייבת להיות מותאמת לשעון ישראל (Asia/Jerusalem), כולל המרה מ-UTC במידת הצורך.
§
The user sends voice messages in Hebrew, so the speech-to-text (STT) configuration should be forced/locked to Hebrew to prevent incorrect language auto-detection on short audio recordings.
§
User prefers to manually run the restart command (/restart or hermes gateway restart) if a change requires restarting the gateway, rather than the agent using raw kill commands.
§
Hotel emails (Austria 2026): extract details, update sheet + map tab, create cancellation reminder 3 days before free-cancellation deadline (not when fees start), also add to family calendar and message Liat directly.
§
WhatsApp photos from Liat → Google Drive only (no local backup). Use embedded photo date if available, else fall back to transfer time.
§
WhatsApp family engagement: proactive — don't wait for family to message first. Reach out, introduce yourself, offer concrete help examples.
§
Family calendar ID: family08415384193829322896@group.calendar.google.com. Always use this ID for family calendar events instead of the default primary calendar.
§
בעבודה עם שירותי Google (Sheets, Docs, Gmail, Calendar), יש לבדוק גם את יכולות ה-CLI וגם את ה-API כדי להבטיח שימוש בפונקציונליות המלאה, שכן ה-CLI עשוי להיות מוגבל.
§
When troubleshooting WhatsApp connectivity or gateway issues, check for missing Node.js dependencies in the bridge directory (e.g., link-preview-js) and monitor for 'AwaitingInitialSync' timeouts in bridge.log, as these often block group chat functionality.