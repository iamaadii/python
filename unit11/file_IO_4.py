with open('unit11/file4.txt','r') as f:
    print(type(f))
    
    f.seek(10)
    print("current position :",f.tell())
    print(f.read(6))