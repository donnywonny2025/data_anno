# Momo Project - Worker Chat Log Analysis (Mar 23, 2026)

## Raw Worker Comments

- **JessicaS:** Tried to do multiple rounds but getting blocked by 8k token limit.
- **Melissa C:** Token amount changed recently? 5k document won't work.
- **Brittany S:** Copying multiple docs only copies one.
- **Admin SS:** If model says it can't access history, use escape hatch or restart (not a reasoning error).
- **DavidS:** Every single criterion must begin with "The response should".
- **AndrewC (and others):** Getting blocked by the automatic rubric analyzer for formatting issues. "The Quotation Trap" - do not use quotation marks in criteria.
- **DonhemB:** How to add second doc? Public/historical figures don't need anonymizing.
- **MichaelS:** "The response must" fails. Must use "The response should". Rubric checker is strict about "binary presence verbs".
- **SavionT:** Final criterions having hidden formatting issues preventing submission.
- **Angell S:** People are using `<{TASK}>` or `<[TASK]>`. It MUST be exactly `<|TASK|>`.
- **KristyC:** Lost 4+ hours of work because of the `<|TASK|>` separator error.
- **Admin CL:** If content used 3 times, 4th time must be 100% new.
- **Various:** Portland/Washington/Texas users reporting they are unexpectedly ineligible for the task due to location restrictions.
- **JessicaK:** Model failing to construct timeline due to incomplete dates (e.g., "49 weeks ago").
- **DinaH:** There is a hard check preventing submission if tokens are under 8,000, even if the warning checkbox is ticked.
- **Virginia D:** PII mapping tool showing nothing when text is typed in.
- **Admin AP:** Public YouTubers/BBC do not need anonymization. Small personal accounts do.

## Key Traps to Avoid
1. **The `<|TASK|>` Formatting Bug:** Exact syntax matters.
2. **The 8,000 Token Hard Stop:** The DA token counter is strict.
3. **The Rubric Validator Death Trap:** Do not use quotation marks, and every criterion must start with exactly "The response should".
4. **The Ghost Anonymizer:** The built-in PII tool is glitchy; verify outputs manually.
