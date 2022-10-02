from sender import Sender
from receiver import Receiver
from up import Up
from down import Down
from across import Across
from container import Container

from echo import Echo

class HelloWorldSequential (Container): 
  def __init__ (self, parent, name):
      e1 = Echo (None, f'{name}/e1')
      e2 = Echo (None, f'{name}/e2')
      self._children = [e1,e2]
      self._connections = [
          Down (Sender (self,'stdin'), Receiver (e1,'stdin')),
          Across (Sender (e1,'stdout'), Receiver (e2,'stdin')),
          Up (Sender (e2,'stdout'), Receiver (self,'stdout'))
      ]
      super ().__init__ (parent, name, self._children, self._connections)
