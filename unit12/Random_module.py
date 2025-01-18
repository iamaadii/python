import random as r
print(r.randint(1,5))
print(r.randrange(7,12))
print(r.random())
print(r.uniform(2,5))

l = [45,82,-1,43]
print(r.choice(l))
r.shuffle(l)
print(l)

s = 'aditya'
print(r.choice(s))