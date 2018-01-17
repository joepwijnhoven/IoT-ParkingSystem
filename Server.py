import sys
import datetime

from twisted.internet import defer
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.python import log
from ApplicationLayer.TimeResource import TimeResource
from ApplicationLayer.TestResource import TestResource

import txthings.resource as resource
import txthings.coap as coap
import socket

from ApplicationLayer.ParkingspotStateResource import ParkingspotStateResource


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

# Resource tree creation
log.startLogging(sys.stdout)
root = resource.CoAPResource()

well_known = resource.CoAPResource()
root.putChild('.well-known', well_known)
core = CoreResource(root)
well_known.putChild('core', core)

time = TimeResource()
root.putChild('time', time)

test = TestResource()
root.putChild('test', test)

parkingspotstate = ParkingspotStateResource()
root.putChild('register', parkingspotstate)

other = resource.CoAPResource()
root.putChild('other', other)

endpoint = resource.Endpoint(root)
reactor.listenUDP(coap.COAP_PORT, coap.Coap(endpoint)) #, interface="::")
reactor.run()