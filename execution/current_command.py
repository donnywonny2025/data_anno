import asyncio
import random

async def human_type(page, selector, text):
    try:
        await page.locator(selector).first.scroll_into_view_if_needed()
        await page.locator(selector).first.click()
    except:
        pass
    await asyncio.sleep(0.1)
    for char in text:
        delay = max(0.01, random.gauss(0.04, 0.015))
        await page.keyboard.press(char, delay=delay * 1000)
    await asyncio.sleep(0.1)

# Type the name and email into the actual form fields
print("Typing First Name...")
await human_type(page, "input#first_name", "Jeffery")
print("Typing Last Name...")
await human_type(page, "input#last_name", "Kerr")
print("Typing Email...")
await human_type(page, "input#email", "colour8k@mac.com")
print("Typing Email Confirmation...")
await human_type(page, "input#email_confirmation", "colour8k@mac.com")

# Take evidence screenshot
await page.screenshot(path="/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/execution/form_typing_proof.png")
print("✅ Typed info into the fields. Proof captured.")
