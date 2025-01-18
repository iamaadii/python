from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres=n
    
    @abstractmethod
    def start(self):
        pass
    
    def display(self):    #concrete method
        print('From vehicle class')

class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color = color
    def start(self):
        print('Starts with kick')
        
class Scooty(Vehicle):
    def __init__(self,n):
        self.no_of_tyres=n
    def start(self):
        print('Starts with self')
        
class Car(Vehicle):
    def __init__(self,n):
        self.no_of_tyres=n
    def start(self):
        print('Starts with key')
        

bike = Bike(2,'Red')
print(bike.no_of_tyres)
print(bike.color)
bike.start()
bike.display()
print('-------------------------------------------------------------------------------')

scooty = Scooty(2)
print(bike.no_of_tyres)
scooty.start()
scooty.display()
print('-------------------------------------------------------------------------------')

car = Car(2)
print(bike.no_of_tyres)
car.start()
car.display()