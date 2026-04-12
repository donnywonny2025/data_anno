import asyncio
import random
import numpy as np

# Ghost Fox - Stealth Engine
# Primitives for human-like interaction.

async def human_type(page, selector, text):
    """Types text with randomized delays and slight pauses."""
    try:
        await page.locator(selector).first.scroll_into_view_if_needed()
        await page.locator(selector).first.click()
    except:
        pass
    
    await asyncio.sleep(random.uniform(0.1, 0.3))
    for char in text:
        # Randomized delay between keystrokes (Gaussian distribution)
        delay = max(0.01, random.gauss(0.05, 0.02))
        await page.keyboard.press(char, delay=delay * 1000)
        
        # Occasional "thinking" pause
        if random.random() < 0.05:
            await asyncio.sleep(random.uniform(0.2, 0.6))
            
    await asyncio.sleep(0.1)

async def human_mouse_move(page, target_x, target_y):
    """Moves mouse in a non-linear, human-like curve."""
    # This is a placeholder for Bezier curve movements
    # For now, we use a simple jittery linear move
    curr_x, curr_y = 0, 0 # In a real system, we'd track last pos
    
    steps = 10
    for i in range(steps):
        # Add slight jitter to the path
        x = curr_x + (target_x - curr_x) * (i / steps) + random.uniform(-2, 2)
        y = curr_y + (target_y - curr_y) * (i / steps) + random.uniform(-2, 2)
        await page.mouse.move(x, y)
        await asyncio.sleep(random.uniform(0.01, 0.03))

async def human_click(page, selector):
    """Clicks an element with a slight hesitation."""
    try:
        element = page.locator(selector).first
        box = await element.bounding_box()
        if box:
            center_x = box["x"] + box["width"] / 2 + random.uniform(-2, 2)
            center_y = box["y"] + box["height"] / 2 + random.uniform(-2, 2)
            
            await human_mouse_move(page, center_x, center_y)
            await asyncio.sleep(random.uniform(0.1, 0.2))
            await page.mouse.down()
            await asyncio.sleep(random.uniform(0.05, 0.15))
            await page.mouse.up()
            return True
    except:
        return False
    return False
