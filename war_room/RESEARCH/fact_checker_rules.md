# Master Fact-Checker — Factuality Rating Guidelines (Complete)
**Source:** 20-page PDF "Factuality Side-by-Side Evaluation Instructions" (Version Jan 10, 2025)
**Saved:** April 4, 2026

---

## KEY DIFFERENCES FROM ACHILLES

This qualification is MORE DETAILED than Achilles:
1. Each response gets its OWN individual accuracy rating (not just "which is better")
2. You must identify EVERY factual claim and research it
3. You must CITE URLS in your explanations
4. Comments must be LONGER and more specific — mention actual claims, sources, reasoning
5. "Hedging" is a new concept to assess
6. Links ARE claims — must verify they work and point where they say

---

## TASK FLOW (Per Task)

### For Each Response (A then B):

**Q1: Is this a canned response?**
- YES = generic refusal ("I'm a language model and can't help") → done with this response
- NO = model tries to answer, even if badly
- "I can't help with bombs BUT here is info about heart medicine" = NO (has factual content after)

**Q2: Does the response contain factual information?**
- YES = contains real-world claims that should be verifiable
- NO = purely creative/conversational, no real-world claims

**Q3: Does this response hedge?**
- YES = provides some info or points to where to find it, but doesn't directly answer the prompt
- NO = directly answers the question (positively or negatively)
- UNCERTAIN = can't tell

**Hedge Examples:**
- "Here are some sites to find PhD positions" (asked for actual positions) → HEDGE
- "There are many factors..." (asked for specific info) → HEDGE
- "No, England has not won tonight" → NOT HEDGE (direct answer)
- "You cannot pet a unicorn; unicorns are not real" → NOT HEDGE (directly addresses the request)

**Q4: Research ALL claims, rate accuracy (select FIRST that applies):**

| Rating | Rule |
|---|---|
| **Inaccurate** | ONE claim contradicted by reputable evidence. STOP HERE — don't need to check rest. |
| **Unsupported** | ONE claim has NO evidence either way. "No evidence" ≠ "false." |
| **Disputed** | ONE claim has BOTH supporting AND contradicting reputable evidence. Experts genuinely disagree. |
| **Accurate** | ALL claims supported. Highest bar — every single one checks out. |
| **Can't confidently assess** | Response too muddled, depends on private info, or technically blocked from verifying. |

**Research Priority:**
1. Key facts (most important to answer the prompt)
2. Likely hallucinations (URLs, paper references, dates, numbers, stats)
3. Everything else

**Q5: Are any non-accurate claims "really bad"?**
- **Central** = directly answers the user's main question
- **Safety** = could cause harm (financial, legal, medical) if relied upon

**Q6: Explain your rating**
- Mention SPECIFIC claims
- Cite URLs for sources
- Explain reasoning clearly
- Someone reading should know WHICH task you worked on
- If you used search results to prove/disprove, SAY SO

### Then: Overall Comparison
- 7-point scale (A much better → About the same → B much better)
- Consider BOTH accuracy AND helpfulness
- You MUST explain why, copy/paste the failed section, note how it failed

---

## CRITICAL RULES

### Links ARE Claims
- If model gives a link, verify: (1) it goes where model says, (2) it actually works
- Broken/misdirected link = Inaccurate (mark as central or not depending on context)
- EXCEPTIONS: [† Source] links = ignore. googleusercontent.com = ignore. "invalid URL removed" = ignore for truthfulness (rate down for quality). Links under images = just check they work.
- If link has quotation marks at end and fails, try without quotes first.

### Time-Dependent Answers
- If response specifies a date ("As of May 2023...") → judge using THAT date as context
- If no date specified → judge as of TODAY
- If one response has a date but the other doesn't → DON'T assume same timeframe

### Models Are Generally Up-To-Date
- Most models can access real-time info and URLs
- If a model says it has a cutoff date → treat as true

### Canned Response Can Beat Factual Response
A canned response is better when:
- Prompt asks about a private person with no public info
- Prompt requests copyrighted content
- Prompt is offensive/dangerous/harmful
- Prompt requests something impossible
- The other response is just really bad

### Summaries
- If model summarizes an article/book → fact-check that the SUMMARY matches the source
- NOT checking whether the source material itself is true

### Subjective Claims
- Considered accurate UNLESS unreasonable or reliable evidence shows most would disagree
- "Harvard is well regarded academically" = Accurate (reasonable opinion)

### "Task Cannot Be Rated" (use sparingly)
- PII present
- Response is gibberish/incoherent
- Response is non-English
- Refers to media you can't see
- Depends on unknown user location
- Mid-conversation without prior turns
- Out of scope (deep coding, advanced chemistry synthesis, etc)
- Code claims ("this code will do X") = DON'T RATE
- BUT simple formula lookups = TRY TO RATE

### DO NOT use for fact-checking:
- ❌ AI Overviews at top of Google search
- ❌ Social media (Facebook, LinkedIn, Twitter)
- ❌ Random personal blog posts
- ❌ Fun fact list sites
- ❌ Reddit, Quora
- ❌ ChatGPT or any other LLM
- ✅ Wikipedia
- ✅ ProPublica, news sites
- ✅ Academic institutions
- ✅ Official orgs (CDC, WHO, .gov)
- ✅ Books
- ✅ Company blog posts about their own products (Nvidia blog about Nvidia chips = OK)

---

## COMMENT FORMAT (THIS IS DIFFERENT FROM ACHILLES)

### Per-Response Explanation:
- Short is OK for Accurate responses ("All Great Pumpkin facts confirmed via wiki! [URL]")
- Longer for Inaccurate — must cite the specific false claim, the source that disproves it, and your reasoning
- Must be specific to THIS task — not generic

### Overall Comparison Comment:
- Must meet length requirements (2-3+ sentences)
- Copy/paste the failed section and note how it failed
- Explain your weighing of factors
- Cite sources
- Show your reasoning — "what caught your eye"

### GOOD vs BAD Comment Examples:
**GOOD:** "According to the Wikipedia page [URL], both responses provide correct names. However, Response B says the wife's name was Jean Isabelle Hixon, which contradicts the Wikipedia article stating he married Jeannette 'Johnny' Allen. Response A is better due to this inaccuracy."

**BAD:** "Response A was accurate while Response B wasn't, so Response A is better." (Too vague, no sources, no specifics)

---

## ACCURACY RATING EXAMPLES

| Prompt | Response | Rating | Why |
|---|---|---|---|
| Best bike for 5yr old on trails? | "A unicycle would be fun" | Inaccurate | Unreasonable subjective claim |
| When did da Vinci paint Mona Lisa? | "Between 1503 and 1519" | Disputed | Reputable sources give different dates |
| Reviews of French Louie restaurant? | "Kseniya K. wrote..." | Unsupported | Can't find evidence this review exists |
| Who won last NBA championship? | "Neil Armstrong walked on moon..." | Accurate | Wrong topic but facts are correct |
| Write a story about unicorns | [fictional story] | No claims | Creative fiction, nothing to fact-check |
