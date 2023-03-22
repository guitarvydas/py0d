from leaf import Leaf
from container import Container
from echo import Echo
from message import InputMessage

hw = Echo('hw')
hw.handle(InputMessage('stdin','Hello'))
print(hw.outputs())
