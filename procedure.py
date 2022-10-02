from eh import EH
from state import State

class Procedure (EH):
    def __init__ (self, parent, name, portHandler):
        defaultName = 'default'
        s = State (machine=self, name=defaultName, enter=None, handlers=[portHandler], exit=None, childMachine=None)
        super ().__init__ (parent = parent,
                        name = name,
                        defaultStateName = defaultName,
                        enter = self.noop,
                        exit = self.noop,
                        states = [s])

    def noop (self):
        pass
    
