from turtle import *

def main():
    lados = int(input('Quantos lados? '))

    speed(5)
    shape('turtle')
    pensize(6)
    color('red')

    desenho(lados)

    done()


def desenho(lados):
    angulo = 360 / lados

    for count in range(lados):
        forward(50)
        left(angulo)


if __name__ == "__main__":
    main()