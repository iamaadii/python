import asyncio as a

async def fun1():
    await a.sleep(1)
    print("fun1 done")
    
async def fun2():
    await a.sleep(1)
    print("fun2 done")

async def fun3():
    await a.sleep(4)
    print("fun3 done")
    
async def main():
    task = a.create_task(fun1())
    await fun2()
    await fun3()
    
async def main1():
    task = a.create_task(fun1())
    await fun2()
    await fun3()
    
a.run(main())
    