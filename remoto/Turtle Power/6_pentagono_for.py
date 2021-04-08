from turtle import *

def pentagono():
    for c in range(5):
        forward(100)
        left(72)


def main():
    speed(5)
    pensize(3)
    color('Blue')
    shape('turtle')

    pentagono()

    done()


if __name__ == "__main__":
    main()