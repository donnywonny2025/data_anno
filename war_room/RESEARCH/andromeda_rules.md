# 🌌 Andromeda Project Family Rules

## 1. Context Typology
- **Active Context**: The file/workspace the user is currently working on.
- **Mentioned Context**: Specific file/URL referenced by the user in the Prompt.
- **Context Source(s)**: Files the model retrieves to help it (corroborating info).
- **Citations**: Direct links (e.g. `[1]`) referring to specific locations in the context sources.
- **Search Results**: Web results retrieved by the model. 

## 2. Rule of Relevance
- **Empty Context**: If all context is empty, Groundedness = **N/A**.
- **Irrelevance Rule**: If *all* context is entirely irrelevant, Groundedness = **N/A**. But if even *one* piece of context is relevant, you MUST rate Groundedness holistically using that one piece.
- **Prompt as Context**: Prompts are NEVER context *unless* the prompt acts as "active context" (e.g., text to be refined) or contains explicit "mentioned context".

## 3. Rating Axes
### Completeness (Instruction Following)
- Did it fully deliver on the prompt? 
- It does **NOT** mean it used all provided context. A model can use 2 out of 5 files and be 100% complete.
- Vagueness is usually a Completeness issue.

### Understanding (Readability)
- Is it easy to read, well-formatted, devoid of verbosity or digression?
- Markdown syntax errors (broken bolding/lists) = **Understanding issue**.

### Groundedness (Internal Accuracy)
- Is the content supported by or consistent with the provided context?
- Leaving out context info is *not* a Groundedness issue unless the omission distorts the original claim.
- **Creative Additions vs Hallucinations**: Extra content is considered a "creative addition" (Completely Grounded) IF it represents a reasonable assumption that fulfills the prompt's intent (like adding a greeting to an email). If it invents unprompted exact figures/facts, it is a hallucination (Ungrounded).

### Truthfulness (External Accuracy)
- Evaluates the accuracy of **Factual Claims** in the real world via standard search engine research (max 15 mins).
- **THE GOLDEN RULE:** Only evaluate Truthfulness for facts that are *independent* of the provided context. If a claim is both factual and context-based, evaluate it on Groundedness and **IGNORE** it for Truthfulness.

### Overall & SxS
- If *any* axis has an issue, Overall cannot be "Amazing".
- SxS must be logically consistent with Overall Quality ratings (e.g. if A is Amazing and B is Pretty Good, SxS must show directional preference for A).

## 4. Punts vs Refusals
- A **punt** fails to answer in a meaningful way (e.g. "I can't find info", or "ErrorRequestCode" or "I am just a language model").
- A safety refusal ("I can't build a bomb") is **NOT** a punt. 
- If a response is a true punt, the ratings default to: Completeness = `Incomplete`, Understanding = `Not understandable`, Groundedness = `Not grounded`, Truthfulness = `N/A`, Overall = `Horrible`.

## 5. PII Traps
- **Context PII**: Tasks containing private SSNs, bank info, or visible faces of non-public figures in the context must be marked **Unratable**. 
- AI identifying public figures is fine. 
- **AI-generated faces do NOT count as PII.**
