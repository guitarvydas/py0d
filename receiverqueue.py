from fifo import FIFO

class ReceiverQueue:
    def __init__ (self):
        self._inputq = FIFO ()
        self._debugHandling = False
        
    def injectMessage (self, message):
        self.enqueueInput (message)

    def handleIfReady (self):
        if self.isReady ():
            m = self.dequeueInput ();
            if self._debugHandling:
                print (f'{self.name} handling {m}') 
            self.handle (m)
            return True
        else:
            return False

    def isReady (self):
        return (0 < self._inputq.len ())
    
# not exported
    def enqueueInput (self, message):
        self._inputq.enqueue (message)
        
    def dequeueInput (self):
        return self._inputq.dequeue ()


            
