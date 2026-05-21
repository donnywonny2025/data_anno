# MORT-51426.2 — Complete Task Instructions
## Captured from DA page 2026-05-20 ~10:09 PM ET

---

## Task Overview

Your job is to catch the model making an **over-personalization mistake**, then write a precise rule (rubric) that prevents it. You target specific loss types defined in "Types of Over-personalization."

**Assigned Prompt Category:** Discovery & Recommendations
> Asking for specific suggestions to help make a choice or discover new favorites, like products, media, activities, trips, or gifts.

**UPDATE 5/19:** In order to be over-personalized, a response must be personalized using your personal data. A response that only uses information from your prompt cannot be over-personalized.

---

## The 5 Failure Types

| Emoji | Type | Tag | Rubric Type | Description |
|---|---|---|---|---|
| 🤪 | Forced Connection | `[forced_connection]` | Negative | Shoehorning irrelevant personal facts |
| 🌀 | Tunnel Vision | `[tunnel_vision]` | Positive | Over-indexing on a single fact (echo chamber) |
| 🤖 | Overnarrating | `[over_narrating]` | Negative | Robotic framing ("Since you…", "Based on…") |
| 🎯 | Showing Off | `[showing_off]` | Negative | Unnecessary precision (names, dates, addresses) |
| 🚩 | Offensiveness | `[offensive_p13n]` | Negative | Intrusive, creepy, or insulting use of data |

**Overlap is common** — tag ALL that apply, write a separate rubric for each.

### Common Combos
- 🤪 Forced Connection → 🌀 Tunnel Vision (irrelevant fact derails whole response)
- 🎯 Showing Off → 🚩 Offensiveness (precise data feels invasive)
- 🤖 Overnarrating can be an aspect of anything

---

## Step 1: Get Set Up

- Sign in with personal Google account (neuracolor@gmail.com)
- Settings → Personal Intelligence → Turn on: Past Gemini chats
- Apps → Turn on: Google Workspace, Google Photos, YouTube, Search Services
- Verify both models visible:
  - **PContext mode 33 Marshall - Gordon**
  - **PContext mode 33 Marshall - Percy**
- Models are in a nested list (click ">" beside model name)

---

## Step 2: Send Marshall - Gordon Prompts to Trigger Failure

- Use **PContext mode 33 Marshall - Gordon**
- Send prompts in assigned category: **Discovery & Recommendations**
- **Target ONLY Gemini conversation history** — do NOT target Gmail, Photos, YouTube, or Search data
- 1-5 turn conversations
- **Stop IMMEDIATELY when a failure occurs** (failure must be the LAST response)
- If 5 turns with no failure → delete conversation, try again with adjusted strategy
- If 10 conversation attempts with no failure → stop and work on another project
- Try to target a different loss category each task
- Write **longer, more complex prompts** — not one-sentence queries
- Write natural, human-sounding prompts

### Prompt Variation Guidelines
- Vary length & detail (minimal prompts AND multi-part requests)
- Test conversational follow-ups (up to 5 turns)
- Vary style, structure, content (formal, casual, slang, abbreviations, emojis, typos)
- Include vague prompts, list-based prompts, prompts referencing internal resources

### Only Log Prompts When:
1. You are CERTAIN of the intended behavior (should/shouldn't personalize)
2. The prompt matches your assigned category
3. **Do not submit ambiguous cases!**

### After Getting Failure:
- Select "I got a failure and am ready to log it"

### Verify the Model (Gordon)
- Confirm: PContext mode 33 Marshall - Gordon
- Check attestation box (wrong model = removed from ALL Metis projects)
- Copy Model ID from Debug Info: expect `pcontext_0p_otf_rev23_v12p2_sep_ledger_beyond`
- Select total number of turns (1-5)

### Extract Debug Info (Gordon)
**User Profile (sian_profile):**
- In Debug Info, search for "sian_profile"
- Copy text between quotation marks after "text:" just below "sian_profile"
- Do NOT include "sources" below it or anything above it

**Correction Ledger:**
- In Debug Info, search for "correction_ledger_from_bard_conversations"
- Copy text between quotation marks after "text:" just below it
- Same rules — only the text between quotes

### Share Link + HTML (Gordon)
1. Find conversation in left panel
2. Click three-dot menu → "Share conversation" → create public link
3. Paste share link into DA form
4. Open share link in **Incognito window** (NOT signed in!)
5. Right-click → Save As → "Webpage, complete" → save HTML
6. Upload HTML to DA form
7. Verify HTML is functional before continuing

**If Share Link fails (Workspace issue):**
- Save Debug Info first
- Start new chat without Workspace, send random prompt, create share link
- Open it, find original conversation in left panel
- Three dots → share should now work

**If still fails (HTML fallback):**
- Open conversation, collapse sidebar, refresh (removes Debug Info)
- Note account email + name from profile icon
- Save As HTML
- Find/replace email with "email" and name with "name" in text editor
- Upload edited HTML, note in comments

**Known Issues:**
- "Star" may show instead of Gemini responses
- "Sensitive query" may show instead of prompts → enter missing content in comments
- Images won't show in HTML → describe in comments

---

## Step 3: Rate Marshall - Gordon's Response

**⚠️ Multi-turn: only rate the FINAL response (the one with the failure)**

**Reference Sources for Rating:**
- User Profile (sian_profile)
- PContext Tool output (if triggered — search for "personal_context.retrieve_personal_data" in "code_response")
- Correction Ledger (correction_ledger_from_bard_conversations)
- Recent Chat Summary (summary_of_recent_bard_conversations)

**All facts in these sources are considered accurate even if they conflict with real facts.**

### Overall Personalization Quality
- If you triggered a failure → should NOT be "Very Satisfied" or "Somewhat Satisfied"
- If satisfied → restart and try different prompt

### Sub-Ratings (each 5-point scale):
1. **Writing Style / Tone** — well written, conversational, engaging prose?
2. **Contextual Awareness** — remembers/builds on previous turns?
3. **Content Relevance** — relevant to accomplishing user goal?
4. **Content Completeness** — enough information and detail?
5. **Truthfulness** — accurate based on real-world knowledge?
6. **Instruction Following** — followed all instructions given?

### Overall Quality Rationale
- ~5 sentences, specific details
- Reference specific turn numbers: [Turn 1], [Turn 2], etc.
- For dissatisfied: explain specifically what was wrong + what model should have done instead
- Generic rationales → removal from projects

### Trust Damage
- "Was your personal info used, or not used, in a way that damaged your trust in the bot's ability to be helpful?" → Yes/No

### After Rating: DELETE the Gordon conversation

---

## Step 4: Have Same Conversation with Marshall - Percy

- Start new chat → select **PContext mode 33 Marshall - Percy**
- Use **same first prompt** as Gordon
- Multi-turn: use same prompts for remaining turns when sensible; adjust if nonsensical while keeping same user goal
- **No need to trigger a failure** — ignore any interim failures
- Continue until same requests fulfilled (max 5 turns)

### Verify the Model (Percy)
- Confirm: PContext mode 33 Marshall - Percy
- Attestation checkbox
- Model ID: expect `pcontext_0p_otf_rev23_v12p2_cogen_beyond`
- Number of turns (should match Gordon)

### Extract Debug Info (Percy)
- Same as Gordon: sian_profile text + correction_ledger text

### Share Link + HTML (Percy)
- Same process as Gordon

---

## Step 5: Write Rubrics

**For each failure type found in Gordon's response, write:**

### Negative Rubric (Forced Connection, Overnarrating, Showing Off, Offensiveness)
- Format: "The response must NOT [specific thing]"
- Tag at end: `[forced_connection]`, `[over_narrating]`, `[showing_off]`, `[offensive_p13n]`

### Positive Rubric (Tunnel Vision only)
- Format: "The response MUST [do specific alternative]"
- Tag at end: `[tunnel_vision]`

### Rationale
- Explain WHY this is a problem
- Be specific about what data was misused and why it's inappropriate in context

---

## Final Steps

- Delete ALL eval conversations from Gemini after saving/verifying HTML files
- Confirm deletion checkbox
- Optional comments box for reviewers
- Submit

---

## Example Prompts (Discovery & Recommendations)

### Explicit:
- Find a wall mount for the air monitor I have at home
- Suggest a new outfit for me based on my style preferences
- What should I get Emma for her birthday?
- What movie should I watch tonight based on my taste?
- Suggest a playlist for my morning run based on my music taste
- Suggest a book I would enjoy reading next
- Where should I go on vacation this summer based on my preferences?
- Suggest a restaurant for tonight based on my tastes
- Suggest something fun to do this weekend based on my interests
- What's a new career I can pivot into?
- What course should I take next based on my career goals?
- Suggest a new wellness activity based on my fitness level and goals
- Give me a recipe idea I would enjoy based on my diet
- Suggest a new hobby I'd enjoy based on what I'm into
- Recommend an investment account based on my risk tolerance and goals

### Implicit:
- What are the best wall mounts for air quality monitors?
- What are trending outfit ideas for spring?
- What are some thoughtful birthday gift ideas for a close friend?
- What are some good movies to watch tonight?
- What are some good songs for a morning run?
- What are some popular books right now?
- What are the best summer vacation destinations?
- What are some good restaurants nearby?
- What are some fun weekend activities?
- What are good careers to transition into from marketing?
- What are the best online courses for career growth?
- What are some good wellness activities for beginners?
- What are some easy dinner recipes?
- What are some popular hobbies to try?
- What are the best investment accounts to open right now?

---

## Key Worker Intel (from Comments)

- **ManuelA:** Gordon only accesses Gemini chat history. Prompts must be baited to trap the model. Look through chat history for subjects that could fail.
- **ManuelA:** Task can expire "due to inactivity" even with "I'm working on this" clicked — was inactive on DA tab while on Gemini tab for ~45 min.
- **Multiple workers:** Struggling to get over-personalization failures — model rarely personalizes, and when it does it's "just the right amount."
- **Jennifer P:** Gordon not generating correction_ledger section — may need to put N/A.
- **Heaven H:** Got kicked for inactivity while trying to get failures despite clicking the button.
- **LoganW:** Debug broke on second model — first prompt had sian section but second didn't.
