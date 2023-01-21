from leaf import Leaf

class D (Leaf):
    def __handler__ (self, message):
        self.send (xfrom=self, portname='out', data=message.data, cause=message)


        
