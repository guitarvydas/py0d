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

