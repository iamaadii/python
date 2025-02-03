import turtle
import random

s=turtle.Screen()
t=turtle.Turtle()
turtle.colormode(255)

t.speed(0)

while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.pencolor(r,g,b)
    t.circle(100)
    t.left(5)
    if(t.heading()==0):
        break

s.exitonclick()