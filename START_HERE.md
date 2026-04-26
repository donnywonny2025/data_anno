# Data Annotation Strategic Operating Directive (START_HERE.md)

## 1. System Architecture & The "North Star" Protocol
- **Primary Visual Input:** The `./look.sh` script is the ONLY authorized method for visual observation. It captures raw macOS desktop pixels (Display 1: Acer, Display 2: LG TV).
- **Secondary Data Channel:** The Gmail API (`execution/da_monitor.py`) is authorized for polling structural invites.
- **BAN ON AUTOMATION:** You are explicitly FORBIDDEN from using `browser-harness`, `camoufox`, or any CDP-based browser automation on the Data Annotation domain. These are detectable and result in account termination.
- **Physical Orientation:**
  - Display 1 (Right): Primary Work Engine (Acer).
  - Display 2 (Left): HUD / Secondary Monitoring (LG TV).

## 2. Time Tracking & Billing (The "Iron Clock" Rule)
- All Data Annotation sessions must be tracked via `execution/da_time_tracker.py`.
- **Session State:** The current session is stored in `.tmp/da_session_timer.json`.
- **Manual Billing:** The user will manually enter hours into the platform. Your job is to provide the precise mathematical log from the tracker.

## 3. Communication Style
- **Concise & Tactical:** No fluff. Give the user the rule, the pay, and the vision analysis.
- **Demonstrate over Describe:** Use artifacts to show logs and screenshots.
- **Bypassing Hallucinations:** If a script fails or a vision capture is unclear, report the failure immediately. Never "guess" the state.

## 4. The Validation Loop Paradox
In the DA platform, front-end red error boxes (e.g., "This question is required") **do not** dynamically disappear when you check the missing box. The AI must explicitly remind the Operator to ignore hovering red errors and click "Submit" to trigger the re-validation script.

## 5. THE ANTI-HALLUCINATION VISUAL RULE (CRITICAL)
- **The Vision-First Rule (MANDATORY)**: Whenever you run `./look.sh`, you are strictly FORBIDDEN from relying on the `.txt` OCR dump for layout, color, or visual state. You MUST use your Vision Model to analyze the `.jpg` screenshot pixels from the **CURRENT** turn only.
- **The "Look" Command Definition**: When the user says "Look," they are commanding the AI to analyze the physical screen state in front of them *contextually*. The AI must prioritize the current screen pixels over all other data sources to describe the present moment. 
- If you describe an element that is not physically visible in the latest screenshot, it is a Tier 1 violation.
- If a visual capture is missing, blurry, or ambiguous, the AI MUST state: "I cannot see your screen" or "I am unsure of the visual content."
- **CONFIDENT INCORRECTNESS IS A BANNABLE FAILURE.** The AI must never "probabilistically guess" what a post or graphic contains based on URL patterns or partial metadata.
- The AI must always post the "Proof Screenshot" it is analyzing when giving high-stakes advice or rationales.

## 6. Current Project State
- **The Factuality Gateway:** Passed Achilles Factuality Onboarding.
- **Slack Hub:** Invite accepted.
- **Google Workspace:** `@aidatatrainer.com` profile active.
- **Demographic Filter:** User is NOT 18-35. User is NOT a student.

## 7. Active Directive (Live Task Execution)
- Current focus: Completing the mandatory dashboard migration (Onboarding Steps 1-3).
