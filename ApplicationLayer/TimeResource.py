import sys
import datetime

from twisted.internet import defer
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.python import log

import txthings.resource as resource
import txthings.coap as coap

class TimeResource(resource.CoAPResource):
    def __init__(self):
        resource.CoAPResource.__init__(self)
        self.visible = True
        self.observable = True

        self.notify()

    def notify(self):
        log.msg('TimeResource: trying to send notifications')
        self.updatedState()
        reactor.callLater(60, self.notify)

    def render_GET(self, request):
        response = coap.Message(code=coap.CONTENT, payload=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        return defer.succeed(response)
