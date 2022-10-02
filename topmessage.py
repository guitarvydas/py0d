from inputmessage import InputMessage

class TopMessage (InputMessage):
    def __init__ (self, xfrom, port, data):
        super ().__init__ (xfrom=xfrom, port=port, data=data, trail=[])
