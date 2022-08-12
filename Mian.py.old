from email.policy import HTTP
from http.server import BaseHTTPRequestHandler, HTTPServer
import time


hostname='localhost'
serverport = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.send_header('Content-Disposition', 'inline')
        self.end_headers()
        with open('index.html','rb') as file:
            self.wfile.write(file.read())
    

webserver = HTTPServer((hostname, serverport), MyServer)
print(f"Server Started http://{hostname}:{serverport}")


try:
    webserver.serve_forever()

except KeyboardInterrupt:
    pass

webserver.server_close()
print("Server Stopped...")