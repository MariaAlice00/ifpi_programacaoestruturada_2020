'''Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade de números pares e números ímpares contidos no mesmo.'''

def main():
    par, impar = quant()
    print(par)
    print(impar)


def quant():
    par = 0
    impar = 0

    for c in range(1, 101):
        num = int(input())

        if eh_par(num):
            par += 1
        else:
            impar += 1

    return par, impar


def eh_par(num):
    return num % 2 == 0


if __name__ == "__main__":
    main()