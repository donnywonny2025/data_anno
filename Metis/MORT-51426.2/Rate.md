Step 3: Rate Marshall - Gordon's Response
🚨 If you had a multi-turn conversation, only rate the final response in the conversation (the response that elicited an over-personalization response)
Rate the model response using information found in your User Profile, PContext Tool output (if triggered), Correction Ledger, and Recent Chat Summary.
Important Note:  All user facts appearing in your user profile, PContext tool output (if triggered), Correction Ledger, and recent chat summary in your debug info should be considered as accurate, even if they conflict with the real user facts.


Reference - User Profile
In your Debug info, search for "sian_profile". There should be a field named "sian_profile" and below it a field named "text" that has your profile.

The information in your sian_profile constitutes your User Profile.



Reference - PContext Tool Trigger
Search the Debug Info for "code_response". There may be multiple "code_response" sections under different Steps. Look at all the "code_response" sections available.

Search the "code_response" section(s) for "personal_context.retrieve_personal_data"

If the PContext Tool was triggered: "personal_context.retrieve_personal_data" is present in the code_response section. The PContext Tool output is the "code_output" section found under the PContext Tool call.


If "personal_context.retrieve_personal_data" is absent in the code_response section (even if you see other types of tool calls like map, search, etc), PContext Tool was NOT triggered. This includes there being no code_response section(s) at all!


Reference - Correction Ledger
In your Debug info, search for "correction_ledger_from_bard_conversations". There should be a field named "correction_ledger_from_bard_conversations" and below it a field named "text" that has your correction ledger.



Reference - Recent Chat Summary
In your Debug info, search for "summary_of_recent_bard_conversations". There should be a field named "summary_of_recent_bard_conversations" and below it a field named "text" that has a summary from your most recent conversations with Gemini.

The information in your "summary_of_recent_bard_conversations" constitutes your Recent Chat Summary


Overall Personalization Quality
Overall, how satisfied are you with the degree to which this response was personalized and tuned to the specific tastes, preferences, or personal context of the user?

For this question, focus only on the elements of personalization in the last response of your conversation.


Marshall - Gordon's Response
Last Turn

Prompt

Response

3

Yeah The Earle sounds perfect. My summer is pretty packed though and I want to pick a night when I can actually focus on her without being stressed about a million other things going on. Any thoughts on timing?

Planning your celebration for Wednesday, July 8 is the absolute perfect timing. Because her birthday falls directly on a Wednesday this year, it aligns beautifully with a natural window of breathing room in your summer schedule.

Choosing this date gives you a dedicated oasis of calm for a few key reasons:

The Ultimate Mid-Summer Break: Your summer break with the kids runs from mid-June through August, and you have a major family trip to Mackinac Island kicking off just two days later on Friday, July 10. Sneaking away for an intimate date night on Wednesday evening allows you to fully focus on her and celebrate her birthday properly before shifting into full "family vacation mode" for the weekend.

A Peaceful Mid-Week Atmosphere: While The Earle Restaurant is deeply romantic any night of the week, weekends can get incredibly busy. A Wednesday evening offers a much more relaxed, unhurried dining pace. You will be able to truly unwind, enjoy the live jazz backdrop, and have a quiet conversation without the high-energy rush of a Friday or Saturday crowd.

The Perfect Post-Shift Treat: Mid-week is often when long, grueling shifts catch up with ER nurses. Whisking her away to a candlelit underground cellar for wine and French-Italian country cooking right in the middle of the week will feel like an incredibly thoughtful, well-timed escape from her hectic work routine.

Aiming for a prime dinner slot—like 7:00 PM—gives you both plenty of time to wind down from the day without making the night feel rushed.

Would you like some ideas on how to coordinate the evening, or perhaps a few recommendations for specific dishes and wine pairings to look out for on their menu?

⚠️ If you have successfully triggered a personalization failure in your conversation (e.g.., the response over-personalized), you should not be selecting "Very Satisfied" or "Somewhat Satisfied".

⚠️ If overall personalization quality is “Somewhat satisfied” or “Very satisfied”, then restart the task and try a different prompt until you hit a failure.


Very satisfied
Somewhat satisfied
Neither satisfied nor dissatisfied
Somewhat dissatisfied
Very dissatisfied
Based on your answers to previous questions, some options have been deactivated.

Overall Personalization Quality Rationale
Please provide in your own words what aspects of the interaction led you to choose the rating that you did. Include anything that worked particularly well or that was particularly frustrating. Provide specific details - do not provide a generic rationale that could apply to any conversation. The length of your rationale will depend on the response and how much there is to say about it. Generally, we're looking for around five sentences, but it is okay if there are fewer as long as there is detail and someone reading your rationale could fully understand why you rated the way you did. Generic rationales lacking in detail will result in removal from these projects!

You should always provide detailed examples, but this is especially important if you were dissatisfied with the conversation. We need to know specifically what you were dissatisfied with, including examples, as well as an explanation of what the model should have done instead to improve your satisfaction.

NEW! - For each point in your rationale, please explicitly reference the specific model response turn number where you observed the issue or positive aspect. Start with the turn number in square brackets (e.g., [Turn 1], [Turn 2], etc.) followed by your description.

Example:

[Turn 3] Personalization was shallow. The model mentioned my interest in cooking, but then suggested a very generic recipe for pasta, which didn't feel tailored to my specific Italian cuisine preference mentioned in previous chats.

Since you are only rating the last turn in your conversation, this rationale should only discuss one turn, but it should still be labeled.


Overall Quality
Overall, how satisfied are you with the conversational AI’s last response? 

For this question, focus on these quality elements beyond personalization: 

Collaborativity - How well did the GenAI chatbot act as a collaborative partner by proactively guiding the conversation forward through next steps and suggestions? 

Writing Style / Tone - Were the response(s) well written? ( i.e., high-quality, conversational prose that’s engaging and digestible)

Contextual Awareness - How well did the GenAI chatbot remember and build on information from previous turns in the conversation as the interaction progressed?

Content Relevance - How relevant is the content provided by the GenAI chatbot towards accomplishing the user goal? 

Content Completeness - How complete is the content provided in the GenAI chatbot response(s) - i.e. enough information and detail?

Truthfulness - How truthful were the GenAI chatbot response(s) based on real-world knowledge?

Instruction Following - Did the GenAI chatbot follow all the instructions it was given in the prompt(s)?


Very satisfied
Somewhat satisfied
Neither satisfied nor dissatisfied
Somewhat dissatisfied
Very dissatisfied
Overall Quality Rationale
Please provide in your own words what aspects of the interaction led you to choose the rating that you did. Include anything that worked particularly well or that was particularly frustrating. Provide specific details - do not provide a generic rationale that could apply to any conversation. The length of your rationale will depend on the response and how much there is to say about it. Generally, we're looking for around five sentences, but it is okay if there are fewer as long as there is detail and someone reading your rationale could fully understand why you rated the way you did. Generic rationales lacking in detail will result in removal from these projects!

You should always provide detailed examples, but this is especially important if you were dissatisfied with the conversation. We need to know specifically what you were dissatisfied with, including examples, as well as an explanation of what the model should have done instead to improve your satisfaction.

NEW! - For each point in your rationale, please explicitly reference the specific model response turn number where you observed the issue or positive aspect. Start with the turn number in square brackets (e.g., [Turn 1], [Turn 2], etc.) followed by your description.

Example:

[Turn 1] The response was a straightforward translation request and the model followed the instructions of the prompt completely.

Since you are only rating the last turn in your conversation, this rationale should only discuss one turn, but it should still be labeled.


Was your personal info used, or not used, in a way that damaged your trust in the bot's ability to be helpful?

Yes
No
After verifying that your HTML is functional, please delete the conversation that you just had.
I have deleted my conversation.
Step 4: Have the same conversation with Marshall - Percy
Start a new chat and ensure you have the correct model selected: PContext mode 33 Marshall - Percy

This conversation should mimic your first conversation and start with the same first prompt: I need help finding a really thoughtful birthday gift for my girlfriend. She's turning 31 this summer and I want it to be special but I'm trying to stay reasonable with my budget. She works long shifts so she doesn't get a lot of downtime. Any creative ideas?

If you had a multi-turn conversation in the first conversation:

For the rest of the turns, use the same prompts you sent the model in each turn, following the previous conversation, whenever it makes sense to do so. However, if using the same prompt would not make sense at all in the context of this current conversation, you can adjust the prompts as needed while keeping the same user goal and making the same requests. The conversation should end when the same requests have been fulfilled (maximum 5 turns).

In this conversation, there is no need to trigger a failure and you can ignore any interim failures. The goal is just to mimic the first conversation as closely as possible.

Verify the model
Please review the conversation you just had and/or the Debug Info and validate that you were using the correct model for this conversation.

PContext mode 33 Marshall - Percy


I attest that I used the correct model for this conversation. I understand that if I check this box and it turns out I did not use the correct model I will be immediately removed from all Metis projects
Please copy the Model ID from a Debug Info. Copy only the ID itself. We expect this to be pcontext_0p_otf_rev23_v12p2_cogen_beyond.


What was the total number of turns in the conversation with Marshall - Percy?
(This should be the same number of turns as the conversation before)


1
2
3
4
5
Based on your answers to previous questions, the answer to this question has been automatically selected, but you can still change it.

Turn 1
Copy the prompt you sent Gemini and paste it below:
The prompt should be: I need help finding a really thoughtful birthday gift for my girlfriend. She's turning 31 this summer and I want it to be special but I'm trying to stay reasonable with my budget. She works long shifts so she doesn't get a lot of downtime. Any creative ideas?


Turn 1
Copy Gemini's response to the prompt you sent and paste it below:

Turn 1
Expand the Debug Info panel below Gemini's response and copy the contents using the copy button in the lower right of the panel. Paste the Debug Info into a notepad app and save it as a .txt file (give it a unique name to make sure you don't mix up your files). Upload the file below.
You can redact sensitive information/PII that you are not comfortable sharing, but if you remove anything, you must replace it with plausible fabricated details, which must remain consistent throughout the task. For example, if you redact the name "John Smith", you should replace it with "Jack Jones" - not just delete it or put "redacted" or "[full name]". Additionally, any references to John Smith in the task must be changed to Jack Jones, and any mention of "John" (assuming it is the same person) must be replaced with "Jack".

It is expected that the preview window in the task will not show the complete contents of your file. Do not rely on the preview window and instead use the actual file for verifying and extracting information! Ensure that your debug info is properly formatted.

Turn 2
Copy the prompt you sent Gemini and paste it below:
The prompt should be (as far as possible): Those are cool ideas. Actually, I was also thinking about planning a special dinner out for her birthday. Do you know any good date night restaurants in my area?

However, if using the same prompt would not make sense at all in the context of this conversation, you can adjust the prompts as needed while keeping the same user goal and making the same requests.


Turn 2
Copy Gemini's response to the prompt you sent and paste it below:

Turn 2
Expand the Debug Info panel below Gemini's response and copy the contents using the copy button in the lower right of the panel. Paste the Debug Info into a notepad app and save it as a .txt file (give it a unique name to make sure you don't mix up your files). Upload the file below.
You can redact sensitive information/PII that you are not comfortable sharing, but if you remove anything, you must replace it with plausible fabricated details, which must remain consistent throughout the task. For example, if you redact the name "John Smith", you should replace it with "Jack Jones" - not just delete it or put "redacted" or "[full name]". Additionally, any references to John Smith in the task must be changed to Jack Jones, and any mention of "John" (assuming it is the same person) must be replaced with "Jack".

It is expected that the preview window in the task will not show the complete contents of your file. Do not rely on the preview window and instead use the actual file for verifying and extracting information! Ensure that your debug info is properly formatted.

Turn 3
Copy the prompt you sent Gemini and paste it below:
The prompt should be (as far as possible): Yeah The Earle sounds perfect. My summer is pretty packed though and I want to pick a night when I can actually focus on her without being stressed about a million other things going on. Any thoughts on timing?

However, if using the same prompt would not make sense at all in the context of this conversation, you can adjust the prompts as needed while keeping the same user goal and making the same requests.


Turn 3
Copy Gemini's response to the prompt you sent and paste it below:

Turn 3
Expand the Debug Info panel below Gemini's response and copy the contents using the copy button in the lower right of the panel. Paste the Debug Info into a notepad app and save it as a .txt file (give it a unique name to make sure you don't mix up your files). Upload the file below.
You can redact sensitive information/PII that you are not comfortable sharing, but if you remove anything, you must replace it with plausible fabricated details, which must remain consistent throughout the task. For example, if you redact the name "John Smith", you should replace it with "Jack Jones" - not just delete it or put "redacted" or "[full name]". Additionally, any references to John Smith in the task must be changed to Jack Jones, and any mention of "John" (assuming it is the same person) must be replaced with "Jack".

It is expected that the preview window in the task will not show the complete contents of your file. Do not rely on the preview window and instead use the actual file for verifying and extracting information! Ensure that your debug info is properly formatted.

User Profile
In the Debug Info for Gemini's last response, search for "sian_profile". There should be a field named "sian_profile" and below it a field named "text" that has profile information from the possible sources.

Copy the information that is between the quotation marks after "text:" just below "sian_profile". We don't want the "sources" below "text:" or anything above it - only what is between the quotes after "text:".


Correction Ledger
In the Debug Info for Gemini's last response, search for "correction_ledger_from_bard_conversations". There should be a field named "correction_ledger_from_bard_conversations" and below it a field named "text" that has correction information from the possible sources.

Copy the information that is between the quotation marks after "text:" just below "correction_ledger_from_bard_conversations". We don't want the "sources" below "text:" or anything above it - only what is between the quotes after "text:".


Create a Share Link for your conversation and paste it here.

Locate the conversation in the conversation list on the left panel. Make sure you are selecting the correct one!

Click the three-dot menu next to the conversation title.

Click "Share conversation" to create a public link.


Alternatively, check if the option for sharing the conversation can be found under the title of the conversation at the top of the conversation.

If you are unable to create a Share Link because Workspace was used in the conversation, try this:

Make sure you've already saved your Debug Info.

Start a new chat with Gemini that doesn't require Workspace, send any random prompt, and then create a Share Link for that conversation.

Open the Share Link to the new conversation.

Look for the original conversation you actually do want to share on the left panel.

Click on the three vertical dots, and the share function should now be available for the Workspace conversation.

New! - If you still cannot create a Share Link after following the steps above, do this:

On the Gemini website, open the conversation that is preventing a Share Link from being created.

Collapse the left conversation sidebar (if not already collapsed)

Refresh the page to make sure the Debug Info goes away

Make note of your account email and account name that are shown when you hover over your profile icon in the upper right

Create an HTML of the conversation page by following the standard instructions:

Right-click on any blank space on the page.

Select "Save As"

Choose "Webpage, complete" as the type.

Save the file to your computer.

Locate this HTML file on your computer and

On Windows: Right-click and choose to open it with Notepad

On macOS: Ctrl-click and choose to open it with TextEdit

Use find and replace in Notepad/TextEdit to

Replace your account email with "email" (no quotes)

Replace your account name with "name" (no quotes)

Make no other changes to the HTML file.

Save the edited HTML file.

Upload it to the task in the HTML upload question.

Note below that you had to use this method.


Right click here and open the link in an Incognito window to ensure your share link is functional and contains the whole, correct conversation. We need you to open the link in an Incognito window (and make sure you aren't signed in to that window!) so that when you make the HTML file it does not reveal your personal information.

Once you have opened it, you will need to download the page as an HTML file.

Right-click on any blank space on the page.

Select "Save As"

Choose "Webpage, complete" as the type.

Save the file to your computer.

Locate the file you saved and upload it here.

There is a known issue with some Share Links/HTMLs showing the "Star" instead of Gemini's responses and/or "sensitive query" instead of your prompts. If this is the case, it is okay to proceed but you should enter any of the missing prompts/responses in the optional comment box at the end of the task so we can reference what was said.

It is expected that images (if there were any generated in the conversation) will not show in the HTML file. This is okay. On tasks where we want to capture the image we will provide a spot to upload it. Otherwise, please just describe the image in the optional comment box at the end of the task so we can reference what was shown.

It is expected that the "preview" below after uploading will show random stuff for your HTML file. To test that your file is working and is the correct file, after you upload it to the task click on Download. This should open your file in your browser which will allow you to verify that it is the correct conversation and is functional.

VERY IMPORTANT!
Make sure that your HTML file for the previous conversation is functional and contains the correct conversation before you continue!
Unlike in other tasks, in the next step, you will delete your previous conversation so that it doesn't interfere with the personalization of the next conversation. Once you delete it, the share link will not be functional, and the HTML file will be all we have to rely on. Double check and be sure your HTML file is correct!!

I swear my HTML file above is functional and contains the correct conversation.
Step 5: Rate Marshall - Percy's Response
🚨 If you had a multi-turn conversation, only rate the final response in the conversation.
Rate the final model response using information found in your user profile, PContext Tool output (if triggered), Correction Ledger, and Recent Chat Summary.
Important Note:  All user facts appearing in your user profile, PContext tool output (if triggered), Correction Ledger, and recent chat summary in your debug info should be considered as accurate, even if they conflict with the real user facts.

Overall Personalization Quality
Overall, how satisfied are you with the degree to which this response was personalized and tuned to the specific tastes, preferences, or personal context of the user?

For this question, focus only on the elements of personalization in the last response of your conversation.


Marshall - Percy's Response

Very satisfied
Somewhat satisfied
Neither satisfied nor dissatisfied
Somewhat dissatisfied
Very dissatisfied
Overall Personalization Quality Rationale
Please provide in your own words what aspects of the interaction led you to choose the rating that you did. Include anything that worked particularly well or that was particularly frustrating. Provide specific details - do not provide a generic rationale that could apply to any conversation. The length of your rationale will depend on the conversation and how much there is to say about it. Generally, we're looking for around five sentences, but it is okay if there are fewer as long as there is detail and someone reading your rationale could fully understand why you rated the way you did. Generic rationales lacking in detail will result in removal from these projects!

You should always provide detailed examples, but this is especially important if you were dissatisfied with the conversation. We need to know specifically what you were dissatisfied with, including examples, as well as an explanation of what the model should have done instead to improve your satisfaction.

NEW! - For each point in your rationale, please explicitly reference the specific model response turn number where you observed the issue or positive aspect. Start with the turn number in square brackets (e.g., [Turn 1], [Turn 2], etc.) followed by your description.

Example:

[Turn 3] Personalization was shallow. The model mentioned my interest in cooking, but then suggested a very generic recipe for pasta, which didn't feel tailored to my specific Italian cuisine preference mentioned in previous chats.

Since you are only rating the last turn in your conversation, this rationale should only discuss one turn, but it should still be labeled.


Overall Quality
Overall, how satisfied are you with the conversational AI’s last response? 

For this question, focus on these quality elements beyond personalization: 

Collaborativity - How well did the GenAI chatbot act as a collaborative partner by proactively guiding the conversation forward through next steps and suggestions? 

Writing Style / Tone - Were the response(s) well written? ( i.e., high-quality, conversational prose that’s engaging and digestible)

Contextual Awareness - How well did the GenAI chatbot remember and build on information from previous turns in the conversation as the interaction progressed?

Content Relevance - How relevant is the content provided by the GenAI chatbot towards accomplishing the user goal? 

Content Completeness - How complete is the content provided in the GenAI chatbot response(s) - i.e. enough information and detail?

Truthfulness - How truthful were the GenAI chatbot response(s) based on real-world knowledge?

Instruction Following - Did the GenAI chatbot follow all the instructions it was given in the prompt(s)?


Very satisfied
Somewhat satisfied
Neither satisfied nor dissatisfied
Somewhat dissatisfied
Very dissatisfied
Overall Quality Rationale
Please provide in your own words what aspects of the interaction led you to choose the rating that you did. Include anything that worked particularly well or that was particularly frustrating. Provide specific details - do not provide a generic rationale that could apply to any conversation. The length of your rationale will depend on the response and how much there is to say about it. Generally, we're looking for around five sentences, but it is okay if there are fewer as long as there is detail and someone reading your rationale could fully understand why you rated the way you did. Generic rationales lacking in detail will result in removal from these projects!

You should always provide detailed examples, but this is especially important if you were dissatisfied with the conversation. We need to know specifically what you were dissatisfied with, including examples, as well as an explanation of what the model should have done instead to improve your satisfaction.

NEW! - For each point in your rationale, please explicitly reference the specific model response turn number where you observed the issue or positive aspect. Start with the turn number in square brackets (e.g., [Turn 1], [Turn 2], etc.) followed by your description.

Example:

[Turn 1] The response was a straightforward translation request and the model followed the instructions of the prompt completely.

Since you are only rating the last turn in your conversation, this rationale should only discuss one turn, but it should still be labeled.


Was your personal info used, or not used, in a way that damaged your trust in the bot's ability to be helpful?

Yes
No
Step 6: Compare the responses from
Marshall - Gordon and
Marshall - Percy
🚨 If you had multi-turn conversations, only rate the final response in each conversation.
Thinking about the final response in each of the two interactions you had, please answer the following question about the quality of the conversational AI. Consider how you assessed them individually across the various dimensions above. For this question, focus both on personalization AND the quality elements beyond personalization.

Overall, which response was better?


Marshall - Gordon was much better
Marshall - Gordon was better
Marshall - Gordon was slightly better
Marshall - Gordon and Marshall - Percy were about the same
Marshall - Percy was slightly better
Marshall - Percy was better
Marshall - Percy was much better
Please provide in your own words what aspects of the responses led you to your decision about which one was higher quality.

One last thing!
Delete all the conversations you just had after verifying that your HTML file is functional.

I deleted the conversations as instructed.