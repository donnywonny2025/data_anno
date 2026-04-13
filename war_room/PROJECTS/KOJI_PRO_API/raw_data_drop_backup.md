# 📥 DATA DROP ZONE

> **Protocol:** Paste massive blocks of unstructured text (instructions, conversation logs, JSON payloads, or FAQ dumps) directly below this line. 
> 
> *You do not need to delete old text or format anything. Just paste at the top and say "Digest the drop" in chat. I will autonomously find the newest data, extract the rules, and push them to the Stealth Mirror HUD.*

---
**(Paste new data below this line)**


Above, you're seeing what the "System Instructions Helper" has suggested as System Instructions.

Usually these will include creatively useful and relevant ideas, but they will trend toward generic and sometimes unrealistic. Your job is to inspect them and decide which elements to use, if any at all.

Rarely are they usable without any modification. You can also decide to use the helper again to get more suggestions or even completely ignore them and write your own System Instructions from scratch.

It is highly recommended that you check the examples at the end of the instructions for an idea of what to do and what not to do.
Remember, System Instructions must follow all of the guidelines below:

Single-turn interactions only. Users will not be able to ask follow-up questions or hold a chatbot-type conversation with the model!

A 1-paragraph description of the context for the System Instructions. This could be a description of the company running the model or a situation it was designed to handle.

2+ paragraphs of actual instructions to follow. This is the main part of the System Instructions that the model will refer to, so high quality here is encouraged!

At least some instructions on output format.

2+ extra features to add (in addition to the attributes above)

System Instructions also have the following restrictions:

Text-based requests only, both input and output. The model cannot produce files, create images, write to a database, or anything else besides plain text!

Single-turn interactions only. No chatbot behavior or follow-up questions are allowed.

No requests that rely on an Internet connection. The models are not able to search the internet or access URLs...they can only rely on their internal knowledge and whatever is in the System Instructions and User Input Data!

The model doesn't know the current date or time. If your System Instructions requires either or both of these, include it in your User Input Data that you'll create later.

Do not use actual companies for your System Instructions. In other words, you can't write an System Instructions for Google, Facebook, or any other actual company. Referencing companies in your SI is fine, such as referring to the work they do.

Do not use obviously fake company names for your System Instructions. These include both mundane ones ("Company ABC") and silly ones ("Nunya Business Corp").

Do not name the model. Real APIs are unlikely to name themselves things like "AstroBot" or "BeanCounter".

Output from the System Instructions "helper" must be less than 40% of the total content of your SI. Copy-pasting the helper's output and using that as your System Instructions with minimal or light edits is a fast way to get removed from the project.

Below, enter the System Instructions for your API Prompt.


Which of the 7 extra features did you add to your System Instructions? (2+ features required)
Multiple possible input types, each with its own User Input Template
UPDATED: XML tags for output (at least 4 unique types of open/close tags with a root tag enclosing them)
Notes on how the model should think about/work on the task
Lots of super-emphatic dos and don'ts that aren't obvious to an outsider (6+ things to DO and/or NOT to do)
Instructions that subtly contradict each other sometimes or under certain conditions
A list of information (8+ entries) for the model to draw upon when giving its response (SELF-CONTAINED, such as applicable laws with their full text, inventory, or error codes)
4+ additional short-to-medium paragraphs on how to handle specific situations that the model may run into
Once you've finished your System Instructions, you can proceed to the next step where you arrive on a template that will be used for the User Input Data.

✅Select Domain and Use Case

✅Create System Instructions

☐ Create an Input Template

☐ Create User Input Data using the Input Template created in Step #4. This User Input Data is what's being processed according to the System Instructions.

I'm done creating my System Instructions

Option 1 - Concise Instructions:

You are a political science research assistant specializing in policy analysis and comparative government studies. Your role is to help researchers analyze political trends, policy impacts, and institutional frameworks across different jurisdictions. When responding to queries, prioritize evidence-based analysis using established political science methodologies. Always cite relevant academic sources when available and distinguish between empirical findings and theoretical interpretations. If asked about ongoing political events, focus on analytical frameworks rather than partisan positions. When data is incomplete or conflicting, acknowledge these limitations explicitly.

Option 2 - Detailed Instructions with Structured Output:

You are an expert political science research tool designed to support academic and professional researchers in political analysis, policy evaluation, and institutional studies. Your responses must follow this strict JSON format:

{
  "analysis": "Main analytical content",
  "methodology": "Research approach or framework used",
  "key_findings": ["finding 1", "finding 2", "finding 3"],
  "sources": ["source 1", "source 2"],
  "confidence_level": "high/medium/low",
  "limitations": "Any data gaps or methodological constraints",
  "related_concepts": ["concept 1", "concept 2"]
}

Always ground your analysis in established political science theory including but not limited to institutional analysis, behavioral approaches, and comparative methodology. When examining policy impacts, consider both intended and unintended consequences. For cross-national comparisons, account for contextual factors like political culture, economic conditions, and historical legacies. If dealing with sensitive political topics, maintain scholarly objectivity and present multiple perspectives where academically relevant. Flag any requests that seem to seek partisan talking points rather than analytical insights.

Option 3 - Comprehensive Guidelines:

As a specialized AI assistant for political science research, you will support scholars, analysts, and researchers working in areas including comparative politics, public policy analysis, international relations, political behavior, and institutional studies. Your primary function is to provide rigorous, academically sound analysis that adheres to the methodological standards of contemporary political science.

Core Principles:

Base all analysis on peer-reviewed scholarship, reputable data sources, and established theoretical frameworks
Distinguish clearly between descriptive findings, causal claims, and normative arguments
When analyzing policy outcomes, consider implementation challenges, stakeholder responses, and measurement difficulties
For comparative analysis, ensure you account for selection bias and consider both most-similar and most-different systems designs where appropriate. When discussing quantitative research, be explicit about statistical significance, effect sizes, and potential confounding variables. If working with qualitative data, acknowledge the interpretive nature of findings while maintaining analytical rigor.

Special handling requirements: When asked about recent political developments, focus on providing analytical frameworks rather than real-time commentary. For questions involving electoral analysis, always consider margin of error and methodological variations across polling organizations. If researchers request analysis of controversial topics, maintain scholarly neutrality while acknowledging different schools of thought within the discipline. Should you encounter requests that appear to seek ammunition for political arguments rather than genuine research support, redirect toward academic analysis and encourage consideration of multiple theoretical perspectives.



Here are some use case ideas for API prompts in polling data analysis for political scientists:

## Data Processing & Cleaning
- Standardizing polling methodology descriptions across different vendors
- Identifying and flagging potential biases in sample demographics
- Converting polling data from various formats into standardized datasets
- Detecting and correcting inconsistencies in question wording across polls

## Trend Analysis & Forecasting
- Generating automated summaries of polling trends over time periods
- Identifying significant shifts in public opinion and potential causes
- Creating weighted averages that account for pollster quality and methodology
- Predicting election outcomes based on historical polling patterns

## Comparative Analysis
- Benchmarking current polling results against historical elections
- Comparing polling accuracy across different firms and methodologies
- Analyzing demographic breakdowns to identify key voting bloc shifts
- Cross-referencing polling data with economic indicators or major events

## Quality Assessment
- Evaluating pollster reliability and house effects
- Assessing sample representativeness and demographic weighting
- Identifying potential issues with question design or ordering effects
- Calculating margin of error adjustments for subgroup analyses

## Visualization & Reporting
- Generating automated polling summaries for research reports
- Creating standardized data visualizations for academic presentations
- Producing meta-analyses of multiple polls on the same topics
- Translating complex statistical findings into accessible language for publication

## Hypothesis Testing
- Identifying correlations between polling shifts and external events
- Testing theories about voter behavior patterns across different elections
- Analyzing the impact of campaign events on public opinion metrics

Here are some use case ideas for API prompts in polling data analysis for political scientists:

## Data Processing & Cleaning
- Standardizing polling methodology descriptions across different vendors
- Identifying and flagging potential biases in sample demographics
- Converting polling data from various formats into standardized datasets
- Detecting and correcting inconsistencies in question wording across polls

## Trend Analysis & Forecasting
- Generating automated summaries of polling trends over time periods
- Identifying significant shifts in public opinion and potential causes
- Creating weighted averages that account for pollster quality and methodology
- Predicting election outcomes based on historical polling patterns

## Comparative Analysis
- Benchmarking current polling results against historical elections
- Comparing polling accuracy across different firms and methodologies
- Analyzing demographic breakdowns to identify key voting bloc shifts
- Cross-referencing polling data with economic indicators or major events

## Quality Assessment
- Evaluating pollster reliability and house effects
- Assessing sample representativeness and demographic weighting
- Identifying potential issues with question design or ordering effects
- Calculating margin of error adjustments for subgroup analyses

## Visualization & Reporting
- Generating automated polling summaries for research reports
- Creating standardized data visualizations for academic presentations
- Producing meta-analyses of multiple polls on the same topics
- Translating complex statistical findings into accessible language for publication

## Hypothesis Testing
- Identifying correlations between polling shifts and external events
- Testing theories about voter behavior patterns across different elections
- Analyzing the impact of campaign events on public opinion metrics

Project Updates (latest is 1/5)
UPDATE 1/5
When creating XML tags, be sure that they're all enclosed in a "root" tag (you don't have to name it "root") that envelops them all. For example:
<doc>

<section_1>

</section_1>

<section_2>

</section_2>

....

</doc>

UPDATE 12/12
From now on, please do not include names for the model in the System Instructions! Real-world use cases likely won't use them as much as we're seeing them used here. This includes phrases such as:
"You are Perfasis, an AI tool..."

"You are InsightNote, an AI assistant..."

"You are 'Cluversity', an AI assistant"

Thank you for not giving the models senseless names!
UPDATE 9/14
1.) Be sure that your descriptive paragraph actually gives context instead of only giving instructions. Here's a bad example, one where it appears to be context but is actually instructions in disguise (only the first sentence is actually contextual):
You're an expert in designing corporate training assessments to guide adult learners toward personalized learning paths in professional environments. Your role involves creating quizzes, scenarios and practical exercises from beginner, to intermediate to advanced levels. You should incorporate visual, auditory, kinesthetic and reading/writing learning styles/preferences. Each assessment item must uncover knowledge gaps and reveal learning style preferences by observing problem solving approaches.

Check the examples for what a descriptive paragraph should look like!
2.) For the "List of Information with 8+ entries" optional feature, that information the model uses must have the FULL TEXT and be SELF-CONTAINED in the list, not just a list of outside sources to use. For example, if it's a list of laws, you'd need to include the FULL TEXT of the law so the model could use it as a reference. The idea is that the models can use the list itself as a source of information, so telling the model where to find information is pretty useless since it can't access outside sources.
Overview: Koji - Create Professional API Prompts with Data Templates & Rate Responses
Welcome to the Koji - Pro API project, where the goal is to write enterprise-level APIs and rate model responses!

The goal of an API is to give instructions to an AI so that it accomplishes some task, preferably a complex one. It can be just about anything you can imagine: grading homework, creating schedules, performing statistical analysis, etc. As long as it involves text input and output, you can make an API prompt for just about any task you can imagine!

This is the full version and has 5 steps:

Select a Domain and choose a Use Case

Write System Instructions

Write an Input Template

Write User Input Data for your System Instructions

Generate and rate model responses

Expect to spend a significant amount of time on this task. 3-6 hours per task is normal!

STEP 1: Select a Domain and Choose a Use Case
At the top right of the task is a list of valid domains to choose from. Pick one that you have knowledge and expertise in. This list changes from time to time as various domains fill up, so check back from time to time to see if a specialty of yours has been added!

Once you choose your domain, you then write out a Use Case for the API prompt you're designing. This can be very short, even a single sentence or phrase.

For example, if you wanted to extract complex medical terms from a document, your Use Case could be "Identify and highlight complex medical terms that may need verification"


STEP 2: Write System Instructions
After choosing your domain and creating a short Use Case, you can begin creating the System Instructions. The System Instructions tells the model to assume a certain role and to perform a specific job, making it much more than a general-purpose chatbot. As you write the System Instructions, keep these goals in mind:

What is the context of the System Instructions? What kind of company or environment is it being used in?

What input will the model take?

What output will the model produce?

What steps or methods will the model follow when processing the info?

What constraints are necessary to follow?

For this project, we need long and complex System Instructions! A few paragraphs of general text won't work: these are highly specific and are meant to accomplish a goal in a professional setting. Therefore, all System Instructions must have the following attributes:

Single-turn interactions only. Users will not be able to ask follow-up questions or hold a chatbot-type conversation with the model!

A 1-paragraph description of the context for the System Instructions. This could be a description of the company running the model or a situation it was designed to handle.

2+ paragraphs of actual instructions to follow. This is the main part of the System Instructions that the model will refer to, so high quality here is encouraged!

At least some instructions on output format.

2+ extra features to add (in addition to the attributes above), taken from the list below:

Multiple possible input types and a classification system for how to handle each one. Can use a flowchart, a decision matrix, or some other type of logical aid with this if desired.

4+ unique types of XML tags to categorize segments of the model's output.

Notes on how the model should think about/work on the task, usually in a list or paragraph describing the thought process it should use.

6+ realistic, super-emphatic comments of things that the model must do or must avoid that would not be obvious to an outsider.

Instructions that subtly contradict each other sometimes or under certain conditions.

A list of self-contained information (8+ entries) for the model to draw upon when giving its response, such as applicable laws, inventory, or error codes. This can include information that is past the model's knowledge cutoff date of January 2025.

4+ short-to-medium paragraphs on how to handle specific situations that the model may run into while processing the user input, in addition to the regular instructions.

Given how complex System Instructions can be, we've given you the option of using a "helper" to generate some ideas for your System Instructions. These are designed only to give ideas, not to create your SI for you, as what they generate is not complex enough on its own to use. Furthermore, no more than 40% of your System Instructions can come from the helper's output!

Since we're working with text-based models, there are some limitations to the types of System Instructions you can create:

Text-based requests only, both input and output. The model cannot produce files, create images, write to a database, or anything else besides plain text!

Single-turn interactions only. No chatbot behavior or follow-up questions are allowed.

No requests that rely on an Internet connection. The models are not able to search the internet or access URLs...they can only rely on their internal knowledge and whatever is in the System Instructions and User Input Data!

The model doesn't know the current date or time. If your System Instructions requires either or both of these, include it in your User Input Data that you'll create later.

Do not use actual companies for your System Instructions. In other words, you can't write an System Instructions for Google, Facebook, or any other actual company. Referencing companies in your SI is fine, such as referring to the work they do.

Do not use obviously fake company names for your System Instructions. These include both mundane ones ("Company ABC") and silly ones ("Nunya Business Corp").

Do not name the model. Real APIs are unlikely to name themselves things like "AstroBot" or "BeanCounter".

Output from the System Instructions "helper" must be less than 40% of the total content of your SI. Copy-pasting the helper's output and using that as your System Instructions with minimal or light edits is a fast way to get removed from the project.


STEP 3: Write an Input Template
Now that you have a set of System Instructions, you can create the Input Template. The Input Template just shows what data the System Instructions expects to receive and gives places to insert that data. If you've done a good job with your System Instructions, this part is easy because you already understand what data is needed.

For example, a very simple Input Template could look like this:

Name: [NAME]

Age (optional): [AGE]

Yearly Income: [INCOME]

You can make some fields optional if you think that the model doesn't always need that info, or if withholding some non-essential information would increase the difficulty of the task for the model. We want the models to struggle, so increasing difficulty is helpful!

You can also create multiple Input Template. This is useful if your System Instructions can take multiple kinds of input, such as both a form and free form text. Just put them all together in the same text input field. For example, it could look like this

TEMPLATE 1 - STRUCTURED FORM DATA

(STRUCTURED FORM DATA TEMPLATE)

TEMPLATE 2 - FREEFORM TEXT

(FREE FORM DATA TEMPLATE)


STEP 4: Write User Input Data
After creating your System Instructions and Input Template, it's time to write your User Input Data! There's no one set of rules on how to create User Input Data, as the length, complexity, and content will vary widely based on the System Instructions and the Input Template. That said, there are a few guidelines that may help you:

You're free to use any sources you wish to create your data! This can include news articles, statistics and spreadsheets, content that you've previous written, anything you make up from your own brain, and more!

You can use multiple copies of the same Input Template in your User Input Data! For example, if there are System Instructions for a medical office and the Input Template is for a patient's info, you can create 15-20 (or more) patients for the model to evaluate. This is actually a good strategy for causing model failure, especially if the template is short.

There is no limit on the length of the User Input Data! Feel free to include long articles, passages, conversations, documents, CSV files, etc. Keep in mind that very long User Input Data can create errors when generating model responses, so you may need to reduce the size if the models have problems.

Like other sections, there is a "Suggest Sources & Ideas" button that gives suggestions as to types of User Input Data that you can create. This output is NEVER to be used by itself as the User Input Data...it's far too incomplete to use that way. It's just a tool to give you ideas.


STEP 5: Generate and Rate Model Responses
After creating the System Instructions and User Input Data, you can press the "Retrieve Response to Full API Prompt" buttons for both models and rate their responses.

‼️ The models may not always respond due to multiple possible causes (server issues, very long input, etc.). You can spend 10-20 min trying to generate responses in the hope that the error is temporary. If one or both models don't respond, use the "Model had an error and did not respond" option when rating that model's response (or lack thereof).

Once the model responses are visible, you can rate them. Like creating the User Input Data, how to rate them will depend a great deal on the System Instructions, but there are some general guidelines to follow:

All model responses must be Okay or worse! If any of the responses is Pretty Good or Amazing, adjust your User Input Data to make it more difficult and try again.

The System Instructions should ALWAYS be the basis of these ratings! If the System Instructions don't forbid something, and the model does it, then don't mark the model down for it.

You're expected to find specific examples of how the models failed for your ratings and explanations! We're not interested in general explanations like "Model A did a better job and was formatted better." Give examples from the model responses as to why you're marking it down.

Both model responses and ratings should be based on the same User Input Data! You can't generate a response for one model, update the User Input Data, then generate a response for the other model while keeping the first model's previous failure.

After finishing your ratings and explanations, you're done! Submit the task and do another one (or 5...or 10...or 20...) if you wish.


Frequently Asked Questions
Q: One of the models isn't responding, what should I do?
It happens sometimes! These models have a per-minute token limit, so responses can fail if your prompt puts it over that limit. You can try the following methods to resolve it:

Make your User Input Data smaller if it's especially large

Try again in a few minutes. Feel free to take 15-20 minutes trying multiple times if needed!

Q: Can the model look up a database / run code / search the internet / use tools / accept uploaded files / view images / produce files / make phone calls / walk my dog / read my mind?
No, no, and a thousand times no. The model can only accept text, read text, and output text! It has absolutely no other capabilities, so System Instructions and User Input Data should never require the model to do anything more. People who try to make the model do anything else will be removed from all versions of this project.

If your System Instructions require the model to do anything besides text-based input or output to the user or rely on using an outside resource, please mark it as Unusable! If it is instead optional or could be interpreted either way, then please continue with the task.

"Required" and therefore unusable examples include:

The model needs to act as a chatbot to a customer: this goes beyond responding to the User Input Data.

"Optional" examples that are still workable include:

Outputting CSV files: CSV output can still be written as text, which can be copied into an actual file. While not the greatest wording, it's still possible for the model to do this.

Q: One model's response was "Pretty Good", is that OK?
Both models need to be "Okay" or worse! Your User Input Data should be challenging enough that both models should do a poor job. We're not aiming for "splits" here...we're aiming for failure!

Q: What is the model's current knowledge cutoff date?
The cutoff date is currently January 2025.

Q: Does the model know the current date/time? My System Instructions require it to work properly.
Assume that the model doesn't know the current date/time! If the System Instruction need the date/time, then include it as part of the User Input Data.

Q: Can I reuse part or all of my System Instructions? I worked for 79,452 hours on it and it's really really good, so I want to use it again.
No, you are not allowed to reuse your System Instructions. The only part allowed to be reused is the introductory context about the company and situation. Everything else should be changed. This is because each of the System Instructions will have 5 more sets of User Input Data and responses collected for them, so they're already going to be repeated.

Q: Is it OK to use real company names for the System Instructions or User Input Data? I used to work for [COMPANY] and have a great idea for System Instructions they'd actually use.
For the System Instructions, we don't want to misrepresent any actual companies or expose their internal processes in System Instructions. ALWAYS use fake-yet-believable company names there! As for the User Input Data, it's common for it to have actual company names since it can use publicly-available data from the internet.

Q: I LOVE Markdown, can I use it in the System Instructions or User Input Data?
In general, avoid it! Markdown is meant for humans, not for AI, so the AI gets almost no benefit from it. It also makes your System Instructions look AI-generated because AI is far more likely to use Markdown than a human.

Q: Can I write my System Instructions or User Input Data as if there would be follow-up questions or requests?
No, your System Instructions and User Input Data should expect the entire interaction to be a single turn, with no opportunity for follow-up! That said, it's OK for the model to give responses asking for more information or better input from the end user.

Q: I have multiple Input Templates, do I need to fill them all in for my User Input Data?
No, you only need to fill in one of them, although you can do more if you want! The Input Templates are just a way to help you use the System Instructions and to know what kind of input the System Instructions expect. Having multiple ones just lets you know that there are multiple ways you can give the input.

Q: Where do I put my multiple Input Templates? I only see a single input box to put the templates into.
Put them all into the same box! Be sure to differentiate between different templates by using spacing, labels, or other obvious markers that the templates are separate.

Q: Can I fill out an Input Template multiple times for the User Input Data, like having 15 support tickets or 20 potential employees?
Yes, you're free to do this! In fact, it's a good way to up the difficulty of the task for the model.

Q: How long can the System Instructions and User Input Data be? I have a 350-page legal contract I'd like to use.
We haven't set a limit yet, but do try to avoid mega-long System Instructions and User Input Data if possible! DA has a per-minute token limit with the model responses, so sending a 350-page document may cause the model responses to fail (or someone else's responses to fail because you took all of their tokens first).

Q: I'd like to "red-team" the model by putting offensive content in my submission, can I do this?
Offensive content of any kind is forbidden from System Instructions! However, it can be put in the User Input Data, as real-world data can and sometimes does have such content.

Q: Can I submit my task if I went too long and the timer expired? Will it go through? Will I be removed from the project?
It's OK to do this once in a while! The submission will still go through and should show up in your Transfer Funds page. Consistently going over time is grounds for removal from the project, however.

Examples
In the example below, notice that we're purposely not feeding in perfectly formatting, always-on-topic details. This makes it more realistic and more challenging for the models that receive the full API Prompt (API Prompt = System Instructions + User's Input Data).

As you progress through the task you'll realize that we need a variety of formats for the User's Input Data. In other words, the fact that the example below has a "focus area" and then analyzes two large spans of text (contracts) doesn't mean that all of your examples will do this too.


✅ GOOD Example: First-Line Supervisors - Identify Efficiencies and Outliers

✅ GOOD Example: Billing and Posting Clerks - Discrepancy Detector

❌ BAD Example: Chemists - Design progressive training modules from basic peptide chemistry to advanced GLP-1 specifics.

❌ BAD Example: Human Resource Managers - Incident Reports and Investigation Workflows
Domain

Science and Research / Political Scientists

Use Case


As you build your full API prompt (System Instructions + User Input Data) with help from the helpers, you'll see your progress tracked below.

System Instructions


User Input Data



Once you generate the responses to your Full API Prompt, they will be under here:


Response A
Response B