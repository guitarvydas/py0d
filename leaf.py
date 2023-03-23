from eh import Eh

class Leaf (Eh):
    def __init__(self, givenName):
        name = f'[Leaf/{givenName}]'
        super().__init__(name)


# descendents must implement handle(message)
