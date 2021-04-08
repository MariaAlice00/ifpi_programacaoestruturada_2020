'''Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.'''

def maior():
    maior = 0
    for n in range(1, 101):
        num = int(input())

        if num > maior:
            maior = num

    return maior


def main():
    print(maior())


if __name__ == "__main__":
    main()