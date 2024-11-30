#union and update
s1 = {1,2,5,6}
s2 ={3,6,7}
print("union : ",s1.union(s2)) #it will not change the actual value present in a set
s1.update(s2) #it will change the actual value present in a set
print(s1,s2)

#intersection and intersection_update
s3 = {3,7,8,6}
s4 = {3,6,5,10};
print("intersection :",s3.intersection(s4)) #it will not change the actual value present in a set
s3.intersection_update(s4) #it will change the actual value present in a set
print(s3,s4)

#symmetric_difference and symmetric_difference_update
s5 = {1,2,7}
s6 = {2,6,7,9}
print("symmetric_difference :",s5.symmetric_difference(s6)) #it will print the value which are not common in both
s5.symmetric_difference_update(s6) #it will change the actual value present in a set
print(s5,s6)

#difference and difference_update
s7 = {4,5,9,6}
s8 = {6,7,8,9}
print("Difference :",s7.difference(s8))
s7.difference_update(s8)
print(s7,s8)

#disjoint
a = {1,2}
b = {4,5}
print(a.isdisjoint(b))

#superset and subset
c = {1,5,3,9}
d = {5,9}
print(c.issuperset(d))
print(d.issubset(c))