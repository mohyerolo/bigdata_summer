import turtle

t = turtle.Turtle()

t.hideturtle()
t.up()
t.goto(100, 100)
t.write("입력된 정수는 양의 정수입니다.", font=('맑은 고딕', 11, 'normal'))

t.goto(100, 0)
t.write("입력된 정수는 0입니다.", font=('맑은 고딕', 11, 'normal'))

t.goto(100, -100)
t.write("입력된 정수는 음의 정수입니다.", font=('맑은 고딕', 11, 'normal'))

t.goto(0,0)
t.showturtle()
t.down()
t.shape("turtle")

num = turtle.numinput("", "숫자를 입력하시오: ")
if num < 0:
    t.goto(100, -100)
elif num > 0:
    t.goto(100, 100)
else: t.goto(100,0)

turtle.done()