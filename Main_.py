from email.policy import HTTP
from http import server
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import time


hostname='localhost'
serverport = 8080

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='./',**kwargs)
        

webserver = HTTPServer((hostname,serverport),Handler)
print(f"Server Started http://{hostname}:{serverport}")


try:
    webserver.serve_forever()

except KeyboardInterrupt:
    pass

webserver.server_close()
print("\nServer Stopped...")