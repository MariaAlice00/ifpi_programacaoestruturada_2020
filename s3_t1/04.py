'''Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for um dígito entre ‘0’ e ‘9’ ou o valor booleano False (falso) caso contrário'''

def main():
    valor = input()
    if valor in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print('True')
    else:
        print('False')


if __name__ == "__main__":
    main()