from helloworldsequential import HelloWorldSequential
from helloworldconcurrent import HelloWorldConcurrent
from topmessage import TopMessage

hw = HelloWorldSequential (None, 'hw')
hw.start (port='stdin', data='Sequential hello world')
print (hw.outputs ())

hw = HelloWorldConcurrent (None, 'hw')
hw.start (port='stdin', data='Concurrent hello world')
print (hw.outputs ())
