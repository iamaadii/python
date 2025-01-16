def gen():
    for i in range(5):
        yield i
        
obj = gen()
print(next(obj))  
print(next(obj))  
print(next(obj))  
print(next(obj))  
print(next(obj))    