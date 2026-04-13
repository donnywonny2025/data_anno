import asyncio
from playwright.async_api import async_playwright

async def main():
    print("🚀 Launching standard Playwright Browser to take control...")
    print("I will navigate directly to the GCP Audience page.")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        await page.goto("https://console.cloud.google.com/auth/audience")
        
        print("\n⏳ ACTION REQUIRED: You must physically enter your password. Google will not let my scripts type it.")
        print("Once you are logged in and the 'Audience' page fully loads, my script will take over and click the buttons.")
        
        # Wait infinitely for the page to load the "+ Add users" element
        try:
            add_user_btn = page.locator('button', has_text="Add users")
            await add_user_btn.wait_for(state="visible", timeout=0)  # 0 means wait forever until you log in
            print("✅ Detected the console screen! Taking control of the UI...")
            
            # Click the ADD USERS button
            await add_user_btn.click()
            print("🖱️ Clicked '+ Add users'")
            
            # Now wait for the user to type in their email if they want, or we can try to fill it
            print("Please type jefferykerr@gmail.com and hit save!")
            
            await asyncio.to_thread(input, "\nPress ENTER in this terminal when it is completely done > ")

        except Exception as e:
            print(f"Error during automation: {e}")

if __name__ == "__main__":
    asyncio.run(main())
