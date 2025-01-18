class A:
    def display(self):
        print("This is class A")
class B(A):
    def display(self):
        print("This is class B")
class C(A):
    def display(self):
        print("This is class C")
class D(B,C):
    pass
    
d1 = D()
d1.display()  
print(D.__mro__)
print(D.mro())