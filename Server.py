import SocketServer
import sys
import datetime

import thread
from twisted.internet import defer
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.python import log

import SocketServer
import cgi
import urlparse

from cgi import parse_header, parse_multipart, parse_qs
from pprint import pprint

from txthings import resource, coap

from ApplicationLayer.Server_Agent import Agent
from BaseHTTPServer import BaseHTTPRequestHandler


from ApplicationLayer.ParkingspotStateResource import ParkingspotStateResource
from BusinessLayer.ReservationService import ReservationService


class CoreResource(resource.CoAPResource):
    """
    Example Resource that provides list of links hosted by a server.
    Normally it should be hosted at /.well-known/core

    Resource should be initialized with "root" resource, which can be used
    to generate the list of links.

    For the response, an option "Content-Format" is set to value 40,
    meaning "application/link-format". Without it most clients won't
    be able to automatically interpret the link format.

    Notice that self.visible is not set - that means that resource won't
    be listed in the link format it hosts.
    """

    def __init__(self, root):
        resource.CoAPResource.__init__(self)
        self.root = root

    def render_GET(self, request):
        data = []
        self.root.generateResourceList(data, "")
        payload = ",".join(data)
        print(payload)
        response = coap.Message(code=coap.CONTENT, payload=payload)
        response.opt.content_format = coap.media_types_rev['application/link-format']
        return defer.succeed(response)

def getFunction():
    print "getFunction got called"

def postFunction(postvars):
    date = postvars["starttime"].value
    duration = postvars["duration"].value
    parkingspot = postvars["parkingspot"].value
    licenseplate = postvars["licensePlate"].value
    client.putResource("192.168.1.11", "reserved", ("32700", "32801",))
    client.putResource("192.168.1.11", "orange", ("3341", "5527",))
    ps = ReservationService()
    ps.makeReservation(parkingspot, licenseplate, date, duration)

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

# Resource tree creation
log.startLogging(sys.stdout)
root = resource.CoAPResource()

well_known = resource.CoAPResource()
root.putChild('.well-known', well_known)
core = CoreResource(root)
well_known.putChild('core', core)

parkingspotstate = ParkingspotStateResource()
root.putChild('register', parkingspotstate)

other = resource.CoAPResource()
root.putChild('other', other)

def test1():
    reactor.listenUDP(coap.COAP_PORT, protocol)

def test2():
    httpd = SocketServer.TCPServer(("", 8085), MyHandler)
    httpd.serve_forever()

endpoint = resource.Endpoint(root)
protocol = coap.Coap(endpoint)
client = Agent(protocol)

reactor.callInThread(test1)
reactor.callInThread(test2)
reactor.run()



