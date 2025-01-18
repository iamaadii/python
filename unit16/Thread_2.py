import threading
import time 
import concurrent.futures

def fun(sec):
    print(f'sleeping for {sec} seconds')
    time.sleep(sec)


def poolingDemo():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(fun,3)
        future2 = executor.submit(fun,1)
        future3 = executor.submit(fun,2)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        
def poolingDemo1():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        l=[1,3,2,1]
        results = executor.map(fun,l)
        for r in results:
            print(r)
    
poolingDemo()
print('-----------------------------------------------------------------------------------------------')
poolingDemo1()