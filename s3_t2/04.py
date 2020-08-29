'''Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma letra (vogal ou consoante) ou um dígito (entre ‘0’ e ‘9’) ou valor booleano False (falso) caso contrário.'''

def letra_digito(valor):
    return valor in 'abcdefghijklmnopqrstuvwxyz0123456789'

def main():
    valor = input().lower()
    if letra_digito(valor):
        print('True')
    else:
        print('False')

if __name__ == "__main__":
    main()
