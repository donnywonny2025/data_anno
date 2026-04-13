import os
import sys
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    if not os.path.exists('token.json'):
        print("Error: token.json not found")
        return

    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('gmail', 'v1', credentials=creds)

    try:
        # Search for the Slack invite from AI Training
        results = service.users().messages().list(userId='me', q='subject:"Slack" "AI Training"', maxResults=5).execute()
        messages = results.get('messages', [])
        
        if not messages:
            # Fallback search if exact quote fails
            results = service.users().messages().list(userId='me', q='Slack', maxResults=5).execute()
            messages = results.get('messages', [])
            
            if not messages:
                print("Could not find the Slack invite email.")
                return
            
        message_id = messages[0]['id']
        url = f"https://mail.google.com/mail/u/0/#inbox/{message_id}"
        print(f"Found Slack Invite. Opening URL natively: {url}")
        
        # Physically open the URL on the host machine's default browser
        os.system(f'open "{url}"')
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
