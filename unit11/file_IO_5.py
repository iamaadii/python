with open('unit11/file5.txt','w') as f:
    f.write("hello world")
    print(f.tell())
    f.truncate(4)
    
with open("unit11/file5.txt",'r') as f:
    print(f.read())