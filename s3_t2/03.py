'''Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma consoante ou o valor booleano False (falso) caso contrário.'''

def main():
    valor = input().lower()
    if valor in 'bcdfghjklmnpqrstvwxyz':
        print('True')
    else:
        print('False')


if __name__ == "__main__":
    main()