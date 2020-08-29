'''Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma vogal ou o valor booleano False (falso) caso contrário.'''

def vogal(valor):
    return valor in 'aeiou'

def main():
    valor = input().lower()
    
    if vogal(valor):
        print('True')
    else:
        print('False')   

if __name__ == "__main__":
    main()
