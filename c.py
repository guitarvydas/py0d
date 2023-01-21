from leaf import Leaf
feedbackCounter = 1

class C (Leaf):
    def __handler__ (self, message):
        if (message.port == 'in'):
            self.send (xfrom=self, portname='out', data=message.data, cause=message)
        elif (message.port == 'fb'):
            if (1 == feedbackCounter):
                self.send (xfrom=self, portname='out', data='x', cause=message)
                feedbackCounter = feedbackCounter + 1
            elif (2 == feedbackCounter):
                self.send (xfrom=self, portname='out', data='y', cause=message)
                feedbackCounter = feedbackCounter + 1
            else:
                self.send (xfrom=self, portname='out', data='?', cause=message)
        else:
            raise Exception (f'internal error: unhandled message in C {message}')

        
