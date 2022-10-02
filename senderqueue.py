from fifo import FIFO
from sender import Sender
from outputmessage import OutputMessage

class SenderQueue:
    def __init__ (self):
        self._outputq = FIFO ()

    def outputsFIFODictionary (self):
        # return a dictionary of FIFOs, one FIFO per output port
        resultdict = {}
        for message in self._outputq.asList ():
            if (not (message.port in resultdict)):
                resultdict [message.port] = FIFO ()
            resultdict [message.port].enqueue (message.data)
        resultdict2 = {}
        for key in resultdict:
            fifo = resultdict [key]
            r = fifo.asList ()
            resultdict2 [key] = r
        return resultdict2

    def outputsLIFODictionary (self):
        # return a dictionary of LIFOs, one LIFO per output port
        resultdict = {}
        for message in self._outputq.asList ():
            if (not (message.port in resultdict)):
                resultdict [message.port] = FIFO ()
            resultdict [message.port].enqueue (message.data)
        resultdict2 = {}
        for key in resultdict:
            fifo = resultdict [key]
            r = fifo.asList ()
            r.reverse () ## newest result first
            resultdict2 [key] = r
        return resultdict2

    # internal - not exported
    def clearOutputs (self):
        self._outputq = FIFO ()

    def enqueueOutput (self, message):
        self._outputq.enqueue (message)
        

    def dequeueOutput (self):
        return self._outputq.dequeue ()

    def send (self, xfrom, portname, data, cause):
        if cause:
            breadcrumbs = [cause, cause.trail]
        else:
            breadcrumbs = [cause]
        m = OutputMessage (xfrom, portname, data, trail=breadcrumbs)
        self.enqueueOutput (m)

    def outputQueue (self):
        return self._outputq.asList ()

    def outputs (self):
        return self.outputsFIFODictionary ()
    
