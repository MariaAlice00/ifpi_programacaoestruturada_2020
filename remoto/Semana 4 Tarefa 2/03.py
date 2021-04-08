'''Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido.
• Nenhum dígito é ímpar.
• Apenas um dígito é ímpar.
• Os dois dígitos são ímpares.'''

def unidade(num):
    return num // 1 % 10


def dezena(num):
    return num // 10 % 10


def impar(num):
    if num >= 10 and num <= 99:
        contador = 0

        if unidade(num) % 2 != 0:
            contador = contador + 1  

        if dezena(num) % 2 != 0:
            contador = contador + 1    

        return contador



def main():
    num = int(input())

    contador = impar(num)

    if contador == 0:
        print('Nenhum dígito é ímpar.')
    elif contador == 1:
        print('Apenas um dígito é ímpar.')
    elif contador == 2:
        print('Os dois dígitos são ímpares.')


if __name__ == "__main__":
    main()