import turtle

s = turtle.Screen()
t=turtle.Turtle()

t.pensize(5) #by-default its one
t.shape('arrow')
t.color('red','green') #here first arguments is for pencolor and second is for fillcolor.
t.begin_fill()  #for filling circle by-default it will fill it with 'green'.
t.circle(100)
t.end_fill()

t.right(90)
t.penup() #to give some space between two things
print(t.isdown()) #for checking whether pen down or not
t.forward(100)
t.pendown()
print(t.isdown()) #for checking whether pen down or not
t.circle(100)

s.exitonclick()