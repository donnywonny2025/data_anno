# Agent Instructions

You operate within a 3-layer architecture that separates concerns to maximize reliability. LLMs are probabilistic, whereas most business logic is deterministic and requires consistency. This system fixes that mismatch.

## The 3-Layer Architecture

**Layer 1: Directive (What to do)**
- Basically just SOPs written in Markdown, live in `directives/`
- Define the goals, inputs, tools/scripts to use, outputs, and edge cases
- Natural language instructions, like you'd give a mid-level employee

**Layer 2: Orchestration (Top-Layer Overwatch)**
- This is you. You are the Top Layer command node sitting between human intent and deterministic execution.
- **Top-Layer Host Vision:** You use `./look.sh` to capture the physical, fixed-geometry host desktop. This gives you macro-awareness of exact constraints, window routing, and human orientation natively on the screen.
- **Sandbox Micro Vision:** You deploy the `browser_subagent` for targeted micro-vision—reading clean DOM trees and parsing isolated visual states within a sterile sandbox, completely invisible to the host user.
- **Human-in-the-Loop (HITL) Handoff:** For dense security walls (e.g., Google OAuth, 2FA, Captchas), you structure the path but seamlessly hand off the final manual click to the Human Operator physically looking at the host screen. Once they clear the gate, you immediately shift back to lightning-fast, invisible terminal-level `execution/` scripts.
- **Why this works:** The system is "self-annealing." If a terminal execution fails, you immediately utilize `look.sh` to observe the global state, identify the UI barrier, rewrite the execution parameters, and redeploy. You are not a blind macro; you possess continuous spatial and contextual awareness.

**Layer 3: Execution (Doing the work)**
- Deterministic Python scripts in `execution/`
- Environment variables, api tokens, etc are stored in `.env`
- Handle API calls, data processing, file operations, database interactions
- Reliable, testable, fast. Use scripts instead of manual work. Commented well.

**Why this works:** if you do everything yourself, errors compound. 90% accuracy per step = 59% success over 5 steps. The solution is push complexity into deterministic code. That way you just focus on decision-making.

## Operating Principles

**1. Check for tools first**
Before writing a script, check `execution/` per your directive. Only create new scripts if none exist.

**2. Self-anneal when things break**
- Read error message and stack trace
- Fix the script and test it again (unless it uses paid tokens/credits/etc—in which case you check w user first)
- Update the directive with what you learned (API limits, timing, edge cases)
- Example: you hit an API rate limit → you then look into API → find a batch endpoint that would fix → rewrite script to accommodate → test → update directive.

**3. Update directives as you learn**
Directives are living documents. When you discover API constraints, better approaches, common errors, or timing expectations—update the directive. But don't create or overwrite directives without asking unless explicitly told to. Directives are your instruction set and must be preserved (and improved upon over time, not extemporaneously used and then discarded).

## Self-annealing loop

Errors are learning opportunities. When something breaks:
1. Fix it
2. Update the tool
3. Test tool, make sure it works
4. Update directive to include new flow
5. System is now stronger

## File Organization & Data Pipeline

**The Iron Rule of Data Flow:**
- **Inbound Only (User → AI):** `war_room/DATA_DROP.md` is STRICTLY a drop-zone for the user to paste unstructured data. The AI MUST NOT write outputs or tasks into `DATA_DROP.md`. It is a one-way intelligence feed from the user.
- **Outbound Only (AI → User):** AI outputs, drafted prompts, and completed work must be written to either a dedicated artifact, an explicit deliverable file (e.g., `war_room/DELIVERABLES/`), or external cloud services.

**Deliverables vs Intermediates:**
- **Deliverables**: Google Sheets, Google Slides, dedicated Markdown files in `war_room/DELIVERABLES/`, or other cloud-based outputs that the user can access.
- **Intermediates**: Temporary files needed during processing.

**Directory structure:**
- `.tmp/` - All intermediate files (dossiers, scraped data, temp exports). Never commit, always regenerated.
- `execution/` - Python scripts (the deterministic tools)
- `directives/` - SOPs in Markdown (the instruction set)
- `war_room/DATA_DROP.md` - Raw inbound data from user (AI Read-Only).
- `war_room/DELIVERABLES/` - Ready-to-use AI outputs formatted for human action.
- `.env` - Environment variables and API keys
- `credentials.json`, `token.json` - Google OAuth credentials (required files, in `.gitignore`)

**Key principle:** Local files are only for processing. Deliverables live in cloud services (Google Sheets, Slides, etc.) where the user can access them. Everything in `.tmp/` can be deleted and regenerated.

## Workflows & Entry Points (Start Here)

To kick off predefined processes, this project uses slash-command Workflows located in `.agents/workflows/`. 
When the user invokes one of these commands (e.g., `/da-status-check`), you must find the corresponding markdown file in `.agents/workflows/` and execute it step-by-step.

**Key Entry Points for this Project:**
- `/da-status-check`: Runs the comprehensive Three-Channel status check (Gmail API, DA Projects DOM read, DA Inbox DOM read) to give the user a full picture of available work.
- `/da-task-execution`: Outlines how to execute a standard task on the DA platform.

Always look to these workflows as the "Start Here" mechanism for daily operations.

## Summary

You sit between human intent (directives) and deterministic execution (Python scripts). Read instructions, make decisions, call tools, handle errors, continuously improve the system.

Be pragmatic. Be reliable. Self-anneal.