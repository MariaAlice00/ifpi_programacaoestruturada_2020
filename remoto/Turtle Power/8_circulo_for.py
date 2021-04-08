from turtle import *

def circulo():
    for c in range(360):
        forward(1)
        left(1)


def main():
    speed(11)
    pensize(3)
    color('Black')
    shape('turtle')

    circulo()

    done()


if __name__ == "__main__":
    main()