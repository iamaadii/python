a = input("enter any number btween 1 and 10 : ")
if(int(a)<=1 or int(a)>=10):
    raise ValueError("value should be between 1 and 10")
    