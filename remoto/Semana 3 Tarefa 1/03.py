'''Escreva um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.'''

def verde(cor):
    return cor == 'V'

def amarelo(cor):
    return cor == 'A'

def vermelho(cor):
    return cor == 'E'

def main():
    cor = str(input()).upper()

    if verde(cor):
        print('Siga')
    elif amarelo(cor):
        print('Atenção')
    elif vermelho(cor):
        print('Pare')
                    
if __name__ == "__main__":
    main()