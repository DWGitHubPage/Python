# Python 3.7.1

import turtle

turtle.hideturtle()
turtle.speed(speed=1000)

for i in range(110):
    turtle.color('red')
    turtle.forward(60)
    turtle.left(90)
    turtle.backward(40)
    turtle.right(50)
    turtle.forward(60)
    turtle.left(60)
    turtle.backward(60)
    turtle.color('black')
    turtle.circle(25*i)
    turtle.circle(-25*i)
    turtle.left(i)

turtle.end_fill()
turtle.done()
