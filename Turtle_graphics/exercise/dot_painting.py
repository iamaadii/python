import turtle
import random

s=turtle.Screen()
print(s.screensize()) #for getting screen size
s.screensize(600,700)

t=turtle.Turtle()
turtle.colormode(255)
t.speed(0)

for i in range(100):
    t.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.dot(20)
    t.penup()
    t.goto(random.randint(-300,300),random.randint(-300,300))
    t.pendown()









s.exitonclick()