import turtle
import random

s=turtle.Screen()
s.bgcolor('black')

turtle.colormode(255)
t=turtle.Turtle()

t.width(10)

for i in range(30):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.setheading(random.randrange(0,360,90))
    t.pencolor((r,g,b))
    t.forward(20)


s.exitonclick()
