from time import sleep
from turtle import *
from random import randint

def art1():
    bgcolor('black')
    penup()
    goto(-200, -100)
    pendown()

    '''
    color("#154c79", "#1e81b0")
    begin_fill()
    right(60)
    width(5)
    circle(230)
    left(60)
    end_fill()
    '''

    def triangle(a, b, c):
        colormode(255)
        color((a-50, b-50, c-50), (a,b,c))
        begin_fill()
        width(5)
        for i in range(3):
            forward(400)
            left(120)
        end_fill()
        penup()
        left(30)
        forward(50)
        right(30)
        pendown()


    for i in range(5):
        r = int(randint(150, 255))
        v = int(randint(150, 255))
        b = int(randint(150, 255))
        triangle(r,v,b)
    #triangle("#478425", "#77dc3d")
    #triangle("#e28743", "#eab676")

    hideturtle()

def art2():
    hideturtle()
    speed(0)
    delay(0)

    while True:
        begin_fill()
        r = randint(0, 255)
        v = randint(0, 255)
        b = randint(0, 255)
        colormode(255)
        color(r,v,b)
        width(3)
        square_side = randint(150, 500)
        for i in range(5):
            for c in range(square_side+1):
                forward(1)
            left(90)
        end_fill()

        penup()
        screensize()
        rand_x = randint(-screensize()[0], screensize()[0])
        rand_y = randint(-screensize()[1], screensize()[1])
        goto(rand_x, rand_y) 
        pendown()

    
    
art2()
done()