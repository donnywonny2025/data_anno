# Playwright Python: Stealth & HITL Cheatsheet

This cheatsheet covers the essential Playwright Python patterns needed for the Human-in-the-Loop (HITL) stealth architecture, explicitly designed for use with Camoufox.

## 1. Initializing the Agent
We use `camoufox.async_api.AsyncCamoufox` which perfectly wraps Playwright's browser instance.

```python
import asyncio
from camoufox.async_api import AsyncCamoufox

async def main():
    # Geoip=True matches IP timezone. Headless=False lets the human see and solve CAPTCHAs.
    async with AsyncCamoufox(headless=False, geoip=True) as browser:
        page = await browser.new_page()
        await page.goto("https://tasks.dataannotation.tech")
        # Proceed with logic...
```

## 2. Using Playwright Selectors Safely
Do not use `page.click()` or `page.fill()` natively if you are absolutely paranoid about detection, as they dispatch perfectly centered clicks and instant typing. Wait for elements instead:

```python
# Just find the element box, don't interact directly via DOM API
element = page.locator("#submit-button")
await element.wait_for(state="visible")
box = await element.bounding_box()

if box:
    # box['x'], box['y'], box['width'], box['height']
    target_x = box['x'] + (box['width'] / 2)
    target_y = box['y'] + (box['height'] / 2)
```

## 3. Human-like Mouse Movement (The "Hands")
To bypass trajectory analysis, you must move the mouse before clicking.

```python
# Using Playwright's underlying mouse controller
await page.mouse.move(target_x, target_y, steps=10) # steps interpolates movement
await page.mouse.down()
await asyncio.sleep(0.05) # Random human click delay
await page.mouse.up()
```
*Note: For perfect Bezier curves, use a Python port of `ghost-cursor` to calculate the x/y steps over a curve.*

## 4. Human-like Typing (Gaussian Delays)
Do not use `page.fill("Some text")`. It types instantly.
Do not use `page.type("Some text", delay=100)`. It types with a perfectly robotic 100ms interval.

```python
import random

async def human_type(page, text):
    for char in text:
        # Mean 85ms delay, standard deviation 35ms, floor at 30ms
        delay = max(0.03, random.gauss(0.085, 0.035))
        await page.keyboard.press(char, delay=delay * 1000) # Playwright expects ms

        # Inject "Thinking Pauses" during long strings
        if random.random() < 0.05: # 5% chance of a pause
            await asyncio.sleep(random.uniform(0.5, 1.5))
```

## 5. The HITL Pause (Human In The Loop)
When the AI encounters a CAPTCHA or needs human review before submitting text:

```python
print("🚨 INTERVENTION REQUIRED: Please solve the CAPTCHA in the browser window.")
print("Type 'y' and press Enter here when you are done.")
await asyncio.to_thread(input, "Ready to resume? [y]: ")
print("✅ Resuming agent workflow...")
```
*Because Playwright is async, we use `asyncio.to_thread(input, ...)` to pause the Python execution and wait for the terminal input without blocking the asyncio event loop.*
