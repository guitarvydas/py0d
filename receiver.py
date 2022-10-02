class Receiver:
    def __init__ (self, component, port):
        self._who = component
        self._port = port

    @property
    def port (self):
        return self._port

    # _who is used internally only and is never accessed externally
    
    @property
    def name (self):
        return f'{self._who.name}[{self._port}]'

    def enqueueInput (self, message):
        self._who.enqueueInput (message)

    def enqueueOutput (self, message):
        self._who.enqueueOutput (message)

