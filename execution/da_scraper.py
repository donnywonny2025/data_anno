import asyncio
import json
import os
from datetime import datetime
from playwright.async_api import async_playwright

TRACKER_FILE = "war_room/TASK_LOG/da_projects_tracker.json"
SCREENSHOT_FILE = "screenshots/da_dashboard_latest.png"

def load_previous_state():
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return {"qualifications": {}, "projects": {}}
    return {"qualifications": {}, "projects": {}}

def save_state(state):
    os.makedirs(os.path.dirname(TRACKER_FILE), exist_ok=True)
    with open(TRACKER_FILE, "w") as f:
        json.dump(state, f, indent=4)

async def scrape_dashboard(page):
    """Extract projects and qualifications with exact differentiation."""
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] 🔍 Scanning dashboard and capturing screen...")
    
    try:
        await page.wait_for_selector("table", timeout=10000)
    except:
        print("⚠️ Dashboard not fully loaded or no projects found.")
        return None
        
    os.makedirs("screenshots", exist_ok=True)
    await page.screenshot(path=SCREENSHOT_FILE, full_page=True)
    
    data = {"qualifications": {}, "projects": {}}
    
    # Try to find the qualifications section
    # Usually it's under a heading "Qualifications"
    qual_headers = await page.locator("h1, h2, h3", has_text="Qualifications").all()
    if qual_headers:
        # Find the first table after this header
        qual_table = page.locator("h1, h2, h3", has_text="Qualifications").locator("~ * table, ~ table").first
        if await qual_table.count() == 0:
            # Fallback: look for the closest table in the DOM flow
            qual_table = page.locator("xpath=//*[(self::h1 or self::h2 or self::h3) and contains(text(), 'Qualifications')]/following::table[1]")
        
        if await qual_table.count() > 0:
            rows = await qual_table.locator("tr").all()
            for row in rows:
                cells = await row.locator("td").all_inner_texts()
                if len(cells) >= 3:
                    name, pay, tasks = cells[0].strip(), cells[1].strip(), cells[2].strip()
                    if name and name.lower() != 'name':
                        data["qualifications"][name] = {"pay": pay, "tasks": tasks, "last_seen": datetime.now().isoformat()}

    # Try to find the projects section
    proj_headers = await page.locator("h1, h2, h3", has_text="Projects").all()
    if proj_headers:
        proj_table = page.locator("h1, h2, h3", has_text="Projects").locator("~ * table, ~ table").first
        if await proj_table.count() == 0:
            proj_table = page.locator("xpath=//*[(self::h1 or self::h2 or self::h3) and contains(text(), 'Projects')]/following::table[1]")
            
        if await proj_table.count() > 0:
            rows = await proj_table.locator("tr").all()
            for row in rows:
                # Need to handle potential nested tables or weird formatting, just get raw cells
                cells = await row.locator("td").all_inner_texts()
                if len(cells) >= 3:
                    name, pay, tasks = cells[0].strip(), cells[1].strip(), cells[2].strip()
                    if name and name.lower() != 'name':
                        data["projects"][name] = {"pay": pay, "tasks": tasks, "last_seen": datetime.now().isoformat()}
                        
    # Fallback if the strict header->table finding failed (e.g., nested differently)
    if not data["qualifications"] and not data["projects"]:
        print("⚠️ Strict header parsing fell through. Falling back to multi-table heuristic...")
        tables = await page.locator("table").all()
        if len(tables) == 2:
            # Table 0 is Quals, Table 1 is Projects
            for t_idx, category in enumerate(["qualifications", "projects"]):
                rows = await tables[t_idx].locator("tr").all()
                for row in rows:
                    cells = await row.locator("td").all_inner_texts()
                    if len(cells) >= 3:
                        name = cells[0].strip()
                        if name and name.lower() != 'name':
                            data[category][name] = {"pay": cells[1].strip(), "tasks": cells[2].strip(), "last_seen": datetime.now().isoformat()}
        elif len(tables) == 1:
            # Assume all are projects if there's only one table
            rows = await tables[0].locator("tr").all()
            for row in rows:
                cells = await row.locator("td").all_inner_texts()
                if len(cells) >= 3:
                    name = cells[0].strip()
                    if name and name.lower() != 'name':
                        data["projects"][name] = {"pay": cells[1].strip(), "tasks": cells[2].strip(), "last_seen": datetime.now().isoformat()}

    return data

async def main():
    print("🚀 Connecting to your active Chrome session via CDP...")
    
    async with async_playwright() as p:
        try:
            browser = await p.chromium.connect_over_cdp("http://localhost:9222")
            
            da_page = None
            for context in browser.contexts:
                for page in context.pages:
                    if "app.dataannotation.tech/workers" in page.url:
                        da_page = page
                        break
            
            if not da_page:
                print("🌐 DA dashboard not found in tabs. Please open it!")
                return
            
            print("✅ Tracking started. I will screenshot and scan every 60 seconds.")
            
            previous_state = load_previous_state()
            
            while True:
                current_data = await scrape_dashboard(da_page)
                
                if current_data:
                    new_quals = 0
                    for name, data in current_data['qualifications'].items():
                        if name not in previous_state.get('qualifications', {}):
                            print(f"🌟 NEW QUALIFICATION: {name} | {data['pay']} | Tasks: {data['tasks']}")
                            new_quals += 1
                            
                    new_projs = 0
                    for name, data in current_data['projects'].items():
                        if name not in previous_state.get('projects', {}):
                            print(f"🚨 NEW PROJECT: {name} | {data['pay']} | {data['tasks']}")
                            new_projs += 1
                            
                    if new_quals == 0 and new_projs == 0:
                        print(f"💤 No new items detected. (Quals: {len(current_data['qualifications'])} | Projects: {len(current_data['projects'])})")
                        
                    previous_state = current_data
                    save_state(previous_state)
                
                await asyncio.sleep(60)
                await da_page.reload()
                
        except Exception as e:
            print(f"❌ Error connecting to Chrome: {e}")

if __name__ == "__main__":
    asyncio.run(main())
