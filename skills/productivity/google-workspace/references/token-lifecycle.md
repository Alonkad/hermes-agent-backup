# OAuth2 Token Lifecycle

This document explains how OAuth2 tokens are managed in the Google Workspace skill.

- Tokens are stored securely in `google_token.json` and refreshed automatically before expiry.
- If token expires without refresh, Hermes prompts re-authentication.
- Tokens include scopes defining access like Gmail, Calendar, Drive.
- Hermes checks scopes at startup and warns if scopes are missing.
- Revoked or disabled tokens require re-setup via OAuth flow.

# How This Affects Calendar Events

- Incomplete scopes can lead to missing calendar events in query results.
- Token revocation leads to failed API calls; events won’t show.
- Correct token management ensures event data freshness and availability.

# Troubleshooting

- Run `gws setup` again if events don't appear as expected.
- Always verify token status after permission changes.

---

# Timezone Handling in Google Calendar

- Google Calendar API uses RFC3339 time format with timezone offsets.
- The skill uses UTC internally but formats requests considering user timezone `Asia/Jerusalem`.
- Misalignment in timezone causes events to appear on wrong dates or be missing.

# Best Practices

- Always specify start/end time with timezone in API calls.
- Use Israel timezone (UTC+3 in summer) for accuracy.
- Confirm with `list events` command that event appears correctly.

---

# Reference

This file supports the 'google-workspace' skill.