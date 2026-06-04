# Timezone Handling and Shared Calendar ID in Google Calendar API

Google Calendar API expects datetime values in RFC 3339 format including timezone offset. Correct timezone handling is critical for event accuracy. Additionally, when managing shared or dedicated family/group calendars, using the exact calendar identifier rather than the default "primary" calendar is crucial.

## Key Points

- Use ISO8601/RFC3339 with offset, e.g., `2026-06-04T16:00:00+03:00` for Israel Daylight time.
- Internally, Hermes skill uses UTC for consistency but converts user inputs/outputs respecting the `Asia/Jerusalem` timezone.
- Mismatch of timezone info may cause events to appear an hour or more off or disappear from date range queries.
- Always specify start and end date/time with explicit timezone offsets when creating or querying events.
- **Shared Calendar IDs:** Never assume the "primary" calendar represents a shared family or group calendar. If a shared calendar (like "Kaduri Family") exists, all read, write, and delete operations must explicitly pass its specific calendar ID (e.g. `family08415384193829322896@group.calendar.google.com`) using the `--calendar` parameter. Otherwise, changes will be pushed to the agent's private "primary" account calendar and will not be visible to other members of the shared calendar.

## Common Pitfalls

- Omitting timezone or using UTC timestamps directly may exclude events from date filters.
- Daylight saving changes must be taken into account for Israel time.
- Command-line defaults: The `google_api.py` CLI default for `--calendar` is `primary`. Always override this explicitly when dealing with a user's shared calendar.
- Listing events: Failing to specify the explicit calendar ID when querying events will return an empty list or show unrelated events from the agent's private primary calendar.

## Recommendations

- Clients of the skill should specify the `Asia/Jerusalem` timezone explicitly when interacting with calendar events.
- Always specify the target shared calendar ID explicitly on calendar creation, listing, and deletion commands.
- Verify existing calendar lists programmatically to ensure the shared calendar is tracked with adequate access rights (like 'owner' or 'writer').

This document supports the `google-workspace` skill.
