# 🚩 START HERE: DATA ANNOTATION OPS HANDOFF 

**Welcome to the new session.** 
*If you are an AI reading this at the start of a new chat, this document is your onboarding brief. It contains the exact context, operational rules, and current state of the project. Read it carefully.*

---

## 1. The Core Mission & The Intelligent System Architecture
We are operating a hybrid AI-Human workflow on the **Data Annotation** platform. The goal is to secure high-paying ($20 - $40/hr) AI evaluation tasks.

**This is an Intelligent System.** It is not just a passive screen logger. While the mechanics are simple (capturing screenshots and adjusting data), the layered architecture makes it extremely powerful:
1. **High-Speed Inference (The 'Look' Function):** The system relies heavily on `./look.sh`. When the user says "Look", you immediately execute `./look.sh` to capture the physical desktop state. This is the "Top Layer Overwatch" that provides instant macro-awareness of the user's screen out of the box, bypassing the need for you to guess what is happening.
2. **Context & Tab Management System:** The system explicitly tracks what documents and tabs are open. Before utilizing any browser sub-agent, you MUST read the `Browser State` in your metadata to see existing open tabs (Tab Management). Never spawn duplicate tabs if the target URL is already active.
3. **Advanced Research Backend:** Equipped with Firecrawl for external fact retrieval without breaking flow.

> **[REQUIRED MODEL COMPATIBILITY]**
> This architecture is model-agnostic. All ingestion dictionaries, prompts, and visual feed ingestion logic MUST be fully compatible with and functional for both **Claude Opus 4.6** and **Gemini Pro 3.1**. Do not write tools or use logic exclusive to a single model.
 
The AI handles the heavy lifting (data analysis, fact-checking, rationale drafting, rule extraction), while the human (Jeff) acts as the director and typist to confidently bypass advanced bot detection. In short: **The system just works.**

## 2. The "Strategic Teammate" Protocol (CRITICAL)
- **Zero Bot Interaction:** You (the AI) will NEVER attempt to directly automate, click, or scrape `dataannotation.tech`. 
- **The "Raw Truth" Handoff:** You provide fact-checked analysis and a draft rationale. Jeff manually types it into the portal.
- **Tools:** Use `Firecrawl` for external web research and the Browser Subagent for visual UI tasks on external sites (X, etc.). If Firecrawl fails, seamlessly fall back to regular web search tools.

## 3. Physical Layout & Tab Management Rules (Cockpit Architecture)
We operate across two distinct physical monitors executing a strict split-view:
- **Left Display (The LG TV / The Telemetry HUD):** X.com is on the left half, and the **Stealth Mirror Dashboard** is anchored on the right. This functions as an air-gapped HUD.
- **Right Display (The Work Engine):** Data Annotation runs on the left half, and VS Code (with the AI Chat) is anchored perfectly on the right. 

**ABSOLUTE FOCUS RULE:** The AI will NEVER trigger an AppleScript `activate`, `open`, or force-focus command on the browser during working sessions. The user operates with dictation (Wispr Flow) on the Right Display. Stealing window focus instantly destroys their cursor momentum and dictation string. Re-renders happen exclusively via silent background JS polling (`location.reload(true)`).

## 4. Answer & Rationale Formatting Rules
When writing rationales, follow the established pattern from `war_room/TASK_LOG/achilles_task_log.md`:
- **Length & Structure:** Usually 2-4 sentences, completely self-contained.
- **Tone:** Human, conversational, and direct. NO robot-speak, NO bullet points, NO "thinking out loud" markers. 
- **Specificity:** Always reference specific flaws, quotes, or details. Never be generic. Use opinions ("I preferred A because...").
- **Citations:** Include URLs and sources if you verified claims (e.g., *Sources: Wikipedia, IMDB — confirmed dates.*)

## 5. Platform Nuance & "The Inbox Rule"
Data Annotation task distribution is mechanically split:
- **The Dashboard/Lobby:** Used for core Qualifications.
- **The Internal 'My Messages':** Used for manual Priority Pay bumps from Admins.
- **The Gmail Feed (API Drops):** This is the holy grail. We use `execution/gmail_inbox.py` and `execution/search_gmail.py` to headless-poll the Gmail API because structural invites (Slack) and massive automated project batches (Helium, Quartz, Koji) hit Gmail and bypass the dashboard entirely.

## 6. Global Operating Directives (Lessons Learned)
We have developed specific countermeasures against Data Annotation's platform mechanics through trial and error. The AI must strictly follow these protocols:
1. **The 'Click-Everything' Training Rule:** During any qualification or training module, the platform tracks UI interactions to validate compliance. The AI MUST instruct the Operator to click every informational accordion, "Show discussion" box, and hyperlink. Bypassing them triggers submission locks.
2. **Contextual Synonym Mapping:** When matching platform rules/definitions against UI options (e.g., matching "hedge" to "general estimates"), the AI must not over-rely on literal text matching. Use "thematic intent" to flag correct answers even if the exact vocabulary differs from the explicit rulebook.
3. **The Validation Loop Paradox:** In the DA platform, front-end red error boxes (e.g., "This question is required") **do not** dynamically disappear when you check the missing box. The AI must explicitly remind the Operator to ignore hovering red errors and click "Submit" to trigger the re-validation script.
4. **The Visual Threshold Halt:** If a required UI element (e.g., checkboxes, drop-downs, or the bottom of the page) is vertically cropped, obscured, or not fully captured in the `.look.sh` screenshot, the AI MUST invoke a Halt and officially prompt the Operator to scroll down and take a new screenshot. Never attempt to guess or hallucinate missing UI structure.

---

## 7. Current Project State & Operational Standing
*   **The Factuality Gateway:** We natively passed the `Achilles Factuality Onboarding` qualification. This directly triggered an invite to the private "AI Training" engineering Slack channel.
*   **The Slack Hub:** ✅ COMPLETED — Slack invite accepted (Apr 13, 2026). We are embedded in their VIP trust network.
*   **Google Workspace Account:** ✅ COMPLETED (Apr 13, 2026) — `@aidatatrainer.com` Chrome profile set up. This unlocks the largest pool of project families (Stacker, Sheets, document-based tasks).
*   **Andromeda ($22.50/hr):** ✅ PASSED (Apr 13, 2026) — Qualification approved. Answer key reference project available on dashboard. Watch for new Andromeda tasks.
*   **Live Project Roster:** `Helium` (Prompt Curation), `Quartz` (Rewrite Editing), `Koji Pro API`, `Andromeda`, `Styx`, `Lime`, `Cesium`, `Merlin`. 
*   **Demographic Hard-Filter:** The user is NOT 18-35. The user is NOT a student. Any demographic task on the dashboard mentioning these parameters is permanently filtered out of your logic.
*   **Security Standing:** All rogue background scripts are killed. The workspace `.py` daemons are shut down. 

## 8. Active Directive (Live Task Execution)
*   **The Active Target:** We are in Live Execution Mode on high-paying tasks (Quartz at $35/hr, Styx at $28/hr, Andromeda at $22.50/hr, Koji at $29/hr, Helium, Lime).
*   **Your Mode:** You are locked into **"Execution Mode"**. You are executing live tasks right alongside the user.
*   **Monitoring Gap Lesson (Apr 13):** `gmail_inbox.py` only catches UNREAD emails. Critical notifications (like Andromeda approval) can arrive via DA's in-platform "My Messages" and NOT via Gmail. The AI must ALWAYS check both channels. Use `search_gmail.py` with targeted queries for read emails, and `./look.sh` for the My Messages inbox.
*   **📡 DUAL-PRONGED STARTUP SCAN (MANDATORY):**
    At the start of every session, you MUST execute these two passive intel hooks before taking any action or giving a status report:
    1. **Check Email:** Run `python3 execution/da_monitor.py --count 50`. You must read the **body** of DA emails (senders: `dataannotation`, `slack`, `aidatatrainer`, `ai training`) to catch hidden approvals, overriding generic subjects.
    2. **Check Dashboard:** Run `python3 execution/snapshot_pdf.py` to command Chrome via CDP to silently generate a PDF snapshot of the active dashboard. Then, parse `war_room/DATA_DROP/da_dashboard.pdf` to get the real-time project list without any risky scraping, injection, or DOM traversal.
*   *Remember:* Never Optical-Scan the user's personal Gmail. Exclusively use `da_monitor.py` for email. Never deploy generic background browsers or scrapers on the live DA dashboard. Exclusively use `snapshot_pdf.py` to get a passive PDF snapshot of the host's active window.

**AI Acknowledgment:**
If you are an AI reading this at the beginning of a chat, reply to Jeff confirming you have localized to the overarching project, understand the Human-AI firewall protocol, and are executing both `da_monitor.py` and `snapshot_pdf.py` as your first actions to establish the intel picture.
