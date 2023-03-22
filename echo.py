from leaf import Leaf

class Echo (Leaf):
    def __init__(self,givenName):
        super().__init__(f'{givenName}/Echo')
    def handle (self, message):
        self.send (port='stdout', datum=message.datum)


        
