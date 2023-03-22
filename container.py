from connection import Sender
from message import InputMessage
from message import OutputMessage
from eh import Eh

class Container(Eh):
    def __init__(self,givenName,children,connections):
        name = f'{givenName}/Container'
        super().__init__(name)
        self.children = children
        self.connections = connections
        
    def handle(self,msg):
        self.routeDownwards(msg.port, msg.datum)
        while (self.isAnyChildReady()):
            self.dispatchAllChildren()

    def dispatchAllChildren(self):
        for child in self.children:
            if (not child.isInputEmpty()):
                msg = child.dequeueInput()
                child.handle(msg)
                self.routeAndClearOutputsFromSingleChild(child)

    def routeAndClearOutputsFromSingleChild(self,child):
        for output in child.outputsAsList():
            self.routeChildOutput(child, output.port, output.datum)
        child.clear-outputs()

    def routeChildOutput(self, frm, port, datum):
        # a child can produce messages only for other children (across), and,
        # for output from its parent (up)
        # down and through cannot apply here
        self.route(frm, port, datum)

    def routeDownwards(self, frm, port, datum):
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
            if (not child.isInputEmpty()):
                result = True
        return result
