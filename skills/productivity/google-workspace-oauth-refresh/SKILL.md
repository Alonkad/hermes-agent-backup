---
name: google-workspace-oauth-refresh
description: Use when Google Workspace OAuth token refresh fails/expires in Hermes. Documents the exact re-auth flow, common terminal pitfalls, and how to prevent recurring 7-day refresh-token expiry by moving the Google OAuth app out of Testing or using Workspace internal/trusted controls.
version: 1.0.0
author: Hermes Assistant
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [google, workspace, oauth, refresh-token, gmail, calendar, drive, sheets, docs]
    related_skills: [google-workspace]
---

# Google Workspace OAuth Refresh

## Overview

Use this skill when Hermes Google Workspace access fails with `RefreshError`, `invalid_grant`, `TOKEN_REVOKED`, `REFRESH_FAILED`, or the user says the Google Workspace OAuth token expired.

The goal is to avoid guessing: generate a fresh Google OAuth URL, have the user paste the localhost callback URL, exchange it with the setup script, and verify authentication.

## When to Use

- Google Workspace OAuth token expired or was revoked.
- `google-workspace` API calls fail because the refresh token no longer works.
- The user asks to initiate a Google OAuth refresh and paste back the callback URL.
- The user asks why the token expires every few days/weeks and how to make it persistent.

## Exact Re-Authentication Flow

1. **Load the Google Workspace skill.**
   - Run `skill_view(name="google-workspace")` before acting.
   - Completion criterion: you know the current setup script path and expected flow.

2. **Generate the authorization URL with `terminal`, not `execute_code`.**
   ```bash
   python /home/agentuser/.hermes/skills/productivity/google-workspace/scripts/setup.py --auth-url
   ```
   - Do not use `execute_code` with Python subprocess; it may be blocked.
   - Completion criterion: terminal output is a Google `accounts.google.com/o/oauth2/...` URL.

3. **Send the URL to the user.**
   Tell them:
   - Open the URL and approve access.
   - The browser will likely fail on `http://localhost:1`; that is expected.
   - Copy the entire redirected URL from the browser address bar and paste it back.
   - If they get `403 access_denied`, add their Google account as a test user or fix OAuth consent screen status.

4. **Exchange the callback URL.**
   Use the full pasted URL exactly, quoted:
   ```bash
   python /home/agentuser/.hermes/skills/productivity/google-workspace/scripts/setup.py --auth-code "<FULL_CALLBACK_URL>"
   ```
   - Do **not** add `--format json`; this local script may reject it with `unrecognized arguments: --format json`.
   - Completion criterion: output says `OK: Authenticated. Token saved to /home/agentuser/.hermes/google_token.json`.

5. **Verify.**
   ```bash
   python /home/agentuser/.hermes/skills/productivity/google-workspace/scripts/setup.py --check
   ```
   - Completion criterion: output says `AUTHENTICATED: Token valid at /home/agentuser/.hermes/google_token.json`.

## Why Refresh Tokens Expire Repeatedly

Google access tokens are short-lived by design; the long-lived credential is the refresh token. Refresh tokens can still stop working.

Official Google-documented causes include:

- User revoked the app's access.
- Refresh token was not used for six months.
- User changed password and the token includes Gmail scopes.
- User/account exceeded the maximum number of live refresh tokens.
- User granted time-based access and it expired.
- Admin policy restricted requested services/scopes.
- For Google Cloud Platform APIs, admin session length controls can force reauth.
- Most importantly for recurring weekly failures: an OAuth consent screen configured as **External** with publishing status **Testing** issues refresh tokens that expire in **7 days**, unless only basic identity scopes are requested.

Hermes Google Workspace requests Gmail, Calendar, Drive, Contacts, Sheets, and Docs scopes, so it is not limited to basic identity scopes. If the OAuth app is External + Testing, expect repeated 7-day reauthorization.

## How to Make It Persistent

There is no absolute “never expires” guarantee for Google user OAuth refresh tokens. The correct target is “long-lived and automatically refreshed unless revoked or hit by a Google/admin policy.”

Preferred fixes:

1. **If using Google Workspace and the app is only for the family/domain: set User Type to `Internal`.**
   - Google Cloud Console → APIs & Services → OAuth consent screen / Google Auth Platform.
   - Internal apps are for users in the Workspace organization.
   - Verification is not required for internal-only use.
   - Then re-run the OAuth flow so the newly issued refresh token is not a Testing-mode token.

2. **If the app must remain External: publish it to `In production`.**
   - Google Cloud Console → OAuth consent screen / Google Auth Platform → Publishing status → Publish app / In production.
   - For personal/small use, an unverified production external app may show warnings and may have user caps, but it avoids the Testing 7-day refresh-token expiry.
   - If sensitive/restricted scopes require verification for your use case, complete Google's verification steps.
   - After changing status, re-run the OAuth flow; tokens created while the app was Testing can retain the old 7-day expiry.

3. **Workspace admin alternative: mark the OAuth app as `Trusted`.**
   - Google Workspace Admin Console → Security → Access and data control → API controls → App access control.
   - Find the OAuth client/app and mark it Trusted.
   - Google says Trusted status can override standard OAuth limitations for the organization, including the 7-day Testing refresh-token expiry.

Operational hygiene:

- Avoid repeatedly generating tokens on many machines; Google has a 100 live refresh-token limit per Google Account per OAuth client ID, and oldest tokens are invalidated silently.
- Keep `~/.hermes/google_token.json` persistent and backed up securely; do not delete it during deployments.
- Use the token regularly; unused refresh tokens can expire after six months.
- If Gmail scopes are included, expect re-auth after a Google password reset.

## Common Pitfalls

1. **Using `execute_code` to shell out.** Use `terminal` directly for the setup script.
2. **Adding `--format json` to `--auth-code`.** This local setup script may not support it.
3. **Publishing after generating the token but not re-authing.** Re-run OAuth after changing Testing → Production/Internal/Trusted.
4. **Assuming production means impossible to expire.** Google refresh tokens can still be revoked by user/admin policy, password reset with Gmail scopes, six-month inactivity, or refresh-token limits.
5. **Confusing access-token expiry with refresh-token expiry.** Access tokens expire frequently; this is normal. Manual login is only needed when the refresh token fails.

## Verification Checklist

- [ ] `setup.py --check` returns `AUTHENTICATED`.
- [ ] `~/.hermes/google_token.json` exists and contains a refresh token.
- [ ] Google Cloud OAuth app is not External + Testing, or Workspace admin marked it Trusted.
- [ ] OAuth flow was re-run after changing publishing status/user type/trust.
- [ ] A simple Google Workspace API call succeeds.
