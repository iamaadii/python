x = 10 #global variable

def fun():
    x = 11
    y = 20 #local variable 
    print("local variable : ",x,y)
    
fun()
print("global variable : ",x)
#print("local variable : ",y) shows an error bcoz we cannot access local variable from outside the function

    
