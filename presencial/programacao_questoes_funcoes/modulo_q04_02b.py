#2b. Recebe um número inteiro de 4 dígitos e retornar a soma dos elementos que o compõem.
# Ex.: número = 9534; soma = 9+5+3+4 = 21.

def main():
    num = int(input('Digite um número de quatro digítos: '))
    soma(num)
    print('A soma é', soma(num))

def soma(num):
    num_1 = num // 1 % 10
    num_2 = num // 10 % 10
    num_3 = num // 100 % 10
    num_4 = num // 1000 % 10
    return num_1 + num_2 + num_3 + num_4

if __name__ == '__main__':
    main()