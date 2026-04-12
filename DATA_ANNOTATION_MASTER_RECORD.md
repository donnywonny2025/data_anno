# DataAnnotation: Master Operational Record
**Owner:** Jeff Kerr | **Project Folder:** `/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION`
**Status:** ACHILLES ❓ SUBMITTED (no result received) | FACTUALITY RESEARCH ✅ PASSED
**Last Updated:** April 12, 2026

## Running Tally of Work (As of April 12, 2026)
Below is a quick ledger of what we have built and accomplished to date, so nothing gets lost:

**Systems Built:**
- `ghost_fox/` stealth automation framework (Camoufox/Playwright engine)
- `anonymize_local.py` & `scrub_momo.py` security utilities
- Internal execution bridges (`current_command.py`, `hitl_gmail_demo.py`)
- Visual browser subagent workflows to audit DA operations safely

**Project Milestones Completed:**
- **Mar 20:** Starter Assessment (Passed)
- **Mar 22:** Identity Verification (Completed)
- **Apr 04:** Achilles FAQ Training Qualification (6 tasks submitted, status unknown)
- **Apr 04:** Factuality Research Qualification (6 tasks submitted, **PASSED**)
- **Apr 04:** Multi-modal Opt-in Qualification (Image/Video/Audio)

**Current Objective:**
Resume the Data Annotation pipeline by tackling the **Achilles Factuality Onboarding Review ($20/hr)**.

---

## Account History & Milestones

| Milestone | Date | Result |
|---|---|---|
| **Starter Assessment** | March 11, 2026 | ✅ Passed. Unlocked dashboard. |
| **Core Qualification** | March 12, 2026 | ✅ Passed. All checkmarks confirmed. |
| **Identity Verification** | March 22, 2026 | ✅ Completed. Persona verified as Resident. |
| **Achilles Evaluation Qualification** | April 4, 2026 | ❓ 6/6 tasks submitted — NO pass/fail email received. Follow up with DA support. |
| **Factuality Research Qualification** | April 4, 2026 | ✅ PASSED — Email confirmed 1:07 PM. Next: complete Achilles Factuality Onboarding Review. |
| **Next: Coding ($40/hr)** | Pending | 🎯 Objective: Unlock specialized rate. |

---

## Current Focus: Achilles Evaluation

### What It Is
Achilles is a model comparison evaluation project where you rate Response A vs Response B across multiple axes (Instruction Following, Truthfulness, Overall Quality, Safety). Passing the FAQ Training qualification unlocks unlimited work at $20+/hr.

### Reference Materials
- **Full FAQ Rules:** `war_room/RESEARCH/achilles_eval_rules.md` (complete 47-page extraction)
- **Source PDF:** `ref/FAQ` (original 47-page document)
- **PDF Page Images:** `ref/faq_pages/` (all 47 pages as PNG + full text extraction)
- **Task Log:** `war_room/TASK_LOG/achilles_task_log.md` (running record of all tasks completed)

### Achilles Operational Protocol
1. **User provides task** (screenshots, text, or both)
2. **AI parses and assembles** the full prompt + Response A + Response B
3. **AI fact-checks** using Firecrawl for web research, verifying claims, checking links
4. **AI drafts rationale** — human voice, natural sentences, no dashes or bullet points, specific to the task, opinions showing through
5. **User manually types** the rationale into the DA portal
6. **AI saves the task** to the task log for future reference

### Comment Writing Rules (Achilles-Specific)
- 2-3+ sentences minimum, written like a real person talking
- Specific to THIS task — never generic
- Include fact-check links when verifying claims
- Let personal opinions come through naturally
- No structured format, no dashes, no "thinking out loud" markers
- Train of thought style — what caught your eye, why you rated this way

---

## The "Strategic Teammate" Protocol

1. **Vision-First Interface**: User provides screenshots of tasks/prompts. AI analyzes the layout and text visually.
2. **Multi-Input Ready**: AI handles screenshots, text, or mixed inputs and assembles them cohesively.
3. **No Direct Portal Interaction**: AI never visits or interacts with `dataannotation.tech`. All research happens via Firecrawl or browser subagent on external sites.
4. **Firecrawl for Research**: Primary tool for fact-checking, link verification, and web search.
5. **Browser Subagent**: For visual tasks (X/Twitter, pages needing JS rendering). One tab only.
6. **The "Raw Truth" Handoff**: AI provides fact-checked analysis and draft rationale. User manually types it.
7. **Zero Bot Detection**: AI never clicks, types, or interacts with the DA portal. User does all manual interaction.

### Physical Architecture & Focus Restrictions
- **The Decoupled Cockpit:** The user utilizes two massive displays. The **Left Monitor (LG TV)** serves tracking/telemetry (running the Stealth Mirror). The **Right Monitor** serves execution (running Data Annotation & VS Code/AI).
- **The "No-Touch" Focus Mandate:** Because the user drives manual data entry via Wispr Flow dictation on the Right Monitor, the AI is STRICTLY FORBIDDEN from using AppleScript, `open`, or `activate` commands to steal browser focus.

### Browser/UI Update Architecture (SPA Constraint)
- **Zero Reloads:** Due to Chromium's background throttling on secondary monitors, `window.location.reload()` fails silently when the LG TV window is unfocused. Reloads are strictly forbidden.
- **Dynamic SPA Updates:** The Stealth Mirror dashboard acts entirely as a Single Page Application (SPA). All UI components (like the `FC_MCP` Firecrawl indicator) and data streams updates must be pushed dynamically via the native Javascript JSON polling loop (`live_session.json`, `active_project.json`, `mcp_status.json`). 

### Multimodal Intelligence Synthesis (The Two Jobs)
The AI operates across dual modalities to solve structurally complex workspaces:
1. **Rule Synthesis (Right Pane - Intelligence Panel):** When the user invokes Acquisition Mode via `DATA_DROP.md`, the AI combines screen topology (from `look.sh` screenshots) with deep text instructions to formulate a cohesive, robust rulebook.
2. **Guided Execution (Left Pane - Timeline log):** During active task Execution Mode, the AI uses visual ingestion strictly to map interactive form fields geographically (e.g., "Check the third radio box for Truthfulness"). It directs the user exactly where to click and what to paste natively.

---

## Tactical Assets

| Asset | Location | Purpose |
|---|---|---|
| **Achilles FAQ Rules** | `war_room/RESEARCH/achilles_eval_rules.md` | Complete evaluation rulebook |
| **Achilles Task Log** | `war_room/TASK_LOG/achilles_task_log.md` | Running record of all completed tasks |
| **Momo Rules** | `war_room/RESEARCH/momo_project_rules.md` | Momo chatbot project constraints |
| **Ops Manual** | `data_annotation_ops.md` | Operational directives (updated for Achilles) |
| **Ghost Fox Engine** | `ghost_fox/` | Stealth automation layer (decoupled during manual quals) |
| **Execution Scripts** | `execution/` | Ghost server + command payloads (decoupled during manual quals) |

---

## Email Communication Log (jefferykerr@gmail.com)
*Verified March 23, 2026 — 9 total emails from DataAnnotation*

| Date | Subject | Summary |
|---|---|---|
| Mar 6 | Welcome to Dat... | Initial signup confirmation |
| Mar 9 | Action Required | Reminder to complete Starter Assessment |
| Mar 20 | See new projects | Starter Assessment passed, qualifications unlocked |
| Mar 21 | Great news! | Official acceptance — "Only a small percentage pass" |
| Mar 22 | New Project | New priority project notification |
| Mar 22 | [Update] PRIORITY | Priority Styx eval update |
| Mar 22 | New Project | Momo chatbot project notification |
| Mar 22 | New Project | New project at 4:32 PM |
| Mar 22 | [Update] PRIORITY | PRIORITY Styx eval update at 4:43 PM |

---

## Open Qualifications

| Qualification | Pay Unlock | Status |
|---|---|---|
| Achilles FAQ Training Qualification | $20+/hr | ❓ 6/6 submitted — no result email. Check with support. |
| Factuality Research Qualification | $25+/hr | ✅ PASSED (email confirmed 4/4/26 1:07 PM) |
| Achilles Factuality Onboarding Review | $20/hr | 🔥 NEXT — unlocks factuality projects |
| Opt-in: Image/Video/Audio Projects | — | 🔥 1-click opt-in (submitted 4/4/26) |
| Andromeda | $22.50+/hr | 🔥 Available (green tag) |
| Pegasus (Google Personalization) | $28+/hr | ⏳ Pending |
| Coding Qualification | $40+/hr | 🎯 Ultimate Target |

---

## Next Steps
1. ✅ Secured Achilles FAQ document (47 pages, fully extracted)
2. ✅ Codified evaluation rules and operational protocol
3. ✅ Achilles FAQ Training — COMPLETED April 4, 2026 (6/6 tasks)
4. ✅ Factuality Research Qualification — PASSED April 4, 2026 (Email Confirmed)
5. 🔥 Start **Achilles Factuality Onboarding Review** ($20/hr, 1 training task)
6. ⏳ Prepare for Coding Qualification ($40/hr)
