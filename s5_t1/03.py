'''Escreva um programa que leia um conjunto 100 números inteiros e exiba o valor médio dos mesmos (com duas casas decimais).'''

def main():
    print('{:.2f}'.format(media()))


def media():
    soma = 0

    for n in range(1, 101):
        num = int(input())

        soma += num

    media = soma / 100    
    return media


if __name__ == "__main__":
    main()