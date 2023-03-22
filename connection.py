# exported low-level constructors

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

    def sender_matches (self, other):
        if (isinstance (other, 'Sender')):
            return (self.component == other.component and self.port == other.port)
        else:
            return False

class Down (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.enqueueInput (InputMessage (receiver.port, datum))

class Up (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.enqueueOutput (OutputMessage (receiver.port, datum))

class Across (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.enqueueInput (InputMessage (receiver.port, datum))

class Through (Connector):
    def __init__ (self, sender, receiver):
        super().__init__ (sender, receiver)
    def deposit (self, datum):
        self.receiver.enqueueOutput (OutputMessage (receiver.port, datum))

