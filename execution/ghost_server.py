import asyncio
import os
import traceback
from camoufox.async_api import AsyncCamoufox

COMMAND_FILE = "/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/execution/current_command.py"

async def main():
    print("🦊 Ghost Server booting...")
    
    # We pass geoip=True to match ISP geolocation
    # Headless=False because the user physically interacts with it
    async with AsyncCamoufox(headless=False, geoip=True) as browser:
        # no_viewport=True tells Playwright to stop enforcing a strict bounding box
        # This completely fixes the "white borders / bad scaling" issue when the user manually resizes the window!
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()
        
        print("\n✅ Ghost Server Online.")
        print(f"👀 Watching `{COMMAND_FILE}` for live execution payloads...")
        print("   (The browser will NOT close. Waiting for instructions...)")
        
        # Touch the command file to ensure it exists
        if not os.path.exists(COMMAND_FILE):
            with open(COMMAND_FILE, "w") as f:
                f.write("# Write async code here. `page` is available globally.\n")
        
        # Track file modification time to know when a new command is injected
        last_mtime = os.path.getmtime(COMMAND_FILE)
        
        while True:
            try:
                mtime = os.path.getmtime(COMMAND_FILE)
                if mtime > last_mtime:
                    last_mtime = mtime
                    
                    with open(COMMAND_FILE, "r") as f:
                        code = f.read()
                    
                    # Ensure it is an actual command, not just empty comments
                    if any(line.strip() and not line.strip().startswith('#') for line in code.split('\n')):
                        print(f"\n📦 New payload detected! Executing...")
                        
                        # Wrap the dynamic code in an async function so we can await it
                        wrapper = "async def execute_payload(page, browser, context):\n"
                        for line in code.split("\n"):
                            wrapper += f"    {line}\n"
                        
                        # Compile and evaluate the wrapper function
                        env = globals().copy()
                        exec(wrapper, env)
                        
                        # Execute the payload in the active browser
                        await env['execute_payload'](page, browser, context)
                        print("✅ Payload execution complete. Listening for next command...")
            except Exception as e:
                print("\n❌ Error executing payload:")
                traceback.print_exc()
            
            # Tick every half second
            await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())
