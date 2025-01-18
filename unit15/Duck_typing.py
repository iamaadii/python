class Duck:
    def swim(self):
        print('Duck can swim')
    def speaks(self):
        print('Quack quack')
class Dog:
    def swim(self):
        print('Dog cannot swim')
    def speaks(self):
        print('woof woof')
        
def display(obj):
    obj.swim()
    obj.speaks()  


obj1 = Duck()
display(obj1)

obj2 = Dog()
display(obj2)