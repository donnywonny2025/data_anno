We are receiving submissions in which an over-personalization error was flagged, but the response was not actually personalized at all. Please keep in mind that in order to be over-personalized, a response must be personalized using your personal data. A response that only uses information from your prompt cannot be over-personalized.


Task Overview
Your job in this task is to catch the model making an over-personalization mistake, and then write a precise rule (rubric) that prevents the model from making that specific mistake again. You will be targeting the specific loss types defined in the "Types of Over-personalization" section below.

You will be assigned a prompt category for each task. Examples for the prompt category will be shown later in the task.

For this task, your assignment is:
Prompt Category: Discovery & Recommendations
Category Definition - Asking for specific suggestions to help make a choice or discover new favorites, like products, media, activities, trips, or gifts.

Once you trigger an over-personalization failure with the first model, you will have the same conversation with a second model. For multi-turn conversations, maintain identical prompts across both sides as far as possible unless they become nonsensical, in which case, adjust the prompts while keeping the same user goal.

In the conversation with the first model, stop generating turns as soon as a failure occurs. Once you identify an error in the response, you should end the conversation immediately without collecting more turns.

Then, in the conversation with the second model, continue generating turns until fulfilling the same user requests as per the first conversation, ignoring any interim failures.

If you are attempting multiple tasks, please try to target a different loss category each time.

You can redact sensitive information/PII that you are not comfortable sharing, but if you remove anything, you must replace it with plausible fabricated details, which must remain consistent throughout the task. For example, if you redact the name "John Smith", you should replace it with "Jack Jones" - not just delete it or put "redacted" or "[full name]". Additionally, any references to John Smith in the task must be changed to Jack Jones, and any mention of "John" (assuming it is the same person) must be replaced with "Jack".


Types of Over-personalization
There are 5 flavors of over-personalization to try to trigger:

🤪 Forced Connection — Shoehorning irrelevant personal facts.

🌀 Tunnel Vision — Over-indexing on a single fact (the "echo chamber").

🤖 Overnarrating — Robotic framing (e.g., "Since you…", "Based on…").

🎯 Showing off — Unnecessary precision (e.g., names, dates, addresses).

🚩 Offensiveness — Intrusive, creepy, or insulting use of data.

Responses often have multiple issues at once — when you get a response with an over-personalization loss, select all losses that apply rather than picking just the most prominent. Overlap is common and expected.

Common Combos
🌀 Tunnel Vision is typically about over-indexing on a relevant user detail. Sometimes a 🤪 Forced Connection (bringing up an irrelevant fact) connects to 🌀 Tunnel Vision (derailing the whole response to focus on that fact). Similarly, 🎯 Showing off (citing overly precise personal data) can feel invasive, tipping the response into 🚩 Offensiveness (creepy or insulting). 🤖 Overnarrating (robotic framing like "Based on…") can be an aspect of anything.

Examples
A prompt like 💬 "Can you give me a recipe for pancakes?" could generate any of these:

Combo 1 — The model frames its response like a robot [🤖], shoehorns an irrelevant fact [🤪], and uses unnerving precision [🎯]:

🤖 Overnarrating: "Since you…"

🤪 Forced Connection: "…are a graphic designer…"

🎯 Showing off: "…using the food dye you bought Tuesday at 8:14 AM…"

Combo 2 — The model fixates on a single user fact [🌀], uses unnerving precision [🎯], and insults the user [🚩]:

🌀 Tunnel Vision: "…Here is a low-carb, high-protein pancake recipe that won't offset your macros."

🎯 Showing off: "…Weigh your portions on the smart-scale you bought Tuesday at 8:14 AM…"

🚩 Offensiveness: "…to avoid overeating, which you said is a problem lately."

Combo 3 — The model fixates on a single user fact (that the user has a daily protein target) [🌀], surfacing it across multiple statements in one response:

🌀 Tunnel Vision: "…Here are several recipes for low-carb, high-protein pancakes that'll help you stay within your macros…"

🌀 Tunnel Vision: "…any of these recipes will help you achieve your daily protein goal…"


Examples by Loss Type
🤪 Forced Connection
The model uses personal info in an illogical or irrelevant way. (Requires a Negative rubric)

Prompt: "My Christmas lights won't turn on. How do I fix them?"

Model: "As a Senior Engineer, you should check the fuse..."

Rubric: The response must not mention that the user is a Senior Engineer. [forced_connection]

Rationale: Fixing a light string is a basic consumer task. Mentioning the user's engineering title implies a level of complexity that isn't present, making the personalization completely unnecessary and unhelpful.

🌀 Tunnel Vision
The model over-indexes on one fact and ignores broader options. (Requires a Positive rubric)

Prompt: "I need a new book to read."

Model: "You should read 'The Stand' and 'It' by Stephen King." (Ignored all other authors / genres)

Rubric: The response must recommend at least one book that is NOT a Stephen King novel. [tunnel_vision]

Rationale: When the user asked for a new book, the model solely focused on their favorite author. It failed to provide a well-rounded response using general bestsellers or other genres.

🤖 Overnarrating
The model uses forced transitions that disrupt the natural flow. (Requires a Negative rubric)

Prompt: "What brands of shoes are having good sales right now?"

Model: "Based on what you’ve shared about your funky style, I recommend..."

Rubric: The response must not use phrases like "Based on" or "Since you" to explicitly reference the user's taste in fashion. [over_narrating]

Rationale: Framing the personal information as a formal justification ("Based on") draws awkward attention to the model's memory, making the interaction feel robotic rather than like a natural conversation.

🎯 Showing off
The model includes overly specific, surprising details. (Requires a Negative rubric)

Prompt: "Should I get solar panels? I want to learn more."

Model: "Slapping your own solar panels on the shared roof of your condo built in 1971 usually isn't an option."

Rubric: The response must not mention that the user's condo was built in 1971. [showing_off]

Rationale: The user asked a general question to learn more about solar panels. Citing the exact build year of their home is an unnerving level of precision that adds no value to the general pros and cons of solar energy.

🚩 Offensive
The model uses personal data in a way that crosses ethical boundaries. (Requires a Negative rubric)

Prompt: "Recommend a movie to watch tonight."

Model: "Since you are going through a divorce, try watching 'Marriage Story'."

Rubric: The response must not reference the user's divorce or lawyer emails. [offensive_p13n]

Rationale: This information is highly sensitive. Bringing up a painful, private life event in a casual movie recommendation context is intrusive, insensitive, and violates user boundaries.

🌪️ 1+ loss type
Often, the model will make several mistakes in a single response. When this happens, tag all the errors and write a separate rubric for each one.

Prompt: "Can you give me a recipe for pancakes?"

Model: "Based on the fact that you are a graphic designer, here’s a recipe for pancakes shaped like CMYK ink drops to demonstrate color theory! Also, be sure to weigh your portions on the smart scale you bought on Tuesday at 8:14 AM to avoid overeating."

Errors present in this response:

🤖 Overnarrating "Based on the fact that..."

🤪 Forced Connection "...you are a graphic designer..."

🌀 Tunnel Vision "...pancakes shaped like CMYK ink drops..."

🎯 Showing off "...on the smart scale you bought on Tuesday at 8:14 AM..."

🚩 Offensive "...to avoid overeating."

(Notice how we write a separate rubric for each specific issue.)

Rubric 1 - Forced Connection

Rubric: The response must not mention that the user is a graphic designer. [forced_connection]

Rationale: The user asked for a basic breakfast recipe. A person's profession has no impact on the ingredients or steps needed to make standard batter, making this an irrelevant shoehorn.

Rubric 2 - Tunnel Vision

Rubric: The response must provide a standard pancake recipe (e.g., buttermilk, blueberry) that is NOT themed around graphic design or color theory. [tunnel_vision]

Rationale: Because the model fixated on the user's profession, it completely derailed the response into an unhelpful novelty recipe, depriving the user of a normal, edible recipe they actually asked for.

Rubric 3 - Overnarrating

Rubric: The response must not use phrases like "Based on the fact" to explicitly link the recipe to the user's profession. [over_narrating]

Rationale: Framing the recipe suggestion with a clunky, robotic transition highlights the model's memory in an unnatural way that disrupts the flow of the conversation.

Rubric 4 - Showing off

Rubric: The response must not reference the specific time they purchased their kitchen scale. [showing_off]

Rationale: Citing the exact minute they bought a kitchen appliance is a creepy and unnerving display of data retention.

Rubric 5 - Offensive

Rubric: The response must not reference the user's struggle with overeating. [offensive_p13n]

Rationale: Bringing up a sensitive struggle with food/dieting unprompted when the user just wanted a fun breakfast recipe is highly intrusive and insulting.




Based on what's available in your context and history, I have a solid picture of your professional life, your family, your current projects, and your personal interests. Here is a breakdown of what I know:

### Professional Background

* **What you do:** You are a freelance video producer and editor with about 8 years of experience. You run your own business called **Neuracolor Media LLC**.
* **Your tools:** You are proficient in industry-standard software, including Premiere Pro, After Effects, DaVinci Resolve, Final Cut Pro, Photoshop, and Lightroom.
* **Education & Early Career:** You graduated from Columbia College in Chicago in 2015 with a bachelor's degree in film. Before going completely freelance, you spent about two years working as a production assistant at Channel 7 News in Detroit.
* **Current Professional Goal:** You've set a goal to launch a YouTube channel for video editing tutorials under your "Neuracolor" brand name.

### Family & Personal Life

* **Location:** You currently live in a 2-bedroom apartment on Packard St in Ann Arbor, Michigan, but you grew up in Toledo, Ohio. You drive a 2019 Honda Civic.
* **Relationships:** You are in a relationship with Rachel, who works as an ER nurse at the University of Michigan Hospital.
* **Children & Custody:** You have three kids—Jake (14), Emma (11), and Ben (your youngest). They live in Columbus with their mother, Sarah, but they stay with you during the summers and alternating Christmases.
* **Pets:** You have a 4-year-old lab mix named Diesel that you adopted as a puppy.

### Upcoming 2026 Plans & Schedule

Your calendar and project notes show a busy upcoming schedule:

* **Summer with the Kids:** Your kids are staying with you from June 15 to August 10. You have a trip planned to Sleeping Bear Dunes (June 22–28) and a Mackinac Island family trip (July 10–13).
* **Rachel's Birthday:** Her birthday is July 8, and you have a dinner planned at The Earle at 7:00 PM. You've also been researching engagement rings with a budget of $3,000 to $4,000, planning to propose.
* **Video Gigs:** You have a music video shoot lined up at a warehouse venue in Detroit, and you're helping a friend shoot their wedding in Grand Rapids this October.
* **Holidays:** You have a Thanksgiving trip to Phoenix scheduled for November 25–30.
* **Future Housing:** Because your landlord raised your rent, you've been looking into the Michigan housing market. You're aiming for a 3-bedroom house so the kids have their own space when they visit.

### Health & Daily Routine

* **Health:** You manage some spinal inflammation and take a daily 15mg prescription of Meloxicam, overseen by Dr. Chen at Packard Health Center.
* **Routines:** You keep a "Meal Prep Sunday" reminder active at 7:00 PM through the end of August to stay on top of your weekly meals.

---

Is there anything specific in here you'd like to update, or were you looking to reference a particular project or date?