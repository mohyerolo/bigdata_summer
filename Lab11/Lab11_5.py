import turtle

def draw(x, y):
    t1.penup()
    t1.goto(x, y)
    t1.down()

    t1.color("orange", "orange")
    t1.begin_fill()
    for i in range(3):
        t1.forward(100)
        t1.left(120)
    t1.end_fill()

t1 = turtle.Turtle()

screen = turtle.Screen()
screen.onscreenclick(draw)

screen.listen()
turtle.done()