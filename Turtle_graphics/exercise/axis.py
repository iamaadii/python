import turtle

s=turtle.Screen()
s.bgcolor('black')
t=turtle.Turtle()
t.pensize(5)
t.color('red','yellow')


t.forward(100)
t.penup()
t.backward(100)
t.pendown()
t.backward(100)
t.penup()
t.forward(100)
t.pendown()
t.left(90)
t.forward(100)
t.penup()
t.backward(100)
t.pendown()
t.backward(100)

t.hideturtle()


s.exitonclick()