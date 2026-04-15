---
description: Check Data Annotation status — dashboard, inbox, Gmail, and active projects
---

# Data Annotation Status Check

> **Trigger:** User says "check DA status", "what's going on", "status check", or `/da-status-check`
> **Full procedure:** See `directives/daily_status_check.md`

// turbo-all

## Step 1: Gmail API Check (No Browser Needed)

```bash
cd /Volumes/WORK\ 2TB/WORK\ 2026/DATA_ANNOTATION && python3 execution/da_monitor.py --count 30
```

Parse the output. Note HIGH and CRITICAL priority items. Hold this data for cross-reference in Step 4.

## Step 2: DA Projects Board (Browser DOM Read)

1. Read `Browser State` from ADDITIONAL_METADATA.
2. If a DA tab is already open → use that Page ID. If not → dispatch subagent to navigate to `https://app.dataannotation.tech/workers/projects`
3. Dispatch a DOM read subagent with these exact instructions:
   > "The DA dashboard is already open on Page ID [ID]. Do NOT click anything. Read the full DOM text content. Extract every project name, pay rate, task count, and created date from BOTH the Qualifications table and the Projects table. Return the complete list — every single row."
4. **Use DOM read, NOT screenshot-scroll.** The page is 7000-8000px tall. Screenshots will miss content.

## Step 3: DA Inbox (Browser DOM Read)

1. Dispatch subagent to navigate to `https://app.dataannotation.tech/workers/inbox` (same tab is fine).
2. Read all messages via DOM — date, subject, preview text.
3. Look for: priority pay bump announcements, rule changes, admin instructions.

## Step 4: Cross-Reference All Three Channels

Build a comparison:
- **Gmail vs DA Inbox:** Priority bumps that appear in one but not the other.
- **Gmail vs Projects Board:** Emailed projects still available? Any filled up?
- **DA Inbox vs Projects:** Do pay rates reflect announced priority bumps?
- **Dashboard-only projects:** Things the user hasn't been notified about.

## Step 5: Report to User

Present a clean summary with:
1. **Top opportunities** — sorted by effective pay rate, highest first
2. **New since last check** — anything new since the previous session
3. **Priority alerts** — time-limited pay bumps with expiry windows
4. **Admin notes** — rule changes or instructions from DA Inbox
5. **Auto-excluded** — note any 18-35/student tasks filtered out

## CRITICAL RULES
- **NEVER** click "Start Working" or submit anything on the DA platform
- **READ ONLY** — no replies, no form submissions, no clicking into projects
- Gmail is checked via API (`da_monitor.py`), NOT by opening Gmail in the browser
- **jefferykerr@gmail.com** is the only Gmail account — never touch other accounts
- DOM read over screenshot-scroll — always
- Update `war_room/browser_tabs.json` after any tab changes
