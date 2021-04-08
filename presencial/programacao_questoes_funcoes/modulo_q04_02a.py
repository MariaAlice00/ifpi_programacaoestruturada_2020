#2a. Receber um número inteiro de 3 dígitos e retornar o inverso do número.
# Ex.: número = 532; inverso = 235

def main():
    num = int(input('Digite um número de três digítos: '))
    num_1, num_2, num_3 = inverso(num)
    print(f'O inverso de {num} é {num_1}{num_2}{num_3}')


def inverso(num):    
    num_1 = num // 1 % 10
    num_2 = num // 10 % 10
    num_3 = num // 100 % 10
    return num_1, num_2, num_3

if __name__ == '__main__':
    main()