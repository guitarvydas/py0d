from leaf import Leaf

class Echo (Leaf):
    def handle (self, message):
        self.send (port='stdout', datum=message.datum)


        
