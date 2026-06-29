# Hotel Email Processing Notes — Austria 2026

Use this reference when processing hotel/accommodation emails for the Kaduri family vacation, including both adding new bookings and handling cancellations.

## Core user expectation
- When Liat/Alon sends or forwards an email related to hotels/accommodation, extract the details from Gmail rather than asking for manual entry.
- Always update the central vacation Spreadsheet and map-related tab for any verified vacation accommodation information.
- If a critical field is missing, ask the user directly and record a task in `📋 משימות פתוחות`.

## Required outputs for each accommodation booking
1. `🏨 לינה` — check-in/out, real property name, address, area, contact, booking ref, price, payment status, cancellation note.
2. `📍 נקודות למפה` — real property name, address, coordinates if geocoded, concise description, category `לינה`.
3. `📅 לו"ז יומי` — lodging row/field for each night of the stay.
4. `💰 תקציב והוצאות` — lodging expense if price is available, with approximate ILS conversion if price is EUR/CHF.
5. `📋 משימות פתוחות` — only for missing documents/details or follow-up actions.
6. Cancellation reminders:
   - Family Calendar event on `family08415384193829322896@group.calendar.google.com`.
   - Direct WhatsApp reminder to Liat via `cronjob` delivered to `origin`.
   - Default timing: three days before the end of the free-cancellation window, 09:00 Israel time. Use the free-cancellation-until date/time as the source of truth; if cancellation fees start the next day, use the previous day at 23:59 as the free-cancellation deadline.

## Cancellation cleanup workflow (when user says "ביטלתי את ההזמנה")
When a family member (especially Liat) says they cancelled a reservation:

1. **Confirm which property** — ask which property/booking code was cancelled if not specified.
2. **Remove cron reminders** — search active cron jobs for the property name or booking code (cronjob action='list', grep by name). Remove ALL matching jobs.
3. **Search every tab** — search ALL 8 tabs in the spreadsheet:
   - `🏨 לינה` — clear the lodging row
   - `📍 נקודות למפה` — clear the map point row
   - `💰 תקציב והוצאות` — clear the expense row
   - `📅 לו"ז יומי` — if dates overlap with schedule rows, clear the לינה column
   - Check `✈️ טיסות`, `🚗 השכרת רכב`, `🎭 אטרקציות`, `📋 משימות פתוחות` too (usually clean but verify)
4. **Clear rows** — use the Sheets API to update cells to empty strings (`[''] * column_count`) for the affected rows.
5. **Check family calendar** — search `family08415384193829322896@group.calendar.google.com` for events mentioning the property. Delete any found.
6. **Verify** — read back the cleared ranges to confirm no remnants remain.
7. **Report** — explicitly tell the user every tab that was cleaned.

**Pitfall:** A cancelled reservation leaves traces in 3+ tabs. Budget rows (💰 תקציב) and map points (📍 נקודות למפה) are independent entries — cleaning only 🏨 לינה is incomplete.

## Pitfalls learned
- Do not invent placeholder hotel data, booking codes, prices, or cancellation dates. Search/read Gmail first; if not found, say what is missing.
- Use the real property name from the confirmation email. Avoid generic translated labels such as “מלון הריזורט האלפיני”.
- Forwarded Gmail threads may not contain all bookings the user expects. Verify by extracting all `Confirmation:` / booking numbers and check-in dates from the actual message body. If only one confirmation is present, mark the missing expected reservation as an open task and ask for the missing email.
- Remove or correct stale wrong rows/reminders immediately when a name/date correction is discovered.
- Use timezone-aware schedules (`+03:00` / Asia/Jerusalem for reminder delivery). Avoid naive timestamps that may be interpreted as UTC.
- Verification matters: after writing, read back relevant tabs and list the created calendar/reminder items before reporting success.

## Useful Gmail searches
- `newer_than:30d (Booking.com OR booking OR hotel OR Novotel OR Ferienhaus OR Astrid OR TAUERN OR SPA OR מלון OR דירה OR accommodation)`
- `label:Austria2026 newer_than:30d`
- Search by property/booking-specific strings: `"Novotel München Airport"`, `"TAUERN SPA"`, `"Ferienhaus Astrid"`, `"Nordallee 29"`, booking reference number.

## Automation pattern
A quiet watchdog is appropriate for this recurring class:
- Script under `~/.hermes/scripts/` does deterministic Gmail scanning, duplicate checks, sheet/calendar writes, and prints only when it updated something or needs clarification.
- Schedule with `cronjob no_agent=True` so empty stdout is silent.
- Keep a state file of processed Gmail message IDs, but still dedupe writes by booking reference and property name.