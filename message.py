# Message =
# | Sender Port Message State Trail -- encapsulated
# | Base                            -- bottom


from debuggable import Debuggable

class BaseMessage (Debuggable):
    def __init__ (self, data):
        super ().__init__ ()
        self._data = data
    def __repr__ (self):
        return "%s" % (self._data)
    @property
    def data (self):
        return self._data

class Message (BaseMessage):
    def __init__ (self, direction, xfrom, port, data, trail):
        super ().__init__ (data)
        self._direction = direction
        self._xfrom = xfrom
        self._port = port
        self._trail = trail

    def __repr__ (self):
        if self._excrutiatingDetail:
            nm = '?'
            if self._xfrom:
                nm = self._xfrom.name
            return "{%s:'%s','%s', %s->%s}" % (self._direction, self.port, self.data, nm, self.trail)
        else:
            return "{'%s'}" % (self.port)


    @property
    def xfrom (self):
        return self._xfrom

    @property
    def port (self):
        return self._port

    @property
    def trail (self):
        return self._trail
