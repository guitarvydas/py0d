from eh import EH

class Leaf (Eh):
    def __init__(self, ancestor, givenName, f):
        name = f'{givenName}/Leaf'
        super().__init__(name)
        self.synchronousFunction = f

    def handle(self,msg):
        return self.synchronousFunction(msg)
