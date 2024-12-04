d = {'name' : 'Aditya','age' : 18,'rno' : 28}
d.update({'DOB' : 2006})
print(d)

# to remove only one key-value pair at a time
d.pop('rno')
print(d)
del d['age']
print(d)

#to remove last key-value pair
d.popitem()
print(d)

# to remove all items(key-values) from dict
d.clear()
print(d)
