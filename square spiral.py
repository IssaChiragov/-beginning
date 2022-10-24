from turtle import Turtle
from math import pi, sin, cos

turtle = Turtle(visible=True)
turtle.shape('turtle')
turtle.speed('fastest')  # because I have no patience


for _ in range(1):
    x = 0
    y = 0
    turtle.goto(x, y)

    turtle.color('black')
          
    for i in range(100):
        t = i / 2 * pi
        dx = t * cos(t)
        dy = t * sin(t)

        turtle.goto(x + dx, y + dy)




