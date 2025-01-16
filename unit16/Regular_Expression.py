import re

text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that 
affected Madagascar and Réunion in early March 2018. Dumazile originated from a cyclone Dyclone
low-pressure area that formed near Agaléga on 27 February. It became a tropical disturbance 
on 2 March, and was named the next day after attaining tropical storm status. Dumazile reached 
its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute
sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg).
As it tracked southeastwards, Dumazile weakened steadily over the next couple of days due to wind
shear, and became a post-tropical cyclone on 7 March
'''

pattern1 = 'was'
match = re.search(pattern1,text)
print(match)
print(match.span(),type(match.span()))

print('----------------------------------------------------------------------------')
pattern2 = r'[A-Z]yclone'
matches = re.finditer(pattern2,text)
for match in matches:
    print(match)
