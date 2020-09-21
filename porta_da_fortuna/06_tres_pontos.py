from random import *

def main():
    tentativas = 0

    score = 0

    print('''
    Porta da Fortuna!
    =========

    Existe um super prêmio atrás de uma destas 3 portas! Adivinhe qual é a porta certa para ganhar o prêmio!
    _____   _____   _____   
    |     | |     | |     | 
    | [1] | | [2] | | [3] | 
    |   o | |   o | |   o | 
    |_____| |_____| |_____| 
    ''')

    while score < 3:
        tentativas = tentativas + 1

        print('\nTentativa', tentativas, ': Escolha uma porta (1, 2 ou 3):')

        porta_escolhida = input()
        porta_escolhida = int(porta_escolhida)

        porta_certa = randint(1, 3)

        print('A porta escolhida foi a', porta_escolhida)
        print('A porta certa é a', porta_certa)

        if certa(porta_certa, porta_escolhida) == True:
            print('Parabéns')
            score += 1
        else:
            print('Que peninha!')

    print('\nVocê conseguiu! Terminou o jogo em', tentativas, 'tentativas **')


def certa(porta_escolhida, porta_certa):
    return porta_escolhida == porta_certa


def parar(resposta):
    return resposta == 'n' or resposta == 'nao'


if __name__ == "__main__":
    main()