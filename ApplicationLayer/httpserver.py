

import SocketServer
import cgi
import urlparse
import json
from sys import version as python_version
from cgi import parse_header, parse_multipart, parse_qs
from pprint import pprint

from BaseHTTPServer import BaseHTTPRequestHandler
from BusinessLayer.ParkinspotStateService import ParkingspotStateService
from BusinessLayer.ReservationService import ReservationService


def getFunction():
    print "getFunction got called"

def postFunction(postvars):

    pprint(postvars)
    date = postvars["starttime"].value
    duration = postvars["duration"].value
    parkingspot = postvars["parkingspot"].value
    licenseplate = postvars["licensePlate"].value
    print(date)
    print(duration)

    ps = ReservationService()
    ps.makeReservation(parkingspot, licenseplate, date, duration)

    #print(parkingspots[0][0])

    print "postFunction got called"




class MyHandler(BaseHTTPRequestHandler):



    def parse_POST(self):
        ctype, pdict = parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = urlparse.parse_qs(
                self.rfile.read(length),
                keep_blank_values=1)
        else:
            postvars = {}
        return postvars

    def parse_Post2(self):
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            return form

    def do_GET(self):
        if self.path == '/ParkingSpotsAvailable':
            # Insert your code here
            getFunction()

        self.send_response(200)
    def do_POST(self):
        postvars = self.parse_Post2()
        postFunction(postvars);
        self.send_response(200)



httpd = SocketServer.TCPServer(("", 8085), MyHandler)
httpd.serve_forever()