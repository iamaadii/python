class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromstr(cls,str):
        return cls(str.split(',')[0],int(str.split(',')[1]))
        
e1 = Employee("harry",51000)
print(e1.name)
print(e1.salary)

s = "John,12000"
e2 = Employee.fromstr(s)
print(e2.name)
print(e2.salary)
