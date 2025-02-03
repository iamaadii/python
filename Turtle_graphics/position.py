import turtle

s=turtle.Screen()
s.bgcolor("black")

t=turtle.Turtle()
t.pensize('5')
t.shape('turtle')
t.color('white','red')

t.hideturtle() #for hiding turtle
print(t.isvisible()) #for checking whether turtle is visible or not
t.circle(100)
print(t.position())
t.goto(100,0) #for moving turtle position 100 towards x-axis.
t.showturtle()
print(t.isvisible()) #for checking whether turtle is visible or not

s.exitonclick()