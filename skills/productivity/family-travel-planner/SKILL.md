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

---

## Technical Workflows for Hermes

### Updating the Spreadsheet
To update/append spreadsheet rows, execute `google_api.py` from the shell wrapper or Python:
```bash
# E.g. To append a row to the Flight sheet:
python ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py sheets append "1xjW_s4pjyXCEmsB02btq0_zCwI2odI8VazaOkrwiuBc" "'✈️ טיסות'!A:K" --values '[["2026-07-30", "El Al", "LY361", "TLV", "VIE", "06:15", "09:45", "ABCDEF", "Confirmed", "450 USD", ""]]'
```

### Dynamic Currency Conversion (Expenses Tab)
When updating `💰 תקציב והוצאות`:
1. If the amount is input in Euros (`EUR`) or Swiss Francs (`CHF`), calculate the approximate conversion to Israeli New Shekels (`ILS`) using current rates (fetch via web search if necessary) and populate `סכום (בשקלים)` automatically.

### Automated Parsing of Email Bookings
When the user indicates that bookings are in their Gmail:
1. Search Gmail using:
   ```bash
   python ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py gmail search "booking OR flight OR reservation OR rental car" --max 10
   ```
2. Retrieve relevant emails via `get` and parse flight numbers, dates, hotel locations, check-in dates, and car pickup hours.
3. Verify data parameters with the user, then automate insertion into Sheets.

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
