from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>MyApp Docker v2</h1>")

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("MyApp Docker v2 running on port 8000")
server.serve_forever()
