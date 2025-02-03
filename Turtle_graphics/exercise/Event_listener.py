import turtle

s=turtle.Screen()
t=turtle.Turtle()

def up():
    t.setheading(90)
    
def down():
    t.seth(270)
   
def left():
    t.seth(180)
   
def right():
    t.seth(0)
    
def forward():
    t.fd(20)

def clear():
    t.reset()
    
turtle.listen()   #or s.listen()
s.onkey(fun=up,key="Up")
s.onkey(fun=down,key="Down")
s.onkey(fun=left,key="Left")
s.onkey(fun=right,key="Right")
s.onkey(fun=clear,key="c")
s.onkey(forward,'space')


s.exitonclick()