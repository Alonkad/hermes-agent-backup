Hermes Agent runs under user 'agentuser'. Active systemd services: hermes-gateway and hermes-dashboard (reverse proxied via Caddy on https://62.238.18.137, port 9119).
§
Git hourly backup via systemd tracks config.yaml, SOUL.md, cron/, memories/, skills/ to private repo Alonkad/hermes-agent-backup; ignores env/logs/caches/secrets.
§
VPS is intended as a long-running agent host.
§
כל פעולה הקשורה לזמנים (תזכורות, יומן) חייבת להיות מותאמת לשעון ישראל (Asia/Jerusalem), כולל המרה מ-UTC במידת הצורך.
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
§
אלון מעדיף שתזכורות ושירותים יתבצעו לפי שעון ישראל (IDT/IST), ועבור הקפדה על כך, עליי לאמת תמיד את השעה באמצעות פקודת date בטרמינל לפני קביעת תזמון.
§
Vacation 2026: Liat's family (Eitan 10, Tamar 7) trip to Germany/Austria (July 31 - Aug 16). Bookings: Novotel Munich (x2), Schlader, Unterfischergut, Tauern Spa. Liat manages logistics/reminders via Hermes. Use Family Calendar ID: family08415384193829322896@group.calendar.google.com. Liat prefers iterative packing list building.