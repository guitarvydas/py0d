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
print(f'*** {hw.name}')
hw.handle(InputMessage('stdin','Hello'))
hw.handle(InputMessage('stdin','World'))
print(hw.outputs())

class WrappedEcho(Echo):
    def __init__(self,givenName):
        super().__init__(f'{givenName}/wrapped')
        children = [Echo('echo0'),Echo('echo1')]
        self.children = children
        self.connections = [
            Down(Sender(None,'stdin'),Receiver(children[0],'stdin')),
            Across(Sender(children[0],'stdout'),Receiver(children[1],'stdin')),
            Up(Sender(children[1],'stdout'),Receiver(None,'stdout'))
            ]
whw = WrappedEcho('we')
print(f'*** {whw.name}')
whw.handle(InputMessage('stdin','wHello'))
whw.handle(InputMessage('stdin','wWorld'))
print(whw.outputs())


class WrappedWrappedEcho(WrappedEcho):
    def __init__(self,givenName):
        super().__init__(f'{givenName}/wrappedwrapped')
        children = [WrappedEcho('wecho0'),WrappedEcho('wecho1')]
        self.children = children
        self.connections = [
            Down(Sender(None,'stdin'),Receiver(children[0],'stdin')),
            Across(Sender(children[0],'stdout'),Receiver(children[1],'stdin')),
            Up(Sender(children[1],'stdout'),Receiver(None,'stdout'))
            ]
wwhw = WrappedWrappedEcho('ww')
print(f'*** {wwhw.name}')
wwhw.handle(InputMessage('stdin','wwHello'))
wwhw.handle(InputMessage('stdin','wwWorld'))
print(wwhw.outputs())

class ParallelWrappedWrappedEcho(WrappedEcho):
    def __init__(self,givenName):
        super().__init__(f'{givenName}/pww')
        children = [WrappedEcho('pecho0'),WrappedEcho('pecho1')]
        self.children = children
        self.connections = [
            Down(Sender(None,'stdin'),Receiver(children[0],'stdin')),
            Down(Sender(None,'stdin'),Receiver(children[1],'stdin')),
            Up(Sender(children[0],'stdout'),Receiver(None,'stdout')),
            Up(Sender(children[1],'stdout'),Receiver(None,'stdout'))
            ]
phw = WrappedWrappedEcho('par')
print(f'*** {phw.name}')
phw.handle(InputMessage('stdin','pHello'))
phw.handle(InputMessage('stdin','pWorld'))
print(phw.outputs())


