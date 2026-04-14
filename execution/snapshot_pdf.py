import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    print("Attempting to connect to Chrome over CDP to generate PDF...")
    try:
        async with async_playwright() as p:
            browser = await p.chromium.connect_over_cdp("http://localhost:9222")
            
            da_page = None
            for context in browser.contexts:
                for page in context.pages:
                    if "app.dataannotation.tech/workers" in page.url:
                        da_page = page
                        break
            
            if not da_page:
                print("Could not find the DA dashboard. Make sure it is open.")
                return
                
            print("Found DA Dashboard. Generating PDF...")
            # We must use emulated print media for better PDF formatting
            await da_page.emulate_media(media="print")
            
            output_path = os.path.join(os.getcwd(), "war_room/DATA_DROP/da_dashboard.pdf")
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # The 'pdf' method might throw in headful mode, let's see
            await da_page.pdf(path=output_path, format="A4", print_background=True)
            print(f"✅ Success! PDF saved to {output_path}")
            
            await da_page.emulate_media(media="screen") # Reset
            
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())
