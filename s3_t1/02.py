'''Escreva um programa que leia um número e mostra o valor booleano True (verdadeiro) se o número for ímpar ou o valor booleano False (falso) caso contrário.'''

def main():
    num = int(input())
    if num % 2 != 0:
        print('True')
    else:
        print('False')


if __name__ == "__main__":
    main()