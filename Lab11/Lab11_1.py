import turtle

t1 = turtle.Turtle()
t1.shape("turtle")

t1.color('red')
t1.stamp()

t1.color('yellow')
t1.forward(200)
t1.left(50)
t1.begin_fill()
t1.circle(60)
t1.end_fill()

t1.goto(-150, -100)
t1.color('black')
t1.speed(4)
for i in range(5):
    t1.forward(100)
    t1.right(72)

t1.up()
t1.forward(200)
t1.write('20180973')
t1.pensize(15)
t1.down()
t1.color('red')
t1.right(180)
t1.forward(100)
t1.write("메시지", font=('맑은 고딕', 9, 'normal'))

turtle.done()
