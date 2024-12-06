import string
import random

ran = ''.join(random.choices(string.ascii_letters,k=3))
print(ran) 

a = input("enter word : ")
b = input("what to do of given characters : ")

if b=="code":
    if len(a)>3 or len(a)==3:
        c = a.replace(a[len(a)-1],a[0])
        d = c.replace(a[0],'')
        e = ran+d+ran
        print(e)
    else:
        print(a[::-1])
        
elif b == "decode":
    if len(a)<3:
        print(a[::-1])
    else:
        pass