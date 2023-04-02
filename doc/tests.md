![[tests 2023-03-22 16.30.08.excalidraw]]
# Feedback
[see essay for the most up-to-date version](https://publish.obsidian.md/programmingsimplicity/2023-04-02-Feedback)

Feedback is not recursion.  Recursion uses LIFOs, feedback uses FIFOs.  A feedback "call" in recursion jumps to the front of the queue, whereas a feedback "message" goes to the end of the queue.  "Calls" are processed immediately, whereas "messages" are processed later, in order of arrival.

A simplisitic test of feedback is to have 2 components, A and B.  A sends messages *v* then *w* (in that order).  B has 2 input pins, one for raw data and one for feedback data.  B has two output pins - (1) an output and (2) a feedback pin.  B follows the algorithm:
- when a message arrives on the raw input, B sends 2 messages - the raw data is sent on the the output, AND, a *z* is sent on the feedback output pin
- when a message arrives on the feedback input, B sends only 1 message - the incoming data is sent to the output, but, nothing is sent to the feedback pin.

In the system shown below, we would expect to see output *v*, *w*, *z*, *z*.

---

![[feedback with messages tests 2023-04-02 08.35.26.excalidraw.png]]

---

![[tests 2023-04-02 10.00.35.excalidraw]]

---


### Why Not Use an IF-THEN-ELSE on the Raw Input?

It is *possible* to use an if-then-else statement on the raw input *v*, *w*, instead of using two pins.

Using two in put pins, though, allows the engine to perform the conditional statement in any way that it pleases, and, makes the design more visual. 

In FP, this kind of thing is called "pattern matching".  Instead of using complicated patterns, we restrict patterns to be simple *tags*.  This allows us to easily draw diagrams. 

Q: What happens if you need to deal with complex patterns? A: Break the complex patterns down into simpler tag-driven problems in a pipeline instead of handling everything in one fell swoop.

## Why is Feedback Important?
The most obvious use-case for feedback is to implement a distributed *for* loop.

Languages that have *for* built into them constrain the way we are allowed to think about distributed problems.

One of the tennets of FP style - in fact, Denotational Semantics style - of programming, is to *make everything explicit*.  FP fails this simple goal, in that it hides the use of the call-stack (a LIFO).  

Using *explicit* drawings allows software architects to create solutions using many more degrees of freedom.  In many cases, too much explicitness becomes a burden, is visually "too busy" and breaks the Rule of 7[^ruleof7]  In such cases, *syntax* comes to the rescue.  One can wrap *skins* around solutions to make the appearance of the solution more pallatable.

At this moment, most of our syntaxing tools - like Ohm-JS - are targeted at creating skins for textual representations of programs.  On the other hand, most of our current diagram-editing tools, like Excalidraw and draw.io and SVG, can create textual representations of diagrams, so, we can use existing text-biased syntaxing tools while waiting for better diagram-biased syntaxing tools to appear (diagram macros, diagram parsers, etc.)

[^ruleof7]: Rule of 7: All details are chopped up into layers.  No node in a layer has more than 7±2 items in it.  Most programming languages encourage breaking this rule, i.e. they encourage writing functions that have more than 7±2 lines of code in them, they encourage writing program modules that have more than 7±2 functions in them, they encourage the use of more than 7±2 types, etc, etc.

Feedback is used heavily in electronics designs, in ways that haven't permeated software development culture.  For example, in *op-amp* designs, negative feedback is used by ICs to self-regulate.

# Code
[see the repo](https://github.com/guitarvydas/py0d)
## Program Using Components and Messaging
```
class A(Leaf):
    def handle(self, message):
        self.send(port='stdout',datum='v')
        self.send(port='stdout',datum='w')

class B(Leaf):
    def handle(self, message):
        if (message.port == 'stdin'):
            self.send(port='stdout',datum=message.datum)
            self.send(port='feedback',datum='z')
        elif (message.port == 'fback'):
            self.send(port='stdout',datum=message.datum)

class FeedbackTest(Container):
    def __init__(self,givenName):
        super().__init__(f'[FeedbackTest/{givenName}]')
        children = [A('a'),B('b')]
        connections = [
            Down(Sender(None,'stdin'),Receiver(children[0].inq,'stdin')),
            Across(Sender(children[0],'stdout'),Receiver(children[1].inq,'stdin')),
            Across(Sender(children[1],'feedback'),Receiver(children[1].inq,'fback')),
            Up(Sender(children[1],'stdout'),Receiver(self.outq,'stdout'))
        ]
        self.children = children
        self.connections = connections

print()
print('*** Feedback ')
fb = FeedbackTest('feebacktest')
fb.handle(InputMessage('stdin',True))
print(fb.outputs())
```
The output is
```
...
*** Feedback 
[<stdout,v>, <stdout,w>, <stdout,z>, <stdout,z>]
```

[usage: make]

## Program Using Recursion
```
def B2 (input):
    print (input,end='')

def B1 (input):
    print (input,end='')
    B2 ('z')

def A ():
    B1 ('v')
    B1 ('w')
    
A()
print()
```

The output is
```
vzvw
```

[usage: python3 recursion.py]

## Code Size
The textual code for the messaging case is larger than that textual code for the recursion case.

Humans shouldn't have to read code, so code size doesn't actually matter.

What really matters, is 
- that humans be able to express programs in a convenient manner with many degrees of freedom in their designs
- that machines can understand what needs to be done
- that other humans can read and understand the designs of programs.

We can hide code size issues by wrapping syntax skins around code.  Compilers are - basically - just boilerplate generators.  Compilers breathe in convenient syntax and breathe out boilerplate code that humans don't bother reading.  When compilers were first invented, assembler programmers scoffed at the idea, since Assember programmers could produce Assembler code that was tighter than the boilerplate Assembler code produced by compilers.  In the end, smart people figured out how to optimize the code generated by compilers.  GCC put the final nail in the coffin of Assembler programming.

I expect to see a similar revolution in programming language design.  I expect to see designs of programming languages that use technical diagrams instead of text.  I expect to see new optimization techniques that will nail the door shut on all screams about the superiority of text-based programming languages.

Text isn't going to die, but will be relegated to its rightful place along-side of other kinds of syntax.  SVG already does this - text is just another element type, like rectangles and ellipses.
