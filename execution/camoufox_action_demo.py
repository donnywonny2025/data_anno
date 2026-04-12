import asyncio
import random
from camoufox.async_api import AsyncCamoufox

async def human_type(page, text):
    """Types text with Gaussian delays to simulate human typing rhythm"""
    for char in text:
        # Mean 85ms delay, standard deviation 35ms, absolute minimum 30ms
        delay = max(0.03, random.gauss(0.085, 0.035))
        await page.keyboard.press(char, delay=delay * 1000)
        
        # 5% chance of a "thinking pause"
        if random.random() < 0.05:
            await asyncio.sleep(random.uniform(0.3, 0.8))

async def human_mouse_move(page, start_x, start_y, end_x, end_y, steps=25):
    """Moves mouse smoothly from current position to target using an easing function"""
    for i in range(1, steps + 1):
        t = i / steps
        # Simple ease-in-out curve
        ease_t = t * t * (3 - 2 * t) 
        
        current_x = start_x + (end_x - start_x) * ease_t
        current_y = start_y + (end_y - start_y) * ease_t
        
        # Add tiny jitter (human noise)
        jitter_x = random.uniform(-1, 1)
        jitter_y = random.uniform(-1, 1)
        
        await page.mouse.move(current_x + jitter_x, current_y + jitter_y)
        await asyncio.sleep(0.015)

async def main():
    print("🦊 Launching Camoufox Action Demo...")
    async with AsyncCamoufox(headless=False, geoip=True) as browser:
        page = await browser.new_page()
        
        url = "https://en.wikipedia.org/wiki/Main_Page"
        print(f"🌐 Navigating to {url}")
        await page.goto(url)
        await asyncio.sleep(2) # Give the human a moment to look
        
        print("🖱️ Finding search box coordinates using the DOM...")
        search_input = page.locator("input[name='search']").first
        box = await search_input.bounding_box()
        
        if box:
            target_x = box['x'] + (box['width'] / 2)
            target_y = box['y'] + (box['height'] / 2)
            
            print("🚀 Moving mouse to search box with human easing...")
            # Start mouse from arbitrary off-screen point
            await human_mouse_move(page, 5, 5, target_x, target_y)
            
            # Human click (down, short random wait, up)
            await page.mouse.down()
            await asyncio.sleep(random.uniform(0.05, 0.12))
            await page.mouse.up()
            
            print("⌨️ Typing search query with Gaussian rhythm...")
            await human_type(page, "Artificial general intelligence")
            
            await asyncio.sleep(0.4) # Pause before hitting enter
            print("⏎ Pressing Enter...")
            await page.keyboard.press("Enter")
            
        print("✅ Action complete. The browser will close in 30 seconds.")
        await asyncio.sleep(30)
        print("Done.")

if __name__ == "__main__":
    asyncio.run(main())
