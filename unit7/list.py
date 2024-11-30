l2 =["aditya",4,78.5,True,None]
print(type(l2))
#accesing element
print(l2) #postive indexing
print(l2[-3])  #negative indexing
print(l2[len(l2)-3])    
print(l2[2])  
#check whether element is present in list or not
if "adi" in "aditya":
    print("yes")
else:
    print("no")
if 4 in l2:
    print("yes")
else:
    print("no")
    
if "4" in l2:
    print("yes")
else:
    print("no")
    
    
    
l1=[5,10,15,20,25]
print(l1[:]) #print all elements
print(l1[1:]) #print all elements from index 1
print(l1[:3]) #print all elements up to index 2
print(l1[1:4]) #print all element from index 1 to 3
print(l1[1:-1])
print(l1[0:5:2]) #print alternative values