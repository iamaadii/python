class B:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f'Name is {self.name}'
    
    def __repr__(self):
        return f'My age is {self.age}'
    
    def __call__(self):
        print('Hello World')

e=B("Ajay",18)
print(e)
print(str(e)) 
print(repr(e))
e()


'''
=> all the above given print statements will print the address of object(e) 
   without '__str__' and '__repr__'  method.
=>  If we comment the '__str__' method and trying to print 'str' or 'object_name' then by-default
    it will print the 'repr' method.
=>  If we comment the '__repr__' method and trying to print 'repr' then it will print the object 
    address and if we are printing the 'object_name' then it will by-default print 'str' method.
=>  If we not commenting any one of the method and trying to print 'object_name' then by-default 
    it will print the '__str__' method. 



'''

