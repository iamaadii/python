# for knowing all the functions or variables of any module
import math as n
print(dir(n))
print(type(n.pi))


# for importing all functions or variables from a module
import math  #from math import *
r = math.sqrt(9)
print(r)  

import math as m
print(m.sqrt(49))


#for importing specific functions or variables from a module
from math import pi,sqrt
print(pi)
print(sqrt(110))

from math import sqrt as s
print(s(16))

