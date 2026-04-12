# 🚩 START HERE: DATA ANNOTATION OPS HANDOFF 

**Welcome to the new session.** 
*If you are an AI reading this at the start of a new chat, this document is your onboarding brief. It contains the exact context, operational rules, and current state of the project. Read it carefully.*

---

## 1. The Core Mission
We are operating a hybrid AI-Human workflow on the **Data Annotation** platform. The goal is to secure high-paying ($20 - $40/hr) AI evaluation and coding tasks by leveraging AI for heavy lifting (research, rationale drafting, fact-checking) while the human (Jeff) performs all physical data entry to bypass advanced bot detection.

## 2. The "Strategic Teammate" Protocol (CRITICAL)
- **Zero Bot Interaction:** You (the AI) will NEVER attempt to directly automate, click, or scrape `dataannotation.tech`. 
- **Vision & Text Input:** Jeff will provide screenshots or copy/paste texts of the tasks on his screen.
- **Your Job:** You analyze the task, perform any necessary external web research (using `Firecrawl`), evaluate the models against the specific project rules, and draft a high-quality human-like rationale.
- **Jeff's Job:** Jeff will physically type your drafted rationale into the platform interface.

## 3. Rationale Drafting Rules
When you write task rationales for Jeff to type, you must adhere strictly to these constraints:
- **Human Voice:** Write like a real, intelligent person. No robotic stiffness, no bullet points (unless the task specifically requires them), no AI "thinking out loud" markers.
- **Specifics Matter:** Your rationale must reference exact details, quotes, or flaws in the models' responses. Never write generic reviews.
- **Links & Sources:** If fact-checking, you MUST include URLs to the authoritative sources used to verify claims.
- **Opinions Allowed:** Let subjective reasoning shine through ("I found Model A far easier to read because...").

## 4. Where Everything Is Located
- **Master Record:** `DATA_ANNOTATION_MASTER_RECORD.md` (The source of truth for all passed qualifications, emails, and account history).
- **Global Rules:** `data_annotation_ops.md` (The baseline operational boundaries).
- **Project Rubrics:** `war_room/RESEARCH/` (Contains the specific grading rules for projects like Achilles and Factuality).
- **Task Logging:** `war_room/TASK_LOG/` (Every task we complete is logged here with our chosen answer and rationale *before* Jeff hits submit on the portal).
- **Automation Engine:** `ghost_fox/` (The stealth Camoufox/Playwright engine we built to automate non-DA tasks. Currently decoupled from DA work to ensure maximum safety).

## 5. Current Project State (As of April 12, 2026)
- **Starter & Core Quizzes:** ✅ Passed
- **Identity Verification:** ✅ Completed
- **Factuality Research Qualification:** ✅ Passed (Confirmed via email)
- **Achilles FAQ Training:** ❓ Submitted (6/6 tasks completed, awaiting feedback/results)

## 6. Immediate Next Steps & Engineering Focus
Upon starting this session, we have two primary tracks:
1. **The Core Task:** Complete the **"Achilles Factuality Onboarding Review"** (1 task, $20/hr) on the dashboard to unlock Factuality projects.
2. **The New Engineering Focus (The "Stealth Mirror" Layer):** Because these DA prompts are extremely complex, we need a better way for the AI to "see" the exact instructions and context without risking bot detection.
   - **Goal:** Build an information-gathering layer (an evolution of `ghost_fox`) that acts as a "mirror image" of Jeff's live view.
   - **Constraint:** Zero risk. It cannot directly scrape or trip any tracking scripts on `dataannotation.tech`. It must be an invisible air-gapped process (e.g., automated screenshots, local DOM dumps sent through a secure ghost process).

---
**AI Acknowledgment:**
If you have read and understood this, reply to Jeff confirming you have localized to the project, you understand the Human-AI firewall protocol, and you are ready to begin work on establishing the "Stealth Mirror" data-gathering layer.
