'''Escreva um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.'''

def main():
    cor = str(input()).upper()
    if cor == 'V':
        print('Siga')
    elif cor == 'A':
        print('Atenção')
    elif cor == 'E':
        print('Pare')


if __name__ == "__main__":
    main()