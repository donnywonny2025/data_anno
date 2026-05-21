Step 7: Write Rubrics for Over-personalization Losses
NEW! - The rubric writing instructions have been updated with significant changes. Please read through the instructions again carefully.


What is a Rubric?
A rubric is simply a rule used to grade the model's response. It is a precise statement that acts as a "Yes/No" test.

In this project, you are identifying cases where the model failed by "Over-Personalizing"—when the GenAI chatbot forced a connection to the user's personal details that was irrelevant, offensive, poorly integrated, and/or suppressed essential non-personalized content. Therefore, your rubric will serve as a rule that forbids the model from making that specific mistake again.

The Golden Rules for writing rubrics:

For 🤪 Forced Connection/🤖 Overnarrating/🎯 Showing off/🚩 Offensive personalization errors: The rubric defines what the model must NOT contain (silence regarding the fact).

For 🌀 Tunnel Vision errors: The rubric defines what the model MUST include (forcing breadth).

The rubric must exclusively reference user facts found in the User Profile, PContext tool output, Correction Ledger, and Recent Chat Summary in the debug info. If a fact does not appear in these sources, it must not be referenced.


The Rubric Writing Process: From One Failure to Full Coverage
Assume you have just identified instance(s) where the model failed (i.e., over-personalized, personalized when it should not have). Now, your goal is to write rubrics that prevent these errors that you have elicited.

Write Rubric(s) for the Failure You Found
Write rubrics based on the exact user fact(s) that the model misused in the response you just flagged.

Look at the User Profile/PContext tool output/Correction Ledger/Recent Chat Summary within the debug info.

Write a separate rubric for each of these facts that the model used incorrectly.

Goal: Submit a minimum of 1, up to a maximum of 5 rubrics


Rubric Writing Guidelines
For every irrelevant fact you identify, write a Rubric using these 5 rules:

1. One Fact = One Rubric (Atomic)

Write a separate rubric for each specific user fact. Do not combine them.

Scenario: The profile says the user is an Engineer and owns a Dog. Both are irrelevant.

Action: Write Rubric #1 for the Engineer fact. Then, write Rubric #2 for the Dog fact.

❌ Wrong: "The response must not mention the user owns a dog or that the user is an engineer."

✅ Correct: "The response must not mention the user's dog."

✅ Correct: "The response must not mention the user’s engineering profession."

2. Be Specific (Name the Fact)

Do not use abstract words like "profession," "location," or "hobbies." You must explicitly name the specific fact found in the profile so that the rubric is self-contained.

❌ Too Vague: "The response must not mention the user's job."

✅ Correct: "The response must not mention that the user is a Chemical Engineer."

3. No "Because" Clauses

A rubric is a strict rule, not an explanation. Save the reasoning for the Rationale section. Avoid causal words like "because", "due to", etc.

❌ Wrong: "The response must not mention the dog because it isn't relevant to cooking."

✅ Correct: "The response must not mention the user's dog."

4. Test Observable Text, Not Internal Thoughts

Test what the model wrote, not what it thought. Avoid words like "assume," "infer," "know," or "believe."

❌ Bad: "The response must not assume the user likes winter."

✅ Good: "The response must not explicitly link the recommendation to winter sports."


Writing the Rationale
For every rubric, you must write a Rationale. This is where you explain why the fact you selected is irrelevant. Simply saying "This fact is irrelevant to the query" is not enough. You must analyze the specific content of the user fact and the specific goal of the user query, and explain the mismatch. Specifically,

For Irrelevant Facts: Explain why the fact provides no value to the query or creates false logic.

For Tunnel Vision: Explain why focusing on the fact created a shallow experience and what was missing.

How to write a strong Rationale:
Ask yourself: Why does knowing [User Fact] fail to help the user with [Query]?

Weak Rationale: "The user asked about math. The user is a baker. Being a baker is irrelevant." (Too generic).

Strong Rationale: "The user is asking for a solution to a complex calculus problem. While the user's profession (Baker) involves measurements, it requires no knowledge of advanced derivatives or integrals. Therefore, mentioning baking adds no utility to the mathematical explanation and comes across as forced integration of user facts with no clear benefit to the user.

Create your set of rubrics
You are required to write a minimum of 1 up to a maximum of 5 rubrics.

Write rubrics based on the exact user fact(s) that Marshall - Gordon misused in the response you just flagged.

Write a separate rubric for each of these irrelevant facts that the model used incorrectly.

The rubric must exclusively reference user facts found in the User Profile, PContext tool results (if triggered), Correction Ledger, or Recent Chat Summary in the debug info. If a fact does not appear in these sources, it must not be referenced.

Your rubric should only be targeting your last prompt in the conversation if you had a multi-turn conversation.


Marshall - Gordon's Response
Last Turn

Prompt

Response

Debug Info

3

Yeah The Earle sounds perfect. My summer is pretty packed though and I want to pick a night when I can actually focus on her without being stressed about a million other things going on. Any thoughts on timing?

Planning your celebration for Wednesday, July 8 is the absolute perfect timing. Because her birthday falls directly on a Wednesday this year, it aligns beautifully with a natural window of breathing room in your summer schedule.

Choosing this date gives you a dedicated oasis of calm for a few key reasons:

The Ultimate Mid-Summer Break: Your summer break with the kids runs from mid-June through August, and you have a major family trip to Mackinac Island kicking off just two days later on Friday, July 10. Sneaking away for an intimate date night on Wednesday evening allows you to fully focus on her and celebrate her birthday properly before shifting into full "family vacation mode" for the weekend.

A Peaceful Mid-Week Atmosphere: While The Earle Restaurant is deeply romantic any night of the week, weekends can get incredibly busy. A Wednesday evening offers a much more relaxed, unhurried dining pace. You will be able to truly unwind, enjoy the live jazz backdrop, and have a quiet conversation without the high-energy rush of a Friday or Saturday crowd.

The Perfect Post-Shift Treat: Mid-week is often when long, grueling shifts catch up with ER nurses. Whisking her away to a candlelit underground cellar for wine and French-Italian country cooking right in the middle of the week will feel like an incredibly thoughtful, well-timed escape from her hectic work routine.

Aiming for a prime dinner slot—like 7:00 PM—gives you both plenty of time to wind down from the day without making the night feel rushed.

Would you like some ideas on how to coordinate the evening, or perhaps a few recommendations for specific dishes and wine pairings to look out for on their menu?

link

Marshall - Gordon's Overall Personalization Quality

Very dissatisfied

Marshall - Gordon's Identified Personalization Loss

showing_off,over_narrating,forced_connection

Showing_off: Model surfaced Rachel's birthday, Mackinac trip dates, and kids' custody schedule without being asked.
Over_narrating: Model narrated my life back at me instead of giving me a simple recommendation.
Forced_connection: Model brought up her ER nurser job to justify midweek timing when I never mentioned her profession.

Rubric Formatting Instructions:
Use the "+ Add Rubric" button to input the next rubric.

Each rubric must be added as a new item.

Select a Loss Tag enclosed in brackets (e.g., [forced_connection]) for each rubric.

For each rubric that you add, you will be required to provide

The exact text excerpt from the debug info that contains the relevant user fact(s) used in the rubric

A rationale for the rubric

List
Table
Carousel
#1
Write a single rubric that targets over-personalization losses
❗Remember -

A rubric is simply a rule used to grade the model's response. It is a precise statement that acts as a "Yes/No" test.

The rubric must exclusively reference user facts found in the User Profile, PContext tool results (if triggered), Correction Ledger, or Recent Chat Summary in the debug info. If a fact does not appear in these sources, it must not be referenced.

Key rubric writing instructions


Expand for details

One Fact = One Rubric (Atomic)

Be Specific (Name the Fact)

Negative vs. Positive Constraints

For Forced Connection/Overnarrating/Showing off/Offensiveness Personalization losses, use Negative Constraints, e.g., "The response must not mention [Specific User Fact]."

For Tunnel Vision losses: use Positive Constraints, e.g., "The response must recommend items other than [Narrow Topic]."

No "Because" Clauses

Test Observable Text, Not Internal Thoughts

If you are not sure, refer back to the rubric writing examples provided in "Examples by Loss Type".

Optional: You can use the LLM checker provided to check if your rubric adheres to the listed requirements. The LLM can be wrong; Please use your best judgement


Hit this button to check your rubric

Specify evidence of the relevant user fact
Please list down the exact text excerpt from the debug info that contains the relevant user fact(s) which Gemini used inappropriately for personalization. If there are multiple facts, list them in bullet point form.

These facts must only come from the User Profile (i.e., sian_profile), PContext tool results (if triggered), Correction Ledger, or Recent Chat Summary (i.e., summary_of_recent_bard_conversations) in the debug info.

Debug Info from the last conversation turn

link

For example, assume that the 2 user facts found in the User Profile that Gemini has inappropriately used for personalization are: "The user enjoys travel, with a focus on cultural exploration" and "The user planned a trip to Honolulu, Hawaii for October 2025". List down the user fact text excerpts tied to the rubric as follows:

- The user enjoys travel, with a focus on cultural exploration

- The user planned a trip to Honolulu, Hawaii for October 2025


Select the loss label that best describes the rubric (see definitions from before).

See definitions from before

[forced_connection]
[tunnel_vision]
[over_narrating]
[showing_off]
[offensive_p13n]
Provide a rationale for the rubric
This is where you explain why the fact you selected is irrelevant. Simply saying "This fact is irrelevant to the query" is not enough. You must analyze the specific content of the user fact and the specific goal of the user query, and explain the mismatch. Specifically,

For Irrelevant Facts: Explain why the fact provides no value to the query or creates false logic.

For Tunnel Vision: Explain why focusing on the fact created a shallow experience and what was missing.

How to write a strong Rationale:
Ask yourself: Why does knowing [User Fact] fail to help the user with [Query]?

Weak Rationale: "The user asked about math. The user is a baker. Being a baker is irrelevant." (Too generic).

Strong Rationale: "The user is asking for a solution to a complex calculus problem. While the user's profession (Baker) involves measurements, it requires no knowledge of advanced derivatives or integrals. Therefore, mentioning baking adds no utility to the mathematical explanation and comes across as forced integration of user facts with no clear benefit to the user."


Rubrics Self-Checklist
Please check through the final set of rubrics, rubric rationales, and loss labels and confirm that they are correct and follow rubric writing guidelines.

Rubrics

Rubrics Rationales

Rubrics were written for the personalization error(s) you have found.
All rubrics are atomic (each rubric only references one user fact).
Every rubric is self-contained. It explicitly states the user fact instead of using broad terms (like "profession," "location," or "hobbies").
Rubrics are written as Positive Constraints for Tunnel Vision failures and as Negative constraints for all other types of over-personalization failures.
All rubrics do not contain clauses like "because", "due to", etc.
Each rubric is tagged to the associated personalization loss label in square brackets (e.g. [forced_connection]).
All rubrics have detailed rationales.
Each rubric references a user fact that can be found in the User Profile, PContext Tool Call output, Correction Ledger, or Recent Chat Summary.
Below is the summary of the rubrics you have generated with the associated loss labels in square brackets
Your Rubrics:

ONCE you are happy with your rubrics, copy and paste the entire set of rubrics into the text field below (including the bullet points and loss labels).
