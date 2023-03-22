from connection import Sender
from message import InputMessage
from message import OutputMessage
from eh import Eh

class Container(Eh):
    def __init__(self,givenName):
        name = f'[Container/{givenName}]'
        super().__init__(name)
        # child must supply self.children, self.connections
        
    def handle(self,msg):
        self.routeDownwards(msg.port, msg.datum)
        while (self.isAnyChildReady()):
            self.dispatchAllChildren()

    def dispatchAllChildren(self):
        for child in self.children:
            if (isReady(child)):
                msg = child.dequeueInput()
                child.handle(msg)
                self.routeAndClearOutputsFromSingleChild(child)

    def routeAndClearOutputsFromSingleChild(self,child):
        for output in child.outputs():
            self.routeChildOutput(child, output.port, output.datum)
        child.clearOutputs()

    def routeChildOutput(self, frm, port, datum):
        # a child can produce messages only for other children (across), and,
        # for output from its parent (up)
        # down and through cannot apply here
        self.route(frm, port, datum)

    def routeDownwards(self, port, datum):
        # an input message to a container can go 2 places: (1) to a child(ren), or
        # (2) to its own output (Down and Through, resp).
        # across and up cannot apply here
        self.route(self, port, datum)

    def route(self, frm, port, datum):
        fromSender = Sender(frm, port)
        for connection in self.connections:
            if (connection.sender_matches(fromSender)):
                connection.deposit(datum)

    def isAnyChildReady(self):
        result = False
        for child in self.children:
            if (isReady(child)):
                result = True
        return result

def isReady(child):
    return not child.isInputEmpty() or not child.isOutputEmpty()
