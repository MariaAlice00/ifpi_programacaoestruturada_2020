'''Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma vogal ou o valor booleano False (falso) caso contrário.'''

def main():
    valor = input().lower()
    if valor in ('a', 'e', 'i', 'o', 'u'):
        print('True')
    else:
        print('False')


if __name__ == "__main__":
    main()
