class Message:
    def __init__ (self, datum):
        self.datum = datum

# InputMessage and OutputMessage are messages that hold onto the port tag

# InputMessage and OutputMessage have the same structure, but are semantically
#  different - the port of an InputMessage refers to a port of the receiver, whereas
#  the port of an OutputMessage refers to a port of the sender
# The router (in Container.lisp) remaps ports as appropriate.

class InputMessage (Message):
    def __init__ (self, port, v):
        super ().__init__ (v)
        self.port = port
    def __repr__(self):
        return f'<{self.port},{self.datum}>'

class OutputMessage (Message):
    def __init__ (self, port, v):
        super ().__init__ (v)
        self.port = port
    def __repr__(self):
        return f'<{self.port},{self.datum}>'

