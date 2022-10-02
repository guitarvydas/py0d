to use: make

The repo contains example Python code that uses 0D techniques.  Basically message sending using FIFOs. 

Test.py calls 2 different HelloWorld objects.

The first is Sequential.

The second is Concurrent.

Due to the simplicity of this example, the same input is passed into all connections in the concurrent version of HelloWorld.  This should result in 1 pass-through routings, 3 down routings and 3 up routings, resulting in a total of 4 ouptuts on the 'stdout' FIFO of HelloWorldConcurrent.

