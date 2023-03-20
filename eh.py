from schedulable import Schedulable
from chain import Chain
from message import OutputMessage
from fifo import FIFO

class Eh (Chain):
    def __init__ (self, ancestor, given_name):
        super ().__init__ (ancestor)
        self.inq = FIFO ()
        self.outq = FIFO ()
        self.put ('name', f'{given_name}/Eh')
        self.put ('enqueue-input', lambda x: return self.inq.__lookup__ ('enqueue')(x)
        self.put ('dequeue-input', lambda: return self.inq.__lookup__ ('dequeue')())
        self.put ('empty-input?', lambda: return self.inq.__lookup__ ('empty?')())
        self.put ('enqueue-output', lambda x: return self.outq.__lookup__ ('enqueue')(x))
        self.put ('dequeue-output', lambda: return self.outq.__lookup__ ('dequeue')())
        self.put ('empty-output?', lambda: return self.outq.__lookup__ ('empty?')())
        self.put ('clear-outputs', lambda: return self.outq.__lookup__ ('clear')())
        self.put ('send', self._send)
        self.put ('outputs-as-list', self._outputs_as_list)
        self.put ('for-each-output', self._for_each_output)

      def _send (self, port, datum):
          fenqueue = self.outq.__lookup__ ('enqueue')
          return fenqueue (self.outq, OutputMessage (port, datum))

      def _outputs_as_list (self):
          return self.outq.asList ()

      def _for_each_output (self, f):
          for output in self.outq:
              f (self, output)
          return True
