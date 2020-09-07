'''Escreva um programa que leia um número inteiro entre 100 e 999, mostre quantos dígitos pares existem nesse número. Por exemplo: 245 tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.'''

def unidade(num):
    return num // 1 % 10


def dezena(num):
    return num // 10 % 10


def centena(num):
    return num // 100 % 10


def par(num):
    if num >= 100 and num <= 999:
        contador = 0

        if unidade(num) % 2 == 0:
            contador = contador + 1  

        if dezena(num) % 2 == 0:
            contador = contador + 1    

        if centena(num) % 2 == 0:
            contador = contador + 1    

        print(contador)


def main():
    num = int(input())

    par(num)



if __name__ == "__main__":
    main()