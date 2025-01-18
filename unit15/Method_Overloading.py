#ways for achieving method overloading

#1
class demo:
    def add(self,a,b,c=0):
        return a+b+c

d1 = demo()
print(d1.add(12,34))
print(d1.add(12,34,45))



#2
class demo:
    def add(self,*args):
        res = 0
        for i in args:
            res += i
        return res

d2 = demo()
print(d2.add(12,34))
print(d2.add(12,34,45))
