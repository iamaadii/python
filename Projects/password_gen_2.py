#prgm to generate hard password

import random as r
import string as s
print('Welcome to password Generator')
lett = int(input('No of letters : '))
sym = int(input('No of symbols : '))
num = int(input('No of digit : '))

l = s.ascii_letters
d = s.digits
s = s.punctuation

list = []
for i in range(0,lett):
    list += r.choice(l)
for i in range(0,sym):
    list +=r.choice(s)
for i in range(0,num):
    list+=r.choice(d)

r.shuffle(list)
a = ''.join(list)
print('Your password is :',a)