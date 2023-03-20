from eh import EH

class Leaf (Eh):
    def __init__(self, ancestor, givenName, f):
        name = f'{givenName}/Leaf'
        super().__init__(ancestor, name)
        self.put('handle', lambda msg: return f(msg))
