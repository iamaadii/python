import array as a

arr = a.array('i',[4,5,8,9]) #here i is typecode
print(arr)  
print(arr.buffer_info())
print(arr.typecode)

arr.reverse()
print(arr)
arr.append(55)
print(arr)
arr.remove(5)
print(arr)

print(type(arr))

print("Size:",len(arr))
print("Sum:",sum(arr))
print("min:",min(arr))
print("max:",max(arr))

print(arr[0])

b=arr.__copy__()
print(b)