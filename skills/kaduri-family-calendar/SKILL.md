---
name: kaduri-family-calendar
description: "Management of the Kaduri family shared calendar to ensure events are never posted to the agent's private calendar."
version: 1.0.0
author: Hermes
---

# Kaduri Family Calendar

## Core Rule
**NEVER** use the default primary calendar for family events. Always specify the family calendar ID.

## Configuration
- **Family Calendar ID:** `family08415384193829322896@group.calendar.google.com`

## Workflow for Adding Events
1. **Identify Target:** When Alon, Liat, or any family member asks to add an event to the "family calendar" or "shared calendar", immediately use the configured ID.
2. **Command Execution:** Always use the `--calendar` flag in the `google_api.py` call:
   `python .../google_api.py calendar create --summary "..." --start "..." --end "..." --calendar "family08415384193829322896@group.calendar.google.com"`
3. **Verification:** Report the `htmlLink` to the user so they can verify the event is in the shared calendar.

## Pitfalls
- **Default Calendar:** The Google API defaults to the primary account calendar if no ID is provided. This is a failure.
- **Timezones:** Always ensure Israel time (Asia/Jerusalem) is converted to ISO 8601 with the correct offset (+03:00) before sending to the API.
