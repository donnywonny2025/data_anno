import asyncio
from camoufox.async_api import AsyncCamoufox

async def main():
    print("🦊 Launching Camoufox in headful mode...")
    
    async with AsyncCamoufox(headless=False, geoip=True) as browser:
        page = await browser.new_page()
        
        url = "https://bot.sannysoft.com/"
        print(f"🌐 Navigating to {url}")
        
        await page.goto(url)
        
        print("✅ Page loaded!")
        print("⏳ The browser will now stay open for 1 HOUR so you can inspect.")
        print("   Feel free to browse around, open new tabs, and check out other sites like pixelscan.net.")
        print("   You can close the browser manually when you're done.")
        
        # Keep open for 1 hour so user can inspect or close it manually
        await asyncio.sleep(3600)
        
        print("Done. Closing browser securely.")

if __name__ == "__main__":
    asyncio.run(main())
