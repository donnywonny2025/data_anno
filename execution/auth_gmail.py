import asyncio
from camoufox.async_api import AsyncCamoufox

async def main():
    print("🦊 Launching Stealth Browser to authenticate Gmail...")
    print("This will save your session locally so we never have to do this again.")
    print("---------------------------------------------------------")
    
    # We use a user_data_dir to persistently save the cookies/session state
    # Notice we removed user_data_dir from AsyncCamoufox and we instead use storage_state inside new_context
    async with AsyncCamoufox(headless=False) as browser:
        # Create a persistent context, so your login writes a json file 
        # that we can use to bypass login later
        context = await browser.new_context()
        page = await context.new_page()
        
        await page.goto("https://mail.google.com/")
        
        print("\n⏳ WAITING FOR HUMAN AUTHENTICATION")
        print("Please click your account and log into Gmail in the browser window.")
        print("Once you can see your Inbox, press ENTER in this terminal.")
        
        # Pause script execution entirely until it receives an enter key
        await asyncio.to_thread(input, "Press ENTER here when you fully see your inbox > ")
        
        # Save state manually on context
        import os
        os.makedirs(os.path.dirname("./.camoufox_env/gmail_profile/state.json"), exist_ok=True)
        await context.storage_state(path="./.camoufox_env/gmail_profile/state.json")
        
        print("✅ Session saved securely into ./.camoufox_env/gmail_profile/state.json")
        print("I am shutting down the visible browser. I now have permanent, stealth access.")

if __name__ == "__main__":
    asyncio.run(main())
