from turtle import *
from random import *

def move_to_random_location():
    penup()
    setpos(randint(-300,300), randint(-300,300))
    pendown()


def draw_sun(sun_size, sun_colour):
    color(sun_colour)
    pendown()
    begin_fill()

    for sun in range(30):
        forward(sun_size)
        right(100)
    
    end_fill()
    penup()


def many_sun():
    colours = ['red', 'gold3', 'skyblue', 'darkgreen', 'deeppink2', 'magenta3', 'black']
    for sun in range(60):
        move_to_random_location()
        draw_sun(randint(10,50), choice(colours))


def main():
    speed(11)
    bgcolor('bisque')

    many_sun()

    hideturtle()
    done()


if __name__ == "__main__":
    main()