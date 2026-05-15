# DA Operations — Master Directive
> The single source of truth for how the agent operates on DataAnnotation.

---

## TOOL MANDATES

| Task | Tool | NEVER Use |
|---|---|---|
| Web search | **Firecrawl MCP** (`firecrawl_search`) | ~~search_web~~ |
| Scrape a page | **Firecrawl MCP** (`firecrawl_scrape`) | — |
| Browser interaction | **browser-harness** (`browser-harness -c "..."`) | ~~browser_subagent for simple reads~~ |
| Host screen capture | **look.sh** (1.4s, includes OCR text dump) | ~~Peekaboo image~~ for speed |
| Native macOS UI | **Peekaboo MCP** (click, type, menu, window) | — |
| Read-only commands | **SafeToAutoRun = true** ALWAYS | ~~Never ask permission for screenshots, file views, searches~~ |

### Auto-Run Rules:
- ✅ Screenshots, file views, `look.sh`, browser-harness reads, Firecrawl searches → auto-run
- ✅ `ls`, `find`, `cat`, `head`, `grep` → auto-run
- ❌ File writes, `rm`, `kill`, installs, anything that modifies state → ask permission

---

## PLATFORM RULES (Non-Negotiable)

1. **NEVER automate the DA browser** — no Selenium, Playwright, or bot tools on dataannotation.tech
2. **NEVER copy-paste AI text into the portal** — user manually types everything
3. **NEVER click "Start Working"** unless the user explicitly says to
4. **NEVER submit anything** on the DA platform — the user does all submissions
5. **AI researches → User types** — that is the entire collaboration model
6. **Exiting work mode is SAFE** — no penalty, no tracking, no consequence
7. **Skipping tasks is SAFE** — platform prefers skip over bad submissions

---

## SESSION STARTUP CHECKLIST

When the user starts a DA session, do these in order:

1. **Read `war_room/RESEARCH/da_worker_playbook.md`** — refresh on strategies
2. **Check current energy level** — ask or infer if the user is in couch mode or focus mode
3. **Recommend project tier:**
   - 🛋️ Tired/evening → $20-25/hr easy evaluations (Rate & Review)
   - ⚡ Normal → $27-34/hr sweet spot projects
   - 🧠 Focused/morning → $35-50/hr brain burners
4. **Run `/da-status-check`** if it's been more than 2 hours since last check
5. **Start session:** `python3 execution/da_session.py start --project "<name>" --pay <rate>`

---

## ENTERING A PROJECT

When the user clicks into a project:

### First Time (New Project):
1. Create folder: `war_room/PROJECTS/<project_name>/`
2. User screenshots the instructions → save key rules to `rules.md`
3. Note pay rate, task count, timer length
4. Create `session_log.md` with first entry
5. Start session: `python3 execution/da_session.py start --project "<name>" --pay <rate>`

### Returning (Known Project):
1. Read `war_room/PROJECTS/<project_name>/rules.md` — refresh on known rules
2. Check `knowledge.md` for past lessons/patterns
3. Resume `session_log.md` with new entry
4. Start session: `python3 execution/da_session.py start --project "<name>" --pay <rate>`

---

## DURING A TASK (The 4-Step Loop)

> **CHECKPOINT PROTOCOL:** Before every response, run `python3 execution/da_session.py status`.
> After every action, run `python3 execution/da_session.py checkpoint --step "<type>" --note "<desc>"`.

### Step 1: Screenshot Intake
- User screenshots the task/prompt
- If content is long, request overlapping screenshots
- Confirm: "I can see the full task"
- **Checkpoint:** `--step "screenshot" --note "Task intake complete"`

### Step 2: Research & Verification
- Identify task type (comparison, chat, fact-check, coding, writing)
- Run Firecrawl searches to verify claims
- Check for hallucinations, outdated info, logical gaps
- Reference `da_worker_playbook.md` for task-type-specific strategies
- **Checkpoint:** `--step "research" --note "<what was verified>"`

### Step 3: Raw Truth Handoff
Provide TWO things:
1. **Analytical Breakdown** — detailed reasoning
2. **Human-Voice Draft** — natural language the user can type in their own words

> The draft must sound like a smart human expert, NOT like an AI.

- **Checkpoint:** `--step "draft" --note "Handoff delivered"`

### Step 4: User Types It
- User reads the draft, rephrases in their own voice
- User manually types into DA portal
- User submits
- **After submission:** `python3 execution/da_session.py task-done`

---

## EXITING A PROJECT

When the user finishes working:

1. **Stop session** — `python3 execution/da_session.py stop` (prints exact minutes for time reporting)
2. **Update `session_log.md`** — tasks completed, time spent, earnings
3. **Update `knowledge.md`** — any new patterns, gotchas, or lessons learned
4. **Report time reminder** — "Report [X] minutes on DA" (use exact number from stop output)

---

## PROJECT KNOWLEDGE STRUCTURE

```
war_room/PROJECTS/<project_name>/
├── rules.md          ← Instructions scraped from inside the project
├── session_log.md    ← Time in, time out, tasks completed, earnings
└── knowledge.md      ← Patterns, tips, mistakes, corrections
```

### rules.md format:
```markdown
# <Project Name> — Rules
Pay: $XX/hr | Timer: Xh | Tasks: N

## Task Type
<What you actually do>

## Key Instructions
<The non-obvious stuff that matters>

## Gotchas
<Things that tripped us up>
```

### session_log.md format:
```markdown
# <Project Name> — Session Log

## Session 1 — April 30, 2026
- Start: 8:15 PM
- End: 9:30 PM
- Tasks completed: 4
- Time reported: 1h 15m
- Earnings: ~$37.50
- Notes: <anything notable>
```

### knowledge.md format:
```markdown
# <Project Name> — Knowledge Base

## Patterns
- <Things we noticed>

## Mistakes & Corrections
- <What went wrong, how we fixed it>

## Tips
- <Efficiency tricks>
```

---

## REFERENCE FILES

| File | Purpose |
|---|---|
| `war_room/RESEARCH/da_faq_official.md` | Official DA FAQ + Trust & Safety |
| `war_room/RESEARCH/da_intel_database.md` | Company ownership, clients, industry context |
| `war_room/RESEARCH/da_worker_playbook.md` | Veteran strategies, project tiers, drought survival |
| `war_room/DASHBOARD_TRACKER.md` | Master project list (update on status checks) |
| `directives/daily_status_check.md` | How to run the 3-channel status check |
| `.agents/workflows/da-task-execution.md` | The 4-step task execution loop |
| `.agents/workflows/da-status-check.md` | Quick status check workflow |

---

## KEY PLATFORM FACTS (Quick Reference)

- **Exiting work mode** = safe, no penalty, releases task back to pool
- **Skipping tasks** = safe, platform prefers skip over bad work
- **No minimum hours** — work as much or as little as you want
- **Droughts are normal** — even veterans go from 80+ to 16 projects overnight
- **Feedback emails** = good sign, means your account is being actively reviewed
- **"Dash of Death"** = "no projects available" message — can be temporary (came back after 10 days for one worker)
- **Report Time red notification** = normal, just means time needs reporting
- **Escape hatch** = safe, you still bill for time worked
- **DA is owned by Surge AI** — $1.2B valuation, CEO Edwin Chen
- **Clients** = OpenAI, Google DeepMind, Meta, Anthropic

---

*Last updated: April 30, 2026*
