# Koji - Pro API (G-113b)

## 🕒 Baseline Parameters
- **Pay Rate:** $29/hr
- **Expected Duration:** 3-6 hours per task
- **Goal:** Write enterprise-level APIs & rate model responses
- **Interaction Type:** Single-turn only (no chatbot/follow-ups)
- **Desired Outcome:** FORCE MODEL FAILURE. Both models **must** score "Okay" or worse.

## 🚨 Critical Constraints (Project Updates & FAQs)
- **NO NAMES:** Do not name the model in the System Instructions (e.g., never say "You are AstroBot").
- **NO REAL/SILLY COMPANIES:** Use completely fake but realistic-sounding company names. No "Google", no "Company ABC", no "Nunya Business Corp."
- **NO MARKDOWN:** Avoid markdown in System Instructions and User Data. It makes it look AI-generated.
- **ROOT XML:** All XML tags generated must be enclosed in a master root tag (e.g., `<doc> ... </doc>`).
- **NO INTERNET/TOOLS:** Text-only. The model cannot search the web, run code, or view images.
- **NO CURRENT DATE/TIME:** The model doesn't know the date. If needed, hardcode it into User Input Data.
- **NO REUSING S.I.:** You cannot reuse System Instructions from previous tasks, except for the introductory company context.
- **HELPER LIMIT:** You cannot copy-paste the "Helper" output. It must make up **less than 40%** of your System Instructions.

## 📋 The 5-Step Execution Flow

### STEP 1: Domain & Use Case
- Keep it a realistic use case (e.g., "Identify and highlight complex medical terms").

### STEP 2: Write System Instructions (S.I.)
*Must be long, complex, and professional. Must include:*
1. **1 paragraph** describing the context (company/situation). Must actually be context, not disguised instructions.
2. **2+ paragraphs** of actual instructions.
3. Instructions on **output format**.
4. **PLUS 2+ EXTRA FEATURES** from this list:
   - Classification system/decision matrix for multiple inputs.
   - 4+ unique types of XML tags.
   - Notes on model thought process.
   - 6+ highly emphatic "must do" / "must avoid" comments.
   - Subtly contradicting instructions.
   - 8+ self-contained info list items (MUST contain FULL TEXT of the reference, not just a link).
   - 4+ paragraphs on handling edge-case situations.

### STEP 3: Write Input Template
- Set placeholders for the data (e.g., `Name: [NAME]`). 
- Can have multiple templates combined in one box.

### STEP 4: Write User Input Data
- Provide the actual text/data for the template.
- Can use multiple copies of the template (e.g., supply 15 medical records) to increase difficulty.
- Length is unlimited but avoid breaking the token context limit.

### STEP 5: Generate & Rate Responses
- **BOTH MODELS MUST FAIL.** If a model scores "Pretty Good" or "Amazing," the task is too easy. You must go back and make the User Input Data harder.
- Grade strictly against your own System Instructions. If your S.I. didn't forbid it, don't penalize the model for doing it.
- You must provide specific text examples from the model's output in your rationale. No generic statements.
