import asyncio
import os
import sys

# Add Lemmings python path if needed (contains crawl4ai)
sys.path.append("/Volumes/WORK 2TB/WORK 2026/Lemmings/execution")

async def run_detection_tests(url):
    print(f"🚀 Launching Detection Test on: {url}")
    
    # Internal paths within the AGENTMONEY workspace
    crawl_script = "/Volumes/WORK 2TB/SAVE/AGENTMONEY/execution/crawl_job.py"
    venv_python = "/Volumes/WORK 2TB/WORK 2026/Lemmings/.venv/bin/python3"
    
    # Run the crawl and capture result
    cmd = f'"{venv_python}" "{crawl_script}" "{url}"'
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    stdout, stderr = await process.communicate()
    
    result_path = "/Volumes/WORK 2TB/SAVE/AGENTMONEY/STEALTH_AGENT/execution/last_test_result.md"
    
    if process.returncode == 0:
        print(f"✅ Crawl successful. Result saved to {result_path}")
        with open(result_path, "wb") as f:
            f.write(stdout)
    else:
        print(f"❌ Crawl failed with code {process.returncode}")
        print(stderr.decode())

if __name__ == "__main__":
    # Test Targets:
    # 1. SannySoft: https://bot.sannysoft.com/
    # 2. PixelScan: https://pixelscan.net/
    # 3. Cloudflare: https://www.nowsecure.nl/
    
    target = sys.argv[1] if len(sys.argv) > 1 else "https://bot.sannysoft.com/"
    asyncio.run(run_detection_tests(target))
