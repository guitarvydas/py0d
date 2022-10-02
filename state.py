class State:
    def __init__ (self, machine, name, enter, handlers, exit, childMachine):
        self._machine = machine
        self._name = name
        self._enter = enter
        self._handlers = handlers
        self._exit = exit
        self._childMachine = childMachine
        
    def enter (self):
        if  self._enter:
            self._enter (self)
        if (self._childMachine):
            self._childMachine.enter ()

    def exit (self):
        if (self._childMachine):
            self._childMachine.exit ()
        if self._exit:
            self._exit (self)

    def handle (self, message):
        r = self.handlerChain (message, self._handlers, self._childMachine)
        if r:
            return r
        elif self._childMachine:
            return self._childMachine.handle (message)
        else:
            return False

    def step (self):
        if self._childMachine:
            self._childMachine.step ()
        else:
            pass
    
    def isBusy (self):
        if self._childMachine:
            return self._childMachine.isBusy ()
        else:
            return False

# worker bees
    def handlerChain (self, message, handlers, subMachine):
        if 0 < len (handlers):
            handler = handlers [0]
            rest = handlers [1:]
            if (handler.matchPort (message.port)):
                handler.func (message)
                return True
            else:
                return self.handlerChain (message, rest, subMachine)
        else:
            if subMachine:
                return subMachine.handle (message)
            else:
                return False
    
