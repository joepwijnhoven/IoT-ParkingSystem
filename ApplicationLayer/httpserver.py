

import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler

def getFunction():
    print "getFunction got called"

def postFunction():
    print "postFunction got called"

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/parkingspotsAvailable':
            # Insert your code here
            getFunction()

        self.send_response(200)
    def do_POST(self):
        postFunction();
httpd = SocketServer.TCPServer(("", 8085), MyHandler)
httpd.serve_forever()