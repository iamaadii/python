class person:
    name = 'Aman'
    work = 'student'
    age = 18
    def greet(self):
        print(f'{self.name} is a {self.work}')
    
    
a = person()
print(f'Name : {a.name} \nAge : {a.age}')
a.greet()

a.name = 'ajay' #modifying details
print(f'Name : {a.name} \nAge : {a.age}')
a.greet()

#for deleting object properties
del a.age
print(f'Name : {a.name} \nAge : {a.age}')

#for deleting object
del a
    