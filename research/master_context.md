# 🧠 MASTER CONTEXT: Zero-Detection Stealth Agent
> **Location:** `/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION`
> **Project Goal:** Build a browser-based presence indistinguishable from a human at every technical and behavioral layer.

## 1. The Core Architecture (The "Full Stack")
To be truly undetectable, the agent must pass as human across four independent domains:

### A. The Browser Domain (Surface Fingerprinting)
*   **The Engine:** **Camoufox** (Firefox-based).
*   **Why:** It patches fingerprints at the C++ level (WebGL, Canvas, AudioContext, Screen Resolution) rather than using detectable JavaScript "stealth" patches.
*   **Goal:** Pass the "WebDriver" check and have a consistent hardware signature.

### B. The Network Domain (Origin Integrity)
*   **The Gear:** **Rotating Residential Proxies** (Sticky Sessions).
*   **Why:** Data Center IPs (AWS/Google) are a bot death sentence. We must appear to be coming from a standard home ISP (AT&T/Comcast).
*   **The Gap:** IP-Timezone alignment. The browser clock must match the Proxy location perfectly.

### C. The Behavioral Domain (Dynamic Motion)
*   **The Hand:** **OS-Level HID Injection.**
*   **Why:** Web-level automation (Playwright/Puppeteer) leaves traces. OS-level signals (Quartz on Mac) appear as legitimate physical input.
*   **The Logic:** **Gaussian Typing** (human-like rhythm flaws) and **Bezier Mouse Paths** (natural non-linear acceleration).

### D. The Identity Domain (The "Resident" Pattern)
*   **Persistent Profiles:** We don't use "Guest" modes. We maintain cookies, cache, and localStorage for weeks.
*   **The Gap:** **"Warm-up" cycles.** A real account has a history. The agent should occasionally perform "human-like" fluff tasks (reading unrelated pages) to build a credible session history.

---

## 2. Bridging the Gaps (The "Invisible" Extras)

### Gap 1: Visual Interaction (Vision-based Browsing)
Standard bots move based on element IDs (DOM). Advanced detection monitors **"Hover Patterns."** 
*   **The Solution:** The agent should use a "Vision Model" (like GPT-4o-Vision) to "look" at the screen and decide where to move the mouse based on visual layout, not code selectors.

### Gap 2: Natural Drafting Rhythms
Humans don't just "type." They pause to think, they highlight text they just wrote, they delete a word and re-type it.
*   **The Solution:** Implement a **"Drafting Cycle"** where the AI writes in bursts, pauses to "read," and simulates minor edits before submission.

### Gap 4: CAPTCHA Evasion (Seamless Handhelds)
Advanced sites will still trigger CAPTCHAs if they see "suspiciously perfect" behavior. 
*   **The Solution:** Use an API like **2Captcha** or **CapSolver** integrated directly into the browser automation. The agent should pause, send the CAPTCHA for solving, and then resume once the "I am human" check is satisfied, all without breaking the stealth session.

---

## 3. The Test Suite (Success Metrics)
Before any mission, the agent must pass:
1.  **SannySoft:** 100% green on JS markers.
2.  **PixelScan:** 100% "Consistent" score on IP/UA/Hardware.
3.  **CreepJS:** High trust score (no "Lies" detected in the fingerprint).

---

## 4. The Stealth Co-Pilot (Human-in-the-Loop)
This system is **NOT** a fully autonomous bot. It is a **Hybrid Intelligence System** where the human and AI work in parallel.

### A. Division of Labor
*   **The AI's Job:** Stealthy execution, data retrieval, and generating draft responses. It maintains the "Invisible Presence" (Camoufox, Resident Profile, Gaussian Typing).
*   **The Human's Job:** Strategic monitoring, CAPTCHA solving, "Logic Verification," and final submission.
*   **The Integration:** The AI runs in a "Ghost Mode"—performing the work under the human's supervision. If a manual check is required, the human simply takes over the inputs.

### B. The Tactical Advantage
Because there is a human "in the mix," we don't need to over-engineer 100% autonomous CAPTCHA solvers. The human handles the "Red Flags" manually, which is the most undetectable way to bypass high-level security. 

---

## 5. Immediate Roadmap (For Future Antigravity)
1.  **Prototype `ghost_typer.py`**: A local relay that can type sentences from a clipboard into a focused window with human delays.
2.  **Integrate Camoufox**: Set up a persistent "Human Profile" that matches our physical location.
3.  **HITL Dashboard**: Design a simple overlay/terminal where the human can "Approve" or "Intervene" in the AI's actions.
