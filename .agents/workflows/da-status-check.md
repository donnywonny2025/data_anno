---
description: Check Data Annotation status — dashboard, inbox, Gmail, and active projects
---

# Data Annotation Status Check

> **Trigger:** User says "where are we at", "what's going on", "status check", "check DA", "what do we got", "anything new", "let's work", "what's available", or `/da-status-check`
> **Knowledge Item:** ALWAYS read `DA_Operations` Knowledge Item first — it has credentials, pending actions, and behavioral rules.

// turbo-all

## CRITICAL RULES (Read BEFORE doing anything)

1. **NEVER click into any project, qualification, or message on DA.** Read-only DOM reads only.
2. **Browser harness for status checks. look.sh for work mode.** Never mix these. Disconnect browser harness before user starts any DA task.
3. **DA site structure:** Projects, Qualifications, Surveys, and Report Time are TABS on the SAME page (`/workers/projects`). They are NOT separate URLs. Do NOT try to navigate to `/workers/qualifications` — that URL does not exist and will show an error page.
4. **Inbox IS a separate URL:** `https://app.dataannotation.tech/workers/inbox`
5. **Tab management:** Keeping multiple tabs open (e.g. one for DA, one for Gmail) is perfectly fine and preferred. Use `new_tab()` to open them side-by-side.
6. **Gmail is checked via Python script**, NOT by opening Gmail in the browser.
7. **jefferykerr@gmail.com** is the only Gmail account.
8. **Screenshots go in the workspace** at `/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/screenshots/` — NEVER to /tmp.
9. **Report conversationally.** This user is a verbal processor. Don't give checklists.

## Step 1: Gmail API Check (No Browser Needed)

```bash
cd /Volumes/WORK\ 2TB/WORK\ 2026/DATA_ANNOTATION && python3 execution/da_monitor.py --count 15
```

Parse the output. Note HIGH and CRITICAL priority items. Hold this data for cross-reference in Step 4.

## Step 2: Connect Browser Harness

### If Chrome is NOT running:
```bash
open -a "Google Chrome"
```
Then tell the user: "Pick your profile and let me know when you're in." Wait for confirmation.

### If Chrome IS running:
Check if the daemon is alive:
```bash
browser-harness --doctor
```
- If `[ok] daemon alive` → skip to Step 3
- If `[FAIL] daemon alive` → clean sockets and reconnect:
```bash
rm -f /tmp/bu-default.sock /tmp/bu-default.pid /tmp/bu-default.log
browser-harness -c "print(page_info())"
```

### First-time browser harness errors:
- **"starting..." hang on chrome://inspect** → Check if OBS or screen capture is blocking. If not, quit Chrome fully, clean sockets, reopen Chrome normally, wait 5 seconds, retry.
- **"DevToolsActivePort not found"** → The remote debugging checkbox hasn't been enabled on this profile. Open `chrome://inspect/#remote-debugging` and ask user to check the box. This is a one-time per-profile action.
- **Stale websocket** → `rm -f /tmp/bu-default.sock /tmp/bu-default.pid && browser-harness -c "print(page_info())"`

## Step 3: Read DA Dashboard (Browser DOM Read)

### 3a. Navigate to projects page
First time (no green-dot tab yet):
```bash
browser-harness -c "new_tab('https://app.dataannotation.tech/workers/projects'); wait_for_load(); import time; time.sleep(2); print(page_info())"
```

Subsequent navigations (green-dot tab exists):
```bash
browser-harness -c "goto_url('https://app.dataannotation.tech/workers/projects'); wait_for_load(); import time; time.sleep(2); print(page_info())"
```

### 3b. Read ALL content via DOM (no scrolling needed)
```bash
browser-harness -c "
html = js(\"document.querySelector('body').innerText\")
print(html)
"
```
This gets ALL projects, qualifications, and tabs in one read — the entire page regardless of viewport.

### 3c. Read Inbox (separate URL, same tab)
```bash
browser-harness -c "goto_url('https://app.dataannotation.tech/workers/inbox'); wait_for_load(); import time; time.sleep(2)
html = js(\"document.querySelector('body').innerText\")
print(html[:5000])
"
```

## Step 4: Cross-Reference All Three Channels

Build a comparison:
- **Gmail vs DA Inbox:** Priority bumps that appear in one but not the other.
- **Gmail vs Projects Board:** Emailed projects still available? Any filled up?
- **DA Inbox vs Projects:** Do pay rates reflect announced priority bumps?
- **Dashboard-only projects:** Things the user hasn't been notified about.
- **Pending actions** from the DA_Hub Knowledge Item — anything overdue?

## Step 5: Report to User

Present a CONVERSATIONAL summary covering:
1. **Top opportunities** — sorted by effective pay rate, highest first
2. **New since last check** — anything new since the previous session
3. **Priority alerts** — time-limited pay bumps with expiry windows
4. **Admin notes** — rule changes or instructions from DA Inbox
5. **Pending actions** — anything from the Knowledge Item that's overdue
6. **Ask:** "Want to work or just checking in?"
7. **If working:** Disconnect browser harness, start timer: `./execution/timer.sh start`
