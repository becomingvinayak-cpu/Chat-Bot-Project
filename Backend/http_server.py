import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class ChatHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        if self.path != "/chat":
            self.send_response(404)
            self.end_headers()
            return

        content_length = int(self.headers["Content-Length"])

        body = self.rfile.read(content_length)

        data = json.loads(body)

        message = data["message"]

        response_data = {
            "answer": f"You asked:{message}",
            "status": "success"
        }

        response_json = json.dumps(response_data)

        self.send_response(200)

        self.send_header("Content-Type", "application/json") 
        self.end_headers()

        self.wfile.write(response_json.encode())

server = HTTPServer(("localhost", 8000), ChatHandler)

print("Server running at http://localhost:8000")
server.serve_forever()