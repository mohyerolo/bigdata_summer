import turtle
import random

t1 = turtle.Turtle()

def turn_left():
    t1.color(random.choice(colors))
    t1.setheading(180)
    d = random.randint(20, 100)
    t1.forward(d)

def turn_up():
    t1.color(random.choice(colors))
    t1.setheading(90)
    d = random.randint(20, 100)
    t1.forward(d)
    for i in range(3):
        t1.forward(d)
        t1.left(120)

def turn_right():
    t1.color(random.choice(colors))
    t1.setheading(0)
    d = random.randint(20, 100)
    t1.forward(d)
    for i in range(4):
        t1.forward(d)
        t1.left(90)

def turn_down():
    t1.color(random.choice(colors))
    t1.setheading(270)
    d = random.randint(20, 100)
    t1.forward(d)
    for i in range(5):
        t1.forward(d)
        t1.left(144)

colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
screen = turtle.Screen()
screen.onkey(turn_left, "Left")
screen.onkey(turn_up, "Up")
screen.onkey(turn_right, "Right")
screen.onkey(turn_down, "Down")
screen.listen()

turtle.done()