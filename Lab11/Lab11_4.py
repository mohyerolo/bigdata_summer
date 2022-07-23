import turtle
import random

turtles = []
t1 = turtle.Turtle()
t1.shape("turtle")
t1.up()
t1.speed(1)

for i in range(3):
    turtles.append(t1)
    

for i in range(10):
    dist = random.randint(1, 100)
    degree = random.randint(0, 360)
    t1.setheading(degree)
    t1.forward(dist)
    # t1.write("dist: %d degree: %d" % (dist, degree), font=('맑은 고딕', 9, 'normal'))
turtle.done()