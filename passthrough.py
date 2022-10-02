from outputmessage import OutputMessage
from connection import Connection

class PassThrough (Connection):
    # from input of Container to input of Child

    def __init__ (self, sender, receiver):
        super ().__init__ ()
        self._sender = sender
        self._receiver = receiver

    def guardedDeliver (self, inmessage):
        # try to deliver the message
        # deliver only if message's from and port match this connection's sender's from and port, otherwise do nothing
        if (self._sender.match (inmessage.xfrom, inmessage.port)):
            receiver = self._receiver
            sender = self._sender
            self.debug ('pass-through', inmessage, sender, receiver)
            mappedMessage = OutputMessage (sender, receiver._port, inmessage.data, inmessage)
            receiver.enqueueOutput (mappedMessage)
