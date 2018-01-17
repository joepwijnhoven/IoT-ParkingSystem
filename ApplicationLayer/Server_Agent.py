import sys
from twisted.internet.defer import Deferred
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.python import log

import txthings.coap as coap
import txthings.resource as resource

from ipaddress import ip_address
import SocketServer
import cgi
import urlparse
import json
from sys import version as python_version
from cgi import parse_header, parse_multipart, parse_qs
from pprint import pprint

from txthings import resource, coap


class Agent():
    """
    Example class which performs single GET request to coap.me
    port 5683 (official IANA assigned CoAP port), URI "test".
    Request is sent 1 second after initialization.

    Remote IP address is hardcoded - no DNS lookup is preformed.

    Method requestResource constructs the request message to
    remote endpoint. Then it sends the message using protocol.request().
    A deferred 'd' is returned from this operation.

    Deferred 'd' is fired internally by protocol, when complete response is received.

    Method printResponse is added as a callback to the deferred 'd'. This
    method's main purpose is to act upon received response (here it's simple print).
    """

    def __init__(self, protocol):
        self.protocol = protocol
        #reactor.callLater(1, self.putResource)

    def putResource(self):
        ip = "131.155.186.213"
        payload = "reserved"
        uri = ('32700', '32801',)
        request = coap.Message(code=coap.PUT, payload=payload)
        request.opt.uri_path = ("32700", "32801",)
        request.opt.content_format = coap.media_types_rev['text/plain']
        request.remote = (ip, 61616)
        d = self.protocol.request(request)
        d.addCallback(self.printResponse)

    def printResponse(self, response):
        print 'First result: ' + response.payload
        # reactor.stop()

    def printLaterResponse(self, response):
        print 'Observe result: ' + response.payload

    def noResponse(self, failure):
        print 'Failed to fetch resource:'
        print failure
        # reactor.stop()

