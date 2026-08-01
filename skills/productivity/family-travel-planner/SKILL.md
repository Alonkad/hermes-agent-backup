---
name: family-travel-planner
description: "Use when managing and planning the Kaduri family's 2026 vacation. Details how to read/update the central Spreadsheet and collaborate on Google My Maps."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [vacation, planning, sheets, maps, family, travel, austria]
    related_skills: [google-workspace, maps]
---

# Family Travel Planner (Kaduri Family 2026)

## Overview
This skill provides structured workflows, conventions, and API references for organizing and managing the Kaduri family's travel planning (specifically the Austria trip in summer 2026). It acts as the operational guide for interacting with their central Google Spreadsheet and Google My Maps.

## Project Resources
- **Central Spreadsheet ID:** `1xjW_s4pjyXCEmsB02btq0_zCwI2odI8VazaOkrwiuBc`
  - *URL:* https://docs.google.com/spreadsheets/d/1xjW_s4pjyXCEmsB02btq0_zCwI2odI8VazaOkrwiuBc/edit
  - *Primary Owner:* `alonkad@gmail.com` (Alon)
  - *Access:* Full editor permissions shared with Alon and accessible by Hermes.
### 2. Shared Google My Maps ID
- **Shared Google My Maps ID:** `1e4ljHcgsR0wQI5kxJvGeN4FFkPaG7ks`
  - *URL:* https://www.google.com/maps/d/edit?mid=1e4ljHcgsR0wQI5kxJvGeN4FFkPaG7ks
  - *Primary Owner:* `alonkad@gmail.com`
  - *Access:* Full editor permissions shared with `kaduri.agent@gmail.com` (Hermes).
  - *Programmatic Sync Reference:* Since My Maps has no write API, we use a KML file hosted on Google Drive dynamically syncable in My Maps. For setup instructions and schemas, see `references/google-maps-kml-sync.md`.

## When to Use
- When any family member (Alon, Liat, or in a group chat) asks to:
  - Add flights, accommodations, rental car details, or attractions to the trip details.
  - Query the daily schedule ("מה הלוז ליום רביעי?").
  - Budget or track expenses related to the trip.
  - Calculate travel times or distances between locations.
  - Recommend activities based on geographical proximity on their map.

## Shared Google My Maps and KML Sync Workflow
- **Google My Maps Constraints:** Google My Maps lacks a writing/editing API. Google Maps Lists also lack programmatic APIs.
- **KML Synchronization Solution:** We bypass this limitation by using Google My Maps' ability to import files directly from Google Drive.
  - **Shared KML File ID:** `1dU6v0SUtgAor6y8zOcs2fOVY-TFKUlB5` (Name: `austria_2026.kml`).
  - **Permissions:** Shared with `alonkad@gmail.com` as a writer.
  - **My Maps Linkage:** The user imports this file from their Google Drive ("Shared with me" section) as a layer in Google My Maps. This creates a dynamically synced link layer.
- **Automated Programmatic Updates:**
  - When the user asks to add an attraction, hotel, or location to the map, use the script located inside this skill:
    ```bash
    python ~/.hermes/skills/productivity/family-travel-planner/scripts/update_kml.py \
      --name "מלון - Ferienhaus Astrid" \
      --description "<b>צ'ק אין:</b> 31/07/2026<br/><b>קוד הזמנה:</b> 5134615985" \
      --lat 47.3469901 \
      --lon 13.3946766 \
      --style "hotelStyle"
    ```
  - This script downloads the existing KML from Drive, appends the new Placemark, and uploads it back to the same Google Drive File ID. Google My Maps automatically pulls and updates the layer periodically.

---

## Layout of Spreadsheet Tabs

### 1. `📅 לו"ז יומי` (Daily Itinerary)
- **Columns:** `תאריך` (Date), `יום` (Day), `אזור/יעד מרכזי` (Main Area/Region), `פעילות בוקר` (Morning Event), `פעילות צהריים/אחר הצהריים` (Afternoon Event), `פעילות ערב` (Evening Event), `לינה` (Lodging), `הערות ולינקים חשובים` (Notes/Links).
- **Date Format:** `YYYY-MM-DD` (e.g. `2026-07-30`).

### 2. `✈️ טיסות` (Flights)
- **Columns:** `תאריך` (Date), `חברת תעופה` (Airline), `מספר טיסה` (Flight No), `מוצא (שדה תעופה)` (Departure), `יעד (שדה תעופה)` (Arrival), `שעת המראה (מקומי)` (Dept Time Local), `שעת נחיתה (מקומי)` (Arrv Time Local), `קוד הזמנה (PNR)` (Booking Code), `סטטוס` (Status), `מחיר` (Price), `הערות` (Notes).

### 3. `🏨 לינה` (Accommodations)
- **Columns:** `תאריך צ'ק-אין` (Check-in), `תאריך צ'ק-אאוט` (Check-out), `שם המלון/דירה` (Hotel Name), `כתובת` (Address), `עיר/אזור` (City/Region), `פרטי קשר/טלפון` (Contact Info), `קוד הזמנה` (Booking Ref), `מחיר כולל` (Total Cost), `סטטוס תשלום` (Payment Status), `הערות/לינקים` (Notes/Links).

### 4. `🚗 השכרת רכב` (Car Rental)
- **Columns:** `תאריך ושעת איסוף` (Pickup), `תאריך ושעת החזרה` (Return), `חברת השכרה` (Rental Co), `נקודת איסוף` (Pickup Location), `נקודת החזרה` (Return Location), `סוג הרכב ודגם` (Car Class), `קוד הזמנה` (Booking Ref), `מחיר` (Price), `סטטוס תשלום` (Payment Status), `הערות נוספות` (Notes).

### 5. `🎭 אטרקציות ונקודות עניין` (Attractions Wishlist)
- **Columns:** `שם המקום/אטרקציה` (Place Name), `אזור/עיר` (Area), `שעות פתיחה` (Opening Hours), `מחיר לכרטיס` (Ticket Price), `סטטוס כרטיסים (הוזמן/נדרש מראש/חופשי)` (Booking Status), `לינק לרכישת כרטיסים` (Ticket Link), `הערות/פרטים חשובים` (Notes).

### 6. `💰 תקציב והוצאות` (Expenses & Budget)
- **Columns:** `קטגוריה` (Category), `פירוט/פריט` (Item), `סכום (במטבע מקומי)` (Foreign Cost), `מטבע` (Currency), `סכום (בשקלים)` (Cost in ILS), `שולם ע"י` (Paid By), `סטטוס תשלום` (Status), `הערות` (Notes).

### 7. 📝 משימות פתוחות & 🎒 דברים לארוז (Checklists)
- **`📋 משימות פתוחות`:** עוקב אחרי משימות הכנה לוגיסטיות (דרכונים, ויזות/מדבקות, רישיונות, הזמנות). 
  - **הנחיה:** כשתזכורת או הזמנה מופיעה, יש להוסיף משימה לכאן או לעדכן סטטוס.
- **`דברים לארוז`:** טאב לרשימת הציוד האישי והמשפחתי.
  - **הנחיה:** כשפריט נדרש עולה בשיחה (כמו רישיון נהיגה בינלאומי), יש להוסיפו אוטומטית לטאב זה.

### 8. `📍 נקודות למפה` (Map Locations)
- **Columns:** `שם המקום` (Place Name), `כתובת` (Address), `קו רוחב (Latitude)` (Latitude), `קו אורך (Longitude)` (Longitude), `תיאור / מידע נוסף` (Notes/Info), `קטגוריה` (Category).
- **Usage:** Used as the dynamic source of My Maps import which, as the first tab (index 0), gets parsed by My Maps directly.
---

## Technical Workflows for Hermes

### Updating the Spreadsheet
To update/append spreadsheet rows, you can use the CLI or programmatic Python.

#### ⚠️ CLI Pitfall with Emoji Sheet Names
Because the sheet names in this workbook contain emojis (e.g. `🚗 השכרת רכב`, `💰 תקציב והוצאות`), calling `google_api.py` via shell/subprocess can fail with a `HttpError 400: Unable to parse range` due to shell quoting and character escaping bugs.

**The Solution:** Use programmatic Python inside the active environment to load the credentials and call Google Sheets client directly.

#### Programmatic Python Update (Recommended & Safest)
Always use `execute_code` with the following template to perform reliable reads and writes:
```python
import sys
import json

# Add google-workspace scripts directory to path
sys.path.insert(0, '/home/agentuser/.hermes/skills/productivity/google-workspace/scripts')
from google_api import build_service

service = build_service("sheets", "v4")
spreadsheet_id = "1xjW_s4pjyXCEmsB02btq0_zCwI2odI8VazaOkrwiuBc"

# Example: To update H2:I2 in '🚗 השכרת רכב'
range_name = "🚗 השכרת רכב!H2:I2"
body = {"values": [["4,400.17 ₪", "שולם (ע\"י אלון)"]]}
res = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range=range_name,
    valueInputOption="USER_ENTERED",
    body=body
).execute()
print(json.dumps(res, indent=2))

# Example: To append to '💰 תקציב והוצאות'
range_name = "💰 תקציב והוצאות!A:H"
body = {"values": [["השכרת רכב", "השכרת רכב Budget Germany", "4400.17", "ILS", "4400.17", "אלון", "שולם", ""]]}
res = service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id,
    range=range_name,
    valueInputOption="USER_ENTERED",
    insertDataOption="INSERT_ROWS",
    body=body
).execute()
```

#### CLI Method (Alternative, Use Caution)
If using the CLI, ensure single quotes around the sheet name and take care with shell command arguments:
```bash
# E.g. To append a row to the Flight sheet:
python ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py sheets append "1xjW_s4pjyXCEmsB02btq0_zCwI2odI8VazaOkrwiuBc" "'✈️ טיסות'!A:K" --values '[["2026-07-30", "El Al", "LY361", "TLV", "VIE", "06:15", "09:45", "ABCDEF", "Confirmed", "450 USD", ""]]'
```

### Syncing with Google My Maps (The "First Tab Index" Workflow)
Google My Maps has severe limitations for programmatic updates (no write API, and no longer supports importing via Web URLs / Network Links in newer consumer interfaces). The optimal, proven way to sync locations between Hermes and My Maps is directly via Google Sheets using a dedicated map tab:
1. **Dedicated Map Tab:** Create a sheet tab named `📍 נקודות למפה` with these exact headers:
   `שם המקום` (Place Name) | `כתובת` (Address) | `קו רוחב (Latitude)` | `קו אורך (Longitude)` | `תיאור / מידע נוסף` (Notes/info) | `קטגוריה` (Category)
2. **The Index 0 Restriction:** Google My Maps strictly imports from the **first tab** of a multi-tab Spreadsheet. It does not allow selecting other tabs on import.
   - Always programmatically move `📍 נקודות למפה` to **index 0** (the left-most tab) using `batchUpdate` with `updateSheetProperties`:
     ```python
     # Move sheet to index 0
     req = {
         'requests': [{
             'updateSheetProperties': {
                 'properties': {
                     'sheetId': map_sheet_id,
                     'index': 0
                 },
                 'fields': 'index'
             }
         }]
     }
     ```
3. **User Import & Refresh Flow:**
   - Direct the user to import the central Spreadsheet into their My Maps layer. Google My Maps will automatically read the first tab (`📍 נקודות למפה`).
   - Instruct them to map location to `קו רוחב (Latitude)` and `קו אורך (Longitude)` columns, and title to `שם המקום`.
   - When new locations are appended to this tab by Hermes, the user can instantly sync their map by clicking **Data -> Refresh table** within Google My Maps (or refreshing the browser page/re-opening the maps app).

### Dynamic Currency Conversion (Expenses Tab)
When updating `💰 תקציב והוצאות`:
1. If the amount is input in Euros (`EUR`) or Swiss Francs (`CHF`), calculate the approximate conversion to Israeli New Shekels (`ILS`) using current rates (fetch via web search if necessary) and populate `סכום (בשקלים)` automatically.

### Cancellation/Removal Workflow (Liat's Expectation)
When a family member (especially Liat) says they cancelled a reservation, do NOT only remove it from one tab. The reservation may leave traces in multiple locations:

1. **Identify the reservation** — confirm which property/booking code was cancelled.
2. **Remove cron reminders** — list active cron jobs, identify all jobs referencing the property name or booking code, and remove them via `cronjob(action='remove', job_id='...')`.
3. **Search ALL tabs** — check every tab in the Spreadsheet for mentions of the property name or booking code. Do not stop at `🏨 לינה`. In a real case, Mühlradl Gosau was found in:
   - `🏨 לינה` (lodging details)
   - `📍 נקודות למפה` (map locations)
   - `💰 תקציב והוצאות` (expenses/budget)
4. **Clear each row found** — clear cells (replace with empty strings in all columns) using the Sheets API. Do not leave blank remnants.
5. **Check `📅 לו"ז יומי`** — if the cancelled dates overlap with itinerary date rows, clear the `לינה` column for those rows.
6. **Search for any calendar events** in the family calendar related to the property and delete them.
7. **Read-back verification** — after clearing, read the affected ranges to confirm no remnants remain.
8. **Report the full scope** — tell the user every tab that was cleaned, so they know the job was thorough.

**Pitfall:** Do not assume the reservation only lives in `🏨 לינה`. Budget rows (`💰 תקציב`) and map points (`📍 נקודות למפה`) are independent entries that must be cleaned separately.

### Parsing and Organization of Existing Email Bookings
The automatic Austria-email labeling workflow has been retired at Alon's request because no more relevant emails are expected. The cron job and `~/.hermes/scripts/auto_label_austria_emails.py` were removed. The existing Gmail label `Austria2026` may still be searched manually when historical booking details are needed.

1. **Retrieving & Parsing:**
   - Instead of checking the full inbox, search directly using the label to fetch incoming booking details:
     ```bash
     python ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py gmail search "label:Austria2026" --max 10
     ```
   - Retrieve relevant emails via `get` and parse flight numbers, dates, hotel locations, check-in dates, and car pickup hours.
   - Verify data parameters with the user, then automate insertion into Sheets.
4. **Hotel / Accommodation Emails (Liat preference):** When Liat or Alon forwards hotel/accommodation emails, do not ask them to manually retype fields unless extraction fails. Read Gmail, extract the real property name and booking details, update the Spreadsheet and map tab, and create cancellation reminders two days before the free-cancellation deadline / before cancellation fees begin. See `references/hotel-email-processing.md` for the detailed checklist, pitfalls, and automation pattern.
5. **Maintenance & Safety:** If changes to Gmail search keywords or script paths are necessary, do not kill background processes; instead run the custom Python logic directly, let the user manually execute the `/restart` command if needed to reset active timers on the Gateway, and document the flow.

### Geography-Aided Planning
To determine geographic feasibility of daily schedules:
1. Geocode attractions using the `maps` skill.
2. Calculate route durations between the daily hotel and targeted attractions.
3. Advise on cluster-planning (e.g. "האטרקציות אליוון וגול פוסט קרובות אחת לשנייה, כדאי לשלבן באותו היום").

---

## Verification Checklist
- [ ] For every write command, verify the target Range matches the exact Tab name (e.g., `'📅 לו"ז יומי'!A:H`).
- [ ] Ensure formatting details like Dates are written in standard formats (`YYYY-MM-DD`).
- [ ] Confirm with the user before executing bulk edits or adding rows that might duplicate elements.

---

## ⚡ Execution Cost & Speed Optimizations (Avoid Redundant Reads)
To avoid issuing multiple Google Sheets `get` commands or querying the entire document structure, use these exact column targets and cell mappings directly of the primary tabs:

### 1. Tab `💰 תקציב והוצאות` (Budget & Expenses)
*   **A/B/C/D/E/F/G/H Column Map:**
    *   **A:** `קטגוריה` (Category - common values: `טיסות`, `לינה`, `השכרת רכב`, `אטרקציות וכטיסים`, `דלק ונסיעות`, `אוכל`)
    *   **B:** `פירוט/פריט` (Item description)
    *   **C:** `סכום (במטבע מקומי)` (Foreign Cost)
    *   **D:** `מטבע` (Currency - e.g., `ILS`, `EUR`, `CHF`)
    *   **E:** `סכום (בשקלים)` (Cost in ILS - populate directly; if foreign, calculate `C * current_rate`)
    *   **F:** `שולם ע"י` (Paid By - map user correctly to `אלון` or `ליאת`)
    *   **G:** `סטטוס תשלום` (Status - e.g., `שולם`, `טרם שולם`, `לתשלום בחו"ל`)
    *   **H:** `הערות` (Notes / context)
*   **Quick Append Range:** `'💰 תקציב והוצאות'!A:H`
*   *Note:* Row 1 represents headers. Append operations automatically write starting from Row 4 (under existing sample entries).

### 2. Tab `📅 לו"ז יומי` (Daily Itinerary)
*   **A/B/C/D/E/F/G/H Column Map:**
    *   **A:** `תאריך` (Date in YYYY-MM-DD format, e.g., `2026-07-30`)
    *   **B:** `יום` (Day - e.g., `חמישי`)
    *   **C:** `אזור/יעד מרכזי` (Main Area/Region)
    *   **D:** `פעילות בוקר` (Morning activity description)
    *   **E:** `פעילות צהריים/אחר הצהריים` (Afternoon activity description)
    *   **F:** `פעילות ערב` (Evening activity description)
    *   **G:** `לינה` (Lodging location/hotel)
    *   **H:** `הערות ולינקים חשובים` (Important notes, links, booking refs)
*   **Direct Update Target:** `'📅 לו"ז יומי'!A:H` for daily schedule queries and modifications.

### 3. Tab `🎭 אטרקציות ונקודות עניין` (Attractions Wishlist)
*   **A/B/C/D/E/F/G Column Map:**
    *   **A:** `שם המקום/אטרקציה` (Place Name)
    *   **B:** `אזור/עיר` (Area/City)
    *   **C:** `שעות פתיחה` (Opening Hours)
    *   **D:** `מחיר לכרטיס` (Ticket Price info)
    *   **E:** `סטטוס כרטיסים (הוזמן/נדרש מראש/חופשי)` (Booking status)
    *   **F:** `לינק לרכישת כרטיסים` (Ticket purchase link)
    *   **G:** `הערות/פרטים חשובים` (Crucial notes)
*   **Quick Append Range:** `'🎭 אטרקציות ונקודות עניין'!A:G`

### 4. User Identity Mapping (Telegram & WhatsApp)
*   User **`Kaaadd` / `Alon`** -> Always write as **`אלון`** in matching fields.
*   User **`Liat`** -> Always write as **`ליאת`** in matching fields.

