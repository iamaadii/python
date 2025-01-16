#public
class A:
    def __init__(self):
        self.name = "aditya"   #public variable    
obj = A()
print(obj.name)




#private
class B:
    def __init__(self):
        self.__name = "Amit"  #private variable
    
obj = B()
#print(obj.__name) cannot accessed directly
print(obj._B__name)
print(dir(obj)) #name mangling




#protected
class Student:
    def __init__(self):
        self._name = "Harry"    #protected variable

    def _funName(self):     # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())