import turtle

s=turtle.Screen()
t=turtle.Turtle()

def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)
    
def turn_left():
    new_heading = t.heading()+20
    t.setheading(new_heading)
    t.forward(20)
    
def turn_right():
    new_heading = t.heading()-20
    t.setheading(new_heading)
    t.forward(20)

def clear_screen():
    t.reset()
    
s.listen()
s.onkey(move_forward,'f')
s.onkey(move_backward,'b')
s.onkey(turn_left,'l')
s.onkey(turn_right,'r')
s.onkey(clear_screen,'c')



s.exitonclick()