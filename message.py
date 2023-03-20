class _Message(Chain):
    def __init__ (self, datum):
        self.put ('datum',datum)


;; InputMessage and OutputMessage are messages that hold onto the port tag

;; InputMessage and OutputMessage have the same structure, but are semantically
;;  different - the port of an InputMessage refers to a port of the receiver, whereas
;;  the port of an OutputMessage refers to a port of the sender
;; The router (in Container.lisp) remaps ports as appropriate.

class InputMessage (_Message):
    def __init__ (self, port, v):
        super ().__init__ (v)
        self.put('port', port)

class OutputMessage (_Message):
    def __init__ (self, port, v):
        super ().__init__ (v)
        self.put('port', port)

