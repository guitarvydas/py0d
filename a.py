from sender import Sender
from receiver import Receiver
from up import Up
from down import Down
from across import Across
from container import Container

from b import B
from c import C
from d import D

from echo import Echo

class A (Container): 
  def __init__ (self, parent, name):
      b = B (self, f'{name}/b')
      c = C (self, f'{name}/c')
      d = D (self, f'{name}/d')
      self._children = [b,c,d]
      self._connections = [
          Down (Sender (self,'in'), Receiver (b,'in')),
          Across (Sender (b,'out'), Receiver (c,'in')),
          Across (Sender (c,'feedback'), Receiver (c,'fb')),
          Across (Sender (c,'out'), Receiver (d,'in')),
          Up (Sender (d,'out'), Receiver (self,'out'))
      ]
      super ().__init__ (parent, name, self._children, self._connections)
