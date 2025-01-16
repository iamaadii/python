import array as a

arr = a.array('i',[4,5,8,9,]) #here i is typecode
print(arr)  
print(arr.buffer_info())
print(arr.typecode)
arr.reverse()
print(arr)
print(type(arr))