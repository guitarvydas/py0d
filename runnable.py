class Runnable:
    def __init__ (self, parent, name, top):
        self._parent = parent
        self._name = name
        self._top = top

    @property
    def name (self):
        return self._name

    def run (self):
        while self.isBusy ():
            self.step ()
        while self.handleIfReady ():
            while self.isBusy ():
                self.step()

