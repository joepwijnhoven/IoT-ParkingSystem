import json
import sys
import datetime

from twisted.internet import defer
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.python import log
from pprint import pprint

import txthings.resource as resource
import txthings.coap as coap

from BusinessLayer.ParkinspotStateService import ParkingspotStateService


class ParkingspotStateResource(resource.CoAPResource):
    def __init__(self):
        self.psService = ParkingspotStateService()
        resource.CoAPResource.__init__(self)
        self.visible = True
        self.observable = True
        self.notify()

    def notify(self):
        log.msg('ParkingspotStateResource: trying to send state of parkingspot')
        self.updatedState()
        #reactor.callLater(60, self.notify)

    def render_GET(self, request):
        data = eval(request.payload)
        if request.response_type is None:
            updateIfExists = True
        else:
            updateIfExists = False
        state = self.psService.getParkingSpotState(data, request.remote[0], updateIfExists)
        response = coap.Message(code=coap.CONTENT, payload=str(state))
        return defer.succeed(response)