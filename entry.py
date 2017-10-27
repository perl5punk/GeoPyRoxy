
import socketserver

import classes.core.server

PORT = 8000

with socketserver.TCPServer(("", PORT), classes.core.server.GeoHTTPRequestHandler) as httpd:
    print("Serving GeoPyRoxy on", PORT)
    httpd.serve_forever()
