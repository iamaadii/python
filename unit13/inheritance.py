class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Child(Parent):
    def show(self):
        print(f"{self.name},{self.age}")
        print("default language is python")
    
obj = Parent("Abraham",45)
print(obj.info())  
#print(obj.show()) we cannot access child member with the parent class object 

obj1 = Child("Amit",18)
obj1.show()