from leaf import Leaf

class Echo (Leaf):
    def __init__(self,givenName):
        super().__init__(f'[Echo/{givenName}]')
    def handle (self, message):
        print(f'  Handle:{self.name}')
        self.send (port='stdout', datum=message.datum)


        
