import time
t1 = time.strftime('%H:%M:%S')
print(t1)
t = int(t1)
h = int(time.strftime('%H'))
print(h)
m = int(time.strftime('%M'))
print(m)
s = int(time.strftime('%S'))
print(s)
if (h>=04 and h<=07):
    print("Good Morning")
elif(h>=12 and h<=13):
    print("Afternoon")
elif(h>=16 and h<=18):
    print("evening")
else:
    print("end")
    