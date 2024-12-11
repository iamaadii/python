#with single arguments
square = lambda x : x*x
print("Square :",square(5))

#with multiple arguments
add = lambda x,y: x+y
print("sum :",add(6,8))

#with additional print statements
mult = lambda x, y: print(f'{x} * {y} = {x * y}')
mult(5,2)

#passing function inside function also known as higher order function
def sol(fx,val):
    return 6+fx(val)
print(sol(lambda x:2*x , 9))



