#prgm to generate simple password

import random as r
import string as s
print('Welcome to password Generator')
lett = int(input('No of letters : '))
sym = int(input('No of symbols : '))
num = int(input('No of digit : '))

l = s.ascii_letters
d = s.digits
s = s.punctuation

password = ''
for i in range(0,lett):
    password += r.choice(l)
for i in range(0,sym):
    password+=r.choice(s)
for i in range(0,num):
    password+=r.choice(d)

print(password)