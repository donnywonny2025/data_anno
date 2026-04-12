import asyncio
import os
import traceback
from camoufox.async_api import AsyncCamoufox
from browserforge.fingerprints import Screen

# Local imports
import ghost_cursor
import stealth
import icrawl
from tasks import nalearning

# Ghost Fox - Persistent Stealth Server
# This manages the single, persistent Camoufox instance.

COMMAND_FILE = "/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/ghost_fox/execution/current_command.py"

async def run_server():
    print("🦊 [GHOST FOX] Starting Persistent Stealth Server...")
    
    screen_constraint = Screen(max_width=1920, max_height=1080)
    async with AsyncCamoufox(
        headless=False, 
        geoip=True,
        screen=screen_constraint,
    ) as browser:
        # Use a fluid viewport so the page resizes with the window
        context = await browser.new_context(viewport=None)
        page = await context.new_page()
        
        # Initial navigation to show life
        await page.goto("https://nalearning.org/student/register/create")
        print("🌍 [GHOST FOX] Browser ready at NALearning.")

        last_mtime = 0
        while True:
            try:
                if os.path.exists(COMMAND_FILE):
                    current_mtime = os.path.getmtime(COMMAND_FILE)
                    if current_mtime > last_mtime:
                        print("\n📦 [GHOST FOX] New payload detected! Executing...")
                        with open(COMMAND_FILE, "r") as f:
                            code = f.read()
                        
                        try:
                            # 🛠 Refined Async Execution Wrapper
                            # This allows us to use 'await', 'page', 'context', and 'asyncio' in the bridge file
                            namespace = {
                                "page": page, 
                                "context": context, 
                                "asyncio": asyncio,
                                "ghost_cursor": ghost_cursor,
                                "stealth": stealth,
                                "icrawl": icrawl,
                                "nalearning": nalearning,
                                "__name__": "__main__"
                            }
                            
                            # Wrap the command code in an async function
                            indented_code = "\n".join(f"    {line}" for line in code.split("\n"))
                            wrapper_script = (
                                f"async def __ghost_wrapper():\n"
                                f"{indented_code}\n"
                            )
                            
                            exec(wrapper_script, namespace)
                            await namespace["__ghost_wrapper"]()
                            
                            print("✅ [GHOST FOX] Payload execution complete. Listening...")
                        except Exception as e:
                            print(f"❌ [GHOST FOX] Execution Error:\n{traceback.format_exc()}")
                        
                        last_mtime = current_mtime
            except Exception:
                print(f"⚠️ [GHOST FOX] Server Loop Error:\n{traceback.format_exc()}")
            
            await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(run_server())
