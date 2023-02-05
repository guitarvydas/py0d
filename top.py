from sender import Sender
from receiver import Receiver
from up import Up
from down import Down
from across import Across
from container import Container

from a import A
from b import B

class Top (Container): 
  def __init__ (self, parent, name):
      a = A (self, f'{name}/a')
      b = B (self, f'{name}/b')
      self._children = [a,b]
      self._connections = [
          Down (Sender (self,'in'), Receiver (a,'in')),
          Across (Sender (a,'out'), Receiver (b,'in')),
          Across (Sender (b,'feedback'), Receiver (b,'fb')),
          Up (Sender (b,'out'), Receiver (self,'out'))
      ]
      super ().__init__ (parent, name, self._children, self._connections)
