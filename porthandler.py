# A Function associated with a Port (a string)
# The port '*' means any port.
class PortHandler:
    def __init__ (self, port, func):
        self._port = port
        self._func = func

    def matchPort (self, portName):
        r = None
        if self._port == '*':
            r = True
        elif self._port == portName:
            r = True
        else:
            r = False
        return r

    @property
    def func (self):
        return self._func
