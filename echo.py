from leaf import Leaf

class Echo (Leaf):
    def __handler__ (self, message):
        self.send (xfrom=self, portname='stdout', data=message.data, cause=message)


        
