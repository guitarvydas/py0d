from message import Message
class InputMessage (Message):
    def __init__ (self, xfrom, port, data, trail):
        super ().__init__ ('in', xfrom, port, data, trail)
        
