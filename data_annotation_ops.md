# Data Annotation Ops Manual

## The Two-State Ingestion Dictionary (CRITICAL)
To prevent the AI from wasting compute scanning for rules during active tasking, we operate in two distinct modes triggered by specific phrases in chat:

### 1. Acquisition Mode (The Rule Drop)
**Trigger Phrases:** *"Digest the drop", "Prep Andromeda", "Look at these instructions"*
**AI Behavior:** I assume you are giving me raw project guidelines. I ignore task-solving logic. I hyper-focus on extracting project rules, constraints, formatting rubrics, and forbidden actions. I write this data to the Intelligence Panel (Right monitor) and lock it in.

### 2. Execution Mode (Live Tasking)
**Trigger Phrases:** *"Task 1", "Look at this task", "Execute"*
**AI Behavior:** I assume the Intelligence Panel is locked and loaded. I completely stop looking for overarching project rules. I split the screen exactly as the DA UI dictates: I read the **Left Pane** (the prompt/models) and the **Right Pane** (the form fields/questions). I evaluate the exact task at hand quickly, provide your rationale, and drop a "Task Complete" note in the Timeline. 

---## Active Project: Achilles Evaluation

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
