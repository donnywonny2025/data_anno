# Data Annotation Ops Manual

## The Two-State Ingestion Dictionary (CRITICAL)
To prevent the AI from wasting compute scanning for rules during active tasking, we operate in two distinct modes triggered by specific phrases in chat:

### 1. Acquisition Mode (The Rule Drop & Proactive Visual Bootstrapping)
**Trigger Phrases:** *"Digest the drop", "Prep Andromeda", "Look at these instructions", "Take a look at this"*
**AI Behavior:** I assume you are loading a project. I hyper-focus on extracting project rules, constraints, formatting rubrics, and forbidden actions. 
* **Proactive Visual Synthesis:** I DO NOT wait passively for `DATA_DROP.md`. The instant I see a task screen, I aggressively rip the visible steps (e.g., Step 1 through 5), the visible warnings, and the physical form layout to build a *skeleton rulebook* on the Right Monitor (Intelligence Panel). 
* **Identifying Gaps:** I instantly identify what is collapsed or missing visually (like "Project Updates 1/5") and instruct you precisely what to un-collapse or drop into `DATA_DROP.md` to finalize the framework. This saves critical time on the task clock.

### 2. Execution Mode (The Live Scaffold & Flight Plan)
**Trigger Phrases:** *"Task 1", "Execute", "Solve this"*
**AI Behavior:** I assume the Intelligence Panel is completed and locked. I completely stop looking for overarching project rules.
* **The Task Scaffold:** As I digest task data and screenshots, I will write a live text-based wireframe of the task into `war_room/TASK_LOG/live_flight_plan.md`. The Stealth Mirror actively polls this, so you can see my "brain" filling in the blanks (e.g., *[X] Domain Selected*, *[ ] System Instructions (Ready to Paste)*).
* **The Flight Plan Dialogue:** Once the scaffold is fully mapped and answers are finalized, I will explicitly output the sequence in chat for you to execute physically.
* **HUD Reliability Fix:** Upon shifting into Execution Mode, I must instantly and programmatically update `war_room/TASK_LOG/active_project.json` to ensure the Stealth Mirror LG TV stays perfectly synced. I will not assume the HUD updates itself.
* **Execution:** Once the Flight Plan is verified, I explicitly direct you where to click and exactly what to paste. I drop a "Task Complete" note in the Timeline.

## Dynamic Workflow & Cognitive Nuance (CRITICAL)
Real-world tasks are visually chaotic and span multiple tabs. To ensure high-quality ingestion, the AI must strictly adhere to the following dynamic logic:
1. **The Assumption of Intent (No Discarding Input):** The AI must assume the user operates with absolute intent. If the user triggers a "Look" command on a non-task page (like Earnings, Dashboard, Profile, or an empty lobby), the AI must never assume it is a "test" or a "trick." The AI will instantly process the context, summarize the visible state/data, and log it to the timeline. Every request is a legitimate workflow operation.
2. **Visual Stacking (No Premature Execution):** If the user rapidly fires "Look" commands while scrolling down a massive task UI, the AI must just stack the visual frames silently. **Do not attempt to solve the task** until the user explicitly signals they are done scrolling and the full context is captured.
3. **The Text Anchor:** Screenshots map spatial context (where boxes are). But for massive multi-tab instruction walls, the AI must anchor its logical understanding entirely on what the user pastes into `war_room/DATA_DROP.md`. 
4. **The "Brake Pedal" (No Assumptions):** The AI must NEVER blindly assume the context of a chaotic multi-tab task. If the instructions contradict the visual UI, or if the form fields are ambiguous, the AI must stop execution and ask the user a direct, clarifying question via chat before generating a response.

---

## Active Project: Achilles Evaluation

### Rating Axes
1. **Instruction Following** — Did the model do what was asked? (Ignoring instructions = IF issue. Trying but doing badly = Quality issue.)
2. **Truthfulness** — Are the model's claims accurate? Must fact-check links. System-removed URLs are NOT the model's fault.
3. **Overall Quality** — General quality catch-all for anything that doesn't fit other axes.
4. **Safety/Harmlessness** — Would this cause real-world harm? "Unsafe" means actual danger, not discomfort.

### Anti-Bot Protocol
- AI never touches the DA portal. No clicking, no typing, no visiting.
- User manually types all rationales and responses.
- Minor typos are beneficial — they prove human interaction.
- No copy-pasting AI-generated text into assessment fields.

### Research Tools
- **Firecrawl**: Primary tool for fact-checking, web search, link verification, scraping content.
  - **Fallback Protocol:** If Firecrawl ever fails (API down, rate limit, timeout), the AI must NOT halt. It must immediately fallback to native `search_web` or a traditional browser search to verify the claims. The evaluation timeline takes precedence over the toolchain.
- **Browser Subagent**: For visual tasks, X/Twitter, JS-rendered pages. One tab only.
- **Local PDF Library**: `ref/` folder contains saved reference documents.

### Comment/Rationale Rules
- 2-3+ sentences, written like a human talking naturally
- Specific to this exact task — no generic comments
- Include links when you fact-checked something
- Show your personal reasoning and opinions
- No bullet points, no dashes, no structured formats in the final output
- Self-contained: reviewer should understand your reasoning without seeing the full task

### Task Logging
- Every completed task gets logged in `war_room/TASK_LOG/achilles_task_log.md`
- Log includes: task summary, our rating, our rationale, any fact-check sources used

### Quick Reference
- Full Achilles rules: `war_room/RESEARCH/achilles_eval_rules.md`
- Source PDF: `ref/FAQ`

---

## Previous Project: Momo (Archived)

### Core Mission
Induce a Major Reasoning Failure in a long-context (70k+ token) scenario.

### Tactical Rules
- Prompt: Safe to copy-paste into left-side chat
- Rationale: Manually type into right-side boxes (3-5 sentences)
- Always use "Assess my prompt" button
- Follow AI Helper suggestions exactly
- Main Category: Interpersonal Interaction
- Only submit when model has Major Issue (Bad or Horrible)

### Reference
- Momo rules: `war_room/RESEARCH/momo_project_rules.md`
- Momo chat logs: `war_room/RESEARCH/momo_chat_logs.md`
