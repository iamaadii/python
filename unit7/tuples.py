t1 = (15,25.5,"aditya",True)
#t1[0] = 23 shows an error bcoz tuple is immutable in nature
print(type(t1)," ",t1)
print(t1[1]) #accesing element through index
print(len(t1))
if 15 in t1:
    print("found")
else:
    print("not found")

print(t1[1:4])


t2 = (15)
print(type(t2))

t3=(18,)
print(type(t3))