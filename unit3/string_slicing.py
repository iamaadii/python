#positive slicing
a = "Aditya patel"
print(a[0:5]) #here index 0 would be included but not index 5
print(a[:5]) #here interpreter takes starting index as 0 by-default

#negative slicing
b = "Sandeep"
print(b[0:-3])
print(b[0:len(b)-3])
print(b[-1:-3]) #this will print nothing because it is trying to print from index 6 to 4 which is logically wrong
 