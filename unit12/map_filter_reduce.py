l = [1,2,3,4,6,8,5]

#map
l1= map(lambda x: x*x , l)
print('square :',list(l1))


#filter
l2 = filter(lambda x: x>3,l)
print('After filteration :',list(l2))


#reduce
import functools as f
sum = f.reduce(lambda x,y : x+y , l)
print(sum)

from functools import reduce
sum = reduce(lambda x,y : x+y , l)
print(sum)

