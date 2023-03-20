class Container(Eh):
    def __init__(self,ancestor,givenName,children,connections):
        name = f'{givenName}/Container'
        super().__init__(ancestor,name)
        self.children = children
        self.connections = connections
        self.put ('handle', self.handle)
        
    def handle(self,msg):
        self.routeDownwards(msg.__lookup__('port'), msg.__lookup__('datum'))
        self.tryAllChildren()

    def tryAllChildren(self):
        for child in self.children:
            if (not child.__lookup__('empty-input?')()):
                msg = child.__lookup__('dequeue-input')()
                child.__lookup__('handle')(msg)
                self.routeAndClearOutputsFromSingleChild(child)

    def routeAndClearOutputsFromSingleChild(self,child):
        for output in child.__lookup__('outputs-as-list')():
            self.routeChildOutput(child, output.__lookup__('port')(), output.__lookup__('datum'))
            self.routeChildOutput(child, output..port, output..datum)
        child._lookup__('clear-outputs')()

    def routeChildOutput(self, xfrom, port, datum):
        fromSender = Sender(xfrom, port)
        
(defun route-child-output (from port datum myeh connections)
  ;; Container routes one datum from a child to all receivers connected to the given {from,port} combination
  ;; handle across and up connections only - down and through do not apply here
  (let ((from-sender (Sender/new from port)))
    (mapc #'(lambda (connection)
              (cond ((%call connection 'sender-matches? from-sender)
                     (let ((kind (%call connection 'kind))
                           (receiver-port (%call (%call connection 'receiver) 'port))
                           (receiver-component (%call (%call connection 'receiver) 'component)))
                       (cond 
                        ((equal kind 'across)
                         (let ((msg (Input-Message/new receiver-port datum)))
                           (%call receiver-component 'enqueue-input msg)))
                        
                        ((equal kind 'up)
                         (let ((msg (Output-Message/new receiver-port datum)))
                           (%call myeh 'enqueue-output msg)))
                        
                        (t (error "internal error 1 in route-child-output")))))
                    (t nil))) ;; {from, port} doesn't match - pass
          connections)))

(defun route-downwards (port datum myeh connections)
  ;; Container routes its own input to its children and/or itself
  ;; across and up do not apply here
  (mapc #'(lambda (connection)
	    (cond ((%call connection 'sender-matches? (Sender/new $Me port))
		   (let ((kind (%call connection 'kind))
			 (receiver-port (%call (%call connection 'receiver) 'port))
			 (receiver-component (%call (%call connection 'receiver) 'component)))
		     (cond 
		      ((equal kind 'down)
                       (let ((msg (Input-Message/new receiver-port datum)))
                         (%call receiver-component 'enqueue-input msg)))
		      
		      ((equal kind 'through)
                       (let ((msg (Output-Message/new receiver-port datum)))
                         (%call myeh 'send msg)))
		      
		      (t (error "internal error 2 in route-downwards")))))
		  (t nil))) ;; {Me, port} doesn't match - pass
	connections))



from sender import Sender
from inputmessage import InputMessage
from outputmessage import OutputMessage
from topmessage import TopMessage
from porthandler import PortHandler
from state import State
from eh import EH

debugRouting = True

class Container (EH):
    def __init__ (self, parent, name, children, connections):
        defaultName = 'default'
        handler = PortHandler ('*', self.handle)
        s = State (machine=self, name=defaultName, enter=None, handlers=[handler], exit=None, childMachine=None)
        super ().__init__ (parent = parent,
                        name = name,
                        defaultStateName = defaultName,
                        enter = self.noop,
                        exit = self.noop,
                        states = [s])

    def noop (self):
        pass

        
    def handle (self, message):
        for connection in self._connections:
            connection.guardedDeliver (message)
        self.runToCompletion ()

    @property
    def name (self):
        return self._name
    
# helpers
    def runToCompletion (self):
        while self.anyChildReady ():
            for child in self._children:
                child.handleIfReady ()
                self.routeOutputs (child)

    def anyChildReady (self):
        r = False
        for child in self._children:
            if child.isReady ():
                r = True
        return r

    def routeOutputs (self, child):
        outputs = child.outputQueue ()
        child.clearOutputs ()
        for msg in outputs:
            for conn in self._connections:
                conn.guardedDeliver (msg)

    def inject (self, port, data):
        m = TopMessage (xfrom=self, port=port, data=data)
        self.injectMessage (m)

    def start (self, port, data):
        self.inject (port, data)
        self.run()
