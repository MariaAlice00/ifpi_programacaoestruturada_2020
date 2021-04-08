from turtle import *

def flor():
    fillcolor('red')
    for c in range(13):
        circle(100, 70)
        left(110)
        circle(100, 70)


def main():
    speed(7)
    fillcolor('red')
    begin_fill()

    flor()

    end_fill()

    done()


if __name__ == "__main__":
    main()