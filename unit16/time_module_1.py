import time as t

def loop():
    for i in range(50):
        print(i)
        
            
a = t.time()
loop()
print("Time taken by function to execute it in seconds : ",t.time()-a)