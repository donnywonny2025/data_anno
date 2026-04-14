# Data Annotation Stealth Copilot & Sandbox Architecture

> This repository houses the unified Data Annotation AI architecture. It strictly separates production execution (The Stealth Mirror Copilot) from reverse-engineering initiatives (The Synthetic Portal Sandbox) to maintain the ultimate Gold Standard of operation.

---

## 🧭 The Gold Standard 
**If you are a new AI agent spinning up into this workspace, your first and only source of truth is:**
### ➡️ `DATA_ANNOTATION_MASTER_RECORD.md`
Read that file immediately. It contains the exact physical dual-monitor constraints, the overarching goals, and the current state of our account qualifications.

For detailed operational instructions (the "HOW"), refer to:
### ➡️ `data_annotation_ops.md`
This contains the Two-State Ingestion Dictionary (Acquisition Mode vs Execution Mode) and the Fallback Protocols for our tools.

---

## 🏗️ Architectural Map

Our repository is physically separated into two core domains to prevent cross-contamination.

### DOMAIN 1: The AI Copilot (Production Tools)
This is the live assistant layer. We use this to evaluate tasks securely alongside the user.
* **`stealth_dashboard/`** - The visual SPA (Single Page Application) that runs on the Left Monitor (LG TV). It updates completely via JSON polling natively, meaning the AI never steals browser focus with `location.reload()`.
* **`stealth_server.py`** - The Python backend driving the dashboard.
* **`execution/`** - Native Python execution scripts. *(Example: `fact_check.py` handles direct Firecrawl API searches, completely bypassing broken MCP Node wrappers).*
* **`war_room/`** - The central nervous system.
  * `DATA_DROP.md` - Where the user pastes task instructions for the AI to "Acquisition".
  * `TASK_LOG/` - The JSON files (`live_session.json`, `active_project.json`) that the Stealth Mirror polls.
  * `RESEARCH/` - Where we store compiled, digested rulebooks (e.g., `achilles_eval_rules.md`).
* **`ghost_fox/`** - The stealth automation framework utilizing Camoufox/Playwright.

### DOMAIN 2: The UI Sandbox (Reverse Engineering)
This is our clean-room to test, study, and break data structures without jeopardizing live tasks.
* **`synthetic_portal/`** - A completely isolated sandbox where we re-create the physical split-pane layouts, radio buttons, and form arrays used by the Data Annotation platform. We use this to mathematically verify our OCR and spatial visual ingestion scripts.

### DOMAIN 3: Archives & Prior Projects
Old logic and prior project tasks are preserved here so they don't pollute the core loops.
* **`MOMO_*` text files** - Logs and constraints from the archived Momo project.
* **`ref/`** - Local PDF reference library and source files for old evaluations.

---

## 🛠️ Toolchain Realities
* **Firecrawl:** Configured natively via python script (`execution/fact_check.py`) using a global alias `firecrawl`. If it ever drops, we fall back to generic Web Search immediately.
* **Docker/MCP:** Deprecated/Flaky on this machine. We stick to native deterministic Python scripts per `AGENTS.md`.
* **Gmail / Account Ingestion:** NEVER use the browser subagent or optical `look.sh` to read the user's personal Gmail. You must bypass the Human-AI Firewall by running the dedicated OAuth scripts (`execution/search_gmail.py` and `execution/gmail_inbox.py`) to pull email logs securely via API.
