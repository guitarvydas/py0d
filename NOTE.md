> I will try to whip up an example in some example language ...

![simple example](https://github.com/guitarvydas/py0d/blob/feedback/doc/feedback.png)

```
from leaf import Leaf

class A (Leaf):
    def __handler__ (self, message):
        self.send (xfrom=self, portname='out', data='v', cause=message)
        self.send (xfrom=self, portname='out', data='w', cause=message)
```
```
from leaf import Leaf

class B (Leaf):
    def __handler__ (self, message):
        if (message.port == 'in'):
            self.send (xfrom=self, portname='out', data=message.data, cause=message)
            self.send (xfrom=self, portname='feedback', data='z', cause=message)
        elif (message.port == 'fb'):
            self.send (xfrom=self, portname='out', data=message.data, cause=message)
        else:
            raise Exception (f'internal error: unhandled message in C {message}')
```
```
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
```



This example shows a small, 2-component feedback network.

The code does nothing useful, but, it demonstrates message feedback.

The problem statement:

- When A gets a message on its pin 'in', it produces 2 messages 'v'
  and 'w' in that order.
- When B gets a message on its pin 'in', it outputs the message on its
  pin 'out' AND it produces a 'z' message on its pin 'feedback'.
- When B gets a message on its pin 'fb', it outputs the message on its
  pin 'out' (only).

The result of the system is 4 messages 'v', 'w', 'z', 'z' in that
order (left to right).

... for more details, see https://github.com/guitarvydas/py0d/blob/feedback/README.md (note that this is the "feedback" branch of that repo)

Feedback - why bother? In electronics, it is common to use feedback to self-regulate ("negative feedback"). In software, recursion (which only LOOKS like feedback) is used only as a form of divide-and-conquer.

The difference between Recursion and Feedback is the delay imposed by queuing. Recursion is processed immediately in a LIFO manner, whereas Feedback messages are put into a queue in FIFO order, to be processed when their time comes.  It's like someone waiting patiently in a lineup versus someone jumping the queue and going to the front of the line.

Stuff like this matters when you are building sequencers instead of calculators.

The Architect can be very explicit in the design instead of having a certain semantics built into the lower-levels of the tool.  Loops (not Recursion) become explicit messages-to-self.  If the Architect really, really, really wants a Stack, the Architect builds it explicitly and gives it the desired semantics, instead of relying on the built-in call-stack to do the work implicitly. 

