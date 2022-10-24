from turtle import *

shape('turtle')
shapesize(1)
speed(10)
color('black')

def star(n):
    for i in range(n):
        right(180 - 180 / n)
        forward(150)


star(5)
penup()
setposition(200, 0)
pendown()
star(11)

