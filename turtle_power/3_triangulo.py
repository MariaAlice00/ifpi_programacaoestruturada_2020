from turtle import * 

def triangulo():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)


def main():
    shape('turtle') 
    color('Blue')
    pensize(3)
    speed(4)

    triangulo()

    done()


if __name__ == "__main__":
    main()