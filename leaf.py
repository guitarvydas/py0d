from eh import EH
from state import State
from porthandler import PortHandler

class Leaf (EH):
    def __init__ (self, parent, name):
        defaultStateName = 'default'
        h = PortHandler ('*', self.__handler__)
        s = State (machine=self, name=defaultStateName, enter=None, handlers=[h], exit=None, childMachine=None)
        super ().__init__ (parent = parent,
                           name = name,
                           defaultStateName = defaultStateName,
                           enter = self.noop,
                           exit = self.noop,
                           states = [s])

    def noop (self):
        pass
    
    
