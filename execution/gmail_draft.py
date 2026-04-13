import os.path
import json
import argparse
import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.compose']

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print(json.dumps({"error": "Missing credentials.json from Google Cloud Console."}))
                exit(1)
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def main():
    parser = argparse.ArgumentParser(description="Create a Gmail Draft")
    parser.add_argument('--to', required=True, help="Recipient email address")
    parser.add_argument('--subject', required=True, help="Email subject")
    parser.add_argument('--body', required=True, help="Email body text")
    args = parser.parse_args()

    try:
        service = get_gmail_service()
        
        message = EmailMessage()
        message.set_content(args.body)
        message['To'] = args.to
        message['From'] = 'jefferykerr@gmail.com'
        message['Subject'] = args.subject

        # encode the message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_draft_request_body = {
            'message': {
                'raw': encoded_message
            }
        }
        
        draft = service.users().drafts().create(userId='me', body=create_draft_request_body).execute()
        print(json.dumps({"status": "success", "draft_id": draft['id'], "message": f"Draft created for {args.to}"}))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == '__main__':
    main()
