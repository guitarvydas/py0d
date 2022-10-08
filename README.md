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

---

# ė (EH)
*from "ė - Concurrent Lambdas" working paper 1 (not published ATM)*
## ė
As a working title for this concept, I'm going to use `ė`.

It is the Lithuanian letter "e" with a dot above it.

It is pronounced like Canadian "eh" or the English-language letter "A" (hard, not soft).

I almost chose another Greek letter, then realized that I could use any unicode character, then, almost chose a smily emoji, but, finally settled on `ė`.

[The choice is almost arbitrary, but, `ė` ties my two inherited cultures together.]