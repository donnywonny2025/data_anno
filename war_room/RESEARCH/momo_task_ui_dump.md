# Momo Task UI - Full Text Dump (Mar 23, 2026)

## PII and Location Restrictions
MMPORTANT: In this task, the context documents you will use may include data that Contains Personally Identifiable Information (PII)
Note that we DO NOT want your personal or sensitive information! It's contexts that occur in private settings that the model is learning from, not your personal data!

We will ask you to anonymize or omit such information from the context. If the context cannot be reasonably treated, do not submit it.
Example documents include: private group chats, financial documents, meeting transcripts.
DO NOT use context that includes medical data or PII/personal information about minors.

To work on this project, you MUST be located/reside in the US and NOT within any of the ineligible states/cities.
Ineligible states: Washington, Texas, Illinois
Ineligible cities: Portland, OR

Before proceeding, please read the linked consent form.

## Escape Hatch Guidelines
If one or more of the models do not respond after 5-10 minutes, are cut short, produce an error message, or respond in a language other than English, please first:
- Click on the "Model Unresponsive" button. If that doesn't produce a response after several minutes:
- Click on the "Stop Model Response" button, then "Undo Last Prompt"
- Resubmit your prompt to the models.
If none of the above works, check the box below and submit. "I can't finish this task".

**FAQ:**
- **The escape hatch is telling me I have zero turns, how can I submit?** This happens when there is a prompt submitted or if the complete escape hatch questions are not completed. Please use the "undo prompt" button, check the escape hatch checkbox, and answer the free text question which appears.
- **I'm trying to move to turn 2, I'm getting an error message about 8000 tokens, but I put my context document in the token check?** The system checks if the actual user prompt submitted matches the requirement. You need to copy/paste your context document into your first turn user prompt.
- **Where do I upload my document?** This project does not support uploading separate documents as the model is text only. All context documents MUST be pasted into the first message of the conversation, above your user prompt.

## Category Info
Category: 💬 Interpersonal Interaction
Subcategory: 📄 Private Chat

## Workflow Steps

### Step 1: Select and Anonymize Documents
Choose between 1-5 documents or excerpts.
The Personally Identifiable Information (PII) in your documents must be anonymized before the documents are used.

### Step 2: Paste into Document List
For each document you use, copy-paste the entire selected text into the corresponding Document Text box in the Document List.
If you want to use more than one document, click the + button in the Document List.
🚨 Do this before you write your question prompt.
Once you have pasted all your documents, click the Estimate Tokens button.
If your combined token total is less than 8,000, you should find more/longer documents to use. Do not exceed 100,000 tokens.

### Step 3: Write Prompt
Draft a question related to the documents. In your final turn, the prompt should be challenging and aim to result in major reasoning issues in the model's response.
In turn 1, use the Copy Context Document buttons from the Token Count section to add your context into your prompt.
In turn 1, ensure your question is separated from the context documents by a `<|TASK|>` tag in your prompt.
In the final round of your conversation, your prompt must cause a major model error in at least one of the following categories: Truthfulness, Instruction Following, Contextual Understanding, Turn Memory, Information Localization, Relational Understanding, or Temporal Reasoning.

## Anonymization Tools
- **Mapping Tool:** Click Map PII to generate an initial mapping for the PII in your pasted text. Any PII that is flagged as 'Medium' or 'Low' confidence will need to be manually reviewed.
- **AI Helper:** Assesses Mapped PII and flags missing PII.
- **Anonymizer Tool:** Use the button to help anonymize your document using the final mapping. Check for unwanted substitutions.

## Quality Dimensions

1. **Instruction Following (Explicit)**
2. **Contextual Understanding (Implicit Instruction Following)**
3. **Turn Memory (Multi-turn Instruction Following)**
4. **Truthfulness / Correctness**
5. **Temporal Reasoning**
6. **Relational Reasoning**
7. **Information Localization**
8. **Comprehensiveness / Depth**
9. **Verbosity / Conciseness / Relevance**
10. **Writing Style & Tone**

## Final Review / Rubric
If there is a major error, tell us what went wrong and why it is wrong. If there are no issues in this round, tell us why the model's response is fine.
- Be 2-5+ sentences long, aim for a good rationale with proper grammar and structure.
- Be self-contained.
- DO NOT MENTION the platform (DAT) or any of the instructions you've been given.

The Rubric questions will only display when the response has Instruction Following, Truthfulness, Turn Memory, Contextual Reasoning, Relational Reasoning, Temporal Reasoning, or Information Localization issues in the current round.

If the model makes no targeted reasoning errors, or only has Minor Issues in any objective axis, the response needs to be redone.
Check here if you completed a lightweight rubric (5 criteria) or a comprehensive rubric (up to 40 criteria).
