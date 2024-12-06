#handling multiple errors
try:
    a = int(input("enter integer : "));
    l = [1,6]
    print(l[a])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("index out of bound")
    
print("some important code")