from message import OutputMessage
from fifo import FIFO

class Eh ():
    def __init__ (self, given_name):
        self.inq = FIFO ()
        self.outq = FIFO ()
        self.name = f'{given_name}/Eh'

    def enqueueInput (self, x):
        return self.inq.enqueue(x)

    def dequeueInput (self):
        return self.inq.dequeue()

    def isInputEmpty (self):
        return self.inq.isEmpty()

    def enqueueOutput (self, x):
        return self.outq.enqueue(x)

    def dequeueOutput (self):
        return self.outq.dequeue()

    def isOutputEmpty (self):
        return self.outq.isEmpty()

    def clearOutputs (self):
        self.outq = FIFO()
        return []

    def send(self, port, datum):
        return self.outq.enqueue(OutputMessage(port, datum))

    def outputs(self):
        # return output queue as a list
        return self.outq.asList()

    def forEachOutput (self, f):
        for output in self.outq:
            f(self,output)
