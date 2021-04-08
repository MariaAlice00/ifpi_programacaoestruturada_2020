from turtle import *

def main():
    color('whitesmoke')
    bgcolor('midnightblue')

    draw_star()
    forward(100)
    draw_star()
    left(120)
    forward(150)
    draw_star()

    hideturtle()
    done()


def draw_star():
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(50)
    end_fill()
    penup()
    

if __name__ == "__main__":
    main()