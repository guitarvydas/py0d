from leaf import Leaf

class B (Leaf):
    def __handler__ (self, message):
        if (message.port == 'in'):
            self.send (xfrom=self, portname='out', data=message.data, cause=message)
            self.send (xfrom=self, portname='feedback', data='z', cause=message)
        elif (message.port == 'fb'):
            self.send (xfrom=self, portname='out', data=message.data, cause=message)
        else:
            raise Exception (f'internal error: unhandled message in C {message}')

        
