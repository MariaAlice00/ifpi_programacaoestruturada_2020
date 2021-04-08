from turtle import *

def main():
    speed(7)
    shape('turtle')
    pensize(6)
    color('red')

    sol()

    done()


def sol():
    for count in range(36):
        forward(100)
        right(100)


if __name__ == "__main__":
    main()