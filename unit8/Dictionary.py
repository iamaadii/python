d = {'name' : 'Aditya','age' : 18,'rno' : 28}
print(d)

# ways of accesing single value using keys
print(d['name']) #shows an error if key doesnot exist
print(d.get('name')) # prints None if key does not exist 

#accessing all keys
print(d.keys())

#accessing all values
print(d.values())

#accesing all values using keys
for i in d.keys():
    print(d[i])
    
#accesing both key-value pairs
print(d.items())