# Daily Status Check — How to Check What's Going On

> This is the standard procedure for checking project availability and notifications on Data Annotation. Run this whenever the user asks "what's going on" or at the start of any session.

---

## The Three-Channel System

DA distributes work and admin communications through THREE channels. You must check ALL THREE to get the full picture.

### Channel 1: Gmail API (Background — No Browser Needed)
**Script:** `python3 execution/da_monitor.py --count 30`
**What it catches:** Email notifications for new projects, priority pay bumps, qualification approvals, Slack invites, admin broadcasts.
**Why it matters:** Project drops and priority pay bumps hit Gmail first. This is the fastest alert channel.

### Channel 2: DA Projects Board (Browser — Subagent DOM Read)
**URL:** `https://app.dataannotation.tech/workers/projects`
**What it catches:** The live project board — everything currently available to work on, with real-time task counts and pay rates.
**Why it matters:** This is the ground truth for what you can actually start working on RIGHT NOW. Projects appear here that never sent an email.

### Channel 3: DA Inbox / My Messages (Browser — Subagent DOM Read)
**URL:** `https://app.dataannotation.tech/workers/inbox`
**What it catches:** Internal admin messages — priority pay bump announcements, project-specific instructions, rule changes, admin notes, and custom messages that NEVER go to Gmail.
**Why it matters:** Priority pay bumps and admin instructions are often posted ONLY here. Missing these means missing money and potentially violating updated project rules.

---

## The Procedure

### Step 1: Run the Email Monitor
```bash
cd /Volumes/WORK\ 2TB/WORK\ 2026/DATA_ANNOTATION
python3 execution/da_monitor.py --count 30
```
Parse the output. Note any HIGH or CRITICAL priority items. Save the data mentally for cross-reference.

### Step 2: Check the DA Projects Board via Browser
1. Read Browser State from ADDITIONAL_METADATA.
2. If the DA dashboard is already open → use that tab's Page ID.
3. If not open → dispatch subagent to navigate to `https://app.dataannotation.tech/workers/projects`
4. Dispatch a **DOM read** subagent (NOT a screenshot-scroll approach):
   - Tell it: "Read the full DOM text content of the page. Extract every project name, pay rate, task count, and date. Return the complete list."
   - DOM reads get ALL content regardless of scroll position.
   - Screenshots only capture the visible viewport — they WILL miss items on long pages.

### Step 3: Check the DA Inbox via Browser
1. Navigate to `https://app.dataannotation.tech/workers/inbox` (same tab is fine — just tell subagent to navigate).
2. Dispatch a DOM read subagent to extract all messages — date, subject, and preview text.
3. Look for: priority pay announcements, rule changes, admin instructions, project-specific guidance.

### Step 4: Cross-Reference All Three Channels
Build a comparison:
- **Gmail + DA Inbox:** Do priority pay announcements in DA Inbox match Gmail notifications? Any admin messages in DA Inbox that Gmail missed?
- **Gmail + Projects Board:** Which emailed projects are still available? Which have filled up?
- **DA Inbox + Projects Board:** Do the pay rates on the board reflect the priority bumps announced in the inbox?
- **Projects only on dashboard:** User might not know about these — no notification was sent.
- **Projects only in email:** Those may have filled up already.

### Step 5: Report to User
Present a clean summary:
1. **Top opportunities** — sorted by effective pay rate (base + priority bumps), highest first
2. **New since last check** — anything that appeared since the previous session
3. **Priority alerts** — time-limited pay bumps with expiry windows
4. **Admin notes** — any rule changes or instructions from DA Inbox
5. **Demographic filter** — auto-exclude 18-35 / student tasks (per MASTER_RECORD)

---

## Tool Selection Guide

| Need | Tool | Notes |
|---|---|---|
| Read Gmail for DA emails | `da_monitor.py` | API, no browser. Works always. |
| Read DA project board | Browser subagent DOM read | Full page content, no scroll needed |
| Read DA internal inbox | Browser subagent DOM read | Navigate to /workers/inbox |
| Quick glance at current screen | `look.sh` | OCR of visible viewport only — use during live task work |
| Detailed email body | `da_monitor.py --full EMAIL_ID` | Read specific email in full |

## Rules
- **Never click "Start Working" on any project.** Read-only recon.
- **Never submit anything on the DA platform.** This is passive intelligence gathering.
- **DOM read over screenshot-scroll.** Screenshots miss content between scroll stops. DOM reads get everything.
- **Cross-reference always.** No single channel gives the full picture.
- **Update `browser_tabs.json`** after opening or closing tabs.
- **Demographic filter:** Skip anything targeting 18-35 year olds or students.

---

## Browser Tab Management (Quick Reference)
- **Gmail:** `https://mail.google.com/mail/u/3/#inbox` (jefferykerr@gmail.com = user index 3)
- **DA Dashboard:** `https://app.dataannotation.tech/workers/projects`
- **DA Inbox:** `https://app.dataannotation.tech/workers/inbox`
- **Tab registry:** `war_room/browser_tabs.json`
- **One tab per purpose.** Never duplicate. DA Dashboard and DA Inbox can share one tab (just navigate between them).
- **Check ADDITIONAL_METADATA** before dispatching any subagent.
- **See `directives/browser_management.md`** for full browser rules.
