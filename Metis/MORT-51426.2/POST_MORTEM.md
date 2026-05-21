# MORT-51426.2 — Post-Mortem

> Task: Marshall-Gordon / Marshall-Percy Personalization Failure Analysis
> Date: May 20-21, 2026
> Time: 9:20 PM – 1:00 AM (3 hours 40 minutes)
> Status: SUBMITTED — cannot be edited or corrected

---

## What We Did Right
1. **Correctly identified the core failure** — model scraped private calendar data via `generic_calendar.search` and surfaced it unprompted
2. **Accurate ratings** — both models rated "Very dissatisfied" for showing_off behavior
3. **Strong rationales** — specific, referenced exact turns, named exact data points
4. **Proper HTML sanitization** — removed PII before archiving
5. **Completed all required sections** — all rating fields, comparison, and rubric filled out
6. **Submitted within the time window** — 55 minutes remaining at submission

## What Went Wrong

### 1. RUBRICS — CRITICAL ERROR
**What happened:** The instructions clearly state "One Fact = One Rubric (Atomic)." Percy's Turn 3 response contained **3 distinct misused facts:**
- Dinner at The Earle (calendar scrape)
- Kids' fishing trip / custody schedule (calendar scrape)
- Family road trip to Mackinac Island (calendar scrape)

**We only wrote 1 rubric** (for Mackinac Island). The AI told the user "the minimum is 1, you have 1, skip adding more." This was **wrong advice** that directly contradicted the task instructions.

**Impact:** Unknown. We met the stated minimum (1), but the instructions said to write one for each fact. We don't know how strictly this is evaluated. DA does not provide feedback on submissions — you never find out if you did it right or wrong. Poor quality can result in silent removal from projects or the platform entirely.

**Root cause:** AI prioritized speed over correctness. AI did not re-read the rubric instructions before advising to skip.

### 2. NO TIMER SET
**What happened:** The user asked the AI to set a timer. The AI either failed to set one or lied about setting one. After conversation truncation, no timer existed on disk or in any running process.

**Impact:** Unable to accurately determine start time. Had to reconstruct from file timestamps and user memory.

**Root cause:** AI did not write timer state to a persistent file on disk. Relied on conversation memory which gets truncated.

**Fix implemented:** Created `execution/task_timer.sh` which writes to `.task_timer` file on disk. Survives truncation. Documented in README and DA_Hub KI.

### 3. AI GAVE WRONG INFORMATION WITH CONFIDENCE
Multiple instances of stating things as fact when unsure:
- Said DA pays per task (wrong — it's primarily hourly)
- Said Google AI Premium is $20/month (wrong — ranges from $8-$200/month depending on tier)
- Flipped positions when corrected instead of verifying first
- Said "wait for the review" when DA doesn't provide submission reviews

**Root cause:** AI tendency to fill gaps with plausible-sounding answers rather than saying "I don't know."

**Fix implemented:** Added HONESTY RULE to DA_Hub.md KI — "If you don't know, say so. Don't guess. Don't flip when corrected — verify first."

### 4. AI MISIDENTIFIED TASK START TIME
Claimed task took 1 hour, then 7 hours, then corrected to 3:40 after user provided the actual start time. Could not determine start time from its own records.

**Root cause:** Earlier conversation was truncated. No persistent timer was set. AI confused setup/qualification screenshots with actual task work.

---

## Rules for Next Task (NON-NEGOTIABLE)

1. **START TIMER IMMEDIATELY** — `./execution/task_timer.sh start "TASK-ID"` before anything else
2. **ONE FACT = ONE RUBRIC** — identify every distinct misused fact in the last turn, write a separate rubric for each
3. **RE-READ INSTRUCTIONS BEFORE EACH MAJOR STEP** — especially before rubrics
4. **NEVER SAY "SKIP IT"** on a required component
5. **IF YOU DON'T KNOW, SAY "I DON'T KNOW"** — then go research it
6. **DON'T FLIP WHEN CORRECTED** — verify independently, then respond
7. **STOP TIMER ON SUBMIT** — `./execution/task_timer.sh stop`

---

## Open Questions We Cannot Answer
- Did the single rubric hurt our score? **Unknown — DA provides no feedback**
- Will this affect future task availability? **Unknown — DA removes silently**
- Was the rest of the submission strong enough to compensate? **Unknown**

We will only know if something is wrong if tasks stop appearing or account access changes.
