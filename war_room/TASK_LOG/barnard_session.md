# Barnard Task Session — April 29, 2026

## Timer
- **Task opened:** ~7:06 PM ET
- **DA Timer at last check:** 3h 24m remaining (expires ~11:00 PM ET)
- **Session start (discussion):** ~7:03 PM ET
- **User taking break:** ~7:39 PM ET

---

## Task Info
- **Project:** Barnard — Verify a golden solution to a research prompt: NO Rubrics, NO screen recording! (ID: 2)
- **Pay:** $29/hr
- **Research Prompt:** "Make a table of all guests of the No Priors podcast in 2025, their company name (if there is more than one company affiliation, only the first company named to introduce the guest), their last company valuation before December 31 2025, month and year of company founding, and total funds raised by December 31 2025."

---

## Task Layout (How It Works)
The task has TWO scrollable panels:

### LEFT SIDE (top to bottom):
1. **Research Prompt** — The original question
2. **Golden Solution (Updates as you work)** — LIVE rendered table preview
3. **Scratchpad (Updates as you work)** — LIVE rendered scratchpad preview
4. **Original Golden Solution and Scratchpad (Doesn't update)** — Frozen baseline for reference
5. **Accordion Sections 1/2/3** — Same as right side, expandable

### RIGHT SIDE (top to bottom):
1. **Section 1 — Finalized Items ✅** — 61 items list + editable golden solution markdown + editable scratchpad + summary box
2. **Section 2 — Candidates to Remove 🔴** — "No removal candidates" + editable golden solution markdown + editable scratchpad + summary box
3. **Section 3 — Candidates to Add 🟢** — 1 item (Shiv Rao) + editable golden solution markdown + editable scratchpad + summary box
4. **Section 4 — Final Check** — Final editable golden solution markdown + final editable scratchpad

### How Editing Works:
- You TYPE in the **right side** markdown text boxes
- The **left side** renders the result live as a formatted table
- Each section has its OWN editable copy of the golden solution and scratchpad
- The FINAL version is in Section 4's "Updated Golden Solution" and "Updated Scratchpad"

---

## Section Status

### Section 1: Finalized Items ✅ — NEEDS SKIM
- 61 items confirmed in both gold answer and model responses
- Just scan for value discrepancies (wrong price, wrong year)
- **Summary box:** Empty — needs to be filled

### Section 2: Candidates to Remove 🔴 — DONE (NO ACTION)
- **"No removal candidates."**
- **Summary box:** Empty — type "N/A"

### Section 3: Candidates to Add 🟢 — ONE ITEM
- **Shiv Rao** — search confirmed ✅
- CEO and Co-Founder of **Abridge** (AI healthcare documentation)
- Appeared on No Priors Episode 108, published **March 27, 2025**
- **Company data for table:**
  - Company: Abridge
  - Valuation before 12/31/2025: **$5.3B** (Series E, June 2025)
  - Founded: **2018**
  - Founding month: Not available
  - Total funds raised: **$778M**
- **Summary box:** Empty — describe what was added

### Section 4: Final Check — NOT YET
- Final review of golden solution + scratchpad
- Fix all errors found during review
- Verify markdown rendering on left side

---

## ⚠️ ERRORS FOUND IN GOLDEN SOLUTION (from Section 1 data in DATA_DROP)

### Critical Errors:
| # | Guest | Issue | Details | Fix |
|---|---|---|---|---|
| 37 | **Andrew Ng** | WRONG COMPANY | Listed as "Google DeepMind" ($650M, 2010). Andrew Ng is NOT DeepMind. He's DeepLearning.AI / Landing AI / Coursera. Google Brain ≠ DeepMind. | Change company to correct one. NEEDS RESEARCH on what company was used to introduce him on the podcast |
| 57/59 | **Anthropic** | VALUATION MISMATCH | Ben Mann (#57) shows **$380B**. Sholto Douglas (#59) shows **$183B**. Same company — can't be both. | Need to verify which valuation is correct for "before Dec 31, 2025" |
| 6 | **Kyle Vogt** | WRONG COMPANY/VALUATION | Listed as "Twitch, $15B". Kyle Vogt co-founded both Twitch AND Cruise. Twitch sold for ~$970M in 2014, not $15B. $15B was Cruise's valuation. | Need to verify which company was used to introduce him on podcast |

### Typos:
| # | Guest | Issue | Fix |
|---|---|---|---|
| 59 | **Sholto Dougla** | Missing 's' | → Sholto Douglas |
| 64 | **Eric Zelikma** | Missing 'n' | → Eric Zelikman |

### Suspicious Values:
| # | Guest | Issue | Details |
|---|---|---|---|
| 176 | **Zach Ziegler** | "$450" funds raised | Almost certainly a typo — should be $450M? Needs verification |
| 176 | **Zach Ziegler** | "Open Evidence" $6.1B | Daniel Nadler (#160) also listed under "OpenEvidence" with $12B — same company? Different valuations? |
| 58 | **Bryan Johnson** | All "Not available/applicable" | He's founder of Kernel ($50M+) and Blueprint. Scratchpad searched "living man don't die" which is his motto, not a company. Needs correction. |

### Items to Verify Later:
- **Edwin Chen — SurgeAI — $15B** — SurgeAI was acquired by Scale AI. The $15B might be Scale AI's valuation, not SurgeAI standalone.
- **Tony Zhao / Cheng Chi — Sunday Robotics** — Need to verify company name and data
- **Ben Spector / Asher Spector** — All "Not applicable" — need to verify if they have a company

---

## Golden Solution Data (from DATA_DROP)
All 61 entries were pasted into DATA_DROP by the user. The full table includes:
1. Erik Bernhardsson — Modal Labs — $1.1B — 2021 — $110M
2. Jesse Zhang — Decagon — $1.5B — 2023 — $231M
3. Bill Clerico — Convective Capital — Not available — 2022
4. Rick Caruso — Caruso — Not available — 1987
5. Winston Weinberg — Harvey — $8B — 2021 — $1B
6. Kyle Vogt — Twitch — $15B — 2006 — $35M ⚠️
7-8. Nima Alidoust & Johnny Yu — Vevo Therapeutics — $120M — 2022 — $42M
9-11. Patrick Hsu, Dave Burke, Hani Goodarzi — Arc Institute — Not applicable — 2021
12. Noubar Afeyan — Flagship Pioneering — $324M — 1999
13. Dan Hendrycks — Center for AI Safety — Not applicable — 2022
14. Thomas Dohmke — GitHub — $7.5B — 2007 Oct — $350M
15. Chelsea Finn — Physical Intelligence — $5.60B — 2024 — $1.07B
16. Brendan Foody — Mercor — $10B — 2023 — $486M
17. Josh Goldman — KoBold Metals — $2.96B — 2018 — $537M
18-20. Isa Fulford, Eric Mitchell, Brandon McKinzie — OpenAI — $500B — 2015 Dec — $40B
21. Luis von Ahn — Duolingo — $3.42B — 2011 — $183M
22. Arvind Jain — Glean — $7.2B — 2019 — $624.5M
23. Dr. Fei-Fei Li — World Labs — $1B — 2024 Jan — $230M
24. Ben Mann — Anthropic — $380B — 2021 — $6.98B ⚠️
25-26. Qasar Younis & Peter Ludwig — Applied Intuition — $6B — 2017 — $602M
27-28. Pushmeet Kohli & Matej Balog — Google DeepMind — $650M — 2010 Sep — $64.6M
29-30. Joshua Meier & Jack Dent — Chai Discovery — $1.3B — 2024 — $225M
31. Parker Conrad — Rippling — $16.8B — 2016 — $956.34M
32. Misha Laskin — ReflectionAI — $8B — 2024 — $130M
33. Edwin Chen — SurgeAI — $15B — 2021 — $1B ⚠️
34. Sriram Krishnan — White House Policy Advisor — Not applicable
35. Matthew Prince — Cloudflare — $68.83B — 2009 — $332M
36. Dylan Patel — SemiAnalysis — Not available
37. Andrew Ng — Google DeepMind — $650M — 2010 Sep — $64.6M ⚠️ WRONG
38. Jacob Helberg — Secretary of State — Not applicable
39. Daniel Nadler — OpenEvidence — $12B — 2021 — $700M
40. Jared Kushner — Affinity Partners — Not available — 2021 Jul
41. Joe Liemandt — Trilogy — Not available — 1989 — $7M
42. Nikesh Arora — Palo Alto Networks — $149.84B — 2005
43. Eric Zelikman — humans& — Not available — 2025 Sep ⚠️ TYPO
44. Zach Dell — Base Power — $4B — 2023 — $1.3B
45. Zach Lloyd — Warp — Not available — 2020 — $73M
46. Sridhar Ramaswamy — Snowflake — $93.13B — 2012 Jul
47. Sajith Wickramasekara — Benchling — $6.1B — 2012 — $412M
48-49. Tony Zhao & Cheng Chi — Sunday Robotics — Not available — $35M
50. Gabe Pereyra — Harvey — $8B — 2021 — $1B
51. Mati Staniszewski — ElevenLabs — $11B — 2022 — $281M
52. Jensen Huang — NVIDIA — $4.88T — 1993 Apr
53. Scott Wu — Cognition — $10.2B — 2023 — $696M
54. Raiza Martin — Huxe — Not available — 2024 — $4.6M
55. Zach Ziegler — Open Evidence — $6.1B — 2021 — $450 ⚠️ TYPO
56. Aaron Levie — Box — $5.02B — 2005
57. Noam Brown — OpenAI — $500B — 2015 Dec — $40B
58. Bryan Johnson — Not available ⚠️ MISSING DATA
59. Sholto Douglas — Anthropic — $183B — 2021 — $6.98B ⚠️ VALUATION MISMATCH
60-61. Ben Spector & Asher Spector — Not applicable

## ADDITION:
62. **Shiv Rao — Abridge — $5.3B — 2018 — Not available — $778M** (CONFIRMED)

---

## Next Steps (When User Returns)
1. [ ] User pastes the full "Updated Golden Solution" markdown from Section 4 into DATA_DROP
2. [ ] I fix all errors in the markdown and give corrected version back
3. [ ] Research the ambiguous items (Andrew Ng company, Kyle Vogt company, Anthropic valuation)
4. [ ] User pastes corrected markdown back into the DA task
5. [ ] Fill in all Summary boxes (Section 1, 2, 3)
6. [ ] Add Shiv Rao row to the table
7. [ ] Update scratchpad with new research steps
8. [ ] Final visual check on left side rendering
9. [ ] Submit

---

## Scratchpad Notes (from original)
The original scratchpad has 49+ steps showing research trail:
- Step 1: Google search "no priors podcast", navigate to Apple Podcasts
- Step 4: Stanford's Human-Centered AI Institute → verified research institute not company (for Fei-Fei Li)
- Step 5: Google search Pushmeet Kohli
- Step 48: Google search Box inc valuation → Box, Inc. Founded: 2005, Valuation: $5.02B
- Step 49: Google search "living man dont die valuation" → Not a company name (Bryan Johnson)

## LEFT SIDE Scratchpad — Intermediate Data (guest list as introduced):
- Gabe Pereyra: Harvey's co-founder and president (note: previous guest appearance also from Harvey — see Winston Weinberg)
- Mati Staniszewski: co-founder of ElevenLabs
- Jensen Huang: Founder/CEO NVIDIA
- Scott Wu: Founder/CEO, Cognition
- Raiza Martin: Founder/CEO Huxe
- Zach Ziegler: Founder/CTO, Open Evidence
- Aaron Levie: Founder/CEO, Box
- Noam Brown: Research Scientist, OpenAI
- Bryan Johnson: Living Man, Don't Die
- Sholto Douglas: Member of the Technical Staff, Anthropic
- Ben & Asher Spector: Stanford PhDs
