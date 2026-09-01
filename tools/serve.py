#!/usr/bin/env python3
"""
Svenska Recept - Local Preview Server
Serves the website locally at http://localhost:8080 (or next available port)
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

DEFAULT_PORT = 8080

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def main():
    web_dir = Path(__file__).resolve().parent.parent
    os.chdir(web_dir)
    
    Handler = http.server.SimpleHTTPRequestHandler
    port = DEFAULT_PORT

    for attempt in range(10):
        try:
            httpd = ReusableTCPServer(("", port), Handler)
            print(f"🇸🇪 Svenska Recept Web Server körs på: http://localhost:{port}")
            print(f"📂 Rotkatalog: {web_dir}")
            print("Tryck Ctrl+C för att stoppa servern.\n")
            httpd.serve_forever()
            break
        except OSError as e:
            if "Address already in use" in str(e) or e.errno == 48:
                port += 1
                continue
            else:
                raise e

if __name__ == "__main__":
    main()
