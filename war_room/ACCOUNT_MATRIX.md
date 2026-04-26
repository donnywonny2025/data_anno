# Data Annotation: Account Matrix

This document tracks the specific roles, qualifications, and API statuses of every email identity used within the Data Annotation (DA) ecosystem. DA actively monitors IP addresses and account linkages, so maintaining strict operational boundaries between these accounts is critical for account safety.

## 1. Primary Profile (The Master Account)
**Email:** `jefferykerr@gmail.com`
**Role:** Official Platform Identity & Financial Hub
**Guidelines:**
- This is the account tied to PayPal payouts and official platform communications.
- **MUST** be used for all legal consent forms, NDAs (e.g., Kardia, Demeter), and official tax/identity verification.
- **DO NOT** opt this account into experimental beta features (like Workspace Labs) unless explicitly required, to keep the core inbox clean.

## 2. Primary Testing Dummy
**Email:** `neuracolor@gmail.com`
**Role:** General Qualification & Task Testing
**Guidelines:**
- Used for general UI/UX testing, chatbot interactions, and filling out demographic/software surveys.
- **Opt-in Status:** Workspace Labs/Experiments Enabled.
- **Usage:** If a task asks "Do you have access to Google Workspace / Gemini," use this account to test the features without cluttering your personal inbox.

## 3. Isolated API Monitor (The Air-Gap)
**Email:** `seramusic2025@gmail.com`
**Role:** Automated Inbox Scraping & Pegasus Qualification
**Guidelines:**
- **Opt-in Status:** Workspace Labs/Experiments Enabled.
- **Google Cloud Project:** "DA Monitor Sera" (Project ID: `647429654790`). This is a completely isolated GCP project to prevent cross-contamination with the main JefferyKerr developer profile.
- **API Status:** Gmail API Enabled (Readonly & Compose scopes).
- **Execution:** Used strictly by the `execution/da_monitor.py` script. The script dynamically loads `credentials_seramusic.json` to scrape this inbox for high-priority DA project alerts without touching any other accounts.

---

### Operational Rules for API Testing

1. **Never Push Credentials:** All `credentials_*.json` and `token_*.json` files are strictly local and ignored by `.gitignore`.
2. **Token Lifecycle:** If a token expires or encounters a `403` error, simply delete `token_seramusic.json` and run the script again to trigger a fresh OAuth flow.
3. **The Buffer:** `war_room/DATA_DROP.md` is the designated copy-paste zone for moving data between the DA interface and the AI assistant.
