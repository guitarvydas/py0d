# exported low-level constructors

from message import OutputMessage
from message import InputMessage

class Sender:
    def __init__ (self, component, port):
        self.component = component
        self.port = port

class Receiver:
    def __init__ (self, component, port):
        self.component = component
        self.port = port

class Connector:
    def __init__ (self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    # def sender_matches (self, other):
    #     if (isinstance (other, Sender)):
    #         return (self.sender.component == other.component and 
    #                 self.sender.port == other.port)
    #     else:
    #         return False

    def sender_matches (self, other):
        return (self.sender.component, self.sender.port) == (other.component, other.port)

class Down (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.component.enqueueInput (InputMessage (self.receiver.port, datum))

class Up (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.component.enqueueOutput (OutputMessage (self.receiver.port, datum))

class Across (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.component.enqueueInput (InputMessage (self.receiver.port, datum))

class Through (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.component.enqueueOutput (OutputMessage (self.receiver.port, datum))

