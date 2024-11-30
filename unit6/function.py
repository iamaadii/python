def add(a,b):
    print("sum :",(a+b))

def sub(a,b):
    print("substraction :",a-b)

def maximum(a,b):
    if a>b:
        print("max :",a)
    elif a<b:
        print("max :",b)
    else:
        print("Both are equal")

def minimum(a,b):
    if a>b:
        print("min :",b)
    elif a<b:
        print("min :",a)
    else:
        print("Both are equal")
        
def addition(a,b):
    pass   #here pass tells the interpreter to execute onwards statements
    
a = 7
b = 8   
add(a,b)

c = 15
d = 5
sub(c,d)

maximum(4,5)
minimum(7,9)