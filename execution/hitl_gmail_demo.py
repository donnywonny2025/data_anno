import asyncio
import random
from camoufox.async_api import AsyncCamoufox

async def human_type(page, text):
    """Types text with Gaussian delays to simulate human typing rhythm"""
    for char in text:
        delay = max(0.03, random.gauss(0.085, 0.035))
        await page.keyboard.press(char, delay=delay * 1000)
        
        if random.random() < 0.05:
            await asyncio.sleep(random.uniform(0.3, 0.8))

async def main():
    print("🦊 Launching HITL (Human-in-the-Loop) Gmail Demo...")
    
    # Keeping default viewport/sizing to remain perfectly stealthy
    async with AsyncCamoufox(headless=False, geoip=True) as browser:
        page = await browser.new_page()
        
        print("🌐 Navigating to Gmail...")
        await page.goto("https://mail.google.com/")
        print("✅ Arrived at Gmail.")
        
        print("===============")
        print("⏳ WAITING FOR HUMAN")
        print("Please physically click into the 'Email or phone' box in the browser window.")
        print("The script is completely paused and waiting for the CLI 'Go' signal.")
        print("===============")
        
        # Pause script execution entirely until it receives an enter key via terminal stdin
        await asyncio.to_thread(input)
        
        print("⌨️ CONTINUING: Taking control to type the email address...")
        # Using page.keyboard.type automatically types into whatever element the user already clicked
        await human_type(page, "stealth.agent.test@gmail.com")
        
        print("✅ Typing complete! Handing control back to the human.")
        print("⏳ Browser will stay open for 10 minutes.")
        await asyncio.sleep(600)

if __name__ == "__main__":
    asyncio.run(main())
