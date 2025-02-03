import numpy as n

mat = n.array([ [1,2,3],[4,5,6],[8,9,6]])
print(mat)
print(mat.ndim)
print(mat.shape)
print(mat.size)
print(mat.diagonal())

arr = mat.flatten()  #for converting 2-d array into 1-d array
print(arr)

mat1=arr.reshape(3,3) #for converting 1-d array into 2-d array
print(mat1)
print(n.diagonal(mat))


#another way to create matrix
m=n.matrix('1 2 ; 3 4')
print(m)
print(n.diagonal(m)) #diagonal elements
