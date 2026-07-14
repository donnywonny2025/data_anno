import os
import re

file_path = "/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/Metis/Samples/Michigan Weekend Recap Image Creation - Google Gemini.html"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace exact name
    content = content.replace("Jeff Kerr", "name")
    
    # Let's search for any text that looks like an email and replace it
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    content = email_pattern.sub("email", content)

    # Search for encoded emails (&#64; or %40)
    encoded_email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+(?:&#64;|%40)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    content = encoded_email_pattern.sub("email", content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Replacement complete.")
except Exception as e:
    print(f"Error: {e}")
