import turtle
import random

height=width=400

def no_of_turtles():
    flag=True
    while flag:
        n=int(input('How many turtles u want to race(2-10): '))
        if(n>10 or n<2):
            print('Invalid input...Try again!!!!')
            flag=True
        else:
            return n
    

turtles = no_of_turtles()
print(turtles)

s=turtle.Screen()
s.screensize(height,width)
s.colormode(255)

spacing = 400//(turtles+1)

turtle_list=[]
for i in range(1,turtles+1):
    new_turtle = turtle.Turtle()
    turtle_list.append(new_turtle)
    new_turtle.shape('turtle')
    new_turtle.left(90)
    new_turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    new_turtle.penup()
    new_turtle.setpos(-width//2+(i*spacing),-height//2)
    

def race():
    is_race_on = True
    while is_race_on:
        for index,t in enumerate(turtle_list):
            distance = random.randint(1,20)
            t.forward(distance)
            x,y=t.pos()
            if(y>=height//2):
                print(f'The winner is {index+1} turtle')
                is_race_on = False


race()

s.exitonclick()