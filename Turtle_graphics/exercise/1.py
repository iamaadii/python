import turtle

s=turtle.Screen()

t=turtle.Turtle()

t.color('yellow','red')
t.pensize(5)
t.penup()
t.goto(-320,0)
t.pendown()
t.circle(50)
t.penup()
t.forward(500)
t.pencolor('red')
t.pendown()

for i in range(4):
    t.forward(80)
    t.left(90)

t.right(90)    
t.penup()
t.forward(200)
t.pendown()
t.pencolor('blue')
t.left(90)

angle=360//5

for i in range(5):
    t.forward(80)
    t.left(angle)
    
t.left(180)
t.penup()
t.forward(400)
t.pendown()
t.pencolor('green')

for i in range(3):
    t.forward(80)
    t.right(120)
    
t.hideturtle()

s.exitonclick()