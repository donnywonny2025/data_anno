import os

src = '/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/SAFE_anonymized_context.txt'
dst = '/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/MOMO_FINAL_VERIFIED.txt'
prompt = '\n\n<|TASK|>\n\nAnalyze the trajectory of this interpersonal relationship. Identify the specific moment (date and message content) where the co-parenting dynamic fundamentally collapsed into adversarial hostility. Explain the reasoning behind why this specific moment constitutes the "point of no return" compared to earlier disagreements, citing evidence from the context.'

with open(src, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# HARD SCRUB: Remove any line that HAS triple backticks
clean_lines = [line for line in lines if '```' not in line]

# Ensure it starts with the actual content
while clean_lines and not clean_lines[0].strip():
    clean_lines.pop(0)

with open(dst, 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)
    f.write(prompt)

print(f"SCRUBBED. File start: {clean_lines[0].strip()[:50]}")
