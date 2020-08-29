''' Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma letra (vogal ou consoante) ou o valor booleano False (falso) caso contrário.'''

def letra(valor):
    return valor in 'abcdefghijklmnopqrstuvwxyz'

def main():
    valor = input().lower()
    
    if letra(valor):
        print('True')
    else:
        print('False')   

if __name__ == "__main__":
    main()
