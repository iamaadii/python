class A:
    def __init__(self,v):
        self.value = v
    
    def show(self):
        print(f'Value is {self.value}')
    
    
    @property
    def ten_value(self):
        return self.value
    
    
    @ten_value.setter
    def ten_value(self,v):
        self.value = v
        

obj = A(10)
print(obj.ten_value)
obj.ten_value = 67
print(obj.ten_value)
obj.show()  