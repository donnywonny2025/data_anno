import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/api/clear':
            # Clear the session log safely
            log_path = "war_room/TASK_LOG/live_session.json"
            if os.path.exists(log_path):
                with open(log_path, 'w') as f:
                    f.write("[]")
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"cleared"}')
        else:
            self.send_error(404, "Endpoint not found")

    def end_headers(self):
        # Prevent aggressive browser caching of the JSON tracker
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

# Setup graceful shutdown or persistent thread
print(f"Starting Stealth Mirror API on http://localhost:{PORT}")
print("Serving Air-Gapped Dashboard from /stealth_dashboard/index.html")

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    httpd.serve_forever()
