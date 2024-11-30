def square(n):
    'Takes a number and returns square of that number'
    print(n**2)
    
square(5)  
print(square.__doc__)
    
    
    
def cube(n):
    print(n)
    'Takes a number and returns cube of that number' #docstring should always be the first statement in function definition otherwise interpreter will ignore it
    print(n**3)
    
cube(6)  
print(cube.__doc__)
    