a = 4
b = '4'
print(a==b) #compares values
print(a is b,'\n') #exact location of object in memory

c = [1,2,3]
d = [1,2,3]
print(c is d) #false because tuple is mutable in nature
print(c==d,'\n')

e = (3,4)
f = (3,4)
print(e is f) #true because tuple is immutable in nature
print(e==f,'\n')

g = None
h = None
print(g is h)
print(g==h)
print(g is None)
