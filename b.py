from leaf import Leaf

class B (Leaf):
    def __handler__ (self, message):
        self.send (xfrom=self, portname='out', data='v', cause=message)
        self.send (xfrom=self, portname='out', data='w', cause=message)


        
