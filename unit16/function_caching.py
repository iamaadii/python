import functools as f
import time as t

@f.lru_cache()
def fx(n):
    t.sleep(3)
    return 2*n

print(fx(5))
print(fx(91))
print(fx(45))
print(fx(91))
print(fx(5))


print('---------------------------------------------------------------------')

@f.lru_cache
def fibonacci(n):
    if n<0:
        raise ValueError("Negative arguments are not supported")
    elif n == 0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(50))