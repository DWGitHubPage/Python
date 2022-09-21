# Python 3.7.1

import turtle

turtle.hideturtle()
turtle.speed(speed=1000)

for i in range(70):
    turtle.color('red')
    turtle.circle(20)
    turtle.circle(50)
    turtle.circle(35)
    turtle.circle(40)
    turtle.color('black')
    turtle.circle(25*i)
    turtle.circle(-25*i)
    turtle.left(i)
    
turtle.end_fill()
turtle.done()
