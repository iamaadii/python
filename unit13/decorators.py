#without argument
def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello, how are you?")
    
hello()




#with arguments
def g(fx):
    def mfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@g
def add(a,b):
    print("sum :",a+b)
    
add(5,9)