# 마우스 클릭 이벤트
import turtle

def draw(x, y):
    # t1.goto(x, y)
    t1.penup()
    t2.penup()
    t1.goto(x, y)
    t2.goto(x + 100, y + 100)
    t1.down()
    t2.down()

    t2.circle(20)
    t1.color("red", "gray")
    t1.begin_fill()
    for i in range(4):
        t1.forward(100)
        t1.right(90)
    t1.end_fill()

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t2.color("green")

screen = turtle.Screen()
screen.onscreenclick(draw)

screen.listen()
turtle.done()