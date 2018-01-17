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

    def __init__(self, protocol):
        self.protocol = protocol

    def putResource(self, ip, payload, uri):
        request = coap.Message(code=coap.PUT, payload=payload)
        request.opt.uri_path = uri
        request.opt.content_format = coap.media_types_rev['text/plain']
        request.remote = (ip, 61616)
        d = self.protocol.request(request)
        d.addCallback(self.printResponse)

    def printResponse(self, response):
        print 'First result: ' + response.payload

    def printLaterResponse(self, response):
        print 'Observe result: ' + response.payload

    def noResponse(self, failure):
        print 'Failed to fetch resource:'
        print failure

