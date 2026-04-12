import re
import os

input_file = "/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/melissa_texts_context.txt"
output_file = "/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/SAFE_anonymized_context.txt"

# This mapping table is derived exactly from the user's Data Annotation "Map PII" output
# We use regex word boundaries \b to ensure we don't accidentally replace parts of words
# Note: we handle specific multi-word phrases first to prevent partial replacements.

mapping = {
    # Full Names / Complex
    r'\bMs\. Smith\b': 'Ms. Miller',
    r'\bJeff Kerr\b': 'Mark Davis',
    r'\bLinsey Kerr\b': 'Rachel Davis',
    r'\bDebby Kerr\b': 'Susan Davis',
    r'\bDon Kerr\b': 'Robert Davis',
    r'\bAndrea Curry\b': 'Jessica Park',
    r'\bAction Behavior Centers\b': 'Apex Therapy Centers',
    r'\bSERA MUSIC LLC\.\b': 'AURA SOUND LLC.',
    r'\bUniversal LLC\.\b': 'Global LLC.',
    
    # Locations
    r'\bGun Lake\b': 'Silver Lake',
    r'\bMaricopa County\b': 'Pima County',
    r'\bCape Canaveral\b': 'Cocoa Beach',
    r'\bGrand Rapids\b': 'Chicago', # Handled Kalamazoo mapping locally
    r'\bKalamazoo\b': 'Grand Rapids',
    r'\bWayland\b': 'Holland',
    r'\bScottsdale\b': 'Chandler',
    r'\bTempe\b': 'Mesa',
    r'\bPhoenix\b': 'Tucson',
    r'\bPasco\b': 'Hernando',
    r'\bOrlando\b': 'Tampa',
    r'\bTitusville\b': 'Melbourne',
    r'\bDetroit\b': 'Chicago',
    r'\bkazoo\b': 'GR',
    
    # Addresses
    r'140 Inkster Ave Kalamazoo, MI 49008': '250 Maple St Grand Rapids, MI 49503',
    r'140 Inkster Kalamazoo, MI\. 49001': '250 Maple Grand Rapids, MI. 49504',
    r'1176 E Grey court Wayland, Mi 49348': '3402 W Oak Ln Holland, MI 49424',
    r'1176 East Grey Court Wayland, MI\. 49348': '3402 West Oak Lane Holland, MI. 49424',
    
    # IDs / Dates
    r'12/13/1980': '11/14/1981',
    r'02/03/1948': '04/05/1949',
    r'12/08/1950': '10/10/1951',
    r'January 1st': 'February 2nd',
    r'\b1 Nuk 26\b': '3 Abc 45',
    r'\bHJJG36\b': 'KLMN78',
    r'\bPQDxNS4odgLtY2xR8\b': 'A1B2C3D4E5F6G7H8I',
    
    # Money
    r'\$1288': '$1150',
    r'\$215': '$250',
    r'\$81': '$75',
    r'\$92\.00': '$85.00',
    
    # single names
    r'\bMelissa\b': 'Sarah',
    r'\bSmith\b': 'Miller',
    r'\bJeff\b': 'Mark',
    r'\bKerr\b': 'Davis',
    r'\bJude\b': 'Leo',
    r'\bJudester\b': 'Leoster',
    r'\bJudster\b': 'Leoster',
    r'\bJudas\b': 'Leon',
    r'\bLincoln\b': 'Carter',
    r'\bLink\b': 'Cart',
    r'\bLarry\b': 'Gary',
    r'\bDawn\b': 'Diane',
    r'\bLinsey\b': 'Rachel',
    r'\bLinsey’s\b': "Rachel's",
    r'\bDebby\b': 'Susan',
    r'\bDon\b': 'Robert',
    r'\bAustin\b': 'Tyler',
    r'\bBrandi\b': 'Chloe',
    r'\bEric\b': 'Brian',
    r'\bEvonne\b': 'Yvonne',
    r'\bChris\b': 'Kevin',
    r'\bJosh\b': 'Ryan',
    r'\bShawn\b': 'Derek',
    r'\bJose\b': 'Luis',
    r'\bDavid\b': 'Jason',
    r'\bSteve\b': 'Alan',
    r'\bLynda\b': 'Nancy',
    r'\bAndrea\b': 'Jessica',
    r'\bCurry\b': 'Park',
    r'\bAC\b': 'JP',
    r'\bDexter\b': 'Buster',
    r'\bDex\b': 'Buster'
}

def anonymize_text(text):
    for pattern, replacement in mapping.items():
        # Using regex substitution with IGNORECASE could be risky on names like "link" or names
        # We will use exact case match for safety to avoid ruining the text flow too badly, except where noted
        text = re.sub(pattern, replacement, text)
    return text

with open(input_file, 'r', encoding='utf-8') as f:
    original_content = f.read()

scrambled_content = anonymize_text(original_content)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(scrambled_content)

print(f"Successfully generated anonymized file at {output_file}")
