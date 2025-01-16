import numpy as n

a = n.array([4,1,2,5])
print(a)

a=a+5
print(a)

b = n.array([2,8,7,5],float)
c=a+b
print(c)



print('sum : ',n.sum(b))
print('sin values : ',n.sin(b))
print('log values : ',n.log(b))
print('sqrt : ',n.sqrt(b))
print('min : ',n.min(b))
print(a.dtype)
print(b.dtype)

