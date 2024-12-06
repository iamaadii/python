a = [10,20,40,85,69]

#enumerate function will by-default start index with 0
for index,data in enumerate(a):
    print(f"{index} : {data}")
    
print("\n")
#for starting from some other index rather than 0
for index,data in enumerate(a,start=1):
    print(f"{index} : {data}")