import asyncio
from camoufox.async_api import AsyncCamoufox

async def check_stealth():
    print("🦊 [GHOST FOX] Starting Diagnostic Stealth Check...")
    async with AsyncCamoufox(headless=False, geoip=True) as browser:
        context = await browser.new_context()
        page = await context.new_page()
        
        # Test 1: SannySoft Fingerprint Test
        print("🔍 [CHECK] Testing SannySoft (WebDriver/UA/Platform)...")
        await page.goto("https://bot.sannysoft.com/")
        await asyncio.sleep(5)
        await page.screenshot(path="/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/ghost_fox/data/screenshots/sannysoft_check.png")
        
        # Test 2: PixelScan Bot Check
        print("🔍 [CHECK] Testing PixelScan (Inconsistency/Bot Detection)...")
        await page.goto("https://pixelscan.net/")
        await asyncio.sleep(8) # PixelScan is slow
        await page.screenshot(path="/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/ghost_fox/data/screenshots/pixelscan_check.png")
        
        print("✅ [GHOST FOX] Diagnostic complete. Check screenshots in data/screenshots/")

if __name__ == "__main__":
    asyncio.run(check_stealth())
