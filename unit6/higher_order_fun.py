#without any arguments

def greet():
    print('Hi')
    
def dislay(func): #higher order function
    print('This is display() function')
    func()
    
dislay(greet)

print('---------------------------------------------------------------')


#with arguments
def louder(name):
    print(f'Hello, {name.upper()}')
    
def hello(fx,nam): #higher order function
    print('This is hello() function')
    fx(nam)

hello(louder,'aditya')


print('---------------------------------------------------------------')




#with return-type

def calc(a,b): #higher oder function
    print('From calc function')
    def add():
        print(a+b)
    def mul():
        print(a*b)
    if a==b:
        return add
    else:
        return mul

new_fun=calc(10,10)
new_fun()