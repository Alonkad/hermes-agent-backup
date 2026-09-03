Hermes Agent runs under user 'agentuser'. Active systemd services: hermes-gateway and hermes-dashboard (reverse proxied via Caddy on https://62.238.18.137, port 9119).
§
Git hourly backup via systemd tracks config.yaml, SOUL.md, cron/, memories/, skills/ to private repo Alonkad/hermes-agent-backup; ignores env/logs/caches/secrets.
§
כל פעולה הקשורה לזמנים (תזכורות, יומן) חייבת להיות מותאמת לשעון ישראל (Asia/Jerusalem), כולל המרה מ-UTC במידת הצורך.
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