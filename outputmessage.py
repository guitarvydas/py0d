from message import Message
class OutputMessage (Message):
    def __init__ (self, xfrom, port, data, trail):
        super ().__init__ ('out', xfrom, port, data, trail)
