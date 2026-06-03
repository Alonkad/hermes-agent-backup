# Timezone Handling in Google Calendar API

Google Calendar API expects datetime values in RFC 3339 format including timezone offset. Correct timezone handling is critical for event accuracy.

## Key Points

- Use ISO8601/RFC3339 with offset, e.g., `2026-06-04T16:00:00+03:00` for Israel Daylight time.
- Internally, Hermes skill uses UTC for consistency but converts user inputs/outputs respecting the `Asia/Jerusalem` timezone.
- Mismatch of timezone info may cause events to appear an hour or more off or disappear from date range queries.
- Always specify start and end date/time with explicit timezone offsets when creating or querying events.

## Common Pitfalls

- Omitting timezone or using UTC timestamps directly may exclude events from date filters.
- Daylight saving changes must be taken into account for Israel time.
- Testing and validating events in Hermes should confirm event dates and times align with user expectations.

## Recommendations

- Clients of the skill should specify the `Asia/Jerusalem` timezone explicitly when interacting with calendar events.
- Use Hermes commands that properly handle timezone conversions.

This document supports the `google-workspace` skill.
