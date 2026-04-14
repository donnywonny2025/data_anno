#!/usr/bin/env python3
"""
DA Gmail Monitor — Comprehensive Email Intelligence
====================================================
Checks the LATEST emails (read AND unread), reads bodies/snippets,
classifies by priority, and outputs actionable intelligence.

Usage:
    python3 da_monitor.py              # Default: last 50 DA emails
    python3 da_monitor.py --all        # Last 50 emails from ALL senders
    python3 da_monitor.py --count 20   # Custom count
    python3 da_monitor.py --full ID    # Read full body of specific email
    python3 da_monitor.py --search "Andromeda"  # Search ALL emails for keyword
"""

import os
import sys
import json
import argparse
import base64
import re
from datetime import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.compose']

# DA sender patterns — catch EVERYTHING related to DA ecosystem
DA_SENDERS = [
    'dataannotation',
    'noreply@mail.dataannotation.tech',
    'slack',                    # Slack invites, notifications
    'aidatatrainer',            # Workspace account notifications
    'ai training',              # Slack workspace name
    'no-reply@slack.com',       # Slack system emails
    'feedback@slack.com',       # Slack feedback
    'notification@slack.com',   # Slack notifications
]

# Priority keywords for classification
PRIORITY_KEYWORDS = {
    'CRITICAL': ['passed', 'approved', 'accepted', 'congratulations', 'slack invite', 'welcome to the team'],
    'HIGH': ['priority', 'bonus', '$3', '$4', '$5', '$8', 'boosted', 'limited time', 'last tasks'],
    'MEDIUM': ['new project', 'qualification', 'update'],
    'LOW': ['see new projects', 'reminder']
}

def get_gmail_service():
    """Authenticate and return Gmail service — checks project root for credentials."""
    creds = None
    # Look for token.json in project root (one level up from execution/)
    token_paths = ['token.json', '../token.json']
    cred_paths = ['credentials.json', '../credentials.json']
    
    token_path = None
    for p in token_paths:
        if os.path.exists(p):
            token_path = p
            break
    
    if token_path:
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            cred_path = None
            for p in cred_paths:
                if os.path.exists(p):
                    cred_path = p
                    break
            if not cred_path:
                print(json.dumps({"error": "Missing credentials.json"}))
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(cred_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save token to where we found it (or project root)
        save_path = token_path or 'token.json'
        with open(save_path, 'w') as token:
            token.write(creds.to_json())
    
    return build('gmail', 'v1', credentials=creds)


def classify_priority(subject, snippet, body_preview=''):
    """Classify email priority based on keywords in subject, snippet, AND body.
    Checks from highest priority down — CRITICAL body content always wins."""
    combined = (subject + ' ' + snippet + ' ' + body_preview).lower()
    
    # Check from CRITICAL down — first match wins (highest priority first)
    for level in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        for kw in PRIORITY_KEYWORDS[level]:
            if kw in combined:
                return level
    return 'INFO'


def is_da_email(sender):
    """Check if email is from Data Annotation."""
    sender_lower = sender.lower()
    return any(pattern in sender_lower for pattern in DA_SENDERS)


def get_email_body(payload):
    """Extract plain text body from email payload."""
    body = ''
    
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                data = part.get('body', {}).get('data', '')
                if data:
                    body = base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
                    break
            elif 'parts' in part:
                # Nested multipart
                for subpart in part['parts']:
                    if subpart['mimeType'] == 'text/plain':
                        data = subpart.get('body', {}).get('data', '')
                        if data:
                            body = base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
                            break
    else:
        data = payload.get('body', {}).get('data', '')
        if data:
            body = base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
    
    # Clean up body — remove excessive whitespace and HTML artifacts
    body = re.sub(r'\s+', ' ', body).strip()
    return body[:500] if body else '(no body text extracted)'


def fetch_emails(service, query=None, max_results=50, da_only=True):
    """Fetch emails with full metadata and snippets."""
    try:
        if query:
            results = service.users().messages().list(
                userId='me', q=query, maxResults=max_results
            ).execute()
        else:
            # Get ALL recent emails from inbox (read + unread)
            results = service.users().messages().list(
                userId='me', labelIds=['INBOX'], maxResults=max_results
            ).execute()
        
        messages = results.get('messages', [])
        if not messages:
            return []
        
        emails = []
        for message in messages:
            msg = service.users().messages().get(
                userId='me', id=message['id'], format='full'
            ).execute()
            
            headers = msg.get('payload', {}).get('headers', [])
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
            date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown')
            
            # Skip non-DA emails if filtering
            if da_only and not is_da_email(sender):
                continue
            
            snippet = msg.get('snippet', '')
            labels = msg.get('labelIds', [])
            is_unread = 'UNREAD' in labels
            
            # Get body preview
            body_preview = get_email_body(msg.get('payload', {}))
            
            priority = classify_priority(subject, snippet + ' ' + body_preview, body_preview)
            
            emails.append({
                'id': message['id'],
                'date': date,
                'from': sender,
                'subject': subject,
                'snippet': snippet,
                'body_preview': body_preview,
                'unread': is_unread,
                'priority': priority
            })
        
        return emails
        
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []


def read_full_email(service, email_id):
    """Read the complete body of a specific email."""
    try:
        msg = service.users().messages().get(
            userId='me', id=email_id, format='full'
        ).execute()
        
        headers = msg.get('payload', {}).get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
        date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown')
        
        # Get full body (no truncation)
        payload = msg.get('payload', {})
        body = ''
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain':
                    data = part.get('body', {}).get('data', '')
                    if data:
                        body = base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
                        break
        else:
            data = payload.get('body', {}).get('data', '')
            if data:
                body = base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
        
        print(f"\n{'='*60}")
        print(f"FROM:    {sender}")
        print(f"DATE:    {date}")
        print(f"SUBJECT: {subject}")
        print(f"{'='*60}")
        print(body or '(no body text)')
        print(f"{'='*60}\n")
        
    except Exception as e:
        print(f"Error reading email: {e}")


def print_intel_report(emails):
    """Print formatted intelligence report."""
    if not emails:
        print("\n📭 No DA emails found in the scanned range.\n")
        return
    
    # Sort by priority
    priority_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3, 'INFO': 4}
    emails.sort(key=lambda e: priority_order.get(e['priority'], 5))
    
    print(f"\n{'='*60}")
    print(f"📡 DA EMAIL INTELLIGENCE REPORT")
    print(f"   Scanned: {len(emails)} DA emails")
    print(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    for email in emails:
        unread_marker = '🔵 NEW' if email['unread'] else '⚪ READ'
        
        # Priority emoji
        p_emoji = {'CRITICAL': '🔴', 'HIGH': '🟠', 'MEDIUM': '🟡', 'LOW': '⚪', 'INFO': '📋'}.get(email['priority'], '📋')
        
        print(f"{p_emoji} [{email['priority']}] {unread_marker}")
        print(f"   📧 {email['subject']}")
        print(f"   📅 {email['date']}")
        print(f"   💬 {email['snippet'][:200]}")
        print(f"   🆔 {email['id']}")
        print()
    
    # Summary
    critical = sum(1 for e in emails if e['priority'] == 'CRITICAL')
    high = sum(1 for e in emails if e['priority'] == 'HIGH')
    unread = sum(1 for e in emails if e['unread'])
    
    print(f"{'='*60}")
    print(f"SUMMARY: {critical} critical | {high} high priority | {unread} unread")
    print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(description='DA Gmail Monitor')
    parser.add_argument('--all', action='store_true', help='Show all emails, not just DA')
    parser.add_argument('--count', type=int, default=50, help='Number of emails to scan (default: 50)')
    parser.add_argument('--full', type=str, help='Read full body of email by ID')
    parser.add_argument('--search', type=str, help='Search all emails for keyword')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    service = get_gmail_service()
    
    # Read specific email
    if args.full:
        read_full_email(service, args.full)
        return
    
    # Search mode
    if args.search:
        print(f"🔍 Searching ALL emails for: '{args.search}'...")
        emails = fetch_emails(service, query=args.search, max_results=args.count, da_only=False)
    else:
        # Default: scan latest inbox emails, filter to DA
        emails = fetch_emails(service, max_results=args.count, da_only=not args.all)
    
    if args.json:
        print(json.dumps(emails, indent=2))
    else:
        print_intel_report(emails)


if __name__ == '__main__':
    main()
