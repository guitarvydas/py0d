from debuggable import Debuggable

class Connection (Debuggable):

    def __init__ (self):
        super ().__init__ ()

    def debug (self, note, message, sender, receiver):
        if self._excrutiatingDetail:
            print (f'{note} {message} ... {sender.name} -> {receiver.name}')
        
