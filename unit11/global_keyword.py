x = 10

def fun():
    global x  #changing global variable through inside the function
    x = 20
    print(x)
    
fun()
print(x)