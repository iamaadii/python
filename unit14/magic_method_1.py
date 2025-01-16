#this type of methods used for creating own methods.

class A:
    name = "Aditya"
    
    def __len__(self):
        i=0
        for item in A.name:
            i+=1
        return i
    
obj = A() 
print(len(obj))