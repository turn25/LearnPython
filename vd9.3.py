#from __future__ import print_function
import random
a={1:'a ',2:'b',3:'c'}
b = random.choice(a.keys())
c = random.choice(a.values())
print ('key : %s'% b)
print ('value : %s' %c)
test={'so':'1 2 3 4 5 6 7 8'.split(),'chu':'a b c d e f g h'.split()}
d=random.choice(test.keys())
e=random.randint(0,len(test[d])-1)
n=[test[d][e],d]
print n
