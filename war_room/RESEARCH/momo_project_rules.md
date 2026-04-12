# Momo Task Instructions (Raw Copy)

## Updates
Before You Start
⚠️ PII is the #1 cause of rejected submissions. Fully anonymize all personal information before submitting.
Don't rely solely on the Anonymizer tool — re-read your anonymized text
Watch for word mix-ups (e.g., "Will" the name vs. "will" the verb)
If using multiple documents, anonymize them together (see PII Anonymization section)

20th March
If you are low on time, you can create a lightweight (5 criteria) rubric instead of a comprehensive rubric -- we expect this will reduce the total task time significantly!

19th March
The most important part of this task is making sure your context and prompts are aligned with the goals of this project. Take your time to read the instructions and understand the project.
Your prompts should target the model's ability to reason about the context, not its internal knowledge, simple instruction following, or intuition about things not contained in the context

The errors we want are:
Grounding errors: the model attempts to use the context but cites or presents the wrong information
Logical errors: the model attempts to infer, deduce, or derive information using the context but gives logically unsound explanations or incorrect conclusions

## Your task: 
Have a conversation with the AI about context that you paste in to the chat (1–6 turns).
You can choose from various context types -- check out kinds of context you can use below!
Focus on finding gaps in the model's reasoning capability in dealing with very long context.
Stop as soon as the model makes a reasoning error.
Then write a rubric for that turn.

## What We're Looking For
We want errors that come from how the model uses and understands the context — not from confusing prompts, complex instructions, or the model's general knowledge.
You will create challenging user prompts that test how well AI models reason about the context you provide.
Your goal is to produce tasks where the model makes reasoning errors — failures in logic, deduction, inference, calculation, or application of rules found in the document.
Every submitted task must contain a major reasoning failure on the final turn. The reasoning errors should be based on assessing the long context sent with your first prompt.

**Good errors to catch:**
- Misreads the document
- Misses relevant info
- Flawed reasoning about the document
- Loses track across turns
- Grounding error
- Synthesis failure
- Logical error

**What we do NOT want:**
Generic failures such as wrong language, surface-level factual recall errors, formatting issues, or purely instruction-following mistakes are not targeted failures.
We don't want artificially complex prompts that have several contrived instructions. 

## Context Requirements
- Select one or more documents that are at least 8,000 tokens IN TOTAL.
- Maximum total token count 100,000.
- Context documents must be real text from your everyday life that isn't publicly available online (Messaging apps, group chats, personal archives).
- Your documents must be included in your first turn user prompt, directly above your question/request with a `<|TASK|>` tag.

## Rubric
Write a rubric for the failure turn only. For each criterion (up to 40, but lightweight = 5), specify:
- Criterion text — "The response should…"
- Necessity — Explicit or Implicit
- Type — Objective or Subjective
- Priority — Must Have or Nice to Have
- Dimension — which of the 10 rating axes it maps to
- Response Criterion Rating — No Issues / Minor Issues / Major Issues
