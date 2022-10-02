class Sender:
    def __init__ (self, component, port):
        self._xfrom = component
        self._port = port

    def match (self, othersender, port):
        return (self._xfrom == othersender and self._port == port)

    @property
    def port (self):
        return self._port

    @property
    def xfrom (self):
        return self._xfrom

    @property
    def name (self):
        return f'{self._xfrom.name}[{self._port}]'

