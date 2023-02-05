to use: 
```
make
```

This example shows a small, 2-component feedback network.

The code does nothing useful, but, it demonstrates message feedback.

The problem statement:

- When A gets a message on its pin 'in', it produces 2 messages 'v'
  and 'w' in that order.
- When B gets a message on its pin 'in', it outputs the message on its
  pin 'out' AND it produces a 'z' message on its pin 'feedback'.
- When B gets a message on its pin 'fb', it outputs the message on its
  pin 'out' (only).

The result of the system is 4 messages 'v', 'w', 'z', 'z' in that
order (left to right).


Details:
- The Python program creates a Top level wrapper component which creates A and B components.
- When the Python program is run, it sends a message to the Top level.
- The Top level component forwards the message to its child A.
- A generates two message outputs in rapid succession - 'v' and 'w'.
- The Top level component routes these messages to its child B.
- B responds by echoing the input to its output, and, if the input comes in on its 'in' pin, it also sends another message ('z') to its output pin 'feedback'.
- When B receives input on its 'fb' pin, it simply echoes the message to its 'out' pin, but, does not create a second message.

See doc/feedback.png for a diagram of the source code.

Feedback - why bother? In electronics, it is common to use feedback to self-regulate ("negative feedback"). In software, recursion (which only LOOKS like feedback) is used only as a form of divide-and-conquer.

The difference between Recursion and Feedback is the delay imposed by queuing. Recursion is processed immediately in a LIFO manner, whereas Feedback messages are put into a queue in FIFO order, to be processed when their time comes.  It's like someone waiting patiently in a lineup versus someone jumping the queue and going to the front of the line.

Stuff like this matters when you are building sequencers instead of calculators.

The Architect can be very explicit in the design instead of having a certain semantics built into the lower-levels of the tool.  Loops (not Recursion) become explicit messages-to-self.  If the Architect really, really, really wants a Stack, the Architect builds it explicitly and gives it the desired semantics, instead of relying on the built-in call-stack to do the work implicitly. 
