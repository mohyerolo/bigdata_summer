import turtle

t = turtle.Turtle()
t.shape("turtle")

turtle.bgcolor("black")
t.pencolor("red")

t.setheading(90)
t.forward(100)

print(t.position())
t.write("안녕하세요", align='left', font=('Arial', 8, 'normal'))
turtle.done()