import turtle

t1 = turtle.Turtle()
t1.shape("turtle")

t1.forward(100)
t1.backward(200)
t1.right(90)
t1.goto(-100, 200)
t1.up()
t1.goto(35,98)
t1.color('red')
t1.down()
t1.goto(99, -50)
t1.up()
t1.fillcolor('yellow')
t1.backward(50)
t1.down()
t1.circle(50)
t1.begin_fill()
t1.circle(50)
t1.end_fill()

t1.goto(0,0)
t1.setheading(0)
t1.setheading(90)

t1.stamp()

t1.forward(100)
t1.forward(10)
t1.speed(0)
t1.backward(200)
t1.speed(4)
t1.forward(200)
for i in range(4):
    t1.forward(100)
    t1.right(90)
    t1.speed(i)

t1.speed(0)
for i in range(3):
    t1.forward(100)
    t1.right(120)

t1.hideturtle()
t1.showturtle()
turtle.bgcolor("black")

num1 = turtle.textinput("title", "문자 입력")
t1.write("간단한 그래픽 처리 모듈")
t1.color('white')
t1.pensize(20)
t1.write("글자 쓰기")
t1.write("메시지", font=('맑은 고딕', 9, 'normal'))
t1.forward(200)
t1.write("메시지", font=('맑은고딕', 9, 'normal'))
turtle.done()
# input("Press any key to exit ...")