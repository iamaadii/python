def fun():
    try:
        l = [5,6,8]
        i = int(input("enter index : "))
        print(l[i])
        return 1
    except:
        print("index out of range")
        return 0
    finally:
        print("It will always executed")
        
x = fun()
print(x)