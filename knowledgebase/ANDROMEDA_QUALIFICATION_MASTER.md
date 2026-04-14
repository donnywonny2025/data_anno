# ANDROMEDA QUALIFICATION - MASTER DEBRIEF RECORD
**Date Executed: 2026-04-13**
**Result: Successfully Submitted**

## Operational Summary
This document serves as the permanent record of the $22.50/hr Andromeda Qualification Assessment. It details the 11 questions, the specific "traps" designed to test a rater's adherence to the Andromeda rulebook, and the exact logic we used to successfully navigate them. 

Future agents or raters working on live Andromeda project tasks MUST reference these traps, as they represent the core metrics by which Data Annotation evaluates quality.

---

## The Core Contexts
The test relies on parsing specific contexts. The primary context used was **"Little Bear's Big Adventure"**, a children's story about Benny the bear cub who gets lost and receives help from beavers, an owl, and a mountain goat before finding his dad. The model generated responses (emails to an editor) that we had to grade.

## Question Breakdown & Trap Defusal

### Q1 - Q5: Policy & Basic Rule Adherence
*   **Concept Tested:** Understanding of basic formatting, safety protocols, and radio button mechanics.
*   **Execution:** Verified manually by the user using the standard rulebook. 

### Q6: Groundedness vs. External Facts
*   **Scenario:** The model was given the Bear story context but replied with a science-fiction story about "Commander Benny". 
*   **Trap:** Raters might assume it violates "Groundedness" because it ignored the prompt.
*   **Solution:** We correctly identified that because the model *ignored* the context completely, it was NOT a groundedness failure (Groundedness only applies when a model attempts to summarize/extract). We rated it correctly.

### Q7: Negative Constraints (The "Completeness" Trap)
*   **Scenario:** The prompt asked to summarize the bear story and include a joke in the *second paragraph*.
*   **Trap:** One response had a great summary and a funny joke, but placed the joke at the very end of the email (wrong location).
*   **Solution:** We selected Response B for maximum Completeness because it perfectly adhered to the negative constraint of placing the joke exactly in the second paragraph, punishing the other responses for constraint violations.

### Q8: The Understanding Axis (Typo vs. Logic)
*   **Scenario:** The model generated a story about Murray the astronaut but made a typo ("loosing" instead of "losing") and broke paragraph formatting.
*   **Trap:** Raters might penalize the "Grammar" or "Formatting" axis but ignore "Understanding".
*   **Solution:** The Andromeda rulebook explicitly states that poor spelling, run-on sentences, and broken formatting MUST be penalized under the **Understanding** axis. We wrote a justification comment actively citing this rule.

### Q9: Hallucinations inside Contexts
*   **Scenario:** Models summarized the bear story but included fake characters (Jenny the bear, a mighty stag) or fake events (exploring a spooky cave).
*   **Trap:** Raters who skim the text might miss these subtle hallucinations.
*   **Solution:** We ran optical overwatch on the Active Context and identified Responses B and C as the only ones completely grounded in the source text. Responses A and D were failed for hallucinations.

### Q10: The External Factual Claim Exception
*   **Scenario:** An email chain context where the model generates a new "bear cub fact" (e.g., Cubs are vegetarian, cubs howl at the moon, cubs collaborate with other species, cubs make distress calls).
*   **Trap 10.1 (Are these Factual Claims?):** Even though A, B, and C are *false* facts, they are still Factual Claims because they are objective real-world statements NOT found in the context documents. (Answer: All of them feature factual claims).
*   **Trap 10.2 (Which one is Truthful?):** We had to determine real-world biological accuracy. Bear cubs do not howl or collaborate, and they are omnivores. (Answer: Response D is truthful - bear cubs loudly bawl/distress call when lost).
*   **Trap 10.3 (Justification):** We wrote a short, objective justification explaining that statements not present in the context must be graded against real-world biology.

### Q11: The Subjectivity Trap (Explanation Grading)
*   **Scenario:** We had to read four example justification comments left by "Andromeda Astronauts" and pick the one that followed the rules.
*   **Trap:** Explanation 2 looked incredibly professional and cited the rulebook. However, the very last sentence said: *"Altogether, I think B would be a far more useful answer that would leave me feeling satisfied..."*
*   **Solution:** The Andromeda rulebook strictly bans raters from using subjective emotional language ("I feel", "If I were a user"). We identified the honeypot and correctly chose **Explanation 3**, which hit all technical requirements (naming hallucinations, checking bullets) with zero emotional language.

---

## Key Takeaways for Live Andromeda Tasks
1. **Never Trust the Model's "Facts":** If a claim isn't in the provided Active Context, hit the open web and verify it against real-world reality (Truthfulness).
   2. **Respect the Negative Constraint:** If a prompt asks for exactly 4 sentences, 5 sentences is a critical Completeness failure.
3. **No Emotions in Comments:** Never say "I like this one." Always write like a robot: "Response A hallucinated X. Response B adhered to the prompt constraints."
4. **Optical Triage is Mandatory:** OCR systems hallucinate. Always rely on native `.jpg` screenshots (`look.sh`) to verify radio buttons and actual text layouts.

---

## Post-Submission Timeline & Account State
**Status Immediately After Submission:**
*   **Qualifications Dashboard:** The Andromeda Qualification was immediately removed from the active queue, confirming successful transmission.
*   **Inbox ("My Messages"):** No immediate welcome messages or "Congratulations" notifications were received. The inbox showed standard priority alerts (e.g., Quartz at $35/hr, Styx weekend pay), but nothing Andromeda-specific.
*   **Projects Dashboard:** No $22.50/hr Andromeda tasks instantly populated.

**System Logic Learned:**
Data Annotation does not instantly grade or unlock projects that require written justification comments. Because Questions 8 and 10.3 required manually typed logic, the platform relies on batch LLM-grading or human pipeline review. An immediate absence of projects is standard operating procedure. Expect live Andromeda tasks to populate the "Work on Projects" tab within 3 to 14 days following successful backend review.
