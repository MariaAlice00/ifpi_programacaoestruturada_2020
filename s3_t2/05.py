'''Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”;'''

def main():
    valor = input().lower()
    if valor in 'aeiou':
        print('vogal')
    elif valor in 'bcdfghjklmnpqrstvwxyz':
        print('consoante')
    elif valor in '0123456789':
        print('número')
    else:
        print('símbolo')


if __name__ == "__main__":
    main()