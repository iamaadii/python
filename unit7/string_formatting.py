l1 = "My name is {} and I am from {}"
name = "aditya"
country = "india"
print(l1.format(name,country))  

l2 = "My name is {1} and I am from {0}"
print(l2.format("india","aditya"))

l3 = "for only {price:.3f} dollars"
print(l3.format(price=49.641458))