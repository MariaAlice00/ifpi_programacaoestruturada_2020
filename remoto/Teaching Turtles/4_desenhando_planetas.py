from turtle import *

def draw_planet(planetsize, planetcolour):
    color(planetcolour)
    pendown()
    begin_fill()

    circle(planetsize)

    end_fill()
    penup()


def main():
    bgcolor('midnightblue')

    draw_planet(50, 'tomato')
    forward(100)
    draw_planet(30, 'turquoise')
    right(170)
    forward(80)
    draw_planet(70, 'maroon')

    hideturtle()
    done()


if __name__ == "__main__":
    main()