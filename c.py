from leaf import Leaf
feedbackCounter = 1

class C (Leaf):
    def __handler__ (self, message):
        if (message.port == 'in'):
            self.send (xfrom=self, portname='out', data=message.data, cause=message)
            self.send (xfrom=self, portname='feedback', data=self.feedbackText (), cause=message)
        elif (message.port == 'fb'):
            self.send (xfrom=self, portname='out', data=message.data, cause=message)
        else:
            raise Exception (f'internal error: unhandled message in C {message}')


    # complications to make this example very expicit
    # keep feedback state in variable "fbseed", return text as a function of the seed
    def __init__ (self, parent, name):
        super ().__init__ (parent, name)
        self.fbseed = 1

    def feedbackText (self):
        if (self.fbseed == 1):
            self.fbseed = 2
            return 'x'
        elif (self.fbseed == 2):
            self.fbseed = 3
            return 'y'
        else:
            return '?'


