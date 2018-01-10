import sys
import datetime

from twisted.internet import defer
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.python import log
from pprint import pprint

import txthings.resource as resource
import txthings.coap as coap

class TestResource(resource.CoAPResource):
    def __init__(self):
        resource.CoAPResource.__init__(self)
        self.visible = True
        self.observable = True

        self.notify()

    def notify(self):
        log.msg('TestResource: trying to send notifications')
        self.updatedState()
        reactor.callLater(60, self.notify)

    def render_GET(self, request):
        pprint(vars(request))
        print(repr(request.token))
        response = coap.Message(code=coap.CONTENT, payload="This is a test message, please ignore")
        return defer.succeed(response)
