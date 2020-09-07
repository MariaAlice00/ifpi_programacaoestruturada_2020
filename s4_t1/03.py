'''Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes. NÃO use as funções embutidas min() e max().'''

def maior(num1, num2, num3, num4, num5):
    maior = num1
    if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
        maior = num2
    elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
        maior = num3
    elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
        maior = num4
    elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
        maior = num5
    return maior


def menor(num1, num2, num3, num4, num5):
    menor = num1
    if num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        menor = num2
    elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        menor = num3
    elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
        menor = num4
    elif num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4:
        menor = num5
    return menor


def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())

    print(maior(num1, num2, num3, num4, num5))
    print(menor(num1, num2, num3, num4, num5))


if __name__ == "__main__":
    main()