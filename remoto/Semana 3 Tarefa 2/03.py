'''Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma consoante ou o valor booleano False (falso) caso contrário.'''

def consoante(valor):
    return valor in 'bcdfghjklmnpqrstvwxyz'    

def main():
    valor = input().lower()

    if consoante(valor):
        print('True')
    else:
        print('False')

if __name__ == "__main__":
    main()