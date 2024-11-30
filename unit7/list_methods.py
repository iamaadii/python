l = [7,1,3]
l.append(4)
print(l)
l.sort() #in ascending order
print(l)
l.sort(reverse=True) #in descending order
print(l)
l.reverse() #reverse the list
print(l)
print(l.index(3))

m = l.copy()
m[0] = 0
print(m)
print(l)
m.pop(1)
print(m)

l.insert(2,45)
print(l)

n =[10,20]
l.extend(n)
print(l)
