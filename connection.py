# exported low-level constructors

from message import OutputMessage
from message import InputMessage

class Sender:
    def __init__ (self, component, port):
        self.component = component
        self.port = port
        self.token = hash ((component, port))

class Receiver:
    def __init__ (self, component, port):
        self.component = component
        self.port = port

class Connector:
    def __init__ (self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    def sender_matches (self, other):
        # return (self.sender.component, self.sender.port) == (other.component, other.port)
        if (isinstance (self.sender, Sender) and isinstance (other, Sender)):
            # print (f'{(self.sender.component, self.sender.port) == (other.component, other.port)} {self.sender.token == other.token}')
            # return (self.sender.component, self.sender.port) == (other.component, other.port)
            return self.sender.token == other.token
        else:
            return False

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

