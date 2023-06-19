import http.server
import socketserver

PORT = 8000  # Change this to the desired port number

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started on port {PORT}")
    httpd.serve_forever()
