# Browser Tab Management Directive

## The Rule
Tabs are persistent. Once opened, they stay open. The user does not randomly close or open tabs. Treat every tab as a long-lived resource.

## The Registry
`war_room/browser_tabs.json` tracks every open tab:
```json
{
  "tabs": {
    "gmail": {
      "page_id": "F2231865AFA893816704EBD5CC21DDAB",
      "url": "https://mail.google.com/mail/u/3/#inbox",
      "account": "jefferykerr@gmail.com",
      "monitor": "left",
      "purpose": "DA email monitoring (visual)"
    }
  }
}
```

## Before ANY Subagent Dispatch
1. Read `Browser State` from ADDITIONAL_METADATA.
2. Read `war_room/browser_tabs.json`.
3. If the target tab already exists → tell the subagent the exact Page ID and say "the page is already open — do NOT navigate or open a new tab."
4. If no tabs exist → tell the subagent to navigate in the existing active tab.
5. NEVER open a duplicate of something that's already open.

## After ANY Subagent Completes
1. Read the new Browser State from metadata.
2. Update `browser_tabs.json` with any new Page IDs or removed tabs.

## 🚨 ACTIVE TASK PROTECTION (CRITICAL — NEVER VIOLATE)

**If a DA task, qualification, or timed assessment is open in ANY tab, that tab is SACRED.**

1. **NEVER use `goto_url()` on a tab that has an active DA task or qualification.** This navigates away from the page and can destroy drafts, reset timers, or lose progress.
2. **If you need to check something else (Gmail, Gemini, speedtest, any external site), use `new_tab(url)` to open a SEPARATE tab.** Do your check there.
3. **When the auxiliary check is done, close the aux tab and `switch_tab()` back to the DA task tab.**
4. **Before navigating ANY tab, check `page_info()` first.** If the URL contains `dataannotation.tech/workers/tasks/` — STOP. That is a live task. Do not touch it with `goto_url()`.

### The Pattern for Auxiliary Checks During Active Work:
```python
# CORRECT — preserves the DA task tab
da_tab_id = page_info()['targetId']  # save reference
new_tab('https://mail.google.com/...')  # aux check in new tab
# ... do your read ...
close_tab()  # close aux tab
switch_tab(da_tab_id)  # return to DA task
```

```python
# WRONG — destroys the DA task page
goto_url('https://mail.google.com/...')  # NEVER DO THIS ON A TASK TAB
```

**Why this matters:** DA qualifications have countdown timers (typically 6-10 hours). If you navigate away, the draft may be lost, the page may need to reload, and in worst case the task could expire or error out. The user's earnings depend on these pages staying intact.

---

## Hard Rules
- **One tab per purpose.** Gmail = 1 tab. DA dashboard = 1 tab. No duplicates ever.
- **Never switch Google accounts.** If Gmail opens on the wrong account, navigate directly to the correct `/mail/u/N/` URL. Do NOT click the profile avatar and browse through accounts.
- **jefferykerr@gmail.com = /mail/u/3/.** This is the correct user index. Always use it.
- **donnywonny2023@gmail.com = /mail/u/1/ (in atelier profile).** Secondary account for data collection projects.
- **Never close tabs via script.** If a junk tab exists, ask the human to close it.
- **Never click into other accounts.** The subagent must ONLY interact with the target tab. No exploring.
- **Minimal instructions.** Tell the subagent exactly what to do in 2-3 steps max. The more you say, the more it freestyles.
