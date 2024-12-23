#default constructor
class A:
    def __init__(self):
        print("It's a default constructor")
    
a = A()


#parametrized constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'{self.name} is {self.age} years old')
    
a = Student("Sandeep",19)
a.info()
