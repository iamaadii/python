#dir method
l=[2,5] 
print(dir(l))  #display all the methods of list
print("------------------------------------------------------")



#__dict__ attribute
class details:
    def __init__(self,name,age):
        self.name=name
        self.age=age;
        self.DOB = '14/2/2005'

obj=details("Shivam",19)      
print(obj.__dict__)
print("------------------------------------------------------")




#help
print(help(details))


