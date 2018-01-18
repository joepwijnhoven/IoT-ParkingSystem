from twisted.internet import defer
from txthings import resource, coap
from twisted.python import log

class NotifyResource(resource.CoAPResource):
    def __init__(self):
        resource.CoAPResource.__init__(self)
        self.visible = True
        self.observable = True
        self.notify()

    def notify(self):
        log.msg('Notify: a notify ')
        self.updatedState()
        #reactor.callLater(60, self.notify)

    def render_GET(self, request):
        print request.payload
        response = coap.Message(code=coap.CONTENT, payload="succeeded")
        return defer.succeed(response)