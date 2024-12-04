fruits = ("mango","apple","guava")
temp = list(fruits)
temp.append("pineapple")
temp.pop(2)
temp[1] = "orange"
fruits = tuple(temp)
print(fruits)

#concatenate two tuples
coun1 = ("india",'china')
coun2 = ("usa","canada")
overall = coun1+coun2
print(overall)


t1 = (1,5,3,2,4,2)
print(t1.count(2)) #total occurence of particular element in the tuple
print(t1.index(2)) #returns the first occurence of given element that is 2
print(t1.index(2,4)) #returns the first occurence of given element in given range