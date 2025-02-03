import turtle

s=turtle.Screen()
t=turtle.Turtle()

for i in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    
s.exitonclick()