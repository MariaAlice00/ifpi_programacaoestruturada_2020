from turtle import *

def hexagono():
    for c in range(6):
        forward(100)
        left(60)


def main():
    speed(5)
    pensize(3)
    color('Red')
    shape('turtle')

    hexagono()

    done()


if __name__ == "__main__":
    main()