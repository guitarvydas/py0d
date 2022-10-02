from sender import Sender
from receiver import Receiver
from up import Up
from down import Down
from across import Across
from passthrough import PassThrough
from container import Container

from echo import Echo

class HelloWorldConcurrent (Container): 
  def __init__ (self, parent, name):
      e1 = Echo (None, f'{name}/c1')
      e2 = Echo (None, f'{name}/c2')
      e3 = Echo (None, f'{name}/c3')
      self._children = [e1,e2,e3]
      self._connections = [
          PassThrough (Sender (self,'stdin'), Receiver (self,'stdout')),
          Down (Sender (self,'stdin'), Receiver (e1,'stdin')),
          Down (Sender (self,'stdin'), Receiver (e2,'stdin')),
          Down (Sender (self,'stdin'), Receiver (e3,'stdin')),
          Up (Sender (e1,'stdout'), Receiver (self,'stdout')),
          Up (Sender (e2,'stdout'), Receiver (self,'stdout')),
          Up (Sender (e3,'stdout'), Receiver (self,'stdout'))
      ]
      super ().__init__ (parent, name, self._children, self._connections)
    

