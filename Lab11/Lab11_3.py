import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("red")

t.up()
index = 20
for i in range(45):
    t.stamp()
    t.forward(index)
    t.right(25)
    index += 3

turtle.done()