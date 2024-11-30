import time
t1 = time.strftime('%H:%M:%S')
h = int(time.strftime('%H'))
if (h>=0 and h<=12):
    print("Good Morning")
elif(h>12 and h<=16):
    print("Good Afternoon")
elif(h>16 and h<=20):
    print("Good evening")
elif(h>20 and h<=24):
    print("Good Night")

    