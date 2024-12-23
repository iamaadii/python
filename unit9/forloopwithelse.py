# else block only execute if loop is finished
for i in range(5):
    print(i,end=',')   
else:
    print("\nLoop finished")
    
    
for i in range(6):
    print(i,end=',')
    if i == 4:
        continue
else :
    print("\nLoop finished")



#here loop is not finished thats why it will not execute else block
for i in range(6):
    print(i,end=',')
    if i == 4:
        break
else :
    print("\nLoop finished")
    