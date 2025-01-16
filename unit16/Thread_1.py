import threading
import time 

def fun(sec):
    print("sleeping for",sec,'seconds')
    time.sleep(sec)
    
t = time.time()    
fun(2)
fun(1)
fun(0)
print(time.time()-t)


print('----------------------------------------------------------------------------------------')

time1 = time.time()   
t1=threading.Thread(target=fun,args=[2])
t2=threading.Thread(target=fun,args=[2])
t3=threading.Thread(target=fun,args=[1])
t1.start()
t2.start()
t3.start()

time2 = time.time()   
print(time2-time1)



print('----------------------------------------------------------------------------------------')

time1 = time.time()   
t1=threading.Thread(target=fun,args=[4])
t2=threading.Thread(target=fun,args=[2])
t3=threading.Thread(target=fun,args=[1])
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.time()   
print(time2-time1)