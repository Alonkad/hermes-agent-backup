---
name: macos-automation
description: "Control macOS: Notes (memo), Reminders (remindctl), iMessage (imsg), FindMy, and Computer Use."
version: 1.0.0
author: Hermes Curator
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [Apple, macOS, Automation, Notes, Reminders, iMessage, FindMy, Computer-Use]
    category: apple-automation
---

# macOS Apple Automation Playbook

A unified class-level playbook for automating personal productivity and tracking workflows on macOS. This covers Notes, Reminders, iMessage, FindMy, and Computer Use.

---

## 1. Apple Notes (via `memo` CLI)

Use the `memo` CLI to manage Apple Notes directly from the terminal. Notes sync across devices via iCloud.

### Prerequisites & Setup
- **macOS** with Notes.app
- Install: `brew tap antoniorodr/memo && brew install antoniorodr/memo/memo`
- Grant Automation access to Notes.app when prompted (System Settings → Privacy → Automation)

### Quick Actions
- **List/Search:**
  ```bash
  memo notes                        # List all notes
  memo notes -f "Folder Name"       # Filter by folder
  memo notes -s "query"             # Search notes (fuzzy)
  ```
- **Manage Notes:**
  ```bash
  memo notes -a "Note Title"        # Quick add with title
  memo notes -e                     # Edit note (interactive)
  memo notes -d                     # Delete note (interactive)
  memo notes -m                     # Move note to folder (interactive)
  ```
- **Export:**
  ```bash
  memo notes -ex                    # Export to HTML/Markdown
  ```

### Limitations & Rules
- Cannot edit notes containing images/attachments.
- Use `memory` tool for agent-internal notes; use `obsidian` skill for markdown-native knowledge management.

---

## 2. Apple Reminders (via `remindctl`)

Manage tasks synced to iOS using `remindctl` on macOS.

### Prerequisites & Setup
- **macOS** with Reminders.app
- Install: `brew install steipete/tap/remindctl`
- Grant Reminders permission and verify: `remindctl status` / `remindctl authorize`

### Quick Actions
- **View:**
  ```bash
  remindctl                    # Today's reminders
  remindctl today              # Today
  remindctl list               # List all reminder pools/lists
  remindctl list Work          # Show specific list
  ```
- **Create Reminders:**
  ```bash
  remindctl add "Buy milk"
  remindctl add --title "Call mom" --list Personal --due tomorrow
  remindctl add --title "Meeting prep" --due "2026-02-15 09:00"
  ```
- **Complete/Delete:**
  ```bash
  remindctl complete ID          # Complete by ID
  remindctl delete ID --force    # Delete by ID
  ```
- **Early Nudges vs Alarms:**
  Timings for alarms use EventKit. To set a reminder due at 2:00 PM with notification 30 minutes earlier:
  ```bash
  remindctl add --title "Hairdresser" --due "2026-05-15 14:00" --alarm "2026-05-15 13:30"
  ```

---

## 3. iMessage & SMS (via `imsg`)

Send and read iMessage/SMS via macOS Messages.app.

### Prerequisites & Setup
- Messages.app configured and signed in on macOS
- Install: `brew install steipete/tap/imsg`
- Grant Full Disk Access to terminal (System Settings → Privacy → Full Disk Access)

### Quick Actions
- **Chats & History:**
  ```bash
  imsg chats --limit 10 --json
  imsg history --chat-id CUSTOMER_ID --limit 10 --json
  ```
- **Send Messages:**
  ```bash
  imsg send --to "+14155551212" --text "Hello!"
  imsg send --to "+14155551212" --text "Check this out" --file /path/to/image.jpg
  ```

### Rules & Safety
- **Always confirm recipient and message content** with the user before sending.
- Never spam or mass message. Validate file paths before attaching.

---

## 4. Find My (Tracking via AppleScript & Screen Capture)

Since Apple does not expose a public CLI for Find My, we automate it using AppleScript, screenshots, and visual parsing.

### Prerequisites & Setup
- Signed into iCloud on macOS with registered devices/AirTags.
- Screen Recording permission enabled for terminal.
- *Optional:* Install `peekaboo` for advanced annotation: `brew install steipete/tap/peekaboo`

### AppleScript + Verification Actions
- **Open and Snapshot:**
  ```bash
  osascript -e 'tell application "FindMy" to activate'
  sleep 3
  screencapture -w -o /tmp/findmy.png
  ```
  Then run `vision_analyze(image_url="/tmp/findmy.png", question="Analyze device locations")`.
- **Toggle Tabs:**
  ```bash
  # Switch to Devices
  osascript -e 'tell application "System Events" to tell process "FindMy" to click button "Devices" of toolbar 1 of window 1'
  # Switch to Items (AirTags)
  osascript -e 'tell application "System Events" to tell process "FindMy" to click button "Items" of toolbar 1 of window 1'
  ```

### Ongoing AirTag/Location Patrol Tracking
Ongoing tracking can be automated in the background:
```bash
while true; do
  screencapture -w -o /tmp/findmy-$(date +%H%M%S).png
  sleep 300
done
```

---

## 5. macOS Background Computer Use (Universal)

Drive the macOS desktop inside native apps (Logic, Mail, Messages, Finder, Figma, etc.) in the background without stealing current cursor/keyboard focus or switching Space viewports.

### Canonical Workflow
1. **Capture first:**
   ```
   computer_use(action="capture", mode="som", app="Safari")
   ```
2. **Perform action by SOM index:**
   ```
   computer_use(action="click", element=7, capture_after=True)
   ```
3. **Core capabilities:** `double_click`, `right_click`, `scroll`, `drag`, `type`, `key` (e.g. `cmd+s`), `focus_app`, and `list_apps`.

### Crucial Safety Rules
- **Never click permission dialogs, password prompts, payment UIs, or 2FA challenges** unless specifically authorized.
- **Never type passwords or secrets** via `computer_use`.
- Prefer headless `browser_navigate` for general web workflows. Reach for `computer_use` only when driving native desktop applications.
