import turtle

s=turtle.Screen()
t=turtle.Turtle()

colors = ['red','blue','yellow','pink','orange','darkblue','purple','cyan','brown','alice blue']
t.pensize(4)

for i in range(3,11):
    angle = 360/i
    t.pencolor(colors[i-3])
    for j in range(i):
        t.right(angle)
        t.forward(100)
    
s.exitonclick()
