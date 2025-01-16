'''
super() keyword can be used for accessing method of same name which is 
present in the parent class from inherited class
'''

class parent:
    def parent_method(self):
        print("This is a parent method present inside parent class")
    
    
class child(parent):
    def parent_method(self):
        print("This is parent method present inside child class")
        
        
    def child_method(self):
        print("This is a child method")
        super().parent_method() #for calling parent_method of parent class
        self.parent_method() #for calling parent_method of child class


obj = child()
obj.child_method()
