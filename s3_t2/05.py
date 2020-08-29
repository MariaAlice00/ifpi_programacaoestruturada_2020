'''Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”;'''

def vogal(valor):
    return valor in 'aeiou'    

def consoante(valor):
    return valor in 'bcdfghjklmnpqrstvwxyz'

def numero(valor):
    return valor in '0123456789'

def main():
    valor = input().lower()

    if vogal(valor):
        print('vogal')
    elif consoante(valor):
        print('consoante')
    elif numero(valor):
        print('número')
    else:
        print('símbolo')

if __name__ == "__main__":
    main()
