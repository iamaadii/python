def add(a,b):
    print("sum :",(a+b))

def sub(a,b):
    print("substraction :",a-b)

def max(a,b):
    if a>b:
        print("max :",a)
    elif a<b:
        print("max :",b)
    else:
        print("Both are equal")

def min(a,b):
    if a>b:
        print("min :",b)
    elif a<b:
        print("min :",a)
    else:
        print("Both are equal")
    
a = 7
b = 8   
add(a,b)

c = 15
d = 5
sub(c,d)

max(4,5)
min(7,9)