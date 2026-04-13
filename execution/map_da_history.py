import os
import sys
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        return build('gmail', 'v1', credentials=creds)
    return None

def main():
    service = get_gmail_service()
    if not service:
        print("Error: token.json not found")
        return

    print("Fetching entire Data Annotation email history for mapping...")
    
    try:
        # Search all emails from Data Annotation, up to 100
        query = 'from:noreply@mail.dataannotation.tech'
        results = service.users().messages().list(userId='me', q=query, maxResults=100).execute()
        messages = results.get('messages', [])
        
        if not messages:
            print("No Data Annotation emails found in history.")
            return
            
        history = []
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id'], format='metadata', metadataHeaders=['Subject', 'Date']).execute()
            headers = msg.get('payload', {}).get('headers', [])
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown Date')
            
            history.append({
                "date": date,
                "subject": subject
            })
            
        with open('war_room/RESEARCH/da_email_history.json', 'w') as f:
            json.dump(history, f, indent=4)
            
        print(f"Successfully dumped {len(history)} historical emails to war_room/RESEARCH/da_email_history.json")
            
    except Exception as e:
        print(f"Extraction failed: {e}")

if __name__ == '__main__':
    main()
