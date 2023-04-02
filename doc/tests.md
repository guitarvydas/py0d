![[tests 2023-03-22 16.30.08.excalidraw]]
## Feedback
Feedback is not recursion.  Recursion uses LIFOs, feedback uses FIFOs.  A feedback "call" in recursion jumps to the front of the line, whereas a feedback "message" goes to the end of the line and is processed.  "Calls" are processed immediately, whereas "messages" are processed later, in order of arrival,

A simplisitic test of feedback is to have 2 components, A and B.  A sends messages *v* then *w* (in that order).  B has 2 input pins, one for raw data and one for feedback data.  B has two output pins - (1) an output and (2) a feedback pin.  B follows the algorithm:
- when a message arrives on the raw input, B sends 2 messages - the raw data is sent on the the output, AND, a *z* is sent on the feedback output pin
- when a message arrives on the feedback input, B sends only 1 message - the incoming data is sent to the output, but, nothing is sent to the feedback pin.

In the system shown below, we would expect to see output *v*, *w*, *z*, *z*.

![[tests 2023-04-02 08.35.26.excalidraw]]

### Simply Use an IF on v,w?

It is *possible* to use an if-then-else statement on the raw input *v*, *w*, instead of using two pins.

Using two pins, though, allows the engine to perform the conditional statement in any way that it pleases, and, makes the choice more visual. 

In FP, this kind of thing is called "pattern matching".  Instead of using complicated patterns, we restrict patterns to be simple *tags*.  This allows us to easily draw diagrams. 

What happens if you need to deal with complex patterns? Break them down into simpler tag-driven problems in a pipeline instead of handling everything in one fell swoop.


![[tests 2023-04-02 07.52.46.excalidraw]]

## Why is Feedback Important?
The most obvious use-case for feedback is to implement a distributed *for* loop.

Languages that have *for* built into them constrain the way we are allowed to think about distributed problems.

One of the tennets of FP style - in fact Denotational Semantics style - of programming, is *to make everything explicit*.  FP fails in this simple goal, in that it hides the use of the call-stack (a LIFO).  

Using *very explicit* drawings allows software architects to create solutions using many more degrees of freedom.  In many cases, too much explitness becomes a burden, is visually "too busy" and breaks the Rule of 7[^7]  In such cases, *syntax* comes to the rescue.  One can wrap *skins* around solutions to make the appearance of the solution more pallatable.

At this moment, most of our syntaxing tools - like Ohm-JS - are targetted at creating skins for textual representations of programs.  On the other hand, most of our current diagram-editing tools, like Excalidraw and draw.io and SVG, can create textual representations of diagrams, so, we can use exising text-biased syntaxing tools while waiting for proper diagram-based syntaxing tools to appear (diagram macros, diagram parsers, etc.)

[^7]: Rule of 7: All details are chopped up into layers.  No node in a layer has more than 7+-2 items in it.  Most programming languages encourage breaking this rule,i.e. no function should have more than 7+-2 lines of code in it, no program module should have more than 7+-2 functions in it, etc, etc.