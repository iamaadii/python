def fun(*args,name):
    print(args)
    
# fun(1,2,'aman') #by-default it will take 'aman' in the form of tuple thats why it will give error


#ways for solving above problem
def fun(*args,name):
    print(args)
    print(name)
    
fun(1,2,name = 'aman') #by passing name as keyword argumnents

def fun(name,*args):
    print(args)
    print(name)
    
fun('aman',1,2)  #by passing normal arguments first