import turtle

s=turtle.Screen()

t=turtle.Turtle()
t.pensize(3)
t.speed(0)
t.color('red','yellow')

t.begin_fill()
while True:
    t.fd(300)
    t.left(170)
    if t.heading()==0:
        break
    
t.end_fill()
    
s.exitonclick()