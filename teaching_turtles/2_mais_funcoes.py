from turtle import *

def main():
    color('whitesmoke')
    bgcolor('navy')

    square()
    forward(100)
    square()
    left(90)
    forward(150)
    triangle()
    left(90)
    forward(150)
    triangle()

    hideturtle()
    done()


def square():
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(50)
    end_fill()
    penup()
    

def triangle():
    pendown()
    begin_fill()
    for c in range(3):
        forward(50)
        left(120)
    end_fill()
    penup()


if __name__ == "__main__":
    main()