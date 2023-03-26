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
print(hw.outputs())

class WrappedEcho(Container):
    def __init__(self,givenName):
        children = [Echo('0')]
        self.children = children
        self.connections = [
            Down(Sender(None,'stdin'),Receiver(children[0],'stdin')),
            Up(Sender(children[0],'stdout'),Receiver(self,'stdout'))
            ]
        super().__init__(f'[wrapped/{givenName}]')
whw = WrappedEcho('we')
print()
print(f'*** {whw.name}')
whw.handle(InputMessage('stdin','wHello'))
print(whw.outputs())


class WrappedEcho2(Container):
    def __init__(self,givenName):
        children = [Echo('10'),Echo('11')]
        self.children = children
        self.connections = [
            Down(Sender(None,'stdin'),Receiver(children[0],'stdin')),
            Across(Sender(children[0],'stdout'),Receiver(children[1],'stdin')),
            Up(Sender(children[1],'stdout'),Receiver(self,'stdout'))
            ]
        super().__init__(f'[wrapped/{givenName}]')
we2 = WrappedEcho2('we2')
print()
print(f'*** {we2.name}')
we2.handle(InputMessage('stdin','wHello'))
print(we2.outputs())


class WrappedWrappedEcho(WrappedEcho):
    def __init__(self,givenName):
        super().__init__(f'[wrappedWrapped/{givenName}]')
        children = [WrappedEcho('wecho2')]
        self.children = children
        self.connections = [
            Down(Sender(None,'stdin'),Receiver(children[0],'stdin')),
            Up(Sender(children[0],'stdout'),Receiver(self,'stdout'))
            ]
wwhw = WrappedWrappedEcho('ww')
print()
print(f'*** {wwhw.name}')
wwhw.handle(InputMessage('stdin','wwHello'))
# wwhw.handle(InputMessage('stdin','wwWorld'))
print(wwhw.outputs())


class ParEcho(Container):
    def __init__(self,givenName):
        children = [Echo('20'),Echo('21')]
        self.children = children
        self.connections = [
            Down(Sender(None,'stdin'),Receiver(children[0],'stdin')),
            Down(Sender(None,'stdin'),Receiver(children[1],'stdin')),
            Up(Sender(children[0],'stdout'),Receiver(self,'stdout')),
            Up(Sender(children[1],'stdout'),Receiver(self,'stdout'))
            ]
        super().__init__(f'[par/{givenName}]')
par = ParEcho('par')
print()
print(f'*** {par.name}')
par.handle(InputMessage('stdin','pHello'))
print(par.outputs())

class PWEcho(Container):
    def __init__(self,givenName):
        children = [WrappedEcho('30'),WrappedEcho('31')]
        self.children = children
        self.connections = [
            Down(Sender(None,'stdin'),Receiver(children[0],'stdin')),
            Down(Sender(None,'stdin'),Receiver(children[1],'stdin')),
            Up(Sender(children[0],'stdout'),Receiver(self,'stdout')),
            Up(Sender(children[1],'stdout'),Receiver(self,'stdout'))
            ]
        super().__init__(f'[pw/{givenName}]')
pw = PWEcho('pw')
print()
print(f'*** {pw.name}')
pw.handle(InputMessage('stdin','pwHello'))
pw.handle(InputMessage('stdin','pwWorld'))
print(pw.outputs())


class A(Leaf):
    def handle(self, message):
        self.send(port='stdout',datum='v')
        self.send(port='stdout',datum='w')

class B(Leaf):
    def handle(self, message):
        if (message.port == 'stdin'):
            self.send(port='stdout',datum=message.datum)
            self.send(port='feedback',datum='z')
        elif (message.port == 'fback'):
            self.send(port='stdout',datum=message.datum)

class FeedbackTest(Container):
    def __init__(self,givenName):
        children = [A('a'),B('b')]
        connections = [
            Down(Sender(None,'stdin'),Receiver(children[0],'stdin')),
            Across(Sender(children[0],'stdout'),Receiver(children[1],'stdin')),
            Across(Sender(children[1],'feedback'),Receiver(children[1],'fback')),
            Up(Sender(children[1],'stdout'),Receiver(self,'stdout'))
        ]
        self.children = children
        self.connections = connections
        super().__init__(f'[FeedbackTest/{givenName}]')

print()
print('*** Feedback ')
fb = FeedbackTest('feebacktest')
fb.handle(InputMessage('stdin',True))
print(fb.outputs())

            
