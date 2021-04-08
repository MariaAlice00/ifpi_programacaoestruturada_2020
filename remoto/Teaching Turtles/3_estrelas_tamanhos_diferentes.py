from turtle import *

def draw_star(starsize, starcolour):
    color(starcolour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starsize)
    end_fill()
    penup()


def main():
    bgcolor('midnightblue')

    draw_star(50, 'red')
    forward(100)
    draw_star(30, 'white')
    left(120)
    forward(150)
    draw_star(70, 'green')

    hideturtle()
    done()


if __name__ == "__main__":
    main()