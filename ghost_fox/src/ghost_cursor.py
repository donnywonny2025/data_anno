import asyncio
import random
import math
import numpy as np

# Ghost-Cursor: Advanced Human Mouse Pathing
# Generates non-linear Bezier curves with randomized overshoot and jitter.

def _get_bezier_point(p0, p1, p2, p3, t):
    """Calculates a point on a cubic Bezier curve."""
    return (
        (1-t)**3 * p0 + 
        3*(1-t)**2 * t * p1 + 
        3*(1-t) * t**2 * p2 + 
        t**3 * p3
    )

async def move_to(page, target_x, target_y, steps=100):
    """Moves mouse to target using a cubic Bezier curve."""
    # Start position (could be tracked, for now we assume a random start or center)
    # Ideally the server should track current_x, current_y
    start_x, start_y = 500, 500 
    
    # Control points for the curve
    cp1_x = start_x + (target_x - start_x) * random.uniform(0.1, 0.4) + random.uniform(-100, 100)
    cp1_y = start_y + (target_y - start_y) * random.uniform(0.1, 0.4) + random.uniform(-100, 100)
    
    cp2_x = target_x - (target_x - start_x) * random.uniform(0.1, 0.4) + random.uniform(-100, 100)
    cp2_y = target_y - (target_y - start_y) * random.uniform(0.1, 0.4) + random.uniform(-100, 100)
    
    for i in range(steps + 1):
        t = i / steps
        # Human-like speed curve (acceleration/deceleration)
        # We can use a sine or ease-in-out function for 't'
        velocity_t = (1 - math.cos(t * math.pi)) / 2
        
        x = _get_bezier_point(start_x, cp1_x, cp2_x, target_x, velocity_t)
        y = _get_bezier_point(start_y, cp1_y, cp2_y, target_y, velocity_t)
        
        # Micro-jitter
        jitter_x = random.uniform(-0.5, 0.5)
        jitter_y = random.uniform(-0.5, 0.5)
        
        await page.mouse.move(x + jitter_x, y + jitter_y)
        
        # Variable sleep to simulate human muscle reaction times
        await asyncio.sleep(random.uniform(0.005, 0.015))

async def click_element(page, selector):
    """Realistic movement to and click of an element."""
    element = page.locator(selector).first
    box = await element.bounding_box()
    if not box:
        return False
        
    # Pick a random point inside the bounding box (avoiding the exact center)
    padding = 5
    target_x = box["x"] + random.uniform(padding, box["width"] - padding)
    target_y = box["y"] + random.uniform(padding, box["height"] - padding)
    
    await move_to(page, target_x, target_y)
    await asyncio.sleep(random.uniform(0.1, 0.3)) # Hesitation
    await page.mouse.down()
    await asyncio.sleep(random.uniform(0.05, 0.15)) # Hold time
    await page.mouse.up()
    return True
