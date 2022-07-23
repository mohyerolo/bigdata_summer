import turtle
t = turtle.Turtle()
def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def screen_clean():
    t.reset()

def u_pen():
    t.penup()
def d_pen():
    t.pendown()

screen = turtle.Screen()

screen.onkey(turn_left, "Left")
screen.onkey(turn_up, "Up")
screen.onkey(turn_right, "Right")
screen.onkey(turn_down, "Down")

screen.onkey(screen_clean, "c")

screen.onkey(u_pen, "u")
screen.onkey(d_pen, "d")


screen.listen()
turtle.done()