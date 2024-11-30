# finding factorial of a given number
def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))


#printing fibonacci series
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
for i in range(1,6):
    print(fib(i),end=" ")