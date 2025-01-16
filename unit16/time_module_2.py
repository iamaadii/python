import time 

t = time.localtime()
formatted_time = time.strftime("%d/%m/%y  %H:%M:%S",t)
print(formatted_time)