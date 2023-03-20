# queues.py

from collections import deque
from chain import Chain

class FIFO(Chain):
    def __init__(self):
        self._elements = deque()
        self.put ('enqueue', self.enqueue)
        self.put ('dequeue', self.dequeue)
        self.put ('len', self.len)
        self.put ('empty?', self.isEmpty)
        self.put ('asList', self.asList)

    def enqueue(self, element):
        return self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

    def len (self):
        return len (self._elements)

    def isEmpty (self):
        return (0 >= len (self._elements))

    def asList (self):
        return list (self._elements)

    def __repr__ (self):
        return list (self._elements)
