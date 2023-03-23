python version of 0D

It is intended that this will superceded by vsh, in the future.

This version is example of 4 simple tests:
1. echo 'Hello'
2. same as 1, but, using a container to wrap Echo
3. same as 2, except, using a container to wrap the containera of Echo
4. a parallel version - the input messages ('Hello' and 'World') are down-forwarded to two different Echos, both feed the same output, hence, you should see 4 messages in the final output queue ('pHello', 'pHello', 'pWorld', 'pWorld')
