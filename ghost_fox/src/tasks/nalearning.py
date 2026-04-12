import asyncio
import random

# Task: NALearning Student Registration
# This module handles the automated form-filling for NALearning.org

async def fill_registration_form(page, user_data):
    """Fills the registration form using human-like interaction."""
    from ghost_fox.src import stealth
    
    # Navigation
    if "student/register/create" not in page.url:
        await page.goto("https://nalearning.org/student/register/create")
        # Handle disclosures/continue
        try:
            print("[*] Attempting to click 'Continue'...")
            await page.click("button:has-text('Continue')", timeout=5000)
            await asyncio.sleep(random.uniform(1, 2))
            print("[*] Attempting to click 'Accept'...")
            await page.click("button:has-text('Accept')", timeout=5000)
            await asyncio.sleep(random.uniform(1, 2))
        except Exception as e:
            print(f"[!] FAILED to find NALearning disclosure buttons: {e}")
            print("[!] WARNING: The 'Accept' flow may have changed. Stopping for human intervention.")
            # We don't 'pass' here; we alert the orchestrator.
            raise Exception("REDCAP_INTERVENTION_REQUIRED: Could not bypass disclosure wall.")

    # Populate name
    print(f"✍️ Filling name: {user_data.get('first_name')}...")
    await stealth.human_type(page, "input#first_name", user_data.get('first_name'))
    await stealth.human_type(page, "input#last_name", user_data.get('last_name'))
    
    # Populate contact info
    print(f"✍️ Filling email: {user_data.get('email')}...")
    await stealth.human_type(page, "input#email", user_data.get('email'))
    await stealth.human_type(page, "input#email_confirmation", user_data.get('email'))
    
    # Populate phone
    print(f"✍️ Filling phone: {user_data.get('phone')}...")
    await stealth.human_type(page, "input#phone_number", user_data.get('phone'))
    
    print("✅ Form filled (not submitted).")
