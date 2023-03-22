from leaf import Leaf
from container import Container
from echo import Echo
from message import InputMessage
from connection import Down
from connection import Up
from connection import Across
from connection import Through
from connection import Sender
from connection import Receiver

hw = Echo('hw')
hw.handle(InputMessage('stdin','Hello'))
hw.handle(InputMessage('stdin','World'))
print(hw.outputs())

class WrappedEcho(Echo):
    def __init__(self):
        super.__init__('wrapped')
        self.children = [Echo('echo')]
        self.connections = [
            Down(Sender(None,'stdin'),Receiver(children[0],'stdin')),
            Up(Sender(children[0],'stdout'),Receiver(None,'stdout'))
            ]
whw = Echo('whw')
whw.handle(InputMessage('stdin','wHello'))
whw.handle(InputMessage('stdin','wWorld'))
print(whw.outputs())
            
