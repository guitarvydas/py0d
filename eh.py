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
        return self.outq = FIFO()

    def send(self, port, datum):
        return outq.enqueue(OutputMessage(port, datum))

    def outputsAsList (self):
        return self.outq.asList()

    def forEachOutput (self, f):
        for output in self.outq:
            f(self,output)
        self.put ('for-each-output', self._for_each_output)
