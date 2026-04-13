import os
import sys
import base64
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

    msg_ids = sys.argv[1:]
    for msg_id in msg_ids:
        try:
            msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
            print(f"--- FETCHING EMAIL ID: {msg_id} ---")
            headers = msg.get('payload', {}).get('headers', [])
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            print(f"Subject: {subject}")
            print(f"Snippet: {msg.get('snippet', '')}")
            
            payload = msg.get('payload', {})
            parts = payload.get('parts', [])
            body_data = None
            
            # Simple recursive search for text/plain
            def find_text_body(payload_part):
                if payload_part.get('mimeType') == 'text/plain':
                    return payload_part.get('body', {}).get('data')
                
                if 'parts' in payload_part:
                    for part in payload_part['parts']:
                        found = find_text_body(part)
                        if found: return found
                return None

            if not parts and 'body' in payload and 'data' in payload['body']:
                body_data = payload['body']['data']
            else:
                body_data = find_text_body(payload)
                
            if body_data:
                text = base64.urlsafe_b64decode(body_data).decode('utf-8')
                print(f"Body:\n{text[:800]}\n")
            else:
                print("Body: [Only HTML or no plain text found]")
        
        except Exception as e:
            print(f"Could not read {msg_id}: {e}")

if __name__ == '__main__':
    main()
