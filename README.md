to use: 
```
make
```

This repo contains example Python code that uses 0D techniques.  

Demonstrates Sequential and Concurrent routing.

Test.py calls 2 different HelloWorld objects.

The first is Sequential.

The second is Concurrent.

Due to the simplicity of this example, the same input is passed into all connections in the concurrent version of HelloWorld.  This should result in 1 pass-through routing, 3 down routings and 3 up routings, resulting in a total of 4 ouptuts on the 'stdout' FIFO of HelloWorldConcurrent.

Start at test.py.

# Diagrams
## Test
![Test](doc/test.png)

---

## Container
![Container](doc/container.png)

---

## Leaf
![Leaves](doc/leaf.png)

---
## Routing
![Leaves](doc/connection-types.png)

---

## Hello World Sequential
![Hello World Sequential](doc/sequential.png)

---

## Hello World Concurrent
![Hello World Concurrent](doc/concurrent.png)

---

## Names
![Component Names](doc/names.png)