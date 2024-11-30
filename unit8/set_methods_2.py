#some other methods
e = {1,15,7}
if 15 in e:
    print("found")
else:
    print("not found")
e.add(4) #for adding a element in the set
print(e)
e.remove(15) #or e.discard(15)
print(e)
print(e.pop()) #remove a random value from set
print(e)
e.clear() #clear all the value from set
print(e) 
del e #deletes the entire set