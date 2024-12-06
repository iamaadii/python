# handling single error
a = int(input("enter a : "));
b = int(input("enter b : "))

try:
    print("quotient = ",a/b)
except:
    print("error : division by zero is not allowed")
    
print("some important code")

