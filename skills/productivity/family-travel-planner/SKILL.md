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

### 7. `📝 משימות פתוחות` (Open Tasks / Checklist)
- **Columns:** `משימה` (Task), `סטטוס` (Status - פתוח/בוצע), `אחראי` (Owner), `תאריך יעד` (Due Date), `הערות` (Notes).
- **Usage:** Tracks preparatory vacation tasks like passport renewals, international driving permits, printing vouchers, purchasing road vignettes, etc.
- **Durable Preference:** Hermes must proactively identify actionable tasks, required bookings, check-in actions, or missing documents when analyzing incoming travel bookings and record them here dynamically to maintain a clean checklist.

### 8. `📍 נקודות למפה` (Map Locations)
- **Columns:** `שם המקום` (Place Name), `כתובת` (Address), `קו רוחב (Latitude)` (Latitude), `קו אורך (Longitude)` (Longitude), `תיאור / מידע נוסף` (Notes/Info), `קטגוריה` (Category).
- **Usage:** Used as the dynamic source of My Maps import which, as the first tab (index 0), gets parsed by My Maps directly.
---

## Technical Workflows for Hermes

### Updating the Spreadsheet
To update/append spreadsheet rows, execute `google_api.py` from the shell wrapper or Python:
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

### Automated Parsing and Organization of Email Bookings
To keep the mailbox clean and retrieve booking details efficiently:
1. **Dedicated Gmail Label (`Austria2026`):** All vacation-related emails (flights, hotels, car rentals, vouchers, etc.) are organized under the Gmail label `Austria2026`.
2. **Automated Labeling Loop:** A script at `~/.hermes/scripts/auto_label_austria_emails.py` runs regularly via a configured `cronjob` (typically `auto_label_austria_emails_job` running every 12 hours) to auto-detect vacation emails from Alon or Liat and tag them.
3. **Retrieving & Parsing:**
   - Instead of checking the full inbox, search directly using the label to fetch incoming booking details:
     ```bash
     python ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py gmail search "label:Austria2026" --max 10
     ```
   - Retrieve relevant emails via `get` and parse flight numbers, dates, hotel locations, check-in dates, and car pickup hours.
   - Verify data parameters with the user, then automate insertion into Sheets.
4. **Maintenance & Safety:** If changes to Gmail search keywords or script paths are necessary, do not kill background processes; instead run the custom Python logic directly, let the user manually execute the `/restart` command if needed to reset active timers on the Gateway, and document the flow.

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
