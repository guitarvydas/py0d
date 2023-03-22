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
            Down(Sender(self,'stdin'),Receiver(children[0],'stdin')),
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
            Down(Sender(self,'stdin'),Receiver(children[0],'stdin')),
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
            Down(Sender(self,'stdin'),Receiver(children[0],'stdin')),
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
            Down(Sender(self,'stdin'),Receiver(children[0],'stdin')),
            Down(Sender(self,'stdin'),Receiver(children[1],'stdin')),
            Up(Sender(children[0],'stdout'),Receiver(self,'stdout')),
            Up(Sender(children[1],'stdout'),Receiver(self,'stdout'))
            ]
        super().__init__(f'[par/{givenName}]')
par = ParEcho('par')
print()
print(f'*** {par.name}')
par.handle(InputMessage('stdin','pHello'))
par.handle(InputMessage('stdin','pWorld'))
print(par.outputs())





# class ParallelWrappedWrappedEcho(WrappedEcho):
#     def __init__(self,givenName):
#         super().__init__(f'[pww/{givenName}]')
#         children = [WrappedEcho('pecho4'),WrappedEcho('pecho5')]
#         self.children = children
#         self.connections = [
#             Down(Sender(self,'stdin'),Receiver(children[0],'stdin')),
# #            Down(Sender(self,'stdin'),Receiver(children[1],'stdin')),
#             Up(Sender(children[0],'stdout'),Receiver(self,'stdout')),
# #            Up(Sender(children[1],'stdout'),Receiver(self,'stdout'))
#             ]
        
# phw = WrappedWrappedEcho('par')
# print()
# print(f'*** {phw.name}')
# phw.handle(InputMessage('stdin','pHello'))
# # phw.handle(InputMessage('stdin','pWorld'))
# print(phw.outputs())


