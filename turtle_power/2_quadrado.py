from turtle import * 

def quadrado():
    color('Green')
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)


def main():
    color('Green')
    shape('turtle') 
    pensize(3)
    speed(4)

    quadrado()

    done()


if __name__ == "__main__":
    main()