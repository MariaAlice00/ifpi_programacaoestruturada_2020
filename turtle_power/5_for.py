from turtle import *

def linha_tracejada():
    for count in range(30):
        forward(5)
        penup()
        forward(5)
        pendown()


def main():
    speed(11)
    shape('turtle')

    linha_tracejada()

    done()


if __name__ == "__main__":
    main()