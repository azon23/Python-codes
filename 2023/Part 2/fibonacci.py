from turtle import *

goto(-200, 100)
side_1 = 10
side_2 = 10
bgcolor(0,0,0)

start_fill = [(255,255,255), (216, 133, 255)]
for i in range(2):
    pensize(1)
    colormode(255)
    color(start_fill[i])
    begin_fill()
    right(90)
    forward(side_1)
    left(90)
    forward(side_1)
    homeAngle = position()
    left(90)
    for r in range(2):
        forward(side_1)
        left(90)
    end_fill()

    pensize(3)
    color(44, 30, 179)
    penup()
    left(90)
    forward(1)
    right(90)
    pendown()
    circle(side_1, 90)

    penup()
    goto(homeAngle)
    pendown()

    left(90)


def square(side, fill_color):
    pensize(1)
    colormode(255)
    color(fill_color)
    begin_fill()
    right(90)
    forward(side)
    left(90)
    forward(side)
    homeAngle = position()
    left(90)
    for r in range(2):
        forward(side)
        left(90)
    
    end_fill()

    pensize(3)
    color(44, 30, 179)
    penup()
    left(90)
    forward(1)
    right(90)
    pendown()
    circle(side, 90)

    penup()
    goto(homeAngle)
    pendown()

    left(90)

rgd_list = [(176, 180, 255), (96, 252, 233), (178, 255, 182), (249, 255, 199), (255, 214, 165), (255, 173, 173), (176, 180, 255), (63, 201, 139)]
for i in range(8):
    next_side = side_1 + side_2
    inColor = rgd_list[i]
    square(next_side, inColor)

    side_1 = side_2
    side_2 = next_side
    
ht()

done()