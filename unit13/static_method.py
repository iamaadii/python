class math:
    
    def __init__(self,n):
        self.num = n
        
    def addto(self,n):
        self.num = self.num+n
    
    @staticmethod #decorator
    def addition(a,b):
        return a + b
    

A = math(5)
print(A.num)
A.addto(48)
print(A.num)
print('sum :',A.addition(4,8))
print('sum :',math.addition(4,8))