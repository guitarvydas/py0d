# exported low-level constructors

from message import OutputMessage
from message import InputMessage

def genUniqueToken (component, port):
    return hash( (component, port) )

class Sender:
    def __init__ (self, component, port):
        self.component = component
        self.port = port
        self.token = genUniqueToken(component, port)

    def __eq__ (self, other):
        if (isinstance(other,Sender)):
            return self.token == other.token
        else:
            return False

class Receiver:
    def __init__ (self, queue, port):
        self.queue = queue
        self.port = port

class Connector:
    def __init__ (self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    def sender_matches (self, other):
        return self.sender == other

class Down (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.queue.enqueue (InputMessage (self.receiver.port, datum))

class Up (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.queue.enqueue (OutputMessage (self.receiver.port, datum))

class Across (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.queue.enqueue (InputMessage (self.receiver.port, datum))

class Through (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.queue.enqueue (OutputMessage (self.receiver.port, datum))

