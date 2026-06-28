Hermes Agent runs under user 'agentuser'. Active systemd services: hermes-gateway and hermes-dashboard (reverse proxied via Caddy on https://62.238.18.137, port 9119).
§
Git hourly backup via systemd tracks config.yaml, SOUL.md, cron/, memories/, skills/ to private repo Alonkad/hermes-agent-backup; ignores env/logs/caches/secrets.
§
VPS is intended as a long-running agent host.
§
הדרך הנכונה לעבוד עם תזכורות ב-Hermes היא להשתמש במנגנון המובנה cronjob עם Gateway ל-WhatsApp, ללא צורך בסקריפטים חיצוניים.
§
Google family calendar: family08415384193829322896@group.calendar.google.com. Actions use Google Workspace skill with Hermes Gateway, making direct event API queries under Asia/Jerusalem timezone to bypass scope, list, and filtering limits.
§
The user sends voice messages in Hebrew, so the speech-to-text (STT) configuration should be forced/locked to Hebrew to prevent incorrect language auto-detection on short audio recordings.
§
User prefers to manually run the restart command (/restart or hermes gateway restart) if a change requires restarting the gateway, rather than the agent using raw kill commands.
§
מזהי הכלים המרכזיים לתכנון חופשת אוסטריה 2026: Spreadsheet ID: 1xjW_s4pjyXCEmsB02btq0_zCwI2odI8VazaOkrwiuBc, Google My Maps ID: 1e4ljHcgsR0wQI5kxJvGeN4FFkPaG7ks. אלו מוגדרים ב-fact_store בהרחבה.
§
To prevent parsing failures in mixed Hebrew-English sessions, tool call generations must be strictly valid JSON blocks, completely free of surrounding Hebrew explanations or prose.
§
בעת טיפול במיילים/מידע שקשור למלונות בחופשת אוסטריה 2026: לחלץ את הפרטים מהמייל, לעדכן את גיליון החופשה והטאב למפה, ליצור תזכורת ביטול חינמי שלושה ימים לפני מועד סיום הביטול החינמי (לא לפי יום תחילת דמי הביטול) גם ביומן המשפחתי וגם ישירות לליאת, ולשאול ישירות אם פרט חסר.
§
WhatsApp photo imports from Liat: save only to Google Drive (no local backup). Filename should use embedded photo date metadata when available; if WhatsApp stripped metadata, fall back to message/transfer time.