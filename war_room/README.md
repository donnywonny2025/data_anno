# ⚔️ DATA ANNOTATION WAR ROOM

> **📋 FULL OPS DIRECTIVE:** [`directives/data_annotation_ops.md`](file:///Volumes/WORK%202TB/SAVE/AGENTMONEY/directives/data_annotation_ops.md)

## 🚦 Current Status (Updated 2026-05-21)
- ✅ Starter Assessment: **PASSED**
- ✅ Core Assessment: **PASSED**
- ✅ First Metis task: **SUBMITTED** (MORT-51426.2, May 21 2026)
- 💰 Rate: **$20+/hr** base, **$40+/hr** after coding/UX qualifications
- 📊 Acceptance rate: **2-8%** of all applicants (we're in the top tier)

This is the tactical hub for the **"DataAnnotation Job Getter"** role.

---

## ⏱ TASK TIMER — MANDATORY FOR EVERY TASK

**This is Step 0. Before you do ANYTHING on a task, start the timer.**

```bash
# START (when you accept a task)
./execution/task_timer.sh start "TASK-ID"

# CHECK (mid-task, anytime)
./execution/task_timer.sh status

# STOP (when you submit)
./execution/task_timer.sh stop

# HISTORY (see all past tasks)
./execution/task_timer.sh log
```

**How it works:**
- `start` writes the task ID and Unix timestamp to `.task_timer`
- `stop` calculates elapsed time, logs it to `time_log.csv`, and clears the active timer
- `status` shows current elapsed without stopping
- `log` prints the full CSV history

**Rules:**
1. Timer starts the MOMENT you accept a task on the DA platform
2. Timer stops the MOMENT you hit Submit
3. Every task gets logged — no exceptions
4. If the conversation gets truncated, the timer file persists on disk — check `./execution/task_timer.sh status` to recover
5. The AI agent MUST run `start` as its first action when beginning a DA task

**Files:**
- `execution/task_timer.sh` — the timer script
- `.task_timer` — active timer state (auto-deleted on stop)
- `time_log.csv` — permanent history of all tasks

---

## 📂 Structure
- `SCREENSHOTS/`: Human drops task/prompt screenshots here.
- `RESEARCH/`: AI logs web search findings and fact-checks.
- `REFINED_RESPONSES/`: AI provides logically perfect, naturally phrased responses for Human manual-typing.
- `Metis/` — Completed task archives (one folder per task ID)

## 🔄 The Loop
1.  **Timer**: `./execution/task_timer.sh start "TASK-ID"`
2.  **Ingestion**: Human drops a screenshot into `SCREENSHOTS/`.
3.  **Research**: AI analyzes the screenshot, performs live web search, and verifies all claims.
4.  **Sandbox**: AI runs code/logic in a local `/tmp/` environment to ensure 100% accuracy.
5.  **Handoff**: AI deposits the final refined response in `REFINED_RESPONSES/`.
6.  **Execution**: Human manual-types the response into the DataAnnotation portal.
7.  **Submit**: `./execution/task_timer.sh stop`
8.  **Archive**: Move all task files to `Metis/TASK-ID/`

## 🚨 Critical Protocol
- **ZERO AI FOOTPRINT**: Do not copy-paste directly.
- **MANUAL TYPING ONLY**: Human simulates natural behavior.
- **FACTUAL PERFECTION**: AI cites sources and verifies logic.
- **TIMER ALWAYS RUNS**: No task without a running timer.
