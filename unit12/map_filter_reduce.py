l = [1,2,3,4,6,8,5]

#map
l1= list(map(lambda x: x*x , l))
print(f'square : {l1}')



#filter
def filter_function(x):
    return True if x>3 else False

l2 = list(filter(filter_function,l))
print(f'After filteration : {l2}')



#reduce
import functools as f
sum = f.reduce(lambda x,y : x+y , l)
print(sum)

from functools import reduce
sum = reduce(lambda x,y : x+y , l)
print(sum)

