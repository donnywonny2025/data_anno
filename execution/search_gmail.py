import os
import sys
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.compose']

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

    query = sys.argv[1] if len(sys.argv) > 1 else 'Koji'
    print(f"Searching Gmail for: '{query}'...")
    
    try:
        results = service.users().messages().list(userId='me', q=query, maxResults=10).execute()
        messages = results.get('messages', [])
        
        if not messages:
            print("No emails found matching that query.")
            return
            
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id'], format='metadata', metadataHeaders=['Subject', 'From', 'Date']).execute()
            headers = msg.get('payload', {}).get('headers', [])
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown Date')
            print(f"[{date}] ID: {message['id']} | Subject: {subject}")
            
    except Exception as e:
        print(f"Search failed: {e}")

if __name__ == '__main__':
    main()
