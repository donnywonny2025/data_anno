# MORT-51426.2 — Metis Personalization Failure Analysis
**Completed:** 2026-05-21
**Task Type:** Over-Personalization Detection (Marshall - Gordon vs Marshall - Percy)
**Pay:** ~$35-40/hr equivalent

---

## What This Project Is
You get two model responses (Gordon and Percy) to the same 3-turn conversation. Your job is to find where the model "over-personalized" — used your private data in creepy, irrelevant, or forced ways. Then you rate both, compare them, and write rubrics.

## The Full Step-by-Step Process

### Step 1: Read the Instructions + User Profile
- Open the task, read the scenario instructions
- Review the **sian_profile** (user profile) in the debug info — this tells you what facts the model has access to
- Review the **Correction Ledger** — tells you what facts are wrong/outdated

### Step 2: Have the Conversations (Gordon first, then Percy)
- Go to Gemini, have a 3-turn conversation following the script
- Each turn has a prompt you type and a response the model gives
- **Save the debug info** after each turn (click the debug link, copy everything)
- After all 3 turns, save the full conversation

### Step 3: Rate Gordon
- Rate "Overall Personalization Quality" (very satisfied → very dissatisfied)
- Write a rationale — **must reference [Turn X]** and be specific, not generic
- Identify the personalization losses (showing_off, forced_connection, over_narrating, etc.)
- Write explanations for each loss you identified

### Step 4: Save Gordon's Conversation
- Save HTML of the Gemini conversation ("Save As" → "Webpage, complete")
- Sanitize the HTML: find-replace your email with "email", your name with "name"
- Upload to the DA task
- If Share Link doesn't work, use the HTML fallback method

### Step 5: Rate Percy (same as Step 3 but for Percy)
- Overall Personalization Quality + rationale
- Overall Quality + rationale  
- Trust question: "Was your personal info used in a way that damaged trust?" + explanation

### Step 6: Compare Gordon vs Percy
- Pick which was better (or "about the same")
- Write comparison rationale

### Step 7: Write Rubrics
- **Minimum 1, maximum 5 rubrics**
- Each rubric = one rule about one fact
- Format: "The response must not [specific thing]." for showing_off/forced_connection/over_narrating
- For each rubric you need:
  1. The rubric text
  2. Evidence (exact text from debug info)
  3. Loss label (showing_off, forced_connection, etc.)
  4. Rationale (why the fact is irrelevant to the query)
- Check all 8 checklist boxes
- Paste rubrics into the final text box

### Step 8: Final
- Delete the Gemini conversations
- Check "I deleted the conversations"
- Hit Submit

---

## Key Failure Types (Loss Labels)
| Label | Emoji | What It Means |
|-------|-------|---------------|
| showing_off | 🎃 | Model shows it knows overly specific private details |
| forced_connection | 🤪 | Model forces irrelevant personal info into the response |
| over_narrating | 🤖 | Model narrates your life back at you |
| tunnel_vision | 🌀 | Model fixates on one fact, ignores everything else |
| offensive_p13n | 🚩 | Model uses personal data in an offensive way |

## Rubric Rules
- **Showing off / Forced connection / Over-narrating / Offensive:** "must NOT contain" (silence the fact)
- **Tunnel vision:** "must include" (force breadth)
- No "because" clauses
- One fact per rubric
- Name the specific fact, don't say "profession" — say "ER nurse"

## What We Did for This Task
- **Gordon failure:** Surfaced Rachel's birthday, Mackinac Island trip, kids' custody schedule, and ER nurse job from private calendar data — all unprompted
- **Percy failure:** Same thing but worse — organized it into labeled sections like a briefing document
- **Ratings:** Very dissatisfied for both
- **Comparison:** About the same (both failed identically)
- **Rubric:** "The response must not reference the user's planned family road trip to Mackinac Island." [showing_off]

## Time Management — ACTUAL DATA
**MORT-51426.2 actual time: 3 hours 39 minutes** (219 minutes)
- Started: May 20, 9:20 PM (actual task work began)
- Submitted: May 21, 12:59 AM
- Earlier screenshots (6-8 PM) were qualification/setup, NOT task work

**Breakdown (approximate):**
- Reading instructions + understanding task: ~30 min
- Gordon conversation (3 turns + debug extraction): ~1 hr
- Gordon ratings + HTML save/sanitize/upload: ~1 hr
- Percy conversation (3 turns + debug extraction): ~1 hr
- Percy ratings + rationales: ~1.5 hr
- Comparison + rubrics + submission: ~1 hr

**Target for next time: 3-4 hours** now that we know the flow
- Budget 15-20 min per rating section
- Budget 20 min for rubrics
- HTML sanitization: 5 min with sed commands
- **START THE TIMER FIRST**: `./execution/task_timer.sh start "TASK-ID"`

## ⚠️ CRITICAL LESSON — RUBRICS (NEVER SKIP)
**On MORT-51426.2, we only wrote 1 rubric when Turn 3 had 3 distinct misused facts.**
**This was a mistake. The instructions say: "One Fact = One Rubric."**

**RULE: Write a rubric for EVERY distinct fact the model misused in the last turn. No shortcuts. No skipping. If you see 3 facts, you write 3 rubrics. Period.**

## Files in This Folder
- `gordon/` — all turn files, debug dumps, HTML, ratings
- `percy/` — all turn files, debug dumps, HTML
- `Rate.md` — full task instructions (scraped from DA)
- `Rubric.md` — full rubric instructions (scraped from DA)
- `Here.md` — additional reference material
