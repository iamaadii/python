class emplyoee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class programmer(emplyoee):
    def __init__(self,name,age,lan):
        super().__init__(name,age)
        self.lang=lan
    
obj=programmer("Vikram",20,'python')
print(obj.name)
print(obj.age)
print(obj.lang)