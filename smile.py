import turtle

turtle.shape('turtle')
turtle.shapesize(1)
turtle.speed(10)

def arcbig():
    for step in range(11):        
        turtle.forward(18)
        turtle.left(18)

# Main yellow circle
turtle.color('black', 'yellow')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()

# Two blue circles
turtle.setposition(-40, 140)
turtle.pendown()
turtle.color('black', 'blue')
turtle.begin_fill()
turtle.circle(15)
turtle.penup()
turtle.setposition(40, 140)
turtle.pendown()
turtle.circle(15)
turtle.end_fill()

turtle.penup()

# Nose
turtle.setposition(0, 120)
turtle.pendown()
turtle.width(10)
turtle.right(90)
turtle.forward(40)

turtle.penup()

# Smile
turtle.setposition(-60, 80)
turtle.pendown()
turtle.color('red')
arcbig()
