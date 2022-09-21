# Python 3.7.1

import turtle

turtle.speed(speed=100)

turtle.color('black', 'pink')
turtle.begin_fill()
for i in range(9):
    turtle.forward(250)
    turtle.left(160)
turtle.end_fill()

turtle.hideturtle()

turtle.color('grey', 'yellow')
turtle.begin_fill()

for i in range(44):
    turtle.backward(185)
    turtle.right(150)
turtle.end_fill()

turtle.color('purple')
for i in range(38):
    turtle.width(1/100 + 1)
    turtle.forward(40)
    turtle.left(49)
turtle.end_fill()

turtle.color('red', 'yellow')
turtle.begin_fill()

for i in range(44):
    turtle.backward(130)
    turtle.right(170)
turtle.end_fill()

turtle.color('black')

for i in range(30):
    turtle.circle(15*i)
    turtle.circle(-15*i)
    turtle.left(i)
turtle.end_fill()

turtle.done()
