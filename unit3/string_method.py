#strings are immutable
a = "Aditya"
print(a.upper())
print(a.lower())
print(a.islower())
print(a.isupper())

print("------------------------")

b = "!!!!Ajay!!!!"
print(b.rstrip('!'))
print(b.strip("!"))
print(b.replace("Ajay","Amit"))
print(b.replace("!","2"))

print("------------------------")

c = "!!!! Ajay !!!!" 
print(c.split(' '))
print(c.count("!"))
print(c.endswith("!"))
print(c.endswith("ay",0,9)) # index 9 will be not count here
print(c.startswith("!"))

print("------------------------")

d = "introduction To pyThOn"
print(d.capitalize())   
print(d.title())

print("------------------------")

e = "Welcome To Console"
print(e.center(36))
print(e.istitle())
print(e.swapcase())

print("------------------------")

f = "He's name is dan.He is a honest man"
print(f.find("is"))
print(f.find("don")) # returns -1 if it is not find
print(f.index("He")) 
#print(f.index("dog")) gives an error

print("------------------------")

g = "Welcometoconsole01"
print(g.isalnum())
print(g.isalpha())
print(g.isprintable())

print("------------------------")

h =" "
print(h.isspace())

