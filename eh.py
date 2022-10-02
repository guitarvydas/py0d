from receiverqueue import ReceiverQueue
from senderqueue import SenderQueue
from runnable import Runnable
from hsm import HSM

class EH (HSM, ReceiverQueue, SenderQueue, Runnable):
    def __init__ (self, parent, name, defaultStateName, enter, states, exit):
        ReceiverQueue.__init__ (self)
        SenderQueue.__init__ (self)
        top = HSM.__init__ (self, name=name, defaultStateName=defaultStateName, 
            enter=enter, states=states, exit=exit)
        Runnable.__init__ (self, parent=parent, name=name, top=top)
       
