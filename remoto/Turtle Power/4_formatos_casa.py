from turtle import * 

def parede():
    color('yellow')

    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(300)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)


def telhado():
    color('brown')

    left(45)
    forward(70)
    left(90)
    forward(70)

    left(135)
    penup()
    forward(300)
    left(90)
    pendown()
    forward(50)
    left(90)
    forward(250)


def porta():
    color('red')

    left(90)
    penup()
    forward(150)
    left(90)
    forward(20)
    left(90)
    pendown()
    forward(60)
    left(90)
    forward(40)
    left(90)
    forward(60)


def janelas():
    color('blue')

    left(90)
    penup()
    forward(95)
    left(90)
    forward(30)
    pendown()
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)

    right(180)
    penup()
    forward(90)
    pendown()
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)

    done()


def main():
    shape('turtle')
    pensize(3)

    parede()
    telhado()
    porta()
    janelas()


if __name__ == "__main__":
    main()